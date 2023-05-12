import pygame

# TODO replace directory with yours !!

pygame.init()
pygame.mixer.init()
start_sound = pygame.mixer.Sound(
    "/media/deadlypoison/New Volume/الدراسه/ثانيه حاسبات/الترم الثاني/Computer Graphic/PROJECT/beta/FORSA-GAME/sounds/start_car.wav")

back_sound = pygame.mixer.Sound(
    "/media/deadlypoison/New Volume/الدراسه/ثانيه حاسبات/الترم الثاني/Computer Graphic/PROJECT/beta/FORSA-GAME/sounds/back_sound_mp3cut.net.wav")

button_sound = pygame.mixer.Sound(
    "/media/deadlypoison/New Volume/الدراسه/ثانيه حاسبات/الترم الثاني/Computer Graphic/PROJECT/beta/FORSA-GAME/sounds/button.wav")

movement_sound = pygame.mixer.Sound(
    "/media/deadlypoison/New Volume/الدراسه/ثانيه حاسبات/الترم الثاني/Computer Graphic/PROJECT/beta/FORSA-GAME/sounds/Porsche Gt3.mp3")

calcson = pygame.mixer.Sound(
    "/media/deadlypoison/New Volume/الدراسه/ثانيه حاسبات/الترم الثاني/Computer Graphic/PROJECT/beta/FORSA-GAME/sounds/calcson.wav")

# crash_car=pygame.mixer.Sound("sounds/car_crash_car.wav")

# crash_wall=pygame.mixer.Sound("sounds/car_crash_wall.wav")

win = pygame.mixer.Sound(
    "/media/deadlypoison/New Volume/الدراسه/ثانيه حاسبات/الترم الثاني/Computer Graphic/PROJECT/beta/FORSA-GAME/sounds/win_game.wav")
