class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        return (f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: {self.show()}")

    def add(self, other_point):
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        return Point(new_x, new_y)


p1 = Point(5, 3)
print(p1.show())
p1.move(7, 7)
p2 = p1.add(Point(3, 0))
print(p2.show())

