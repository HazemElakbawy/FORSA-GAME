import pygame

# TODO replace directory with yours !!

pygame.init()
pygame.mixer.init()
start_sound = pygame.mixer.Sound(
    "FORSA-GAME/sounds/start_car.wav")

back_sound = pygame.mixer.Sound(
    "FORSA-GAME/sounds/back_sound_mp3cut.net.wav")

button_sound = pygame.mixer.Sound(
    "FORSA-GAME/sounds/button.wav")

movement_sound = pygame.mixer.Sound(
    "FORSA-GAME/sounds/Porsche Gt3.mp3")

calcson = pygame.mixer.Sound(
    "FORSA-GAME/sounds/calcson.wav")

# crash_car=pygame.mixer.Sound("sounds/car_crash_car.wav")

# crash_wall=pygame.mixer.Sound("sounds/car_crash_wall.wav")

win = pygame.mixer.Sound(
    "FORSA-GAME/sounds/win_game.wav")
