from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Rectangle:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.right = x + width
        self.left = x
        self.top = y + height
        self.bottom = y

    def drawRectangle(self, color: tuple = (1, 1, 1)):
        glColor3f(color[0], color[1], color[2])
        glBegin(GL_QUADS)
        glVertex2f(self.left, self.bottom)
        glVertex2f(self.right, self.bottom)
        glVertex2f(self.right, self.top)
        glVertex2f(self.left, self.top)
        glEnd()