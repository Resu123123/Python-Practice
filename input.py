# # Take input as space-separated values
# input_str = input("Enter values: ")

# # Convert input string to list by splitting at spaces
# input_list = input_str.split()
# print(input_list)

# Take input as comma-separated values
# input_str = input("Enter values separated by commas: ")

# # Convert input string to list by splitting at commas
# input_list = input_str.split(',')

# # Strip spaces around elements, if any
# input_list = [item.strip() for item in input_list]
# print(input_list)

a = input()
b = list(map(int,a.split()))
print(b)

