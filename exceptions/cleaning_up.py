try:
    file = open("exception.py")
    age = int(input("Age: "))
    xfactor = 10 / age
# You can add multiple exception types within a single except clause.
    #The first matching error is the one that will be thrown.. even if there are other except clausess for other errors.
except (ValueError, ZeroDivisionError) as exception:
    print("You did not enter a valid age.")
else: 
    print("No exceptions were thrown.")
finally:
    #This line is always run, no matter whether or not we hit the 'except' block or the 'else' block.
    file.close()

# try:
#     file = open("exception.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
#     file.close()
# # In the above example, if line 15/16 is the line of code that throws the error, than
#     # the file ("file" variable) won't be closed.
# except (ValueError, ZeroDivisionError) as exception:
#     print("You did not enter a valid age.")
# else: 
#     print("No exceptions were thrown.")