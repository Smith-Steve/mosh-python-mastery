class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10,20)
other = Point(1,2)

#This compares the objects in memory, their location I presume, etc..

combined = point + other

print(combined.x)

#Performing Arithmatic Operations
