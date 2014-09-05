import sqlite3

conn = sqlite3.connect('phonebook.db', check_same_thread= False)

def create_db():
    c = conn.cursor()
    c.execute('CREATE TABLE phonebook ( id integer AUTOINCREMENT name text phonenum text unique)')
    conn.commit()

def add_entry(entry):
    try:
        with conn:
            conn.execute('INSERT INTO phonebook VALUES (?, ?)', entry)
        return True
    except sqlite3.IntegrityError:
        return False

def lookup(name):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook WHERE name=?', name)
    data = c.fetchall()
    return data

def reverse_lookup(number):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook WHERE phonenum=?', number)
    data = c.fetchall()
    return data


