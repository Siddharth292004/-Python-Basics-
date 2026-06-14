age =  18 

if age >= 18:
    print("you can vote")
else:
    print("you can not vote")


# with elif

marks = 75

if marks >=90:
    print("Grade A")
elif marks >=70:
    print("Grade B")
else:
    print("Grade C")

for i in range(1,6):
    print(i)


name = "Python"

for ch in name:
    print(ch)

numbers = [10,20,30,40]

for num in numbers:
    print(num)


for i in range(5):
    print(i)


for i in range(1,11):
    print(i)

for i in range(2,11,2):
    print(i)

# a the never ends called infinite loop

#while True:
#    print("hello")

for i in range(1,11):
    if i == 6:
        break
    print(i)

# continue

for i in range(1,11):
    if i == 3:
        continue
    print(i)

# Nested loops
# a loops inside another loop


for i in range(1,4):
    for j in range(1,4):
        print(i,j)


num = 5

for i in range(1,11):
    print(num," * ",i," = ",num*i)

total = 0

for i in range(1,11):
    total +=i

print(total)


for i in range(2,22,2):
    print(i)


# print numbers from 1 to 100

for i in range(1,101):
    print(i)

# print even numbers from 1 to 50.

for i in range(2,51,2):
    print(i)

# find the sum of first 100 number.

total = 0

for i in range(1,101):
    total +=i

print("Sum =", total)

#

num = int(input("Enter a number:  "))


for i in range(1,11):
    print(num," * ",i," = ",num*i)

num = int(input("Enter a number: "))

fact = 1

for i in range(1,num+1):
    fact *=i

print(fact)

row = 5

for i in range(1,row +1):
    for j in range(i):
        print("*",end=" ")
    print()


for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()