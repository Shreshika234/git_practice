class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
         
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return  int(((x2-x1)**2+(y2-y1)**2)**0.5)
        
    
    def slope(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return int((y2-y1)/(x2-x1))

coor1 = (3,2)
coor2 = (8,10)

my_line_4= Line(coor1,coor2)

print(my_line_4.distance())
print(my_line_4.slope())