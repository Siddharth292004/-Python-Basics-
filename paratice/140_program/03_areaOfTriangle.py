try :
     
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the length of the base of the triangle: "))

    area = 0.5 * base * height

    print(f"The area of the triangle is: {area}")

except ValueError:
    print("Invalid input. Please enter numeric values for height and base.")