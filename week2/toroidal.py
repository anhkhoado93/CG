from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sqrt, pi, sin, cos, tan
from util import LineSegment, Coord, Line
argv = []

def sec(x):
    return 1/ cos(x)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)



def draw3DAxis():
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-2.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)

    glEnd()
    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -2.0)
    glVertex3f(0.0, 0.0, 2.0)

    glEnd()



def drawToroidal():
    """
    x(t) = (asin(ct) + b)cos(t)
    y(t) = (asin(ct) + b)sin(t)
    z(t) = (asin(ct) + b)sin(t)

    with a = radius, slope = b/a
    """
    a = 0.5
    b = 1
    c = 10

    glBegin(GL_LINE_STRIP)

    lst = [i*0.01 for i in range(1000)]
    glColor3f(1.0, 1.0, 1.0)
    for t in lst:
        x = (a * sin(c * t) + b) * cos(t)
        y = (a * sin(c * t) + b) * sin(t)
        z =  a* cos(c * t)
        glVertex3f(x, y, z)

    glEnd()


def display():
    global argv
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluLookAt(0.7, 0.5, 0.3, 0, 0, 0,  0, 1, 0)

    draw3DAxis()
    drawToroidal()


    glFlush()

def main(args):
    global argv
    argv = args


    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow("Toroidal")

    init()
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main(sys.argv)
