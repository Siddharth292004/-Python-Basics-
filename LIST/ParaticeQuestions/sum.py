def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum



list = [1,2,3,4,5]
list_02 = [1, 2, -8]

print(sum_list(list))
print(sum_list(list_02))