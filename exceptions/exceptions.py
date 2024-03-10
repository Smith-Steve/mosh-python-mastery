#Handling Errors.
try:
    age = int(input("Age: "))
except ValueError as exception:
    print("You didn't enter a valid age.")
    print(exception)
    print(type(exception))
else: #This is an optional clause of a try block.
      #This is the block of code that will operate after the except evaluation is skipped.
      #This is only thrown when
    print("No exceptions were thrown.")

##Handling exceptions prevents applications from crashing.
