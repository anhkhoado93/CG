from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np
from math import floor
args = []
TICK_RATIO = 0.1
CANVAS_COLOR = (221/255.0, 225/255.0, 227/255.0, 1.0)

def init():
    global args
    m = max(args) + 1
    glClearColor(*CANVAS_COLOR)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, m, -1 ,m, -10.0, 10.0)
    glEnable(GL_POINT_SMOOTH)





def getPerp2D(a):
    return np.array([-a[1], a[0]])

def normalize(a):
    return a / np.linalg.norm(a)

def drawTickLine(init, end, arrow = False, numbering = 0):
    """
    draw line with ticks
    ---------------
    init:       (np.ndarray) starting point
    end:        (np.ndarray) ending point
    arrow:      (boolean) default=False
    numbering:  (int) 
        0  -- no numbering  
        1  -- counter-clockwise numbering ( left side )
        -1 -- clockwise numbering ( right side )
    """
    length = np.linalg.norm(end - init)
    v_norm = normalize(end - init)
    # -------------------->
    marks = [init]
    for _ in range(floor(length - 0.1)): marks.append(marks[-1] + v_norm)
    # ---|---|---|---|---|->
    point = []
    v_perp = getPerp2D(v_norm)
    for i in marks:
        p = (i + v_perp * (TICK_RATIO / 2), i - v_perp * (TICK_RATIO / 2))
        point.append(p)
    
    glPointSize(8.0)
    glLineWidth(2.0)
    glColor3f(0.0, 0.0, 0.0)

    # start point
    glBegin(GL_POINTS)
    glVertex2f(*init)
    glEnd()

    # end point
    if arrow:
        tail = end - TICK_RATIO * v_norm
        tail_l = tail + v_perp * 0.05
        tail_r = tail - v_perp * 0.05
        glBegin(GL_LINES)
        glVertex2f(*end)
        glVertex2f(*tail_l)
        glVertex2f(*end)
        glVertex2f(*tail_r)
        glEnd()
    elif not arrow:
        glBegin(GL_POINTS)
        glVertex2f(*end)
        glEnd()

    if numbering:
        font = GLUT_BITMAP_9_BY_15
        for num, pos in zip(range(len(marks)), marks):
            if num == 0: continue
            glRasterPos2f(*(pos + v_perp * TICK_RATIO * numbering * 2))
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(str(num)))
            
    glBegin(GL_LINES)
    # line
    glVertex2f(*init)
    glVertex2f(*end)

    # ticks
    for p in point:
        glVertex2f(*p[0])
        glVertex2f(*p[1])

    glEnd()
        


def display():
    global args
    glClearColor(*CANVAS_COLOR)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    O = np.zeros(2)
    x = np.array([args[0], 0])
    y = np.array([0, args[1]])

    drawTickLine(O, x, arrow = True, numbering=-1)
    drawTickLine(O, y, arrow = True, numbering= 1)
    
    glFlush()

def main(argv):
    global args
    if len(argv) != 3:
        print("python tick.py horizontal vertical")
    args = [float(i) for i in argv[1:]]
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow("Oxy")
    init()
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMainLoop()

main(sys.argv)