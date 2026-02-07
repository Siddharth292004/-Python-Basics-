try:
    num1 = int(input("Enter a numnber: "))

    if(num1 % 2 == 0):
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Please enter the valid value")