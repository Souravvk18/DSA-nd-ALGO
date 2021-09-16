# import sys

# def leftRotation(a, d):
#     out = list(a)
#     a_len = len(a)
#     for ind, el in enumerate(a):
#         out[(ind + a_len - d) % a_len] = el

#     return out
        
# if __name__ == "__main__":
#     n, d = input().strip().split(' ')
#     n, d = [int(n), int(d)]
#     a = list(map(int, input().strip().split(' ')))
#     result = leftRotation(a, d)
#     print (" ".join(map(str, result)))

"""
i/p- 
5 4
1 2 3 4 5
o/p- 
5 1 2 3 4 
"""


def rotate(arr, n , d):
    temp= []
    i=0
    while (i<d):
        temp.append(arr[i])
        i= i+1
    i= 0
    while (d<n):
        arr[i] = arr[d]
        i= i+1
        d= d+1
    arr[ : ] = arr[ 0 : i] + temp
    return arr
n=int(input())
arr = [int(array) for array in input().split(' ')]
print("array after the rotation is:")
print(rotate(arr,n, 4))


"""
5
1 2 3 4 5
array after the rotation is:
[5, 1, 2, 3, 4]"""
