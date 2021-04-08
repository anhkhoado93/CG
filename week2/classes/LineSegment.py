from coord import *

class LineSegment:
    def __init__(self, p1, p2):
        self.coord1 = p1
        self.coord2 = p2
        self.vector = p2.subtract(p1)

    def getStartPoint(self):
        return self.coord1

    def getVector(self):
        return self.vector

    def getSegmentIntersection(self, line2):
        """
        p*: starting Point
        v*: Vector
        ==================
        p1 + v1 * t = p2 + v2 * u
        ...
        t = - ((p1 - p2) * v2_perp) / ( v1 * v2_perp )
        """
        p1, v1 = self.coord1, self.vector
        p2, v2 = line2.getStartPoint(), line2.getVector()
        vect = p1.subtract(p2)
        if v1.isParallel(v2):
            #how to check?
            if not v1.isParallel(vect): raise Exception("2 line segments are parallel: no solution")
        
        v2_perp = v2.getOrthogonalVector()
        t = - vect.dotProduct(v2_perp) / v1.dotProduct(v2_perp)
        if t < 0 or t > 1: 
            raise Exception("2 line segments do not intersect!")

        else: return p1.addVector(v1.scalarProduct(t))