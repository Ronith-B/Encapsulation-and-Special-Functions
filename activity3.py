
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)
print(p1)

p2 = Point(4,7)
print(p2)

p3 = Point(9,1)
print(p3)

p4 = Point(-3,8)
print(p4)
