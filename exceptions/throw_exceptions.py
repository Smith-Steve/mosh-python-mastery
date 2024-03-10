from timeit import timeit

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

##Best way to handle exceptions in tandem with performance.
    #Exceptions come at a cost.
    #Python Developers should avoid throwing exceptions.

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
print("First Code = ",timeit(code1, number=10000)) #This allows us to understand how long it takes the function to run.

#none is absence of value
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
#If you want to raise an exception in your code, think twice.
#See if you can find another way to control the exception without raising error.
# Below code demonstrates that the second body of code (in 'code2') runs faster.
print("Second Code = ",timeit(code2, number=10000))

