items = [
    ("Car", 1),
    ("House", 18000),
    ("Boat", 22000),
    ("Gym", 500000)
]

#What if we want to get a list of all items equal to or greater than 10.

#Filter takes two arguements. A function, and an iterable.
## Essentially it takes in a function and

##The result of this function is an boolean value.
### In the cases where it is above 10, presumably the list will be updated to include that item.
result = filter(lambda item: item[1] >= 10, items)
print(result)