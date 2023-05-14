import pygame

# TODO replace directory with yours !!

pygame.init()
pygame.mixer.init()
start_sound = pygame.mixer.Sound(
    "Sounds Assets/start_car.wav")

back_sound = pygame.mixer.Sound(
    "Sounds Assets/back_sound_mp3cut.net.wav")

button_sound = pygame.mixer.Sound(
    "Sounds Assets/button.wav")

movement_sound = pygame.mixer.Sound(
    "Sounds Assets/Porsche Gt3.mp3")

calcson = pygame.mixer.Sound(
    "Sounds Assets/calcson.wav")

# crash_car=pygame.mixer.Sound("Sounds Assets/car_crash_car.wav")

# crash_wall=pygame.mixer.Sound("Sounds Assets/car_crash_wall.wav")

win = pygame.mixer.Sound(
    "Sounds Assets/win_game.wav")
