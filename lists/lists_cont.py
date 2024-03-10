items = [
    ("Car", 1),
    ("House", 18000),
    ("Boat", 22000),
    ("Gym", 500000)
]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

#Above we created a list of tubles.
## We used a for loop to pass the prices into a newly instantiated list.. called, 'prices'. There is a simpler way to do this.

result = list(map(lambda item: item[1], items))
# A map function recieves a lambda (I believe this is the equiv of an 'anonymous' function.)
##
print(result)