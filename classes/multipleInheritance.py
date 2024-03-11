class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass

man = Manager()
#Python looks at the manager class first. then it looks at the Person class, and then it looks to the employee class.
#Changing the order of inheritance can change the functionality of an application, because of the overide.
#
## Why multi-level inheritance if it can cause problems?
man.greet()

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    #This is multiple inheritance. It is a good example of it.
    pass