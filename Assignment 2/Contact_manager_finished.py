# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:09:13 2023

@author: Matt
"""

contact_list = [["Guido van Rossum", "guido@guidovanrossum.com", "+22 10 4523 0535"],
                ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]

def display_title():
    print("Contact Manager")
    
def commands_list():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")

def list_contacts(contact_list):
# Lists all contacts by first name
    for i, contact in enumerate(contact_list, start = 1):
        print(f"{i}. {contact[0]}")
    
def get_contact(contact_list):
# Asks user for integer input in relation to the contacts list
    while True:
        try:
            number = int(input("Number: "))
            if number > len(contact_list):
                print("That is not a valid contact number.")
            elif number < 1: # Little joke if you don't mind
                print("That's not even a possible contact number. Try again.")
            else:
                return number
        except ValueError as ve: # Another little joke based on error handling
            print(f"\n{ve}.")
            print("That's not even a number. C'mon man.\n")
        
def view_contact(contact_list):
# Takes number from get_contact and prints the corresponding rows for
# name, email, and phone
    number = get_contact(contact_list) - 1
    print(f"Name: {contact_list[number][0]}")
    print(f"Email: {contact_list[number][1]}")
    print(f"Phone: {contact_list[number][2]}")
    
def add_contact(contact_list):
# Takes 3 string inputs from user, puts them in a list, and appends that
# list to the main contacts list
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = [name, email, phone]
    contact_list.append(contact)
    if "-" in phone:
    # Allows dashes to put between numbers in the phone input
        print(f"{name} has been added.")

def delete_contact(contact_list):
# Takes number from get_contact and pops corresponding row from main
# contact list
    number = get_contact(contact_list)
    contact_number = int(input("Number: "))
    contact_list.pop(number - 1)
    print(f"{contact_number} was removed.")
    
def main():
    display_title()
    commands_list()
    while True:
        command = input("\nCommand: ")
        if command.lower() == "list":
            list_contacts(contact_list)
        elif command.lower() == "view":
            view_contact(contact_list)
        elif command.lower() == "add":
            add_contact(contact_list)
        elif command.lower() == "del":
            delete_contact(contact_list)
        elif command.lower() == "exit":
            del contact_list[2:]
            print("Bye!")
            break
        else:
            print("\nInvalid command. Please try again.\n")
            

if __name__ == "__main__":
    main()