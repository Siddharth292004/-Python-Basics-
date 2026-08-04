# Write a Python program to get n (non-negative integer) copies of 
# the first 2 characters of a given string. Return n copies of the 
# whole string if the length is less than 2.

def string_copies(str1, n):

    #if len(str1) < 2:
    #    return str1 * n
    #else:
    #    return str1[:2] * n


    #return str1[:2] * n if len(str1) >= 2 else str1 * n
    flen = 2

    if flen > len(str1):
        flen = len(str1)

    substring = str1[:flen]

    result = ""

    for i in range(n):
        result += substring
        
    return result

print(string_copies('Python', 3))  # Output: 'PyPyPy'
print(string_copies('Py', 5))      # Output: 'PyPyPyPy