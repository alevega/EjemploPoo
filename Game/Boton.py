import pygame

class Boton:
    def __init__(self, texto, width, height, pos, window, elevacion):
        __gui_font = pygame.font.Font("C:/Users/Lucho/OneDrive/Escritorio/Poo/EjemploPoo/Game/imagenes/Grand9K Pixel.ttf", 20)
        self.__top_rect = pygame.Rect(pos, (width, height))
        
        self.__top_color = '#F2F3F6'
        self.__text_surf = __gui_font.render(texto, True, '#000000')
        self.__text_rect = self.__text_surf.get_rect(center = self.__top_rect.center)
        self.__window = window
        self.__presionado = False
        self.__elevacion = elevacion
        self.__elevacion_dinamica =elevacion
        self.__original_y_pos = pos[1]

        self.boton_rect = pygame.Rect(pos,(width,elevacion))
        self.boton_color = '#475F77'

        
    def draw(self):
        self.__top_rect.y = self.__original_y_pos - self.__elevacion_dinamica
        self.__text_rect.center = self.__top_rect.center

        self.boton_rect.midtop = self.__top_rect.midtop
        self.boton_rect.height = self.__top_rect.height + self.__elevacion_dinamica

        pygame.draw.rect(self.__window, self.boton_color, self.boton_rect, border_radius= 12)
        pygame.draw.rect(self.__window, self.__top_color, self.__top_rect, border_radius= 12)

        self.__window.blit(self.__text_surf, self.__text_rect)
        self.__check_click()
    
    def __check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.__top_rect.collidepoint(mouse_pos):
            self.__top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.__elevacion_dinamica = 0
                self.__presionado = True
            else:
                self.__elevacion_dinamica = self.__elevacion
                if self.__presionado == True:
                    self.__presionado = False
        else:
            self.__elevacion_dinamica = self.__elevacion
            self.__top_color = '#F2F3F6'
        
    
    def get_presionado(self):
        return self.__presionado