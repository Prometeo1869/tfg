import mysql.connector
from sqlalchemy import create_engine

def get_conn():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="usuario",
        password="usuario",
        port="3307",
        database="movies"
    )
    return conn

def get_engine():
    engine = create_engine('mysql+mysqlconnector://usuario:usuario@127.0.0.1:3307/movies')
    return engine

def create_filmes_table():
    conn = get_conn()
    cursor = conn.cursor()
    filmes_table = """CREATE TABLE IF NOT EXISTS filmes (
     id INTEGER PRIMARY KEY,
     title VARCHAR(80),
     rating FLOAT,
     year YEAR,
     image VARCHAR(180),
     genre VARCHAR(20),
     director VARCHAR(40)
    )"""
    cursor.execute(filmes_table)
    conn.commit()
    conn.close()