# Write a Python program to count the number 4 in a given list


def count_four(lst):
    count = 0

  # count = lst.count(4)  # This line is commented out, but it can be used as an alternative way to count the number of 4s in the list
    for num in lst:
        if num == 4:
            count += 1

    return count


print(count_four([1, 2, 3, 4, 5, 4, 6, 4]))  # Output: 3

