import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
from reportlab.pdfgen import canvas

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gerador de relatório')

        self.number_label = QLabel('Número do relatório:')
        self.number_input = QLineEdit()

        self.client_label = QLabel('Cliente:')
        self.client_input = QLineEdit()

        self.date_label = QLabel('Data:')
        self.date_input = QLineEdit()

        self.nf_label = QLabel('Nota fiscal:')
        self.nf_input = QLineEdit()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Descrição', 'Quantidade', 'Valor'])

        self.addRowBtn = QPushButton('Adicionar linha')
        self.addRowBtn.clicked.connect(self.addRow)

        self.generate_button = QPushButton('Gerar relatório')
        self.generate_button.clicked.connect(self.generate_report)

        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.number_label)
        hbox1.addWidget(self.number_input)
        hbox1.addWidget(self.client_label)
        hbox1.addWidget(self.client_input)
        hbox1.addWidget(self.date_label)
        hbox1.addWidget(self.date_input)
        hbox1.addWidget(self.nf_label)
        hbox1.addWidget(self.nf_input)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.table)
        vbox.addWidget(self.addRowBtn)
        vbox.addWidget(self.generate_button)

        self.setLayout(vbox)

        self.show()

    def addRow(self):
        numRows = self.table.rowCount()
        self.table.insertRow(numRows)
        for col in range(self.table.columnCount()):
            self.table.setItem(numRows, col, QTableWidgetItem(''))

    def generate_report(self):
        number = self.number_input.text()
        client = self.client_input.text()
        date = self.date_input.text()
        nf = self.nf_input.text()

        # Conexão com o banco de dados SQLite
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Criação da tabela caso ela não exista
        cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, numero TEXT, cliente TEXT, data TEXT, nf TEXT, descricao TEXT, quantidade TEXT, valor TEXT)')


        # Inserção dos dados na tabela
        cursor.execute('INSERT INTO usuarios (numero, cliente, data, nf) VALUES (?, ?, ?, ?)', (number, client, date, nf))
        conn.commit()

        # Geração do relatório em PDF
        c = canvas.Canvas('relatorio.pdf')

        c.drawString(100, 750, 'Relatório')
        c.drawString(100, 700, f'Número do relatório: {number}')
        c.drawString(100, 650, f'Cliente: {client}')
        c.drawString(100, 600, f'Data: {date}')
        c.drawString(100, 550, f'Nota fiscal: {nf}')

        # Adição da tabela no relatório
        y = 500
        for row in range(self.table.rowCount()):
            descricao = self.table.item(row, 0).text()
            quantidade = self.table.item(row, 1).text()
            valor = self.table.item(row, 2).text()
            c.drawString(100, y, descricao)
            c.drawString(250, y, quantidade)
            c.drawString(350, y, valor)
            y -= 20

        c.save()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())