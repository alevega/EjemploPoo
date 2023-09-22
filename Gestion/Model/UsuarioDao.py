from DataBase import DataBase

class UsuarioDao:

    def __init__(self):
        self.base = DataBase()
    
    def get_all(self):
        return self.base.getAll("SELECT * FROM usuarios")

    def get(self, id):
        return self.base.get("SELECT * FROM usuarios WHERE id = {}".format(id))

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass