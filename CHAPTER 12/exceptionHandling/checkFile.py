try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")



"""
try:
    # code
except ErrorType1:
    # handle error
except ErrorType2:
    # handle error
else:
    # runs if no error
finally:
    # always runs


"""