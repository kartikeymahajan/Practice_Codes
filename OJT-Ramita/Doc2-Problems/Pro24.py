'''24. Write a class that represents a circle.The circle should have a radius, a diameter,
and an area. It should also have a nice string representation.'''

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2*radius
        self.area = 3.14*(radius**2)

    def show(self):
        print(f'The details of my circle:\nRadius - {self.radius}\nDiameter - {self.diameter}\nArea - {self.area}')

obj = Circle(5)
obj.show()