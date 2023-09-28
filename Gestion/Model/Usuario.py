

from Model.UsuarioDao import UsuarioDao


class Usuario:

    def __init__(self, correo, password):
        self.__correo = correo
        self.__password = password
        self.__usuariodao = UsuarioDao()
    
    def login(self):
        result = self.__usuariodao.login(self.__correo, self.__password)
        return result