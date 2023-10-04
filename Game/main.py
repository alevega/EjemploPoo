#pip install pygame
import pygame, sys
from pygame.locals import *
from Menu import Menu

window = Menu()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.movimiento_fondo()
    window.crear_menu()
    pygame.display.update()
    