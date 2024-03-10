#Handling Errors.
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError as exception:
#     print(exception)
# else: 
#     print("No exceptions were thrown.")
# This code will error on line 4 because there is no except clause that handles the type of error that raises,

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError as exception:
    print(exception)
except ZeroDivisionError:
    print("Age cannot be 0")
else: 
    print("No exceptions were thrown.")

try:
    age = int(input("Age: "))
    xfactor = 10 / age
# You can add multiple exception types within a single except clause.
    #The first matching error is the one that will be thrown.. even if there are other except clausess for other errors.
except (ValueError, ZeroDivisionError) as exception:
    print("You did not enter a valid age.")
else: 
    print("No exceptions were thrown.")
