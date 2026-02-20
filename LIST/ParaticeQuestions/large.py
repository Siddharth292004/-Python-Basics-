#  Write a Python program to get the largest number from a list.

def largest_num(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest


print(largest_num([1,2,3,4,5]))