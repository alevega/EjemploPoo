import pygame

class Boton:
    def __init__(self, texto, width, height, pos):
        self.__top_rect = pygame.Rect(pos, (width, height))
        self.__top_color = '#475F77'
        
        #self.__text_surf = gui_font.render(texto, True, '#FFFFFF')
        self.__text_rect = self.__text_surf.get_rect(center = self.__top_rect.center)
        
    def draw(self):
        pass