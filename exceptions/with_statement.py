try:
    with open("exception.py") as file: #you can add multiple clauses here. For example, you could open more than one file.
        #this can read/write from file.
        print("File Opened")
    age = int(input("Age: "))
    xfactor = 10 / age
# You can add multiple exception types within a single except clause.
    #The first matching error is the one that will be thrown.. even if there are other except clausess for other errors.
except (ValueError, ZeroDivisionError) as exception:
    print("You did not enter a valid age.")
else: 
    print("No exceptions were thrown.")