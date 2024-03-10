from array import array
#arrays are good if you have a large set of numbers.
## For 90% of problems, you would use a list.
## lists are primarily a functionality data type - you can speed up an app by using an array over a standard list.

## The array function takes two args.
### The first is 'typecode' which is the data type that will go into the array.
#### It is a string.
#### Each data type has a single char string that indicates to the function what kind of data will be in the array.

numbers = array("i", [1,2,3])
numbers.append(5)
#You can use 'pop' and many list methods.
#If you try to add a different type of data type it an array than the type of array that was defined, you will recieve an error.


