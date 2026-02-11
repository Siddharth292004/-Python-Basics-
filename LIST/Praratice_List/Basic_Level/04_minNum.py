def Min_num_in_List(lst):
    min = lst[0]

    for i in lst:
        if i < min:
            min = i
    return min

print(Min_num_in_List([1,2,3,4,5]))