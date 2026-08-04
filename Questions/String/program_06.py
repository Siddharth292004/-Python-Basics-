#Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged


def add_ing_or_ly(str1):
    if len(str1) < 3:
        return str1
    elif str1.endswith('ing'):
        return str1 + 'ly'
    else:
        return str1 + 'ing'


print(add_ing_or_ly('play'))  # Output: 'playing'
print(add_ing_or_ly('playing'))  # Output: 'playingly'