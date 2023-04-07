from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QScrollArea, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QKeyEvent
from ui.ui_window import Ui_MainWindow
from PySide6.QtCore import QTimer, QEvent, QObject
import PyPDF4
from datetime import datetime
from typing import cast
import sys
####imports for table
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
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
        # print(rgc, cliente, data, nota_fiscal )
        table_info = self.tableWidget
        coments = self.plainTextEdit.toPlainText()

        msg = QMessageBox()

        if not all([rgc, cliente, data, nota_fiscal]):# Verifica se todos os campos foram preenchidos
            msg.setWindowTitle("Cuidado!")
            msg.setIcon(QMessageBox.Warning) 
            msg.setStyleSheet("color:white;background:red")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Erro', 'Por favor, preencha todos os campos.")
            msg.exec()
            return

        
        dados = [['COD PRODUTO','DEFEITO','QUANTIDADE', 'ULTIMA COMPRA', 'FORNECEDOR', 'GARANTIA']]
        for row in range(table_info.rowCount()):
            row_data = []
            for column in range(table_info.columnCount()):
                item = table_info.item(row, column)
                row_data.append(item.text())
            dados.append(row_data)
        # print(data) # ta dandos uns bo, veja o modelo model-gpt para arrumar   

        # Define o estilo dos parágrafos
        styles = getSampleStyleSheet()
        nome_style = styles["Heading1"]
        cliente_style = ParagraphStyle(name="ClienteStyle", fontName="Helvetica", fontSize=12, leading=14)
        info_style = ParagraphStyle(name="InfoStyle", fontName="Helvetica", fontSize=10, leading=12)
        comentario_style = ParagraphStyle(name="ComentarioStyle", fontName="Helvetica", fontSize=10, leading=12, spaceBefore=10)

        # Define o nome do arquivo PDF
        filename = f"RGC{rgc}_{cliente}.pdf"

        # Define os dados do cabeçalho
        nome = f"RGC {rgc} - {cliente}"
        data = f"Data: {data}"
        nota = f"Nota fiscal: {nota_fiscal}"

        # Define o comentário
        comentario = f"{coments}"

        # Define o conteúdo do PDF
        conteudo = []

        
        #definir dados


        # Adiciona o nome do relatório
        conteudo.append(Paragraph(nome, nome_style))

        # Adiciona as informações do cliente, ano e nota
        conteudo.append(Paragraph(cliente, cliente_style))
        conteudo.append(Paragraph(data, info_style))
        conteudo.append(Paragraph(nota, info_style))

        # Adiciona a tabela
        tabela = Table(dados)
        tabela.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 14),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
            ("ALIGN", (0, 1), (-1, -1), "CENTER"),
            ("ALIGN", (1, 1), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 10),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]))

        conteudo.append(tabela)
        conteudo.append(Paragraph(comentario, comentario_style))

        doc = SimpleDocTemplate(filename, pagesize=letter)
        doc.build(conteudo)

    #def clear all

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