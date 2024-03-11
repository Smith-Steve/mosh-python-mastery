class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")

class Mammal(Animal):
    #since we're passing the 'animal' class, it is the parent class.
    
    def walk(self):
        print("walk")
#demonstration of inheritance.
#Dry in Programming means - "Don't Repeat Yourself"
class Fish(Animal):
    def swim(self):
        print("swim")

dog = Mammal()
dog.eat()
print(dog.age)