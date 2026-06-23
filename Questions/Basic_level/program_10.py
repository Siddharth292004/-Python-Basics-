"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""


num = (input("Enter a interger value: "))

n1 = int(num)
n2 = int(num + num)
n3 = int(num + num + num)

print(n1 + n2 + n3)