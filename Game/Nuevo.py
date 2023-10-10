import pygame, sys

class Nuevo():

    def __init__(self) -> None:
        super().__init__()
        pygame.init()
    
    def pantalla(self, h, w, titulo, icono, mapa):
        self.__h = h
        self.__w = w
        self.__titulo = titulo
        self.__icono = icono
        self.__mapa = pygame.image.load(mapa).convert()
        self.__window = pygame.display.set_mode((self.__h,self.__w))
        pygame.display.set_icon(self.__icono)
        pygame.display.set_caption(self.__titulo)
        self.__window.blit(self.__mapa, (0,0))
    
    def jugador(self):
        pant_jugador = pygame.image.load("C:/Users/Lucho/OneDrive/Escritorio/Programacion/Poo/EjemploPoo/Game/imagenes/fantasma.png")
        self.__window.blit(pant_jugador, (300,10))