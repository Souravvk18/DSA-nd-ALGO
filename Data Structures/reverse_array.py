# Arrays - DS


import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(" ".join(map(str, arr[::-1])))


"""
o/p- 4
4 3 2 1
1 2 3 4"""


# import sys
# n = int(input("enter the length:"))
# print("enter the array value:")
# arr = [int(array) for array in input().split(' ')]

# # print(" ".join(map(str, arr[::-1])))
# print("The reverse value is: ",arr[::-1])

"""enter the length:4
enter the array value:
10 15 20 25
The reverse value is : [25, 20, 15, 10]"""