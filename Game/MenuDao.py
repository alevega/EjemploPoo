from DataBase import DataBase

class MenuDao:

    def __init__(self):
        self.base = DataBase()

    def get_all(self):
        return self.base.getAll("SELECT * FROM configuracion")