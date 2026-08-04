# Write a Python program that checks whether a specified value 
# is contained within a group of values.


def is_group_member(group_data,n):

    #if value in group:
    #    return True
    #else:
    #    return False

    for value in group_data:

        if n == value:
            return True
    return False

print(is_group_member([1, 5, 8, 3], 3))  # Output: True
print(is_group_member([1, 5, 8, 3], -1))  # Output: False
