# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:17:38 2023

@author: Matt
"""

print("Tip calculator\n")
cost = float(input("Cost of meal:\t"))
print("\n15%")
tip15 = cost * 0.15
print("Tip amount:\t\t{:.2f}".format(tip15))
total_amount = cost + tip15
print("Total amount:\t{:.2f}".format(total_amount))
print("\n20%")
tip20 = cost * 0.20
print("Tip amount:\t\t{:.2f}".format(tip20))
total_amount = cost + tip20
print("Total amount:\t{:.2f}".format(total_amount))
print("\n25%")
tip25 = cost * 0.25
print("Tip amount:\t\t{:.2f}".format(tip25))
total_amount = cost + tip25
print("Total amount:\t{:.2f}".format(total_amount))