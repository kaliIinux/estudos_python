from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys

class Janela(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira janela"
        self.buttons()
        self.carregar_janela()
    
    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def buttons(self):
        ligar = QPushButton('Ligar', self)
        ligar.move(100, 100)
        ligar.resize(150, 50)
        
        desligar = QPushButton('Desligar', self)
        desligar.move(300, 100)
        desligar.resize(150, 50)
        ligar.clicked.connect(self.ligar_click)

    def ligar_click(self):
        print("LIGADO")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    j = Janela()
    sys.exit(app.exec()) # Manter a janela rodando