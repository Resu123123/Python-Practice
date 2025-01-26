# if __name__ == '__main__':
#     s = input()
#     res = "True" if s.isalnum() else "False"
#     print(res) 
#     res1 = "True" if s.isalpha() else "False"
#     print(res1) 
#     res2 = "True" if s.isdigit() else "False"
#     print(res2) 
#     res3 = "True" if s.islower() else "False"
#     print(res3) 
#     res4 = "True" if s.isupper() else "False"
#     print(res4) 

if __name__ == '__main__':
  string = input()

# Check for alphanumeric characters
  print(any(c.isalnum() for c in string))

# Check for alphabetical characters
  print(any(c.isalpha() for c in string))

# Check for digits
  print(any(c.isdigit() for c in string))

# Check for lowercase characters
  print(any(c.islower() for c in string))

# Check for uppercase characters
  print(any(c.isupper() for c in string))