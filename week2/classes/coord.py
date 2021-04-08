from math import sqrt
class Coord:
    def __init__(self, *args):
        if (len(args) == 2):
            self.vector = args
            self.startPoint = (0, 0)
            self.endPoint = args
        elif len(args) == 4:
            self.startPoint = (args[0], args[1])
            self.endPoint = (args[2], args[3])
            self.vector = (args[2] - args[0], args[3] - args[1])
            
        else: raise Exception("Invalid constructor")

    def subtract(self, o):
        o = o.vector
        return Coord(*o,*self.vector)

    def dotProduct(self, o):
        o = o.vector
        return self.vector[0] * o[0] + self.vector[1] * o[1]
    
    def scalarProduct(self, num):
        return Coord(self.vector[0] * num, self.vector[1] * num)
    
    def addVector(self, o):
        a = self.vector
        b = o.vector
        return Coord(a[0] + b[0], a[1] + b[1])

    def getOrthogonalVector(self):
        v = self.vector
        return Coord(v[1], -v[0])

    def isParallel(self, v2):
        return (self.dotProduct(self) * v2.dotProduct(v2) - self.dotProduct(v2)**2) == 0

    def __str__(self):
        return "({}, {})".format(self.vector[0], self.vector[1])

    def getDistance(self,v2):
        v2 = v2.vector
        return sqrt((v2[0] - self.vector[0])**2 + (v2[1] - self.vector[1])**2)