# Inheritance
class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def show(self):
        print(f"My car is {self.brand}")    

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand}, Model: {self.model}")

my_car = Car("Toyoto","Crysta")
my_car.show()
my_car.display_info()   

# Polymorphism
class Animal:
    def sound(self):
        return "Some Generic Animal Sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"        
    
my_dog = Dog()
my_cat = Cat()

print(my_dog.sound())
print(my_cat.sound())

# Method Overloading
class Calculator:
    def add(self,*args):
        return sum(args)

calc = Calculator()

print(calc.add(5))
print(calc.add(3,4))
print(calc.add(3,4,5))
print(calc.add(4,5,53,5))

# Static Method
class Mathoperations:
    @staticmethod
    def add(a,b):
        return a + b
    
result = Mathoperations.add(5,4)
print(result)    

# Multiple inheritance
class Parent1:
    def display(self):
        print("Parent1")
class Parent2:
    def display(self):
        print("Parent2")
class Child(Parent1,Parent2):
    pass

childo = Child()
childo.display()
childo.display()
