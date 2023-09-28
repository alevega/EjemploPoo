from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap

class LoginView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__titulo = QLabel("Inicio de Sesión")
        self.__user = QLabel("Nombre de Usuario")
        self.__password = QLabel("Contraseña")
        self.__btn_login = QPushButton("Login")
        logo = QPixmap("C:/Users/Lucho/OneDrive/Escritorio/Programacion/Poo/EjemploPoo/Gestion/imagen/logo.png")
        
        self.setGeometry(100,100,400,200)

        lbl_logo = QLabel()
        lbl_logo.setPixmap(logo)
        lbl_logo.setScaledContents(True)
        lbl_logo.setFixedSize(400,300)
        layout = QGridLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(10)
        
        self.__inp_usuario = QLineEdit()
        self.__inp_pass = QLineEdit()
        self.__inp_pass.setEchoMode(QLineEdit.EchoMode.Password)
        
        container = QWidget()

        layout.addWidget(lbl_logo,0,1)
        layout.addWidget(self.__titulo,1,1)
        layout.addWidget(self.__user,2,0)
        layout.addWidget(self.__inp_usuario,2,1)
        layout.addWidget(self.__password,3,0)
        layout.addWidget(self.__inp_pass,3,1)
        layout.addWidget(self.__btn_login,4,1)
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
    
    def get_correo(self):
        return self.__inp_usuario.text()
    
    def get_pass(self):
        return self.__inp_pass.text()

    def get_btn_login(self):
        return self.__btn_login