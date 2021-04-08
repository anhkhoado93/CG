from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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


class Ray:
    def __init__(self, p, v):
        self.start = p
        self.vector = v

    def getStartPoint(self):
        return self.start

    def getVector(self):
        return self.vector

    def getRayIntersection(self, line2):
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
        if t < 0: 
            raise Exception("2 ray segments do not intersect!")


        return p1.addVector(v1.scalarProduct(t))


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

    def draw(self, color = None):
        glBegin(GL_LINE_STRIP)
        if color:
            glColor3f(*color)
        glVertex2f(*self.coord1.vector)
        glVertex2f(*self.coord2.vector)
        glEnd()

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

    def draw(self, t_range = [-500, 500], color = None):
        """
        L(t) = A + b*t
        """

        A = self.start
        b = self.vector
        glBegin(GL_LINE_STRIP)

        if color:
            glColor3f(*color)

        for i in range(t_range[0], t_range[1] + 1):
            newCord = A.addVector(b.scalarProduct(i))
            glVertex2f(*newCord.vector)

        glEnd()


class Plane:
    def __init__(self, p, v1, v2):
        self.start = p
        self.v1 = v1
        self.v2 = v2
