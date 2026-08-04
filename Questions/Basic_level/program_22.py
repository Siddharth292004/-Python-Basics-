# Write a Python program to count the number 4 in a given list


def count_four(lst):
    count = lst.count(4)
    return count


print(count_four([1, 2, 3, 4, 5, 4, 6, 4]))  # Output: 3