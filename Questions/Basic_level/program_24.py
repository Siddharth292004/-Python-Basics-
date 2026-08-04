# Write a Python program to test whether a passed letter is a vowel or not.Scripting Languages

def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False

print(is_vowel('a'))  # Output: True
print(is_vowel('b'))  # Output: False