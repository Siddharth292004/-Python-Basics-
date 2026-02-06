"""
Reverse a string without slicing
"""
def reverse_string(string):
    result = ""
    for char in string:
        result = char + result
    return result

def reverse_string2(string):
    result = []
    for char in string:
        result.insert(0, char)
    return ''.join(result)

print(reverse_string("Hell0 World!"))
print(reverse_string2("Hell0 World!"))