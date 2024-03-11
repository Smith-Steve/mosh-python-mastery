#every class in python derives and inherits from the object class.
class Animal(object):
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")

class Mammal(Animal):
    
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

dog = Mammal()
print(isinstance(dog, object))
ob = object()
#This function follows the entire process of inheritance.
print(issubclass(Mammal, Animal))