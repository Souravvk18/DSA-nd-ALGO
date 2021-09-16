# Sparse Arrays

if __name__ == "__main__":
    strings = []
    N = int(input().strip())
    for _ in range(N):
        strings.append(input().strip())
        
    Q = int(input().strip())
    for _ in range(Q):
        substr = input().strip()
        print(strings.count(substr))

"""4 
abc
def
ijk
lmn

3
abc
1
xyz
0
def
1


6
abc
def
ijk
lmn
opq
rst

4
cde
0
abc
1
lmn
1
ijk
1"""