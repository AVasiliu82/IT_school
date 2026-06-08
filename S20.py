import psycopg2

def create_connection():
    connection = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password = "admin",
        port = "5433"
    )
    return connection

connection = create_connection()
if connection:
    print("ok")
else:
    print("eroare")

connection.close()