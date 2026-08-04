# Write a Python program to get a string made of
#  the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
# Scripting Languages


def string_both_ends(str1):
    if len(str1) < 2:
        return ''

    return str1[:2] + str1[-2:]


print(string_both_ends('w3resource'))  # Output: 'w3ce'
print(string_both_ends('w3'))          # Output: 'w3w3'
print(string_both_ends('w'))           # Output: '' 