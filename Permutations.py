from itertools import permutations

S = input().split()
print(S[0])
print(S[1])
for i in sorted(permutations(S[0],int(S[1]))):
    print(''.join(i))