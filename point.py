import math
class point:
    _count=0
    def __new__(cls,*args):
        cls._count=cls._count+1
        if cls._count>5:
            raise TypeError("Can't create more than 5 objects")
        else:
            return object.__new__(cls)
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    def dist(self,p):
        d=math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)
        return d
    def o_dist(self):
        d=math.sqrt((self.x**2)+(self.y**2))
        return d
    def midpt(self,p):
        p.x=(self.x+p.x)/2
        p.y=(self.y+p.y)/2
        return p
p1=point(4,5)
p2=point(7,9)
print("Distance between (4,5) and origin:",p1.o_dist())
print("Distance between (4,5) and (7,9)",p1.dist(p2))
p=p1.midpt(p2)
print("Midpoint of (4,5) and (7,9):(",p.x,",",p.y,")")
p3=point(3,4)
p4=point(4,5)
p5=point(5,6)
p6=point(6,7)
