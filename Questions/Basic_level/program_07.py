"""
Write a Python program that accepts a filename 
from the user and prints the extension of the file
"""

file = input("Input the Filename: ")

f_ext = file.split(".")

print("The extension of the file is : "+f_ext[-1])