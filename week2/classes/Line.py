from coord import *

class Line:
    def __init__(self, p, v):
        self.start = p
        self.vector = v

    def getStartPoint(self):
        return self.start

    def getVector(self):
        return self.vector

    def getLineIntersection(self, line2):
        """
        p*: starting Point
        v*: Vector
        ==================
        p1 + v1 * t = p2 + v2 * u
        ...
        t = - ((p1 - p2) * v2_perp) / ( v1 * v2_perp )
        """
        p1, v1 = self.start, self.vector
        p2, v2 = line2.getStartPoint(), line2.getVector()
        vect = p1.subtract(p2)
        if v1.isParallel(v2):
            #how to check?
            if not v1.isParallel(vect): raise Exception("2 line segments are parallel: no solution")
        
        v2_perp = v2.getOrthogonalVector()
        t = - vect.dotProduct(v2_perp) / v1.dotProduct(v2_perp)

        return p1.addVector(v1.scalarProduct(t))

    