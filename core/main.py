from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np
from car_model import *
from Rectangles import *
from Textures import *

# WINDOW PROPERTIES
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 900

# ROADS WIDTHS AND HEIGHTS
LOWER_ROAD_HEIGHT = UPPER_ROAD_HEIGHT = 200
MIDDLE_ROAD = (250, 150)
UPPER_LEFT_ROAD_WIDTH = UPPER_RIGHT_ROAD_WIDTH = 250

# CAR PROPERTIES
CAR_WIDTH = 50
CAR_LENGTH = 25
CAR_SPEED = 0.03
CAR_ROTATION_SPEED = 0.6
time_interval = 1
keys_pressed = set()
car_pos = [100, 250]
car_angle = 0.0
car_vel = [0.0, 0.0]
obstacle_speed = 0.2  # Changes on linux

# * ========================================================================================= * #
# * ========================================================================================= * #
# * =================================== Init PROJECTION ===================================== * #
# * ========================================================================================= * #
# * ========================================================================================= * #


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)


def Timer(v):
    draw()
    glutTimerFunc(time_interval, Timer, 1)


def keyboard(key, x, y):
    global car_angle, car_vel, keys_pressed

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
    global car_angle, car_vel, keys_pressed

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

# * ========================================================================================= * #
# * ========================================================================================= * #
# * ========================================================================================= * #
# * ========================================================================================= * #


# * ========================================================================================= * #
# * ========================================================================================= * #
# * ========================= Rectangle ( width, height ,  x ,  y ) ========================= * #
# * ========================================================================================= * #
# * ========================================================================================= * #

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


# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================= car model ( left, bottom , right ,  top , direction ) ========================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #


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


def drawState(carObj):
    carObj.left = carObj.left + carObj.car_Direction
    carObj.right = carObj.right + carObj.car_Direction
    glColor(1, 1, 1)  # White color
    carObj.draw_car()

    if carObj.left >= WINDOW_WIDTH and carObj.car_Direction > 0:
        carObj.left = -80
        carObj.right = 0

    if carObj.right <= 0 and carObj.car_Direction < 0:
        carObj.left = WINDOW_WIDTH
        carObj.right = WINDOW_WIDTH + 80


# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #


# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================== TEXTURES PART ================================================ * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #

def load_setup_textures():
    glEnable(GL_TEXTURE_2D)
    glGenTextures(len(textureIdentifiers), textureIdentifiers)
    # TODO: Load all textures here
    loadHelper("World Assets/world.png", 0)
    loadHelper("World Assets/porche_911.png", 1)
    # loadHelper("chess.png", 2)
    # loadHelper("chess.png", 3)
    # loadHelper("chess.png", 4)
    # loadHelper("chess.png", 5)
    # loadHelper("1.png", 6)
    # loadHelper("2.png", 7)
    # loadHelper("3.png", 8)
    # loadHelper("4.png", 9)
    # loadHelper("5.png", 10)
    # loadHelper("6.png", 11)


def drawTextures(color: tuple = (1, 1, 1)):
    # TODO: Draw all textures here [ WORLD , MAIN CAR , OTHER CARS(12)]
    glColor(color[0], color[1], color[2])
    drawHelper(0, world.left, world.right, world.top, world.bottom)
    drawHelper(1, car.left, car.right, car.top, car.bottom)

    # glVertex3f(x/2, y/2, 0)
    # glVertex3f(x/2, -y/2, 0)
    # glVertex3f(-x/2, -y/2, 0)
    # glVertex3f(-x/2, y/2, 0)

    # drawHelper(1, )
    # drawHelper(textureIndex, rectangle.left, rectangle.right,rectangle.bottom, rectangle.top)
    # drawHelper(textureIndex, rectangle.left, rectangle.right,rectangle.bottom, rectangle.top)


# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #


# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ======================================= COLLISION PART ================================================== * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #
def draw():
    global car_pos, car_angle, car_vel, keys_pressed, obstacle_speed
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # * ========================= draw cars ========================= * #
    obs_list = [car_Obj_1_0, car_Obj_1_1, car_Obj_1_2,
                car_Obj_2_0, car_Obj_2_1, car_Obj_2_2,
                car_Obj_3_0, car_Obj_3_1, car_Obj_3_2,
                car_Obj_4_0, car_Obj_4_1, car_Obj_4_2]

    for i in obs_list:
        drawState(i)
        obstacle_collision(i)

    car = main_car(CAR_WIDTH, CAR_LENGTH, car_pos[0], car_pos[1],
                   car_angle, [0.6, 0.8, 0.5])

    if 'base' in keys_pressed:  # only for test
        for i in obs_list:
            i.car_Direction *= 0.99  # Chanes on linux
    if 'notbase' in keys_pressed:  # only for test
        for i in obs_list:
            i.car_Direction /= 0.99  # Chanes on linux

    if 'left' in keys_pressed:
        car_angle += CAR_ROTATION_SPEED
    if 'right' in keys_pressed:
        car_angle -= CAR_ROTATION_SPEED
    if 'up' in keys_pressed:
        car_vel[0] += CAR_SPEED * math.cos(math.radians(car_angle))
        car_vel[1] += CAR_SPEED * math.sin(math.radians(car_angle))
    if 'down' in keys_pressed:
        car_vel[0] -= CAR_SPEED * math.cos(math.radians(car_angle))
        car_vel[1] -= CAR_SPEED * math.sin(math.radians(car_angle))
    car_pos[0] += car_vel[0]
    car_pos[1] += car_vel[1]
    car_vel[0] *= 0.99
    car_vel[1] *= 0.99

    # Arrival line walls

    glBegin(GL_LINE_STRIP)
    glVertex3f(275+25, 710, 0)
    glVertex3f(275+25, 810, 0)
    glVertex3f(275-25, 810, 0)
    glVertex3f(275-25, 710, 0)
    glEnd()

    # Collision detection to the side walls
    wall_collision()

    arrival_line()

    glutSwapBuffers()


def obstacle_collision(ob):
    global car_pos, car_vel, car_angle
    ob_width = ob.right - ob.left
    ob_height = ob.top - ob.bottom
    ob_center = np.array([(ob.left+ob.right)/2, (ob.top + ob.bottom)/2])
    dist = math.sqrt((ob_center[0] - car_pos[0]) **
                     2 + (ob_center[1] - car_pos[1])**2)

    if (dist < (ob_width+CAR_LENGTH)/2) and (dist < (ob_height+CAR_WIDTH)/2):
        # car_vel[0], car_vel[1] = -car_vel[0], -car_vel[1]
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0


def wall_collision():
    global car_pos, car_vel, car_angle
    # Front-side collision
    car_face = car_pos[0] + CAR_WIDTH / 2 * math.cos(math.radians(car_angle))
    car_back = car_pos[0] - CAR_WIDTH / 2 * math.cos(math.radians(car_angle))
    car_top = car_pos[1] + CAR_LENGTH / 2 * math.sin(math.radians(car_angle))
    car_bottom = car_pos[1] - CAR_LENGTH / \
        2 * math.sin(math.radians(car_angle))

    if car_face >= WINDOW_WIDTH:
        car_vel[0] = -car_vel[0]
        print(car_pos[0])
        car_pos[0] = WINDOW_WIDTH - CAR_WIDTH / 2
    elif car_face <= 0:
        car_vel[0] = -car_vel[0]
        print(car_pos[0])
        car_pos[0] = 0 + CAR_WIDTH / 2
    elif car_top >= WINDOW_HEIGHT:
        car_vel[1] = -car_vel[1]
        car_pos[1] = WINDOW_HEIGHT - CAR_WIDTH / 2

    # front collision to layer 1:
    elif car_top <= 160:
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0

    # face collision to layer 2
    elif (340 <= car_top <= 360+150) and \
            ((car_face <= 650) or (car_face >= 650+250)):
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0

    # face collision to layer 3
    elif (340+250+100 <= car_top) and \
            ((car_face <= 150) or (400 <= car_face <= 300+500) or (1200-145 <= car_face)):
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0

    # Back-side collision
    elif car_back >= WINDOW_WIDTH:
        car_vel[0] = -car_vel[0]
        print(car_pos[0])
        car_pos[0] = WINDOW_WIDTH - CAR_WIDTH / 2
    elif car_back <= 0:
        car_vel[0] = -car_vel[0]
        print(car_pos[0])
        car_pos[0] = 0 + CAR_WIDTH / 2
    elif car_bottom >= WINDOW_HEIGHT:
        car_vel[1] = -car_vel[1]
        car_pos[1] = WINDOW_HEIGHT - CAR_WIDTH / 2

    # back collision to layer 1:
    elif car_bottom <= 160:
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0
    # back collision to layer 2
    elif (340 <= car_bottom <= 360+150) and \
            ((car_back <= 650) or (car_back >= 650+250)):
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0

    # back collision to layer 3
    elif (340+250+100 <= car_bottom) and \
            ((car_back <= 150) or (400 <= car_back <= 300+500) or (1200-145 <= car_back)):
        car_pos[0], car_pos[1] = 100, 250
        car_angle = 0
        car_vel[0], car_vel[1] = 0, 0

# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #


