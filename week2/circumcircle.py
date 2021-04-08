import sys
from util import Coord, Line, LineSegment
from math import sqrt, pi, sin, cos
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


triangle_v = []

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, 0.0, 1.0)

def getPerpendicularBisector(p1, p2):
    """
    Perpendicular Bisector = midpoint + v
    """
    vect = p2.subtract(p1)
    vect_perp = vect.getOrthogonalVector()
    midpoint = p1.addVector(vect.scalarProduct(1/2))

    return Line(midpoint, vect_perp)

def draw2DAxis():
    xAxis = LineSegment(Coord(-1.0, 0.0), Coord( 1.0, 0.0))
    xAxis.draw(color = (1.0, 1.0, 1.0))

    yAxis = LineSegment(Coord(0.0, -1.0), Coord(0.0, 1.0))
    yAxis.draw(color = (1.0, 1.0, 1.0))

def display():
    global triangle_v
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(1.5)
    draw2DAxis()
    if len(triangle_v) > 1:
        drawTriangle()
    if len(triangle_v) == 3:
        
        center, radius = calculateCircle()
        drawCircle(center, radius)
    glFlush()


def drawTriangle():
    global triangle_v
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    
    for i in triangle_v:
        glVertex2f(float(i[0]), float(i[1]))
    glEnd()


def drawCircle(center, radius):
    center = center.vector

    div = 50
    step = 2 * pi / div
    angle = 0
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    for i in range(div + 1):
        x = center[0] + radius * cos(angle)
        y = center[1] + radius * sin(angle)
        glVertex2f(x, y)
        angle = angle + step

    glEnd()

def calculateCircle():
    global triangle_v

    A = Coord(*(triangle_v[0]))
    B = Coord(*(triangle_v[1]))
    C = Coord(*(triangle_v[2]))

    AB = B.subtract(A)
    AC = C.subtract(A)
    if AB.isParallel(AC): raise Exception("No triangle can be drawn")

    line1 = getPerpendicularBisector(A, B)
    line2 = getPerpendicularBisector(A, C)

    center = line1.getLineIntersection(line2)
    radius = A.getDistance(center)

    return center, radius


def mouseClick(button, state, x, y):
    global triangle_v
    if len(triangle_v) < 3 and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        triangle_v.append((float(x / 250) - 1.0, -(float(y / 250) - 1.0)))
    glutPostRedisplay()



# def main(argv):

#     A = Coord(float(argv[1]), float(argv[2])) # point A
#     B = Coord(float(argv[3]), float(argv[4])) # point B
#     C = Coord(float(argv[5]), float(argv[6])) # point C

    
#     print("Center of circumcircle: {}".format(intersect))
#     print("Radius of circumcircle: {}".format(radius))




def main(args):
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow("Circumcircle")

    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouseClick)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main(sys.argv)