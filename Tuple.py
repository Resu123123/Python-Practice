# To replace tuple element convert into list
x = ('Ford','Maruti','Kia')
y = list(x)
print(y)
y[2] = 'Hyundi'
x = tuple(y)
print(x)

# To add another element in tuple
a = ('Ford','Maruti','Kia')
b = ('Hyundi',)
a += b
print(a)