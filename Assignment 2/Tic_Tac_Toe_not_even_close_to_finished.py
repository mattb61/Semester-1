# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:48:06 2023

@author: Matt
"""

def display_title():
    print("Welcome to Tic-Tac-Toe")
    
def starting_board():
    print("+---+---+---+")
    print("|   |   |   |")
    print("+---+---+---+")
    print("|   |   |   |")
    print("+---+---+---+")
    print("|   |   |   |")
    print("+---+---+---+")
    
def playing_board():
    board = [["+", "---", "+", "---", "+", "---", "+"],
             ['|', '   ', '|', '   ', '|', "   ", "|"],
             ["+", "---", "+", "---", "+", "---", "+"],
             ['|', '   ', '|', '   ', '|', "   ", "|"],
             ["+", "---", "+", "---", "+", "---", "+"],
             ['|', '   ', '|', '   ', '|', "   ", "|"],
             ["+", "---", "+", "---", "+", "---", "+"]]
    print("", * board[0])
    print("", * board[1])
    print("", * board[2])
    print("", * board[3])
    print("", * board[4])
    print("", * board[5])
    print("", * board[6])
    
    row = int(input("Pick a row: "))
    column = int(input("Pick a column: "))
    if row == 1:
        if column == 1:
            board[1][1] = " O "
            print("", * board[0])
            print("", * board[1])
            print("", * board[2])
            print("", * board[3])
            print("", * board[4])
            print("", * board[5])
            print("", * board[6])
        elif column == 2:
            board[1][3] = " O "
            print("", * board[0])
            print("", * board[1])
            print("", * board[2])
            print("", * board[3])
            print("", * board[4])
            print("", * board[5])
            print("", * board[6])
        elif column == 3:
            board[1][5] = " O "
            print("", * board[0])
            print("", * board[1])
            print("", * board[2])
            print("", * board[3])
            print("", * board[4])
            print("", * board[5])
            print("", * board[6])
            
# Doing all of the above for ever row and every column for both
# players, AND printing the entire board after every single turn
# was the idea, but I didn't like how long the file was getting, how
# big the functions would be, and how bad the code would look. I'm
# also pretty much out of time to write every other needed function
# or to figure out another way of doing it AND writing that instead
# as it's 9 PM on Friday (the due date). I'm writing this comment so
# that you will at least know what I was going for with the code above
# as you've told me to do before, if I can't finish the program.