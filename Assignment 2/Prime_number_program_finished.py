# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:33:58 2023

@author: Matt
"""

def display_title():
    print("Prime Number Checker")
        
def display_factors(number):
    factors = []
    for i in range(1, 5000):
        if number % i == 0:
            factors.append(i)
# Assistance from Matthew King and Steven on how to put factors in a
# list properly
    if len(factors) > 2:
        print(f"{number} is NOT a prime number.")
        print("It has the factors:", * factors)
# Assistance from Michal on how to format the list into the string
# properly
    else:                    
        print(f"{number} is prime.")
    
def main(): 
    loop = "y"
    display_title()
    while loop.lower() == "y":
        number = int(input("\nPlease enter an integer between 1 and 5000: "))
        display_factors(number)
        loop = input("\nTry again? (y/n): ")
        if loop.lower() == "n":
            print("\nBye!")
            break
            
if __name__ == "__main__":
    main()