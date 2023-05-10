from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame



""" STEPS
    1. glEnable(GL_TEXTURE_2D)
    2. Load images
    3. to_string
    4. glGenTextures
    5. glBindTexture
    6. glTexParameterf
    7. glTexImage2D
    8. glBindTexture
    9. glTexCoord 
"""

"""textures:world , main car , 12 cars"""
textureIdentifiers = [i for i in range(14)]


def setupHelper(texture, textureIdentifier, width, height):
    glBindTexture(GL_TEXTURE_2D, textureIdentifier)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, width, height, GL_RGBA, GL_UNSIGNED_BYTE,
                      texture)


def loadHelper(path, index):
    image = pygame.image.load(path)

    binaryImage = pygame.image.tostring(image, "RGBA", True)
    setupHelper(
        binaryImage, textureIdentifiers[index], image.get_width(), image.get_height())


def drawHelper(textureIndex, left, right, top, bottom):
    glBindTexture(GL_TEXTURE_2D, textureIdentifiers[textureIndex])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex(left, bottom, 0)
    glTexCoord2f(1, 0.0)
    glVertex(right, bottom, 0)
    glTexCoord2f(1, 1)
    glVertex(right, top, 0)
    glTexCoord2f(0.0, 1)
    glVertex(left, top, 0)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, -1)
def drawHelper1 (textureIndex, left, right, top, bottom):
    glBindTexture(GL_TEXTURE_2D, textureIdentifiers[textureIndex])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex(left, bottom, 0.5)
    glTexCoord2f(1, 0.0)
    glVertex(right, bottom, 0.5)
    glTexCoord2f(1, 1)
    glVertex(right, top, 0.5)
    glTexCoord2f(0.0, 1)
    glVertex(left, top, 0.5)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, -1)