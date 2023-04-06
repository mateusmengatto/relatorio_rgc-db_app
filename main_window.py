from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QScrollArea, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QKeyEvent
from ui.ui_window import Ui_MainWindow
from PySide6.QtCore import QTimer, QEvent, QObject
import PyPDF4
from datetime import datetime
from typing import cast
import sys
####
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
###




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
            return

        data = []
        for row in range(table_info.rowCount()):
            row_data = []
            for column in range(table_info.columnCount()):
                item = table_info.item(row, column)
                row_data.append(item.text())
            data.append(row_data)
#### tabela no pdf - mudar para A4, com imagem de cabeçalho etc, o modelo ta tabela, a posição e etc.
#Caso não seja possível usar o PyPDF4 utilizando transformação de html para pdf
        doc = SimpleDocTemplate(f"RGC{rgc} - {cliente}.pdf", pagesize=A4)
        # container for the 'Flowable' objects
        elements = []
        t=Table(data,table_info.columnCount()*[1*inch], table_info.rowCount()*[1*inch]) #arrumar isso no loop e tamanho dinâmico e cores e etc
        t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
        ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
        ('VALIGN',(0,0),(0,-1),'TOP'),
        ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
        ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))


        elements.append(t)
        # write the document to disk
        doc.build(elements)



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