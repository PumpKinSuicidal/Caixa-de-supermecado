import sys
# Importar os componetes praa a construçaõ da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout

# Construção da classe janela com o nome de caixa
class caixa(QWidget):
    # Criação do metodo init que inicia a janela e exibe ela em tela
    def __init__(self):
        super().__init__()
        # Definir posição de tamanho da tela
        self.setGeometry(0,30,1300,850)
        # vamos definir o nome da nossa janela
        self.setWindowTitle("Caixa da loja")

        # Vamos criar as labels que representam as colunas esquerda e direita

        # Label da esqueda
        self.Label_coluna_esquerda = QLabel()
        self.Label_coluna_esquerda.setStyleSheet("QLabel{background-color:#b3b3b3}")
        # Label da direita
        self.Label_coluna_direita = QLabel()
        self.Label_coluna_direita.setStyleSheet("QLabel{background-color:#4868E8}")

        # Criar um layout horizontal para as colunas
        self.h_layout = QHBoxLayout()
        # Adicionar as colunas ao layout horizontal
        self.h_layout.addWidget(self.Label_coluna_direita)
        self.h_layout.addWidget(self.Label_coluna_esquerda)

        # Adiciionar o layout na tela
        self.setLayout(self.h_layout)

app = QApplication(sys.argv)
cx = caixa()
cx.show()
app.exec_()