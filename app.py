from flask import Flask, render_template, request, url_for, session, redirect
import mysql.connector
import sqlite3
import bcrypt

app = Flask(__name__)
app.config.from_object('config.Config')
app.secret_key = "super secret key"

def create_db_connection():
    db_config = {
        'host': app.config['MYSQL_HOST'],
        'user': app.config['MYSQL_USER'],
        'password': app.config['MYSQL_PASSWORD'],
        'database': app.config['MYSQL_DB']
    }
    return mysql.connector.connect(**db_config)

def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def inserisci_dati(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

connection = mysql.connector.connect(host='localhost',
                                     database='my_podcast',
                                     user='root',
                                     password='')
cursor = connection.cursor()

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def insert_user(conn, username, password):
    sql = """INSERT INTO users (username, hashed_password) VALUES (?, ?);"""
    try:
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute(sql, (username, hashed_password))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def verify_password(conn, username, password):
    sql = """SELECT hashed_password FROM users WHERE username = ?;"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        if row:
            stored_hashed_password = row[0]
            return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
        else:
            return False
    except sqlite3.Error as e:
        print(e)
        return False

@app.route("/")
def index():
    reg = request.args.get('reg')
    return render_template("index.html", reg=reg)

@app.route('/home.html')
def home():
    if 'username' in session:
        return render_template("home.html", username=session['username'])
    else:
        return render_template("index.html")

@app.route('/chi-siamo.html')
def chi_siamo():
    if 'username' in session:
        return render_template("chi-siamo.html", username=session['username'])
    else:
        return render_template("index.html")

@app.route('/podcasts.html')
def podcasts():
    if 'username' in session:
        return render_template("podcasts.html", username=session['username'])
    else:
        return render_template("index.html")

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute('SELECT * FROM utenti WHERE username = %s', (username,))
        record = cursor.fetchone()

        if record and bcrypt.checkpw(password.encode('utf-8'), record[2].encode('utf-8')):  # Assumendo che la password hashata sia nel terzo campo
            session['logged'] = True
            session['username'] = record[1]
            return redirect(url_for('home'))
        else:
            msg = 'Username/Password errato. Riprova!'
    return render_template("index.html", msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username-reg']
        pwd = request.form['password-reg']
        email = request.form['email']

        # Hashare la password
        hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())

        cursor.execute('INSERT INTO utenti (username, password, email) VALUES (%s, %s, %s)', (username, hashed_pwd, email))
        connection.commit()
        reg = 'Registrazione avvenuta con successo!'

        return redirect(url_for('index', reg=reg))
    reg = request.args.get('reg')
    return render_template('index.html', reg=reg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)