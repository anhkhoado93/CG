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



def drawHelix(a = 0.5, b = 0.05):
    """
    x(t) = acos(t)
    y(t) = asin(t)
    z(t) = bt

    with a = radius, slope = b/a
    """


    glBegin(GL_LINE_STRIP)

    lst = [i*0.1 for i in range(300)]
    glColor3f(1.0, 1.0, 1.0)
    for i in lst:
        x = a * cos(i)
        y = a * sin(i)
        z = b * i
        glVertex3f(x, y, z)

    glEnd()


def display():
    global argv
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluLookAt( 0, 0, 0, 0.7, 0.5, 0.3, 0, 1, 0)

    draw3DAxis()
    drawHelix(float(argv[1]), float(argv[2]))


    glFlush()

def main(args):
    global argv
    argv = args
    if len(argv) < 3:
        print("Wrong input!\nexample: python helix.py 0.5 0.05")
        exit(0)

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow("Helix")

    init()
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main(sys.argv)
