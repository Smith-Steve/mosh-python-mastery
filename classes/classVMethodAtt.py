class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Whenever we define a class method, we pass it a param named crs.
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.z = 10
point.draw()
print(point.default_color)


another = Point(3, 4)
# This is a class reference. This is a 'factory method' becuase it creates a new instance.
newPoint = Point.zero()
# This allows you to effectively instantiate a instance of the class, with the values already passed in.
