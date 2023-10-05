#pip install pygame
import pygame, sys
from pygame.locals import *
from Menu import Menu
from Opciones import Opciones

window = Menu()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.movimiento_fondo()
    window.crear_menu()
    if window.get_btn_opciones().get_presionado() == True:
        Opciones(window.get_h,window.get_w, window)
    pygame.display.update()
    