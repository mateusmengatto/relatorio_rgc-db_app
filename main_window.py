from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QScrollArea, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QKeyEvent
from ui.ui_window import Ui_MainWindow
from PySide6.QtCore import QTimer, QEvent, QObject
import PyPDF4
from datetime import datetime
from typing import cast
import sys





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.rgc_check_btn.clicked.connect(self.check_rgc_number)

        self.rgc_number = self.rgc_lined.text()
        self.cliente = self.cliente_lined.text()
        self.Data = self.date_lined.text()
        self.nota_fiscal = self.notafiscal_lined.text()

        self.gerarrelatorio_btn.clicked.connect(self.gerar_relatorio)
        self.addline_btn.clicked.connect(self.insert_row)
        self.removeline_btn.clicked.connect(self.remove_row)

        self.table_gar = self.tableWidget
        icon_db = QIcon('img\icon_db.png')

        self.setWindowIcon(icon_db)

        #monitorar ação
        self.rgc_lined.installEventFilter(self) #selecionar o objeto para monitorar

        '''
        Botões para gerar função:
        Configurar o Gerar Relatório para criação de pdf (ver estruturação e como deixar no padrão) além de adicionar a db.
        Botões Aba direita de abertura de arquivos como tutorial, guia fornecedor, guia peças;
            - Ver formas de exibir este arquivo, ou externamente em outro programa ou estáticamente dentro de uma nova janela aberta no software
        
        Verificar como colocar uma nova aba no software para configurar a pesquisa e abertura do banco de dados
        '''
    
    def insert_row(self):
        self.table_gar.insertRow(1)
    
    def remove_row(self):
        self.table_gar.removeRow(1)
    

    def check_rgc_number(self): #mudar esse método para caixa de diálogo com aviso.
        msg = QMessageBox()

        # Exibir a caixa de mensagem e obter o resultado do botão pressionado
        rgc_number_typed = self.rgc_lined.text()
        if rgc_number_typed in ('1','123','2'): #mudar para procurar na db
            msg.setWindowTitle("Cuidado!")
            msg.setIcon(QMessageBox.Warning) 
            msg.setStyleSheet("color:white;background:red")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Este Número de RGC já foi utilizado!\n verifique o número correto!")
            msg.exec()
            
        else:
            msg.setWindowTitle("Aviso!")
            msg.setIcon(QMessageBox.Information) 
            msg.setStyleSheet("color:white;background:green")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Ok - Número ainda não utilizado!")
            msg.exec()
    
    def gerar_relatorio(self):
        # -------------- arrumar função -- refazer ----- #
        # relatorio_pdf = PyPDF4.PdfFileWriter()
        # page = PyPDF4.pdf.PageObject #Esta errado
        # relatorio_pdf.add_page(page)
        # page.mergePage(relatorio_pdf.PdfFileReader(open("texto.pdf", "rb")).getPage(0))   
        # with open('arquivo.pdf', 'wb') as f:
        #     relatorio_pdf.write(f)
        
        
        
        
         #modificar para criar pdf e imprimir $ver como deixar mais clean
        rgc = self.rgc_lined.text()
        cliente = self.cliente_lined.text()
        data = self.date_lined.text()
        nota_fiscal = self.notafiscal_lined.text()
        print(rgc, cliente, data, nota_fiscal )
        table_info = self.tableWidget

        msg = QMessageBox()

        if not all([rgc, cliente, data, nota_fiscal]):# Verifica se todos os campos foram preenchidos
            msg.setWindowTitle("Cuidado!")
            msg.setIcon(QMessageBox.Warning) 
            msg.setStyleSheet("color:white;background:red")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Erro', 'Por favor, preencha todos os campos.")
            msg.exec()


        data = []
        for row in range(table_info.rowCount()):
            row_data = []
            for column in range(table_info.columnCount()):
                item = table_info.item(row, column)
                row_data.append(item.text())
            data.append(row_data)

        for i in data:
            print(i)

    def closeEvent(self, event):
        # Criar a caixa de diálogo de confirmação
        reply = QMessageBox.question(self, 'Fechar', 'Deseja fechar o programa?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Aceitar o evento, permitindo que a janela seja fechada
            event.accept()
        else:
            # Rejeitar o evento, mantendo a janela aberta
            event.ignore()
    '''
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.rgc_lined.text()
            self.statusBar. ### FOrmatar para o texto digitado e o campo que esta sendo digitado apararecer no StatusBar.
            print(event.text())

        return super().eventFilter(watched, event)

    '''
# _____Running Code_________#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()