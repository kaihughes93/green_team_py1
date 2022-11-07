import random
import string

#User input needed for naming department
department= input("Enter Department= Accounting, FinOps, Marketing: ")
name = ("What is your department? ").lower()
if names not in department:
    print("The department you selected is not available")
    exit()
    
#User input needed to input the name of their department
names = input("Are names needed for your department? y/n ").lower()
if names == "y":
    print("Continue")
elif names == "n":
    print("Exiting")
    exit()
    