point = (1,2,3,4) #Touple definition
point2 = 1,2,46,4 #You can also define touples this way also.

#If you only have one item in a touple, you must add a comma as a suffix or else it will be defined as the datatype it would be w/out the comma.

#convert list to touple.
convertToTouple = tuple([1,2])
convertToTouple2 = tuple("Hello World")
print(convertToTouple)
print(point[0:1])

if 10 in point:
    print("Exists")
    print("Tuples are immutable. They cannot be changed.")

##Where would you use a touple?
    #If you don't want to modify a sequence, or change it in anyway. It is good for preventing accidental errors
