#Dictionaries.
#Collection of 'key' and 'value' pairs.

#Phone book. Name ("Key") and Phone-Number ("Value")
point = {"x", 1, "y", 2}

#you can also use the "dict" fucntion to create a dictionary.

#This syntax is cleaner and shorter.
point2 = dict(x=1,y=2)
print(point2["x"])

#When reading a value, if we enter an improper value an error is thrown.

#You cna check for existence of key.
if "a" in point2:
    print(point2["A"])

#We can also use 'get'
print(point2.get("a"))

# 'del' is used to delete.

#we can iterate over them.
print("Iterate over dictionary")
for key in point2:
    print(key, point2[key])

for key, value in point2.items():
    print(key, value)

##Dictionary 