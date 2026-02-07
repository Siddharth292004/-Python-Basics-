"""
What is the walrus operator?
The walrus operator is :=
It assigns a value to a variable AND returns that value at the same time.
👉 Introduced in Python 3.8
"""

# simple term: you can assign a value to a variable and use it in the same expression
# without the walrus operator, you would have to do this in two steps:

if (n := len("walrus operator")) > 10:
    print(f"The string is too long with {n} characters.")


if (n := len("siddharth singh")) > 12:
    print("this is too long")


# variable := expression
  

while (data := input("Enter something: ")) != "exit":
    print(data)

