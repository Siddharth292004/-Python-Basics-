#Write a Python program to find the first appearance 
# of the substrings 'not' and 'poor' in a given string. 
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
#  Return the resulting string

def replace_not_poor(str1):
    not_index = str1.find('not')
    poor_index = str1.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        str1 = str1[:not_index] + 'good' + str1[poor_index + 4:]

    return str1

print(replace_not_poor('The lyrics is not that poor!'))  # Output: 'The lyrics is good!'
print(replace_not_poor('The lyrics is poor!'))  # Output: 'The lyrics is poor!'