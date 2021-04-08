from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sqrt, pi, sin, cos, tan
import numpy as np
argv = []



def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -4.0, 2.0, -10.0, 10.0)


def draw3DAxis():
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-2.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)

    glEnd()
    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -2.0)
    glVertex3f(0.0, 0.0, 2.0)

    glEnd()


def getOrthogonal3D(a):
    """
    vector v = (a, b, c)
    => v_ortho = (c, c, -b-a)

    """
    if len(a) != 3: raise "Wrong Input"

    return np.array([a[2], a[2], -a[1]-a[0]])
def normalize(a):
    return a / np.linalg.norm(a)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluLookAt( 0, 0, 0, 0.7, 0.2, 0.3, 0, 1, 0)
    draw3DAxis()


    """ QUESTION A: CIRCUMCIRCLE """
    #POINT
    A = np.array([1.5, 0, 2])
    B = np.array([3, 0, 1])
    C = np.array([3.5, 0, 3.5])
    #VECTOR
    a = B - A
    b = C - B
    c = A - C
    a_ortho = getOrthogonal3D(a)
    
    """
    L(t) = A + a/2 + a_ortho * t"
    t = 0.5 * (b DOT c) / (a_ortho DOT c)
    """
    t = 0.5 * np.dot(b, c) / np.dot(a_ortho, c)
    #CIRCUMCIRCLE
    center = A + a/2 + t*a_ortho
    radius = np.linalg.norm(center-A)
    print("center: {}\nradius: {}".format(center, radius))

    """ QUESTION B: Tetrahedron """
    D = (191/68, 1.3518, 159/68)

    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(*A)
    glVertex3f(*B)
    glVertex3f(*C)
    glVertex3f(*D)
    glVertex3f(*A)
    glVertex3f(*B)
    glEnd()
    glFlush()

def main():



    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow("")

    init()
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMainLoop()

main()