import pygame

class Boton:
    def __init__(self, texto, width, height, pos, window, elevacion):
        __gui_font = pygame.font.Font("C:/Users/Lucho/OneDrive/Escritorio/Programacion/Poo/EjemploPoo/Game/imagenes/Grand9K Pixel.ttf", 20)
        self.__top_rect = pygame.Rect(pos, (width, height))
        self.__top_color = '#F2F3F6'
        self.__text_surf = __gui_font.render(texto, True, '#000000')
        self.__text_rect = self.__text_surf.get_rect(center = self.__top_rect.center)
        self.__window = window
        self.__presionado = False
        self.__elevacion = elevacion
        self.__elevacion_dinamica =elevacion
        self.__original_y_pos = pos[1]
        
    def draw(self):
        pygame.draw.rect(self.__window, self.__top_color, self.__top_rect)
        self.__window.blit(self.__text_surf, self.__text_rect)
        self.__check_click()
    
    def __check_click(self):
        posicion = pygame.mouse.get_pos()
        if self.__top_rect.collidepoint(posicion):
            self.__top_color = "#B739FA"
            if pygame.mouse.get_pressed()[0]:
                self.__presionado = True
            else:
                if self.__presionado == True:
                    self.__presionado = False
        else:
            self.__top_color = '#F2F3F6'
    
    def get_presionado(self):
        return self.__presionado