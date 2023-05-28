# Importar los módulos necesarios
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# Función para obtener una conexión a la base de datos MySQL
def get_conn():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="usuario",
        password="usuario",
        port="3307",
        database="movies"
    )
    return conn

# Función para obtener un objeto engine de SQLAlchemy para interactuar con la base de datos MySQL
def get_engine():
    engine = create_engine('mysql+mysqlconnector://usuario:usuario@127.0.0.1:3307/movies')
    return engine

# Función para crear una tabla en la base de datos
def create_filmes_table():
    # Obtener la conexión a la base de datos
    conn = get_conn()
    # Crear un cursor para ejecutar sentencias SQL
    cursor = conn.cursor()
    # Definir la sentencia SQL para crear la tabla filmes
    filmes_table = """CREATE TABLE IF NOT EXISTS filmes (
     id INTEGER PRIMARY KEY,
     title VARCHAR(80),
     rating FLOAT,
     year YEAR,
     image VARCHAR(180),
     genre VARCHAR(20),
     director VARCHAR(40)
    )"""
    # Ejecutar la sentencia SQL para crear la tabla
    cursor.execute(filmes_table)
    # Guardar los cambios en la base de datos
    conn.commit()
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para eliminar una tabla de la base de datos
def drop_filmes_table():
    # Obtener la conexión a la base de datos
    conn = get_conn()
    # Crear un cursor para ejecutar sentencias SQL
    cursor = conn.cursor()
    # Ejecutar la sentencia SQL para eliminar la tabla filmes
    cursor.execute("DROP TABLE IF EXISTS filmes")
    # Guardar los cambios en la base de datos
    conn.commit()
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para obtener los datos de la tabla filmes de la base de datos y devolverlos como un DataFrame de Pandas
def get_filmes_data():
    # Obtener una conexión a la base de datos
    conn = get_conn()
    try:
        # Intentar leer los datos de la tabla filmes y guardarlos en un DataFrame
        df = pd.read_sql("SELECT * FROM filmes", conn)
    except:
        # Si ocurre un error al leer los datos (la tabla no existe), crear un DataFrame vacío con las columnas especificadas
        columns = ['id', 'title', 'rating', 'year', 'image', 'genre', 'director']
        df = pd.DataFrame(columns=columns)
    finally:
        # Cerrar siempre la conexión a la base de datos
        conn.close()
    # Devolver el DataFrame con los datos leídos (o vacío si ocurrió un error)
    return df
