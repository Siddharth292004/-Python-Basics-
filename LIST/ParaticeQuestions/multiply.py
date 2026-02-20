def multiply_list(lst):
    product = 1
    for x in lst:
        product *= x
    return product


print(multiply_list([3,1,2,3]))