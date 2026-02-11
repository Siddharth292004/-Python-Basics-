def Max_List(list):
    max = list[0]

    for i in list:
        if i > max:
            max = i
    return max

print(Max_List([1,2,3,4,5]))