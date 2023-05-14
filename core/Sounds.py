import pygame

# TODO replace directory with yours !!

pygame.mixer.pre_init(44100, -16, 2, 256)
pygame.init()
pygame.mixer.init()
start_sound = pygame.mixer.Sound(
    "Sounds Assets/start_car.wav")

back_sound = pygame.mixer.Sound(
    "Sounds Assets/back_sound_mp3cut.net.wav")

button_sound = pygame.mixer.Sound(
    "Sounds Assets/button.wav")

movement_sound = pygame.mixer.Sound(
    "Sounds Assets/CadillacLowRevIdlL PE862409.wav")

calcson = pygame.mixer.Sound(
    "Sounds Assets/calcson.wav")

crash_car =pygame.mixer.Sound("Sounds Assets/car_crash_car.wav")

# crash_wall=pygame.mixer.Sound("Sounds Assets/car_crash_wall.wav")

win = pygame.mixer.Sound(
    "Sounds Assets/win_game.wav")

lost = pygame.mixer.Sound(
    "Sounds Assets/youlost.wav")