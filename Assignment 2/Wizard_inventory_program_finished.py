# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:47:34 2023

@author: Matt
"""

import random

def display_title():
    print("The Wizard Inventory program\n")
    
def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    

    
def show_items(items):
# Reads the base 'wizard all items' text file and prints all the lines
# but is never actually used.
# 'items' variable and show_items function called at the bottom of the
# file but commented out if you want to double check it (I tried them,
# they worked for me)
    with open("wizard_all_items.txt") as file:
        print(file.read())
        
def show_inventory(inventory):
# Reads all lines from the 'wizard inventory' text file and prints
# them all as a list
    with open("wizard_inventory.txt") as file:
        inv = (file.read())
        print(inv)
    
def items_index(items):
    with open("wizard_all_items.txt", "r") as file:
        for i in file:
            items.append(file.readline())
        
        
def inventory_index(inventory):
    with open("wizard_inventory.txt", "r") as file:
        for i in file:
            inventory.append(file.readline())
        
def walk(inventory, items):
    name = random.choice(items)
    if "\n" in name:
        item_name = name.strip("\n")
    print(f"Walking down a path, you see {item_name}.")
    choice = input("Would you like to grab it? (y/n): ")
    if choice.lower() == "y":
        with open("wizard_inventory.txt", "r") as file:
            length = len(file.readlines())
            if length >= 4:
                print("You can't carry any more items. Drop something first.")
            else:
                with open("wizard_inventory.txt", "a") as file:
                    file.write(name)
                    file.close()
                if "\n" in name:
                    item_name = name.strip("\n")
                    print(f"You picked up {item_name}.")
    elif choice.lower() == "n":
        print("You ignore the item.")
    
# def grab_item(): Didn't need this function after
#     line_count = []
#     with open(INVENTORY, "r") as file:
#         lines = file.readlines()
#         line_count.append(lines)
#     if len(line_count) > 4:
#         print("You can't carry any more items. Drop something first\n")
#     else:
#         with open(INVENTORY, "a") as file:
#             file.append(INVENTORY)

def drop_item(inventory):
    try:
        inv = []
        with open("wizard_inventory.txt", "r") as file:
            for lines in file:
                for es in lines:
                    es = es.strip("\n")
                inv.append(lines)
        number = int(input("Number: "))
        if number < 0 or number > (len(inv) + 1):
            print("Invalid item number.\n")
        else:
            inv.pop((number) - 1)
            with open("wizard_inventory.txt", "w") as file:
                for element in inv:
                    file.write(element)
            print(f"{inv[number]} was dropped.")
    except IndexError:
        print("\nIt's telling me that the list index is out of range but the")
        print("function still works so I dunno what to do with that except")
        print("type out this error handler. If you use 'show', you'll see the")
        print("item gets popped from the list, so I'm going with it.")

def game():
    with open("wizard_inventory.txt", "r") as inventory:
        INVENTORY = inventory.readlines()

    with open("wizard_all_items.txt", "r") as items:
        ITEMS = items.readlines()
    display_title()
    display_menu()
    inventory = INVENTORY
    items = ITEMS
    while True:
        cmnd = input("\nCommand: ")
        if cmnd.lower() == "show":
            show_inventory(inventory)
        elif cmnd.lower() == "walk":
            walk(inventory, items)
        elif cmnd.lower() == "drop":
            drop_item(inventory)
        elif cmnd.lower() == "exit":
            print("Bye!")
            break
        
if __name__ == "__main__":
    game()
    
# items = "wizard_all_items.txt"
# show_items(items)