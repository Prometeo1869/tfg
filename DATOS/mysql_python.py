import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "usuario",
    password = "usuario", 
    port = "3307",
    database = "movies"
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

conn.close()