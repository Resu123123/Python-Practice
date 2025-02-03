from itertools import * 
n = int(input())
ls = input().split()
k = int(input())
com = list(combinations(ls, k))
print(com)
tol = [i for i in com  if "a" in i ]
print(f'{(len(tol)/len(com)):.12f}')