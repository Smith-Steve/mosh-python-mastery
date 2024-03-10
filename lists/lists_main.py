#Lists can hold any data type.
letters = ["a", "b", "c"]

#LIst of lists... there is a matrix here.
listOfList = [["A", "B"], ["C", "D"]]

zeros = [0] * 100
print(zeros)
#You can combine lists:
## In this way the old list is appended to the new list.
combined = zeros + letters
print(combined)

#list function
##Range function returns an iterable. 

newList = list(range(20))

##list can turn any sequence into a seperate iterable list.
print(newList)

#Accessing Items in a list:
letters2 = ["A", "B", "C", "D"]
letters2[3] = "F"
## Lists can be changed.
print(letters2)

print("Print original list", letters2)

numbers2 = list(range(20))
print(numbers2)


#List Unpacking:
numbers4 = [2,4,5]
first = numbers4[0]
second = numbers4[1]



##Lists can be unpacked into multiple variables.
first, second, *other = numbers4
## "Other" is a generalized, seperate list.
print(first)
print(second)
print(other)

##Looping over lists:
letters5 = ["A", "B", "C", "D"]
def enumerate2(letters):
    for letter in enumerate(letters):
        #tuples are read only.
        #Accessing the properties of a tuple is similar to accessing the properties of a list. Through indices.
        print(letter)
        print("End of initial for loop")
    items = (0, "a")
    index, letter = items
    print("We're hitting the next print statement.")
    for index, letter in enumerate(letters):
        print(index, letter)

#You can use for loops to iterate over lists.
#Calling enumerate allows you to iterate over a list.
enumerate2(letters5)

#Adding/Remove items from a list.
def removeAddList():
    letters = ["A", "B"]
    #Add item to an end of a list.
    letters.append("C")
    #insert somewhere in the list. To do this you must provide the index in the list where you'd like the item to be.
    letters.insert(0, "Z")
    print(letters)

#Remove
    letters.pop() 
    #This removes the last item in a list.
    ## You can also remove an item by selecting its index. The default arguement is the last item.

    ##Remove method.
    letters.remove("B") #This one will remove the first "B" discovered in the list.

    #Delete statement
    ## You can remove either one item, or you can remove a range of items.
    del letters[0:3]

    #Remove all

##Finding Items in a List:
def findIndex():
    letters = ["A", "B", "C", "D"]
    if "A" in letters:
        print(letters)
    #Most programming languages return 'error' if an item is not in a list.
    #In python, the program throws an error
        print(letters.index("C"))
    ## Count allows you to count the number of occurences in a list.   

findIndex()

def sortComplexlists(item):
    return item[1]

def sortingLists():
    print("Sorting Lists Function")
    numbers = [1,33,4,22,2]
    #'Sort' returns a modified version of the original list. The list is changed, and so is the variable, list etc..
    print("Demonstartion of 'sort' method")
    numbers.sort() #returns the list from the lowest number item to the highest.
    numbers.sort(reverse=True) #returns the list in reverse order.

    #Sorted Function - Takes an Iterable.
    print(sorted(numbers), "Demonstartion of 'sorted'") #This will return a 'new' list that is sorted
    print(sorted(numbers, reverse=True)) #You can control the order of the list here.

    #Ordering lists in complex data types.
    items = [("Product", 10), ("Product2", 9), ("Product3", 3)]

sortingLists()



#Lambda Functions:
#Lambda Functions are Anonymous Functions you can pass to other functions
def sort_item(item):
    item.sort(key=lambda item:item[1])
    

