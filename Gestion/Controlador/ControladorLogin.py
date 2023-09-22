from Vista.LoginView import LoginView
from PyQt6.QtWidgets import QApplication
import sys


class ControladorLogin:

    def __init__(self, estilo):
        app = QApplication(sys.argv)
        window = LoginView()
        window.setWindowTitle("Gestion de Aplicaciones")
        window.btn_login.clicked.connect(self.login)
        window.show()
        with open(estilo) as f:
            app.setStyleSheet(f.read())
        app.exec()


    def login(self):
        print("apreto")