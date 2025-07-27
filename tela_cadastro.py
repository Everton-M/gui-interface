from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from tela_login import TelaLogin
from dados import carregar_usuarios, salvar_usuarios

class TelaCadastro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro")
        self.usuarios = carregar_usuarios()

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome de usuário")

        self.senha_input = QLineEdit()
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.Password)

        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.clicked.connect(self.cadastrar)

        self.btn_login = QPushButton("Ir para Login")
        self.btn_login.clicked.connect(self.abrir_login)

        layout = QVBoxLayout()
        layout.addWidget(self.nome_input)
        layout.addWidget(self.senha_input)
        layout.addWidget(self.btn_cadastrar)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def cadastrar(self):
        nome = self.nome_input.text()
        senha = self.senha_input.text()

        if not nome or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        for u in self.usuarios:
            if u["nome"] == nome:
                QMessageBox.warning(self, "Erro", "Usuário já existe.")
                return

        self.usuarios.append({"nome": nome, "senha": senha})
        salvar_usuarios(self.usuarios)

        QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso.")
        self.nome_input.clear()
        self.senha_input.clear()

    def abrir_login(self):
        self.login_window = TelaLogin()
        self.login_window.show()
        self.close()
