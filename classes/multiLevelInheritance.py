class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("Fly")

## Too much inheritance is a bad thing.
## Maintaining multi-level inheritance can be difficult.

class Chicken(Bird):
    #A chicken cannot fly, but it inherits fly method from bird.
    # This is inheritance 'abuse'
    pass