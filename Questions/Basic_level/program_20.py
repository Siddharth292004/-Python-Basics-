"""
Write a Python program that returns a string that is n (non-negative integer)
copies of a given string
"""

def large_string(text,n):

    result  = ""

    for i in range(n):
        result = result + text
    
    return result

print(large_string("abc ",3))
print(large_string("Mark ",2))