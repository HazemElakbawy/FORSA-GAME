from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Car_Model:
    def __init__(self, left, bottom, right, top, car_Direction, obstacle_speed):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        self.car_Direction = car_Direction*obstacle_speed

    def draw_car(self):
        glBegin(GL_QUADS)
        glVertex(self.left, self.bottom, 0)
        glVertex(self.right, self.bottom, 0)
        glVertex(self.right, self.top, 0)
        glVertex(self.left, self.top, 0)
        glEnd()
