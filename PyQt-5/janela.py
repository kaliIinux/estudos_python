from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication

def funcao():
    print('teste')

if __name__ == "__main__":
    aplicativo = QApplication(sys.argv)

    janela = uic.loadUi('janela.ui')
    janela.btnLigar.clicked.connect(funcao)
    janela.show()

    sys.exit(aplicativo.exec())