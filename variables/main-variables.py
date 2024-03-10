students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
message = """
Hi Steve, this is Mosh from Mosh.com
"""

escape_example = "Python \"Programming\""
print(escape_example)

print(len(course_name[0:4]))

# Formatted Strings:
first = "Steve"
last = "Smith"
full = first + " " + last
## String Interpolation? What is this called?
full_test = f"{first} {last} - String Interpolation"
print(full_test)

# String Methods
course2 = "python programming"
print(course2.upper())
#Capitalize the First Letter of Every Word
print(course2.title())
#strip
print(course2.rstrip())
#find (Python is a case sensitive langauge.) This wil return -1 if there is no matching value.
print(course2.find("pro"))
#replace
print(course2.replace("p", "j"))
#This is an expression. This returns a true/false value.
print("pro" in course2)
#Not operator
print("swift" not in course2)

#Type Conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")