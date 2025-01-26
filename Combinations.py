from itertools import combinations

a = input().split()
print(a[1])

for i in range(1, int(a[1]) + 1):
    for j in combinations(sorted(a[0]), i):
        print(''.join(j))

# Combinations_with_replacement 

from itertools import combinations_with_replacement
S = input().split()

for i in combinations_with_replacement(sorted(S[0]),int(S[1])):
     print(''.join(i))