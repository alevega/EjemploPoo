from typing import Any
import pygame
from MenuDao import MenuDao

class Menu:

    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.crear_fondo()

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

    def crear_botones(self):
        print('entro')
        pygame.draw.rect(self.__window, (255,255,255), [50,50,140,40])

    def crear_fondo(self):
        menu = MenuDao()
        res = menu.get_all()
        self.__h,self.__w = res[0][2],res[0][3]
        self.__fps = 60
        self.__reloj = pygame.time.Clock()
        self.__window = pygame.display.set_mode((self.__h,self.__w))
        self.crear_botones()
        icono = pygame.image.load(res[0][4])
        self.__mapa = pygame.image.load(res[0][5]).convert()
        pygame.display.set_icon(icono)
        pygame.display.set_caption(res[0][1])
        self.__x = 0
    
    def movimiento_fondo(self):
        x_relativa = self.get_x() % self.get_fondo().get_rect().width
        self.get_window().blit(self.get_fondo(), (x_relativa - self.get_fondo().get_rect().width,0))
        self.get_window().blit(self.get_fondo(), (x_relativa,0))
        self.set_x(1)
        pygame.display.update()
        self.reloj()