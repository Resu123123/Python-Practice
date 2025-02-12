class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")

person1 = Person('John',31)
person2 = Person('Hardik',21)

person1.show()
person2.show()        