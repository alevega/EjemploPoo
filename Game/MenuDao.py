from DataBase import DataBase

class MenuDao:

    def __init__(self):
        self.base = DataBase()

    def get_all(self):
        return self.base.getAll("SELECT nombre, icono, altura, ancho, fondo FROM ventana v inner join fondo f on v.fondo_id = f.fondo_id")
    
    def cambiar_resolucion(self, altura, ancho, id):
        return self.base.query("UPDATE public.ventana SET altura={}, ancho={} WHERE ventana_id = {};".format(altura,ancho,id))