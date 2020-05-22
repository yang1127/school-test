class Circle:
    def __init__(self,r):
        self.r = r
    def GetGirth(self):
        return 2*3.1415926*self.r
    def GetArea(self):
        return 3.1415926*self.r*self.r
for i in range(10):
    myCircle = Circle(i+1)
    print("半径为 %d 的圆，面积： %.2f 周长： %.2f "%(i+1, myCircle.GetArea(), myCircle.GetGirth()))
