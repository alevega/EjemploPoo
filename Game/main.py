#pip install pygame
import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500,400))
pygame.display.set_caption("Juegon")
icono = pygame.image.load("C:/Users/Lucho/OneDrive/Escritorio/Poo/EjemploPoo/Game/imagenes/icono.jpg")
pygame.display.set_icon(icono)
fondo = (255,255,255) #Color blanco

window.fill(fondo)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()