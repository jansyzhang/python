# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:36:54 2019

"""

import shelve

def store_person(db):
    pid = input("enter unique ID number:")
    person = {}
    person['name'] = input("enter name:")
    person['age'] = input("enter age:")
    person['phone'] = input("enter phone number:")
    db[pid] = person
     
def lookup_person(db):
    pid = input("enter ID number:")
    field = input("know?(name age phone)")
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])
    
def print_help():
    print('The available commands are:')
    print('store  : stores information about a person')
    print('lookup : looks up a person from ID number')
    print('quit   : save changes and exit')
    print('?      : print this message')

def enter_command():
    cmd = input("enter command(? for help):")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open("database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()
        
if __name__ == '__main__':
    main()
        
        
        
        
        