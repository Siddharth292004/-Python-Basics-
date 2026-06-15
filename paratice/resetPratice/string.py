# String method are built-in functions in python that are used to perform operation on strings.such as:

name = "Python"
name.upper()
print(name)

# unchangeable

# String methods 
text = "Hello World"
print(text.lower())

# upper
print(text.upper())
#capitallize()
print(text.capitalize)
#title()
text1 = "python programming language"
print(text1.title())
#strip()
text2 = "  python   "
print(text2.strip())
# lstrip / rstrip()
print(text2.lstrip())
print(text2.rstrip())

text4 = "I like Java"
print(text4.replace('Java','Python'))

text5 = "Pytthon"
print(text5.find("z"))
#print(text5.index("z"))

# count

text6 = "banana"
print(text6.count("a"))


text7 = "Java"
print(text7.startswith("Ja"))
print(text7.endswith("va"))

text = "Python is easy"
print(text.split())

text8 = "Python is hardest language "
print(text8.split())

words = ['Python', 'is', 'hardest', 'language']
print(" ".join(words))


text9 = "python"
print(text9.isalpha())

text10 = "1234"
print(text10.isdigit())

text11 = "Python123"
print(text11.isalnum())
print(text11.isalnum())