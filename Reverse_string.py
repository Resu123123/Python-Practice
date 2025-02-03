# 1...Using Slicing[start,stop,step]

# name = str(input())
# print(name[::-1])
# print(name[slice(None,None,-1)])

#2....The reversed() function returns a reversed iterator
# rev_result = reversed(name)
# print(''.join(rev_result))

#3...Using for loop
# def reverse_string(input_val):
#     s1 = ''
#     for c in input_val:
#      s1 = c + s1
#     return s1

# name1 = str(input())
# print(reverse_string(name1))

#4...Using while loop
def reverse_string(input_val):
     s1 = ''
     length_string = len(input_val) - 1
     while length_string >= 0:
          s1 += input_val[length_string]
          length_string -= 1
     return s1

name1 = str(input())
print(reverse_string(name1))
