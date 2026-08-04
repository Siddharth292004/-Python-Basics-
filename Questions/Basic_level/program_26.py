# Write a Python program to create a histogram from a 
# given list of integers.

#def histogram(lst):
#    for num in lst:
#        print('*' * num)


def histogram(lst):
    for n in lst:
        output = ''
        times = n

        while times > 0:
            output += '*'
            times -= 1

        print(output)

histogram([4, 9, 7])   