values = []
for x in range(5):
    values.append(x * 2)

#List comp syntax
    #[exporession for item in items]
    #our iterable in this case is, 'range'

values = {x: x * 2 for x in range(5)}
print(values)

for y in range(5):
    values[x] = x * 2

print("Tuples")

values2 = (x * 2 for x in range(5))
#This returns a 'generator topic'
print(values2)