class Line():
    def __init__(self, coor1, coor2):
        print("initialized")
        self.coor1 = coor1
        self.coor2 = coor2
        # x1 = coor1[0]
        # y1 = coor1[1]

        # x2 = coor2[0]
        # y2 =coor2[1]

    def slope(self):
        print("inside slope class")
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1] 
        #correct formula for slope
        return f"The slope for {self.coor1} and {self.coor2} is " + str(( (y2 - y1)/ (x2 - x1) ))     

    def distance(self):
        print("inside distance class")
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1] 

        #correct formula for distance
        return f"The distance for {self.coor1} and {self.coor2} is " + str(((x2 - x1)**2 + (y2 - y1)**2)**.5)



        



# a = Line(coor1 = (1,2), coor2 = (3,4))

a = Line(coor1 = (4,12), coor2 = (8,10))

print(a.slope())
print(a.distance())
    
