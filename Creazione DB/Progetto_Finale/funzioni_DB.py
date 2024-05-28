import csv
import mysql.connector
from mysql.connector import Error
import bcrypt
import sqlite3
from tqdm import tqdm
import pandas as pd
import numpy as np

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, name):
    cursor = connection.cursor()
    try:
        query = f"CREATE DATABASE {name}"
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"MySQL Database connection successful to {db_name} ")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query, /,*, dictionary = False):
    if dictionary:
        cursor = connection.cursor(dictionary=True)
    else:
        cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def inserimento_dati(connection,query,file):
    cursor = connection.cursor()
    with open(file,encoding='utf-8') as f:
        lett = csv.reader(f)
        next(lett)
        for riga in tqdm(lett):
            cursor.execute(query, riga)
        connection.commit()

def inserimento_review(connection,file):
    cursor = connection.cursor()
    query = f"INSERT INTO review(podcast_id,titolo,contenuto,rating) VALUES (%s,%s,%s,%s)"
    with open(file, encoding='utf-8') as f:
        lett = csv.DictReader(f)
        for row in lett:
            # Converti i dati se necessario
            podcast_id = row['podcast_id']
            titolo = row['title']
            contenuto = row['content']
            rating = float(row['rating'])  # Assicurati che il rating sia un float

            cursor.execute(query, (podcast_id, titolo, contenuto, rating))
    connection.commit()