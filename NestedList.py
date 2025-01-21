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