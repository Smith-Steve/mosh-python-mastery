## A Set is a 'collection' w/ no duplicates.
## Sets are delineated by curly bracks
# numbers = [1,2,1,3,4]
# uniqueItems = set(numbers)
# print(uniqueItems)

# first = [1,1,2,3,444,4]
# first2 = set(first)
# second = [1,2,4,5]
# print(first2 | second)

numbers = [1,2,3,4,3]
first = set(numbers)
second = {1,5}

#This provides all unique items in set
print("'First | Second'",first | second)
#This shows us all items that are in BOTH sets.
print("'First & Second'", first & second)
#Show difference between two sets
print("'first - second'", first - second)
#
