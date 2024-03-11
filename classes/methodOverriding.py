#every class in python derives and inherits from the object class.
class Animal(object):
    #if there is a method in the parent that is defined in the base, than it overwrites
    def __init__(self):
        print("Aniaml Constructor")
        self.age = 1
    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__() #This allows us to invoke the init method of the 'animal' class
        self.weight = 2
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(m.age)
print(m.weight)
