list1 = [1,2,3]
list2 = [10,20,30]
#How do we combine lists?
## How can we combine these lists,and turn them into a single list of touples?

# [(1, 10), (2, 20), (3,30)] HOw do we get this?

print(zip(list1, list2))
#This returns a 'zip' object that is iterable.
print(list(zip( "ABC",list1, list2)))