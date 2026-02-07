try:
    num1= int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1 / num2)

except ZeroDivisionError as z:
    print(z)
    