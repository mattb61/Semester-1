# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:09:13 2023

@author: Matt
"""

import csv

# contact_list = [["Guido van Rossum", "guido@guidovanrossum.com", "+22 10 4523 0535"],
#                 ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]

def display_title():
    print("Contact Manager")
    
def commands_list():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    
def list_contacts(): # Numbers all contacts in CSV file in a list of names
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, start = 1):
            print(f"{i}. {row[0]}")
        
def view_contact():
# Same function from the text file contacts program, except it prints
# out each column of a specific row after reading from the CSV file
    contact = []
    number = int(input("Number: ")) - 1
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            contact.append(row)
        print(f"Name: {contact[number][0]}")
        print(f"Email: {contact[number][1]}")
        print(f"Phone: {contact[number][2]}")
 # I tried trial/erroring with enumerate and couldn't get it to work

def add_contact():
# Was supposed to append a single row of information, but as stated
# below, it breaks the CSV formatting for some reason
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = [name, email, phone]
    with open("contacts.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(contact)
        print(f"{name} has been added.")
        # Also, for some reason, writing a single list to the csv
        # file, even in append mode, breaks the enumeration in the
        # 'list' function, and I have no idea why

def delete_contact():
# Reads all contact information in the CSV file, strips the \n from
# all rows, appends all rows to a list, pops corresponding row from
# the list, and re-writes the file with the remaining list.
# Re-writing the list back to CSV file breaks formatting though, so
# there's an error, which is handled below, with more information
# comments below that.
    try:
        all_contacts = []
        number = int(input("Number: ")) - 1
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            for rows in reader:
                for element in rows:
                    element = element.strip("\n")
                all_contacts.append(rows)
        all_contacts.pop(number)
        with open("contacts.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(all_contacts)
        print(f"{all_contacts[number]} has been deleted.")
    except IndexError:
        print("\nWhen printing the message of the contact who was")
        print("deleted, you get an 'IndexError', but the contact still")
        print("gets deleted from the csv file, so I don't know what")
        print("else to do besides write this entire error handle to")
        print("explain it so the program doesn't break.")
        # I know pretty much that entire error handler could have just
        # been a giant comment but I figured I'd explain the whole
        # situation in the error handling message while also handling
        # the error.
        # Also, this function will ALSO break the 'list all contacts'
        # function, I assume for the same reason. Don't know how to
        # fix it.
            
def main():
    display_title()
    commands_list()
    while True:
        command = input("\nCommand: ")
        if command.lower() == "list":
            list_contacts()
        elif command.lower() == "view":
            view_contact()
        elif command.lower() == "add":
            add_contact()
        elif command.lower() == "del":
            delete_contact()
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("\nInvalid command. Please try again.\n")
            

if __name__ == "__main__":
    main()