# email = input("Enter your email id: ")
# username = email[:email.index('@')]
# domain = email[email.index('@') + 1:]

# print(f"Your Username is {username} and domain is {domain}")

# t = ['a','b','c','d']
# for i in t:
#     print(i, end='  ')

# for i in range(0, 10):
#     print(i,end = ' ')

letters = 'Rishabh'
# Slicing
great = letters[::-1] 
print(great)

def reverse_string(text):
    return text[::-1]
reference = reverse_string("Hello")
print(reference)    

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

input_str = 'Get extensive placement assistance with GUVI!'
print('Reverse String using for loop =', reverse_for_loop(input_str))

def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 += s[length]
        length -= 1
    return s1

input_str = 'Learn in your native language with GUVI!'
print('Reverse String using while loop =', reverse_while_loop(input_str))