# 1 - create list of 100 random numbers from 0 to 1000
import random

list100 = []  # declare variable
for i in range(100):  # number of random numbers
    a = random.randint(0, 1000)  # range of random numbers
    list100.append(a)  # use append - this function add value for each iteration.
print("""100 random numbers:
""" + str(list100))  # print result for checking

# 2 - sort list from min to max (without using sort())
for i in range(0, len(list100)):  # min
    for j in range(i, len(list100)):
        if list100[i] > list100[j]:  # compare with the previous number
            list100[i], list100[j] = list100[j], list100[i]
print("""Sorted values from min to max:
""" + str(list100))  # print result for checking

# 3 - calculate average for even and odd numbers
sum_even = 0  # declare variable for summing even values
sum_odd = 0  # declare variable for summing odd values
count_even = 0  # declare variable to measure count of even values
count_odd = 0  # declare variable to measure count of odd values

for i in list100:  # loop to find even/odd values and count them
    if i % 2 == 0:  # find even values
        sum_even += i  # sum even values
        count_even += 1  # sum count of even values
    else:
        sum_odd += i  # sum odd values
        count_odd += 1  # sum count of odd values

# 4 - print both average result in console
print('Average for even values:', sum_even / count_even)
print('Average for odd values:', sum_odd / count_odd)
