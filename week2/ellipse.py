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
    glOrtho(-1.0, 1.0, -1.0, 1.0, 0.0, 1.0)

def draw2DAxis():
    xAxis = LineSegment(Coord(-1.0, 0.0), Coord( 1.0, 0.0))
    xAxis.draw(color = (1.0, 1.0, 1.0))

    yAxis = LineSegment(Coord(0.0, -1.0), Coord(0.0, 1.0))
    yAxis.draw(color = (1.0, 1.0, 1.0))


def drawEllipse(W = 0.3, H = 0.2):
    """
    (x/W)**2 + (y/H)**2 = 1
    """
    step = 30
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 0.0, 0.5)

    angle = 0
    for t in range(step):
        x = W * cos(angle)
        y = H * sin(angle)
        glVertex2f(x, y)
        angle = angle + 2 * pi / step
    glEnd()

def display():
    global argv
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(1.5)

    draw2DAxis()
    drawEllipse(W = float(argv[1]), H = float(argv[2]))
    
    glFlush()

def main(args):
    global argv
    argv = args

    if (len(argv) != 3):
        print("Wrong input!\nexample: python ellipse.py 0.3 0.4")
        exit(0)

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow("Ellipse")

    init()
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main(sys.argv)
