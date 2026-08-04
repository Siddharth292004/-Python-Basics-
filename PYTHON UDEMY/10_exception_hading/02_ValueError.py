try:
    n = 0
    res = 100 / 0

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is ",res)
finally:
    print("Exceution complete")