from typing import Any
import pygame
from MenuDao import MenuDao
from Boton import Boton

class Menu:

    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        menu = MenuDao()
        res = menu.get_all()
        self.__h,self.__w = res[0][2],res[0][3]
        self.__fps = 60
        self.__reloj = pygame.time.Clock()
        self.__window = pygame.display.set_mode((self.__h,self.__w))
        self.__icono = pygame.image.load(res[0][1])
        self.__mapa = pygame.image.load(res[0][4]).convert()
        self.__titulo = res[0][0]
        self.__crear_fondo()

    def get_window(self):
        return self.__window

    def get_fondo(self):
        return self.__mapa

    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x -= x
    
    def reloj(self):
        self.__reloj.tick(self.__fps)

    def __crear_fondo(self):
        pygame.display.set_icon(self.__icono)
        pygame.display.set_caption(self.__titulo)
        self.__x = 0
    
    def movimiento_fondo(self):
        x_relativa = self.get_x() % self.get_fondo().get_rect().width
        self.get_window().blit(self.get_fondo(), (x_relativa - self.get_fondo().get_rect().width,0))
        self.get_window().blit(self.get_fondo(), (x_relativa,0))
        self.set_x(1)
        self.reloj()

    def crear_menu(self):
        self.__boton_opciones = Boton("Opciones", 200, 40, (100,100), self.get_window())
        self.__boton_opciones.draw()