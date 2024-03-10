from sys import getsizeof

values = [x * 2 for x in range(10)] #list comprehension expression.
for x in values:
    print(x)
#Generator Objects are iterable.
    #Each iteration will generate a new value.

values2 = (x * 2 for x in range(100)) #tuples
print("Generator Expressions - Tuples")
print("gen: ", getsizeof(values2))
#Using a generator objects consumes less memory. This helps programs run efficiently.
for x in values2:
    print(x)
    #size of generator objects.

#This doesn't work.
print(len(values2))