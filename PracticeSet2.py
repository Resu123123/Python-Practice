# 6 Find missing number

# def missing_num(nums:list , n:int) -> int:
#     expected_sum = 0
#     for i in range(1, n+1):
#         expected_sum += i
#     actual_sum = 0
#     for j in nums:
#         actual_sum += j
#     return expected_sum - actual_sum    
   
# # User input
# n = int(input("Enter the total number n: "))
# nums = list(map(int, input(f"Enter the {n-1} numbers (separated by space): ").split()))

# # Find the missing number
# missing_number = missing_num(nums, n)
# print(f"The missing number is: {missing_number}")

# 7 Count occurences of an element in a List
# def counter(nums:list , target: int) -> int:
#     count = 0
#     for num in nums:
#         if num == target:

a = "A1dsa75fewr"
b = "Cool"
print(a.swapcase())
print(a.islower())
print(a*3)
print(a + ' ' + b)
print(a[:])
print(a[::2])
print(a[::-1])
