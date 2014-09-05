import sqlite3
import sys

import db

def create(phonebook):
#     from pudb import set_trace; set_trace()
    status = db.add_phonebook(phonebook)
    if status:
        print "%s created" % phonebook
    else:
        print "Error: phonenumber %s already present" % phonebook
    
def add(name, number, phonebook):
    from pudb import set_trace; set_trace()
    pb_id = db.get_phonebook_id(phonebook)
    if pb_id:
        status = db.add_entry(pb_id[0], (name, number))
        if status:
            print "%s added to %s with number %s" % (name, phonebook, number)
        else:
            print "Error: phonenumber %s already present in %s" % (number, phonebook)
    else:
        print "Error: phonebook does not exist"

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

