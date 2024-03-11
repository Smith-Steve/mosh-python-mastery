#Classes are a 'blueprint' for creating new objects.


class Point:
    #This is a 'magic method'.
    # All methods in Python should have a single parameter.
    #Self is a ref to the current object.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1,2)
point.draw()
