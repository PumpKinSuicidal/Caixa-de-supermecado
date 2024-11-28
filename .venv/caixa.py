import sys
# Importar os componetes praa a construçaõ da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
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
        self.Label_coluna_esquerda.setStyleSheet("QLabel{background-color:#4868E8}")
        # Label da direita
        self.Label_coluna_direita = QLabel()
        self.Label_coluna_direita.setStyleSheet("QLabel{background-color:#b3b3b3}")

        # <<<<<<<< Montagem de coluna da esquerda >>>>>>>>>
        self.lay_esquerda = QVBoxLayout()

        # Label para adicionar o logo da loja
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/carlos.esilva90/Documents/Janela_Caixa/.venv/logo_padaria.png"))
        # Ajustar a label  e a imagem paar ficar do tamanho ideal
        self.logo_label.setScaledContents(True)

        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedHeight(200)
        self.logo_label.setFixedWidth(200)
        # Adicionar a label com a imagem na tela
        self.lay_esquerda.addWidget(self.logo_label)

        # Colunas da tabela
        colunas = ["Cod.Produto", "Nome do Produto", "Descrição", "Quantidade", "Preço", "Subtotal"]
        # Label e lines edits da coluna da esqueda dentro do lay_esquerda
        self.codigo_produto_label = QLabel("Código do produto")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.setStyleSheet("QLineEdit{font-size:10pt;}")
        self.lay_esquerda.addWidget(self.codigo_produto_label)
        self.lay_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do Produto")
        self.nome_produto_edit = QLineEdit()
        self.lay_esquerda.addWidget(self.nome_produto_label)
        self.lay_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("Descrição do Produto")
        self.descricao_produto_edit = QLineEdit()
        self.lay_esquerda.addWidget(self.descricao_produto_label)
        self.lay_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do Produto")
        self.quantidade_produto_edit = QLineEdit()
        self.lay_esquerda.addWidget(self.quantidade_produto_label)
        self.lay_esquerda.addWidget(self.quantidade_produto_edit)

        self.preco_produto_label = QLabel("Preço do Produto")
        self.preco_produto_edit = QLineEdit()
        self.lay_esquerda.addWidget(self.preco_produto_label)
        self.lay_esquerda.addWidget(self.preco_produto_edit)

        self.subtotal_produto_label = QLabel("Sub Total do Produto")
        self.subtotal_produto_edit = QLineEdit()
        self.lay_esquerda.addWidget(self.subtotal_produto_label)
        self.lay_esquerda.addWidget(self.subtotal_produto_edit)

        self.Label_coluna_esquerda.setFixedWidth(630)


        # <<<<<<<< Montagem de coluna da direita >>>>>>>>>
        self.lay_direita = QVBoxLayout()

        # Criar uma tebela e adiciionar na coluna da direita, esta tabela terá os nomes dos campos que estão ao lado esquedo.
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.lay_direita.addWidget(self.tabela)

        self.total_pagar_label = QLabel("Total a Pagar:")
        self.total_pagar_edit = QLineEdit("0,00")
        self.lay_direita.addWidget(self.total_pagar_label)
        self.lay_direita.addWidget(self.total_pagar_edit)

        self.Label_coluna_direita.setLayout(self.lay_direita)

        # Adicionar o layout vertical da esqueda com todos os controles: label, e lineEdit dentri da coluna da esquerda(label_coluna_esquerda)
        self.Label_coluna_esquerda.setLayout(self.lay_esquerda)

        # Criar um layout horizontal para as colunas
        self.h_layout = QHBoxLayout()
        # Adicionar as colunas ao layout horizontal
        self.h_layout.addWidget(self.Label_coluna_esquerda)
        self.h_layout.addWidget(self.Label_coluna_direita)

        # Adiciionar o layout na tela
        self.setLayout(self.h_layout)

app = QApplication(sys.argv)
cx = caixa()
cx.show()
app.exec_()