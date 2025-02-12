# 1 Fibonacci series

# def fibo(n):
#     fib_series = [0,1]
#     while len(fib_series) < n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series    

# num = int(input())
# print(f"Fibonacci series with {num} terms:")
# print(fibo(num))

# 2 Reverse a string 

# def rev(n):
#     s1 = ''
#     for char in n:
#         s1 = char + s1
#     return s1
    
# value = str(input())
# print(rev(value))    

# 3 Small and large
# def find_largest_smallest(nums):
#     largest = nums[0]
#     smallest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#         if num < smallest:
#             smallest = num
#     return largest, smallest

# # Get user input and split it into a list
# user_input = [12,32,42,43,45,32,43,56]
# print(find_largest_smallest(user_input))

# 4 Reverse a number
# def palindrome(num):
#     a = 0
#     c = num
#     while num > 0:
#         r = num % 10
#         num = num // 10
#         a = (10 * a) + r
#     if a ==c:
#         return True
#     else:
#         return False

# num = int(input())
# print(palindrome(num))  

# 5 Sum of digits
def sum(num):
    c = 0
    while num > 0:
        c += num % 10
        num = num // 10
    return c
value = int(input())
print(sum(value))
