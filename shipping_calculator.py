# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:37:30 2023

@author: Matt
"""

print("=" * 50)
print("Shipping Calculator")
print("=" * 50)

loop = "y"
cost = 0

while loop.lower() == "y":
    cost = float(input("Cost of items ordered: "))
    if cost < 0:
        print("You must enter a positive number. Please try again.")
    else:
        shipping = float(input("Shipping cost: "))
        total_cost = cost + shipping
        print("Total cost: {}".format(total_cost))
        loop = input("\nContinue? (y/n): ")
        print("=" * 50, end = "\n")
print("Bye!")