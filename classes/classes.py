#Classes are a 'blueprint' for creating new objects.

#Creating Classes:
## Pascal naming convention is applied.
## Do not use underscore to seperate multiple words.
class Point:
    def draw(self):
        print("Draw")
    
point = Point()
point.draw()

#Is Instance - Determine if an object is an instance of a class.
## This returns true.
print(isinstance(point, Point))

