# Write a Python program to calculate the length of a string.

def string_count(str1):
    
    count = 0

    for char in str1:
        count +=1

    return count


print(string_count("Hello, World!"))

print(string_count("Python Programming"))

text = "Python programming"
print(len(text))