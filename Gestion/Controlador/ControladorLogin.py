
from Model.Usuario import Usuario
from Vista.LoginView import LoginView
from PyQt6.QtWidgets import QApplication
import sys


class ControladorLogin:

    def __init__(self, estilo):
        app = QApplication(sys.argv)
        self.__window = LoginView()
        self.__window.setWindowTitle("Gestion de Aplicaciones")
        self.__window.get_btn_login().clicked.connect(self.login)
        self.__window.show()
        with open(estilo) as f:
            app.setStyleSheet(f.read())
        app.exec()


    def login(self):
        usuario = Usuario(self.__window.get_correo(), self.__window.get_pass())
        usuario.login()