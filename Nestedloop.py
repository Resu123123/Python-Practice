# products_on_sale = ['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4']
# sale_prices = [100, 120, 135, 150]
# quantities = [1000, 1500, 1300]
# for prod in products_on_sale:
#     for sale in sale_prices:
#         for quan in quantities:
#           print(f"Expected revenue for {prod} if {quan} chairs are to be sold: {sale*quan}")

# if __name__ == '__main__':
#     print('Enter the values after giving spaces in between')
#     arr = list(map(int, input().split()))
#     sorted_score = sorted(arr,reverse = True)
    
#     runner_upscore = None
#     for score in sorted_score:
#         if score < sorted_score[0]:
#             runner_upscore = score
#             break
            
#     print("Answer value is: ", runner_upscore)

# To Print the names of 2nd low scorer.

if __name__ == '__main__':
    n = int(input())
    list1 = []
    list2 = []        

    for i in range(0,n):
        name = input()
        score = float(input())
        print(list1.append([name,score]))
        print(list2.append(score))


print(list1.sort())
print(list2.sort())
m = min(list2)
list2.remove(m)
m2 = min(list2)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] == m2:
            print("\n Names are" , list1[i][0])

