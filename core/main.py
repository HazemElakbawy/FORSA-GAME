from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, numpy as np
from Rectangles import *
from Textures import *
from Collision import *

# WINDOW PROPERTIES
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 900

# ROADS WIDTHS AND HEIGHTS
LOWER_ROAD_HEIGHT = UPPER_ROAD_HEIGHT = 200
MIDDLE_ROAD = (250, 150)
UPPER_LEFT_ROAD_WIDTH = UPPER_RIGHT_ROAD_WIDTH = 250

# CAR PROPERTIES
CAR_WIDTH = 100
CAR_LENGTH = 50
CAR_SPEED = 0.15
CAR_ROTATION_SPEED = 1
time_interval = 1
keys_pressed = set()
car_pos = [100, 250]
car_angle = [0.0]
car_vel = [0.0, 0.0]
obstacle_speed = 0.2  # Changes on linux


# * =================================== Init PROJECTION ===================================== * #


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)


# * ========================= Rectangle ( width, height ,  x ,  y ) ========================= * #

# ! World Rectangle
world = Rectangle(WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0)

# ! LAYER 01
rect_L1_1 = Rectangle(WINDOW_WIDTH, 150, 0, 0)

# ! LAYER 02
rect_L2_1 = Rectangle(
    650, MIDDLE_ROAD[1],
    0, rect_L1_1.top + LOWER_ROAD_HEIGHT)

rect_L2_2 = Rectangle(
    WINDOW_WIDTH - MIDDLE_ROAD[0] - rect_L2_1.width, MIDDLE_ROAD[1],
    rect_L2_1.right + MIDDLE_ROAD[0], rect_L1_1.top + LOWER_ROAD_HEIGHT)

# ! LAYER 03
layer3_height = WINDOW_HEIGHT - rect_L1_1.height - \
                LOWER_ROAD_HEIGHT - rect_L2_1.height - UPPER_ROAD_HEIGHT

rect_L3_1 = Rectangle(
    150, layer3_height,
    0, rect_L2_1.top + UPPER_ROAD_HEIGHT)

rect_L3_2 = Rectangle(
    400, layer3_height,
    rect_L3_1.right + UPPER_LEFT_ROAD_WIDTH, rect_L2_1.top + UPPER_ROAD_HEIGHT)

rect_L3_3 = Rectangle(
    150, layer3_height,
    rect_L3_2.right + UPPER_RIGHT_ROAD_WIDTH, rect_L2_1.top + UPPER_ROAD_HEIGHT)

# * ========================= car model ( left, bottom , right ,  top , direction ) ========================= * #


# road 1
car_Obj_1_0 = Car_Model(100, 160, 180, 205, 3, obstacle_speed)
car_Obj_1_1 = Car_Model(400, 160, 480, 205, 3, obstacle_speed)
car_Obj_1_2 = Car_Model(800, 160, 880, 205, 3, obstacle_speed)

# road 2
car_Obj_2_0 = Car_Model(100, 300, 180, 345, -4, obstacle_speed)
car_Obj_2_1 = Car_Model(400, 300, 480, 345, -4, obstacle_speed)
car_Obj_2_2 = Car_Model(900, 300, 980, 345, -4, obstacle_speed)

# road 3
car_Obj_3_0 = Car_Model(500, 520, 580, 565, 4, obstacle_speed)
car_Obj_3_1 = Car_Model(900, 520, 980, 565, 4, obstacle_speed)
car_Obj_3_2 = Car_Model(200, 520, 280, 565, 4, obstacle_speed)

# road 4
car_Obj_4_0 = Car_Model(600, 650, 680, 695, -9, obstacle_speed)
car_Obj_4_1 = Car_Model(200, 650, 280, 695, -9, obstacle_speed)
car_Obj_4_2 = Car_Model(1100, 650, 1180, 695, -9, obstacle_speed)


# * ================================= Draw other cor state  ================================= * #

def drawState(carObj, texture_index):
    carObj.left = carObj.left + carObj.car_Direction
    carObj.right = carObj.right + carObj.car_Direction
    glColor(1, 1, 1)  # White color
    carObj.draw_texture(texture_index)
    carObj.draw_car()

    if carObj.left >= WINDOW_WIDTH and carObj.car_Direction > 0:
        carObj.left = -80
        carObj.right = 0

    if carObj.right <= 0 and carObj.car_Direction < 0:
        carObj.left = WINDOW_WIDTH
        carObj.right = WINDOW_WIDTH + 80


# * ===============================================  DRAW FUNCTION ========================================== * #

def draw():
    global car_pos, car_angle, car_vel, keys_pressed, obstacle_speed
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # * ========================= Draw cars ========================= * #
    obs_list = [car_Obj_1_0, car_Obj_1_1, car_Obj_1_2,
                car_Obj_2_0, car_Obj_2_1, car_Obj_2_2,
                car_Obj_3_0, car_Obj_3_1, car_Obj_3_2,
                car_Obj_4_0, car_Obj_4_1, car_Obj_4_2]

    j = 2
    for i in obs_list:
        drawState(i, j)
        obstacle_collision(i, car_pos, car_vel, car_angle, CAR_LENGTH, CAR_WIDTH)
        j += 1

    # * ========================= Main car ========================= * #

    if 'base' in keys_pressed:  # only for test
        for i in obs_list:
            i.car_Direction *= 0.99

    if 'notbase' in keys_pressed:  # only for test
        for i in obs_list:
            i.car_Direction /= 0.99

    if 'left' in keys_pressed:
        car_angle[0] += CAR_ROTATION_SPEED
    if 'right' in keys_pressed:
        car_angle[0] -= CAR_ROTATION_SPEED
    if 'up' in keys_pressed:
        car_vel[0] += CAR_SPEED * math.cos(math.radians(car_angle[0]))
        car_vel[1] += CAR_SPEED * math.sin(math.radians(car_angle[0]))
    if 'down' in keys_pressed:
        car_vel[0] -= CAR_SPEED * math.cos(math.radians(car_angle[0]))
        car_vel[1] -= CAR_SPEED * math.sin(math.radians(car_angle[0]))
    car_pos[0] += car_vel[0]
    car_pos[1] += car_vel[1]
    car_vel[0] *= 0.965
    car_vel[1] *= 0.965

    # Collision detection to the side walls
    wall_collision(car_pos, car_vel, car_angle, CAR_LENGTH, CAR_WIDTH)
    arrival_line(car_pos, CAR_LENGTH)
    drawTextures((1, 1, 1), world)

    car = MainCar(CAR_WIDTH, CAR_LENGTH,
                   car_pos[0], car_pos[1], car_angle[0], [0.6, 0.8, 0.5])

    glutSwapBuffers()


def keyboard(key, x, y):
    global keys_pressed

    if key == b'a':
        keys_pressed.add('left')
        # print(keys_pressed)
    elif key == b'd':
        keys_pressed.add('right')
        # print(keys_pressed)
    elif key == b'w':
        keys_pressed.add('up')
        # print(keys_pressed)
    elif key == b's':
        keys_pressed.add('down')
        # print(keys_pressed)
    elif key == b'q':
        keys_pressed.add('base')
        print(keys_pressed)
    elif key == b'e':
        keys_pressed.add('notbase')
        print(keys_pressed)


def keyboard_up(key, x, y):
    global keys_pressed

    if key == b'a':
        keys_pressed.remove('left')
        # print(keys_pressed)

    elif key == b'd':
        keys_pressed.remove('right')
        # print(keys_pressed)

    elif key == b'w':
        keys_pressed.remove('up')
        # print(keys_pressed)

    elif key == b's':
        keys_pressed.remove('down')
        # print(keys_pressed)
    elif key == b'q':
        keys_pressed.remove('base')
        print(keys_pressed)
    elif key == b'e':
        keys_pressed.remove('notbase')
        print(keys_pressed)


def Timer(v):
    draw()
    glutTimerFunc(time_interval, Timer, 1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(500, 100)
    glutCreateWindow(b"FORSA GAME")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboard_up)
    glutTimerFunc(time_interval, Timer, 50)
    init()
    load_setup_textures()
    glutMainLoop()


main()
