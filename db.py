import sqlite3

conn = sqlite3.connect('phonebook.db', check_same_thread= False)

def create_db():
    c = conn.cursor()
    c.execute('CREATE TABLE phonebook ( id INTEGER PRIMARY KEY AUTOINCREMENT, phonebook_name TEXT, name TEXT, phonenum TEXT UNIQUE)')
    conn.commit()

def add_entry(phonebook, entry):
    try:
        with conn:
            conn.execute('INSERT INTO phonebook VALUES (NULL, ?, ?, ?)', (phonebook, entry[0], entry[1]))
        return True
    except sqlite3.IntegrityError:
        return False

def lookup(phonebook, name):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook WHERE phonebook=? AND name=?', phonebook, name)
    data = c.fetchall()
    return data

def reverse_lookup(phonebook, number):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook WHERE phonebook=? AND phonenum=?', phonebook, number)
    data = c.fetchall()
    return data


