from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from dados import carregar_usuarios

class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.usuarios = carregar_usuarios()

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome de usuário")

        self.senha_input = QLineEdit()
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.fazer_login)

        layout = QVBoxLayout()
        layout.addWidget(self.nome_input)
        layout.addWidget(self.senha_input)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def fazer_login(self):
        nome = self.nome_input.text()
        senha = self.senha_input.text()

        for u in self.usuarios:
            if u["nome"] == nome and u["senha"] == senha:
                QMessageBox.information(self, "Login", f"Bem-vindo, {nome}!")
                return

        QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")
