import sqlite3
import sys

import db

def create(phonebook):
    try:
        db.create_db()
    except sqlite3.OperationalError:
        print "Phonebook exists"

def add(name, number, phonebook):
    status = db.add_entry(phonebook, (name, number))
    if status:
        print "%s added to %s with number %s" % (name, phonebook, number)
    else:
        print "Error: phonenumber %s already present in %s" % (number, phonebook)

def change():
    pass
    
def lookup(name, phonebook):
    results = db.lookup(name, phonebook)
    print results

def reverse_lookup(number, phonebook):
    results = db.lookup(name, phonebook)
    print results
    
def remove():
    pass

command_dict = {"create" : create,
                "add" : add,
                "change" : change,
                "lookup" : lookup,
                "reverse-lookup" : reverse_lookup,
                "remove" : remove}

if __name__ == "__main__":
    args = sys.argv
    args = args[1:]
    command = args.pop(0)
    
    try:
        to_run = command_dict[command]
    except KeyError: 
        sys.exit("No such command")
    
    to_run(*args)    

