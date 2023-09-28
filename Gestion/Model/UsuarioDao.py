from Model.DataBase import DataBase

class UsuarioDao:

    def __init__(self):
        self.base = DataBase()
    
    def get_all(self):
        return self.base.getAll("SELECT * FROM usuarios")

    def get(self, id):
        return self.base.get("SELECT * FROM usuarios WHERE id = {}".format(id))
    
    def login(self, correo, passw):
        return self.base.get("SELECT * FROM usuarios WHERE correo = '{}' and pass = '{}'".format(correo, passw))
    
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass