import sqlite3
import bcrypt

# Funzione per hashare una password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Funzione per inserire un nuovo utente nel database
def insert_user(conn, username, password):
    sql = """INSERT INTO users (username, hashed_password) VALUES (?, ?);"""
    try:
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute(sql, (username, hashed_password))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Funzione per verificare la password
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

# Esempio di utilizzo
if __name__ == "__main__":
    database = "test.db"

    # Crea una connessione al database
    conn = create_connection(database)

    # Crea la tabella se non esiste
    create_table(conn)

    # Inserisce un nuovo utente con una password hashata
    username = "test_user"
    password = "secure_password"
    insert_user(conn, username, password)

    # Verifica della password
    if verify_password(conn, username, password):
        print("La password è corretta!")
    else:
        print("La password è errata!")

    # Chiudi la connessione
    conn.close()
