import sqlite3

DB_NAME = "library.db"

def get_db_connect():
    conn = sqlite3.connect(DB_NAME)
    return conn

def migrate():
    conn = get_db_connect()
    cursor = conn.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT UNIQUE,
        password INTEGER NOT NULL
        )
    ''')


    cursor.execute(''' CREATE TABLE books (         
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        author TEXT NOT NULL,           
        category TEXT NOT NULL,           
        status TEXT NOT NULL)
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate()