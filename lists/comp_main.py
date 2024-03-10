#List Comprehension.

items = [("Product", 10), ("Product 2", 30), ("Product 3", 100), ("Product 4", 9)]
prices = list(map(lambda item: item[1], items))

# [expression for item in items]
##In python, the preferred way to map and filter lists is through 'list comprehension.'
prices2 = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
#If we wanted to perform a similar function to the above (in 'filtered' variable) through list comprehension we would..
## filtered2 = [expression for item in items]
filtered2 = [item for item in items if item[1] >= 10]
print(filtered2)
## This prints out - [('Product', 10), ('Product 2', 30), ('Product 3', 100)] (Does not include last touple)