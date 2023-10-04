import pygame

class Boton:
    def __init__(self, texto, width, height, pos, window):
        __gui_font = pygame.font.Font(None, 30)
        self.__top_rect = pygame.Rect(pos, (width, height))
        self.__top_color = '#475F77'
        self.__text_surf = __gui_font.render(texto, True, '#FFFFFF')
        self.__text_rect = self.__text_surf.get_rect(center = self.__top_rect.center)
        self.__window = window
        
    def draw(self):
        segunda_window = pygame.Surface([100,200])
        segunda_window.fill((0,0,255))
        pygame.draw.rect(self.__window, self.__top_color, self.__top_rect)
        self.__window.blit(self.__text_surf, self.__text_rect)
        self.__window.blit(segunda_window, (0,50))
        