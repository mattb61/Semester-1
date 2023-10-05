# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:40:55 2023

@author: Matt
"""
print("Letter grade converter\n")
loop = "y"
while loop.lower() == "y":
        percent = int(input("Enter numerical grade: "))
        if percent <= 100 and percent >= 88:
            grade = "A"
            print("Letter grade: {}".format(grade))
        elif percent <= 87 and percent >= 80:
            grade = "B"
            print("Letter grade: {}".format(grade))
        elif percent <= 79 and percent >= 67:
            grade = "C"
            print("Letter grade: {}".format(grade))
        elif percent <= 66 and percent >= 60:
            grade = "D"
            print("Letter grade: {}\n".format(grade))
        elif percent < 60:
            grade = "F"
            print("Letter grade: {}".format(grade))
        loop = input("\nContinue? (y/n): ")
print("\nBye!")