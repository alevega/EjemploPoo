from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap

class LoginView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.titulo = QLabel("Inicio de Sesión")
        self.user = QLabel("Nombre de Usuario")
        self.password = QLabel("Contraseña")
        self.btn_login = QPushButton("Login")
        logo = QPixmap("C:/Users/Lucho/OneDrive/Escritorio/Poo/EjemploPoo/Gestion/imagen/logo.png")
        
        self.setGeometry(100,100,400,200)

        lbl_logo = QLabel()
        lbl_logo.setPixmap(logo)
        lbl_logo.setScaledContents(True)
        lbl_logo.setFixedSize(400,300)
        layout = QGridLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(10)
        
        self.inp_usuario = QLineEdit()
        self.inp_pass = QLineEdit()
        self.inp_pass.setEchoMode(QLineEdit.EchoMode.Password)
        
        container = QWidget()

        layout.addWidget(lbl_logo,0,1)
        layout.addWidget(self.titulo,1,1)
        layout.addWidget(self.user,2,0)
        layout.addWidget(self.inp_usuario,2,1)
        layout.addWidget(self.password,3,0)
        layout.addWidget(self.inp_pass,3,1)
        layout.addWidget(self.btn_login,4,1)
        container.setLayout(layout)
        
        self.setCentralWidget(container)