numbers = [1,2,3]
print(numbers)

#What if you want to get an output like print(1,2,3) - Just the list.. printing a list shows brackets.
print(*numbers)

values = list(range(5))
values2 = [*range(5)] #We can unpack any iterable. Doens't have to be a list.
values3 = [*range(5), *"Hello"]

#range function returns a list.
print(type(values2))
print("Unpacked List Generated via 'range' function", values2)
print(type(values3))
print("Different list unpacked: ", values3)

#We can also combine lists with this operator.
first = [1,2]
second = [3,4]
values4 = [*first, "A", *second, *"Hello"]

print(" ===== Unpacking Dictionaries Section =====")
#We can unpack dictionaries.
firstDict = {"x": 2}
secondDict = {"x": 10, "z": 10}
#unpacking dictionary.
combinedDictionary = {**firstDict, **secondDict, "z": 1}
print("Print First Dictionary: ", firstDict)
print("Print Second Dictionary: ", secondDict)
print("Unpacked Dictionaries - Into New Dictionaries: ", combinedDictionary)
# When unpacking a dictionary, if there are matching key value pairs, the second key/value pair is unpacked into the new.
# dictionary. 