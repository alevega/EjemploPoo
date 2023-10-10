#pip install pygame
import pygame, sys
from pygame.locals import *
from Menu import Menu
from Nuevo import Nuevo

def cerrar_ventana():
    pygame.quit()
    sys.exit()

window = Menu()
nuevo = Nuevo()

menu = True
menu_principal = True
menu_opcion = False
opciones = False
nuevo_juego = False

reloj = pygame.time.Clock()

while True:

    while menu:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                cerrar_ventana()
        window.movimiento_fondo()
        
        if menu_principal:
            window.crear_menu()
        if menu_opcion:
            window.crear_opciones()

        if window.get_btn_nuevo().get_presionado() == True:
            menu = False
            nuevo_juego = True

        if window.get_btn_opciones().get_presionado() == True:
            menu_principal = False
            menu_opcion = True
        
        if window.get_btn_salir().get_presionado() == True:
            menu_principal = True
            menu_opcion = False

        pygame.display.update()
    
    nuevo.pantalla(window.get_h(), window.get_w(), "Jugando", window.get_icono(), "C:/Users/Lucho/OneDrive/Escritorio/Programacion/Poo/EjemploPoo/Game/imagenes/nivel1.png")
    while nuevo_juego:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                cerrar_ventana()
        nuevo.jugador()
        pygame.display.update()
