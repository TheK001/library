from database import get_db_connect

def user_register(first_name, last_name, username, password):
    conn = get_db_connect()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users (first_name, last_name, username, password) VALUES (?,?,?,?)',(first_name, last_name, username, password))
    conn.commit()
    conn.close()
    print("user added successfuly!!!")

def user_login(username, password):
    conn = get_db_connect()
    cursor = conn.cursor()

    user = cursor.execute('SELECT username,password FROM users WHERE username=? AND password=?',(username, password))
    user.fetchone() is None
    conn.close()
    return user
    
def show_books():
    conn = get_db_connect()
    cursor = conn.cursor()

    book = cursor.execute('SELECT * FROM books').fetchall()

def add_books(name, author, category, status):
    conn = get_db_connect()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO books (name, author, category, status) VALU 





""")
    



    