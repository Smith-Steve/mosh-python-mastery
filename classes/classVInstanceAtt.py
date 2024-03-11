class Point:
    default_color = "red"
    #This is a class level attribute.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
point.z = 10
#We dont' have to define all attributes of a class in a constructor. They can be added later.
point.draw()
print(point.default_color)


another = Point(3,4)
#a seperate instance of the class.
## Class Attributes can be defined at the class level.
## They are shared by all instances of the class.