#Defining Functions:
def greet():
    print("Hi there! Welcome Aboard!")

greet()

#Arguments:
##Nothing valuable in this lesson.

#Types of Funtions
## Two types of functions:
### 1. Perform a Task
### 2. Return a value.

def greet2(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"
#This is a better version of the two. It just returns the value.

message = get_greeting("Stephen")
file = open("content.txt", "w")
file.write(message)

#Key Word Arguements:
def increment(number, by):
    return number + by

result = increment(2, 1)
print(result)

## You can call functions like this:
increment(2, by=1)

#Default Arguments:
def increment2(number, by=1):
    return number + by
print(increment2(2,))

#default Xargs
def multiply(*numbers):
    print(numbers)
## We can't pass more than two args.

multiply(2,3,4,5)

#Touples:
## Similar to lists, but you can't modify it. Touples are iterable.

def multiply2(*numbers):
    total = 1
    for number in numbers:
        total *= number #shorter clearner
        print(number)
    return total
print(multiply2(2,3,4,5))

#XXarges
def save_user(**user):
    print(user["id"])
#We can pass keyword args
    ##XXargs return dictionaries. Equiv of 'object' in javascript.
    
save_user(id=1, name="john", age=22)

def multiply3(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total