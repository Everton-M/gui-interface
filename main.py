import sys
from PyQt5.QtWidgets import QApplication
from tela_cadastro import TelaCadastro

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # (opcional) aplica estilo externo
    try:
        with open("estilo.qss", "r") as f:
            app.setStyleSheet(f.read())
    except:
        pass

    janela = TelaCadastro()
    janela.show()

    sys.exit(app.exec_())
