import sqlite3

conn = sqlite3.connect('phonebook.db', check_same_thread= False)

def create_db():
    c = conn.cursor()
    c.execute('CREATE TABLE contacts ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, phonenum TEXT UNIQUE)')
    c.execute('CREATE TABLE phonebooks ( id INTEGER PRIMARY KEY AUTOINCREMENT, phonebook_name TEXT UNIQUE)')
    c.execute('CREATE TABLE mapping ( id INTEGER PRIMARY KEY AUTOINCREMENT, phonebook_id INTEGER, contact_id INTEGER)')
    conn.commit()

def add_phonebook(phonebook):
    try:
        with conn:
            conn.execute('INSERT INTO phonebooks VALUES (NULL, ?)', (phonebook,))
        return True
    except sqlite3.IntegrityError:
        return False

def get_phonebook_id(phonebook):
    try:
        c = conn.cursor()
        c.execute('SELECT id from phonebooks WHERE phonebook_name=?', (phonebook,))
        pb_id = c.fetchone()
        return pb_id
    except sqlite3.OperationalError:
        return False
        
def add_entry(phonebook_id, entry):          
    try:
        with conn:
            conn.execute('INSERT INTO contacts VALUES (NULL, ?, ?)', entry)
        return update_mapping(phonebook_id, entry)
    except sqlite3.IntegrityError:
        return update_mapping(phonebook_id, entry)

def update_mapping(phonebook_id, entry):
    c = conn.cursor()
    c.execute('SELECT id from contacts WHERE name=?', (entry[0],))
    contact_id = c.fetchone()
    if contact_id:
        present = lookup_in_mapping(phonebook_id, contact_id[0])
        if not present:
            with conn:
                conn.execute('INSERT INTO mapping VALUES (NULL, ?, ?)', (phonebook_id, contact_id[0]))
            return True
        else:
            return False
    else:
        return False
        # the contact is not in the contacts table (could not be added because of phone number uniqueness constraint)

def lookup_in_mapping(phonebook_id, contact_id):
    c = conn.cursor()
    c.execute('SELECT id from mapping WHERE phonebook_id=? AND contact_id=?', (phonebook_id, contact_id))
    mapping_id = c.fetchone()
    return mapping_id # returns tuple with ID or none


def lookup_contact(name):
    c = conn.cursor()
    c.execute('SELECT * FROM contacts WHERE name=?', (name,))
    data = c.fetchall()
    return data

def reverse_lookup(phonebook, number):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook WHERE phonebook=? AND phonenum=?', phonebook, number)
    data = c.fetchall()
    return data

try:
    create_db()
except sqlite3.OperationalError:
    pass
    
# each contact belongs to many groups
# each group has many contacts

# group: name, id -- and many contacts
# contact: name, number, id -- and many groups
# 
# to 'create':
#     add group
# 
# to add contact:
#     find group
#     add contact
#     add group_id contact_id to mapping
# 
# to find contact in group:
#     look up contact, get id
#     look up group, get id
#     check that contact_id, group_id is in mapping
# 
# mapping:
# group_id contact_id


