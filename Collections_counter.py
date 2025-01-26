from collections import Counter

# Total number of shoes
n = int(input()) 
# List all shoe sizes
sizes = Counter(map(int,input().split()))
# Total number of customers
customer = int(input())

total = 0
for i in range(customer):
    size, rate = map(int, input().split())
    if sizes[size]: 
        sizes[size] -= 1
        total += rate
print(total)