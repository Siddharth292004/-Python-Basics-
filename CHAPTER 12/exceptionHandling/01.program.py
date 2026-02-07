#Exception handling is a way to handle runtime errors so that the program does not crash and can continue running normally.
#In Python, we can use try-except blocks to handle exceptions. The code that may raise an exception is placed inside the try block, and the code to handle the exception is placed inside the except block.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except:
    print("Something went wrong !") 