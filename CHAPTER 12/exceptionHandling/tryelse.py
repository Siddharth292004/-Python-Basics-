try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero error")
else:
    print("Calculation successful")

#else runs only if NO exception occurs.