# 2D Array - DS

import sys

arr =[]
for i in range(6):
    j = [int(temp) for temp in input().split(' ')]
    arr.append(j)

sum = 0
for k in range(6-2):
    for m in range(6-2):
        temp = 0
        temp += arr[k][m] + arr[k][m+1] + arr[k] [m+2]
        temp += arr[k+1][m+1]
        temp +=arr[k+2][m] + arr[k+2][m+1] + arr[k+2][m+2]

        if k ==0 and m == 0:
            sum = temp
        else:
            sum = max(sum, temp)
print(sum)

"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

19"""