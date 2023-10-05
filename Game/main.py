#pip install pygame
import pygame, sys
from pygame.locals import *
from Menu import Menu
from Nuevo import Nuevo

window = Menu()
nuevo = Nuevo()

menu = True
menu_principal = True
menu_opcion = False
opciones = False

reloj = pygame.time.Clock()

while True:

    while menu:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        window.movimiento_fondo()
        
        if menu_principal:
            window.crear_menu()
        if menu_opcion:
            window.crear_opciones()

        if window.get_btn_nuevo().get_presionado() == True:
            menu = False
            nuevo = True

        if window.get_btn_opciones().get_presionado() == True:
            menu_principal = False
            menu_opcion = True
        
        if window.get_btn_salir().get_presionado() == True:
            menu_principal = True
            menu_opcion = False

        pygame.display.update()
        
    while nuevo:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        

        pygame.display.update()