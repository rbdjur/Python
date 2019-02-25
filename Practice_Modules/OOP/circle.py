class Circle():
    #class object attribute
    pi = 3.14
    
    #instances of this class Circle
    def __init__(self, radius = 1):
        self.radius = radius

    def circumference(self):
        return self.pi * self.radius * 2

    def area(self):
        return (self.radius ** 2) * Circle.pi

# my_circle = Circle()
my_circle = Circle(30)
#The code above would overwrite the radius assignment of 1 in the class Circle. 

print(my_circle.radius) #1

print(my_circle.circumference()) #3.14 / 188.4

print(my_circle.area())

#Success