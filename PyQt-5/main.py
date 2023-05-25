from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui
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
        self.labels()
        self.carregar_janela()
    
    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def buttons(self):
        ligar = QPushButton('Ligar', self)
        ligar.move(100, 100)
        ligar.resize(150, 50)
        ligar.clicked.connect(self.ligar_click)
        
        desligar = QPushButton('Desligar', self)
        desligar.move(300, 100)
        desligar.resize(150, 50)
        desligar.clicked.connect(self.desligar_click)
        
        
    def labels(self):
        self.label1 = QLabel(self)
        self.label1.setText("TEXTO A SER EXIBIDO")
        self.label1.move(300, 200)
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"blue"}')
        self.label1.resize(250, 20)
        
        self.imagem = QLabel(self)
        self.imagem.move(110, 200)
        self.imagem.resize(120, 120)
        self.imagem.setScaledContents(True)
        
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(100, 500)
        self.caixa_texto.resize(150,25)
        
        botao_leitura = QPushButton('LEIA', self)
        botao_leitura.move(260, 500)
        botao_leitura.resize(150, 25)
        botao_leitura.clicked.connect(self.funcao_leitura)
    
    def funcao_leitura(self):
        texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        self.label1.setText(texto)
        
    def ligar_click(self):
        self.label1.setText("Ligado")
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"green"}')

        self.imagem.setPixmap(QtGui.QPixmap('img/sol.png'))
        
    def desligar_click(self):
        self.label1.setText("Desligado")
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"red"}')
        self.imagem.setPixmap(QtGui.QPixmap('img/lua.png'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    j = Janela()
    sys.exit(app.exec()) # Manter a janela rodando