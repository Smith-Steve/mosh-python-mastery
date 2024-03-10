age = 22

#ternary operator
message = "Eligible" if age >= 17 else "Not Eligible"
print(message)

if age >= 18 and age < 65:
    print("Eligible")

#For Loops:
print("For Loops Lesson")
for number in range(1, 10, 2):
    print("Attempt", (number) * ".")

#For Else:
print("For Else")
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    #This else statement will only be executed if we don't encounter any break.
    print("Attempted 3 times and failed.")

#Nested Loops:
print("Nested Loops")
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

#Iterables
print("Nested Loop")
for x in range(5):
    print(type(5))
    #Range is a 'complex' type.
    #Range objects are iterable.
    print(type(range(5)))

for x in "Python":
    print(x)

for x in [1,2,3,4]:
    print(x)

#While Loops:
print("While Loops")

number = 100
while number > 0:
    print(number)
    number = number // 2

command = ""
while command != "quit":
    command = input(">")
    print("ECHO: ", command)