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
    # glBegin(GL_LINE_STRIP)

    # glColor3f(0.0, 1.0, 0.0)
    # glVertex2f(0.0, -1.0)
    # glVertex2f(0.0, 1.0)

    # glEnd()

def draw3DAxis():
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glEnd()
    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -1.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()


def drawLine():
    """
    Draw the line with respect to the 2D-coordinate
    """
    A = Coord(0.0, 0.0)
    B = Coord(1.0, 2.0)
    line = Line(A, B.subtract(A))

    line.draw(t_range = [-1, 1], color = (1.0, 1.0, 1.0))

def drawEllipse(W = 0.3, H = 0.2, step = 12):
    """
    (x/W)**2 + (y/H)**2 = 1
    """

    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 0.0, 1.0)

    angle = 0
    for t in range(step):
        x = W * cos(angle)
        y = H * sin(angle)
        glVertex2f(x, y)
        angle = angle + 2 * pi / step
    glEnd()

def drawSuperellipse(n = 2, W = 0.3, H = 0.2, step = 12):
    p = 2/n - 1
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 0.0, 1.0)
    
    angle = 0.1
    for t in range(step):
        x = W * cos(angle) * abs(cos(angle)**p)
        y = H * sin(angle) * abs(sin(angle)**p)
        glVertex2f(x, y)
        angle = angle + 2 * pi / step
    glEnd()

def drawSuperhyperbola(n = 2, W = 0.3, H = 0.2, step = 12):
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

def drawHelix():
    pass
def drawToroidalSpiral():
    pass
def drawExt():
    pass



def display():
    global argv
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    

    if argv[1] == 'Line':
        draw2DAxis()
        drawLine()
    elif argv[1] == 'Ellipse':
        if len(argv) == 5: 
            draw2DAxis()
            drawEllipse(W = float(argv[2]), H = float(argv[3]), step = int(argv[4]))
        else: 
            print("\nInput: python3 draw.py Ellipse W H step")
            exit(0)
    elif argv[1] == 'Superellipse':
        if len(argv) == 6: 
            draw2DAxis()
            drawSuperellipse(n = float(argv[2]), W = float(argv[3]), H = float(argv[4]), step = int(argv[5]))
        else: 
            print("\nInput: python3 draw.py Superellipse n W H step")
            exit(0)
    elif argv[1] == 'Superhyperbola':
        if len(argv) == 6: 
            draw2DAxis()
            drawSuperhyperbola(n = float(argv[2]), W = float(argv[3]), H = float(argv[4]), step = int(argv[5]))
        else: 
            print("\nInput: python3 draw.py Superellipse n W H step")
            exit(0)
    elif argv[1] == 'Helix':
        draw3DAxis()
    
    glFlush()

def main(args):
    global argv
    argv = args


    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow(str(argv[1]))

    init()
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main(sys.argv)
