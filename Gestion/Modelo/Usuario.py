from DataBase import DataBase

class Usuario:
    
    def __init__(self):
        pass
    
    def get_all_usuario(self):
        base = DataBase()
        usu = base.getAll("SELECT * FROM usuarios")
        print(usu)