def arrival_line():
    global car_pos, car_vel, car_angle
    car_face = car_pos[0] + CAR_WIDTH / 2 * math.cos(math.radians(car_angle))
    car_back = car_pos[0] - CAR_WIDTH / 2 * math.cos(math.radians(car_angle))
    car_top = car_pos[1] + CAR_LENGTH / 2 * math.sin(math.radians(car_angle))
    car_bottom = car_pos[1] - CAR_LENGTH / \
        2 * math.sin(math.radians(car_angle))

    if (900-100 <= car_top) and (275-25 <= car_face <= 275+25):
        car_vel[0], car_vel[1] = -car_vel[0], -car_vel[1]

    elif (900 - 100 <= car_bottom) and (275 - 25 <= car_back <= 275 + 25):
        car_vel[0], car_vel[1] = -car_vel[0], -car_vel[1]


# * ========================================================================================================= * #
# * ========================================================================================================= * #
# * ===============================================  DRAW FUNCTION ========================================== * #
# * ========================================================================================================= * #
# * ========================================================================================================= * #

class main_car:
    def __init__(self, x, y, trans_x, trans_y, theta, rgb):
        self.x = x
        self.y = y
        self.right = x/2
        self.left = -x/2
        self.top = y/2
        self.bottom = -y/2
        glColor3f(rgb[0], rgb[1], rgb[2])
        glPushMatrix()
        glTranslatef(trans_x, trans_y, 0)
        glRotatef(theta, 0, 0, 1)
        glBegin(GL_POLYGON)
        glVertex3f(x/2, y/2, 0)
        glVertex3f(x/2, -y/2, 0)
        glVertex3f(-x/2, -y/2, 0)
        glVertex3f(-x/2, y/2, 0)
        glEnd()
        glPopMatrix()


def draw():
    global car_pos, car_angle, car_vel, keys_pressed, obstacle_speed, car
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # * ========================= Draw cars ========================= * #
    obs_list = [car_Obj_1_0, car_Obj_1_1, car_Obj_1_2,
                car_Obj_2_0, car_Obj_2_1, car_Obj_2_2,
                car_Obj_3_0, car_Obj_3_1, car_Obj_3_2,
                car_Obj_4_0, car_Obj_4_1, car_Obj_4_2]

    car = main_car(CAR_WIDTH, CAR_LENGTH,
                   car_pos[0], car_pos[1], car_angle, [0.6, 0.8, 0.5])

    for i in obs_list:
        drawState(i)
        obstacle_collision(i)

    # * ========================= Main cars ========================= * #

    if 'base' in keys_pressed:  # only for test
        for i in obs_list:
            i.car_Direction *= 0.99

    if 'notbase' in keys_pressed:  # only for test
        for i in obs_list:
            i.car_Direction /= 0.99

    if 'left' in keys_pressed:
        car_angle += CAR_ROTATION_SPEED
    if 'right' in keys_pressed:
        car_angle -= CAR_ROTATION_SPEED
    if 'up' in keys_pressed:
        car_vel[0] += CAR_SPEED * math.cos(math.radians(car_angle))
        car_vel[1] += CAR_SPEED * math.sin(math.radians(car_angle))
    if 'down' in keys_pressed:
        car_vel[0] -= CAR_SPEED * math.cos(math.radians(car_angle))
        car_vel[1] -= CAR_SPEED * math.sin(math.radians(car_angle))
    car_pos[0] += car_vel[0]
    car_pos[1] += car_vel[1]
    car_vel[0] *= 0.99
    car_vel[1] *= 0.99

    # Arrival line walls
    glBegin(GL_LINE_STRIP)
    glVertex3f(275+25, 710, 0)
    glVertex3f(275+25, 810, 0)
    glVertex3f(275-25, 810, 0)
    glVertex3f(275-25, 710, 0)
    glEnd()

    # Collision detection to the side walls
    wall_collision()
    # arrival_line()
    drawTextures((1, 1, 1))
    rect_L1_1.drawRectangle()
    rect_L2_1.drawRectangle()
    rect_L2_2.drawRectangle()
    rect_L3_1.drawRectangle()
    rect_L3_2.drawRectangle()
    rect_L3_3.drawRectangle()

    glutSwapBuffers()


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

# def obstacle_collision(ob):
#     # global
#     car_face = car_pos[0] + CAR_WIDTH / 2 * math.cos(math.radians(car_angle))
#     car_top = car_pos[1] + CAR_LENGTH / 2 * math.sin(math.radians(car_angle))
#     car_bottom = car_pos[1] - CAR_LENGTH / 2
#     car_back = car_pos[0] - CAR_WIDTH / 2
#
#     #
#     if (car_face >= ob.left or car_back >= ob.left) and ((car_top <= ob.top and car_top >= ob.bottom) or (car_bottom >= ob.bottom and car_bottom <= ob.top)):
#         car_vel[0] = -abs(car_vel[0])
#     if (car_face <= ob.right ) and ((car_top <= ob.top and car_top >= ob.bottom) or (car_bottom >= ob.bottom and car_bottom <= ob.top)):
#         car_vel[0] = -car_vel[0]
#         print(car_face)
