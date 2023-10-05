# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:17:12 2023

@author: Matt
"""

#assistance with diving total cents by different coins from Harvey

print("Change Calculator\n")
loop = "y"
quarters = 25
dimes = 10
nickels = 5
pennies = 1
while loop.lower() == "y":
    cents = int(input("Enter number of cents (0, 99): "))
    qn = cents//quarters
    cents %= quarters
    dn = cents//dimes
    cents %= dimes
    nn = cents//nickels
    cents %= nickels
    pn = cents//pennies
    cents %= pennies
    print("\nQuarters: {}".format(qn))
    print("Dimes: {}".format(dn))
    print("Nickels: {}".format(nn))
    print("Pennies: {}".format(pn))
    loop = input("\nContinue? (y/n): ")
print("\nBye!")