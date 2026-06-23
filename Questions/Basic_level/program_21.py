"""
Write a Python program that determines whether a given 
number (accepted from the user) is even or odd, and prints an appropriate message to the user
"""

def checker(n):

    if n % 2 == 0:
        print(f"{n} is an even number")
        return
    else:
        print(f"{n} is an odd number")
        return
    
checker(10)
checker(11)
checker(7)
checker(3)