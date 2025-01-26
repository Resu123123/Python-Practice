# def print_formatted(number):
#     # your code goes here
#     for i in range(1,number):
#         print(i,end=' ')
#     for j in range(1,number):
#         print(oct(j)[2:], end=' ')
#     # loop through the numbers from 1 to N
#     for i in range(1, n+1):
#     # use string formatting to convert the number to hexadecimal
#         hex_value = "{0:X}".format(i)
#     # print the hexadecimal value
#         print(hex_value, end=" ")      
#     for i in range(1, n+1): 
  
#         # using bin to print binary value 
#         print(int(bin(i).split('0b')[1]), end=" ")      

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# def print_formatted(number):
#     pad = number.bit_length()
#     for i in range(1,number+1):
#         print(str(i).rjust(pad),oct(i).split("o")[1].rjust(pad),hex(i).split("x")[1].upper().rjust(pad),bin(i).split("b")[1].rjust(pad))
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n) 

def print_formatted(number):
    nbin = format(number,'b')
    size = len(nbin)
    for i in range(1,n+1):
        octa = format(i,'o')
        hexa = format(i,'X')
        bina = format(i,'b')
        
        print(str(i).rjust(size),str(octa).rjust(size),str(hexa).rjust(size),str(bina).rjust(size))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)       