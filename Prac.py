print("\"\"\"Hello, my name is \"Rishabh\'s\".How do you do\"\"\"")
# R to left associativity
print(2**3**2**1) 
print('"Python uses \n new line"')
print('"Python uses \\n new line"')
print('//')
print('/\\/\\/\\')

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(list(zip(a,b,c)))

print(10.0//3)
print(-10//3)
print(10//3)

x = 2E3
print(type(x))

str1 = "Sky is blue"
print(' '.join(str1.split()[::-1]))

my_list = [1,2,2,3,4,5,4,4,5,5,6]
print([num for num in my_list if my_list.count(num) == 1])

str2 = "a,a,a,b,b,b,c,c,c,d,d"
my_list = str2.split(',')
visited = []
final_list = []
for ch in my_list:
    if ch not in visited:
        final_list.append(f"{ch}:{my_list.count(ch)}")
        visited.append(ch)
print(','.join(final_list))        