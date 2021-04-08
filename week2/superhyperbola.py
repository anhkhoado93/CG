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
    xAxis.draw(color = (0.0, 1.0, 0.0))

    yAxis = LineSegment(Coord(0.0, -1.0), Coord(0.0, 1.0))
    yAxis.draw(color = (0.0, 1.0, 0.0))

def drawSuperhyperbola(n = 2, W = 0.3, H = 0.2):
    step = 30
    p = 2/n - 1
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 1.0)
    
    angle = 0.1
    for t in range(step):
        x = W * sec(angle) * abs(sec(angle)**p)
        y = H * tan(angle) * abs(tan(angle)**p)
        glVertex2f(x, y)
        angle = angle + 2 * pi / step
    glEnd()



def display():
    global argv
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    draw2DAxis()
    drawSuperhyperbola(n = float(argv[1]), W = float(argv[2]), H = float(argv[3]))


    glFlush()

def main(args):
    global argv
    argv = args
    if len(argv) < 4:
        print("Wrong input!\nexample: superhyperbola.py 2 0.3 0.2")
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
