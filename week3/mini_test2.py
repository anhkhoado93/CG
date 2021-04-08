from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sqrt, pi, sin, cos, tan
import numpy as np
from util import LineSegment, Coord, Line
def draw2DAxis():
    xAxis = LineSegment(Coord(-20.0, 0.0), Coord( 20.0, 0.0))
    xAxis.draw(color = (1.0, 1.0, 1.0))

    yAxis = LineSegment(Coord(0.0, -20.0), Coord(0.0, 20.0))
    yAxis.draw(color = (1.0, 1.0, 1.0))

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-8.0, 8.0, -8.0, 8.0, 0.0, 5.0)

def translate2D(ax, p):
    """
    translate point p by vector ax
    ----------------
    ax: tranlation vector

    p: point to translate
    """
    if len(ax) != 2: 
        raise "Invalid translation"
    M = np.array([1,0,ax[0],0,1,ax[1],0,0,1]).reshape(3, 3)
    # print(M, point)
    return np.matmul(M, p)

def rotate2D(point, angle, center=np.array([0,0])):
    """
    rotate point around center with angle
    ----------------
    point : point to rotate

    angle : angle

    center : center of rotation, [0,0] by default
    """
    cmp = center ==  np.array([0,0])
    if cmp.all():
        M = np.array([cos(angle),-sin(angle),0,sin(angle), cos(angle), 0, 0, 0, 1 ]).reshape(3, 3)
        return np.matmul(M, point)


    ret = translate2D(-center, point)
    ret = rotate2D(ret, angle)
    ret = translate2D(center, ret)

    return ret


def draw():
    """
    """
    A = np.array([2,2,1]).reshape(3, 1)
    B = np.array([5,3,1]).reshape(3, 1)
    C = np.array([3,4,1]).reshape(3, 1)

    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(*(A[:2].ravel()))
    glVertex2f(*(B[:2].ravel()))
    glVertex2f(*(C[:2].ravel()))
    glEnd()


    """Translate (2,-1)"""
    A_T = translate2D(np.array([2,-1]), A)
    B_T = translate2D(np.array([2,-1]), B)
    C_T = translate2D(np.array([2,-1]), C)


    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(*(A_T[:2].ravel()))
    glVertex2f(*(B_T[:2].ravel()))
    glVertex2f(*(C_T[:2].ravel()))
    glEnd()



    """Rotate 30* around (2,2)"""
    A_ = rotate2D(A, angle=30, center=np.array([2,2]))
    B_ = rotate2D(B, angle=30, center=np.array([2,2]))
    C_ = rotate2D(C, angle=30, center=np.array([2,2]))


    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(*(A_[:2].ravel()))
    glVertex2f(*(B_[:2].ravel()))
    glVertex2f(*(C_[:2].ravel()))
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(1.5)
    draw2DAxis()
    draw()
    glFlush()

def main(args):

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
