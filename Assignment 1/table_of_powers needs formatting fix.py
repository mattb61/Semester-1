# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:36:21 2023

@author: Matt
"""

print("Table of Powers\n")
start = int(input("Start number: "))
middle = start + 1
stop = int(input("Stop number:  "))
print("\nNumber\t\tSquared\t\tCubed")
print("======\t\t=======\t\t=====")
print("{}\t\t\t{}\t\t\t{}".format(start, start ** 2, start ** 3))
for i in range(start, stop):
    print("{}\t\t\t{}\t\t\t{}".format(middle, middle ** 2, middle ** 3))
    middle = middle + 1