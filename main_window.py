from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui.ui_window import Ui_MainWindow
from PySide6.QtCore import QTimer
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


    def check_rgc_number(self): #mudar esse método para caixa de diálogo com aviso.
        msg = QMessageBox()

        # Exibir a caixa de mensagem e obter o resultado do botão pressionado
        rgc_number_typed = self.rgc_lined.text()
        if rgc_number_typed in ('1','123','2'):
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
    
    def gerar_relatorio(self): #modificar para criar pdf e imprimir $ver como deixar mais clean
        self.rgc_number = self.rgc_lined.text()
        self.cliente = self.cliente_lined.text()
        self.Data = self.date_lined.text()
        self.nota_fiscal = self.notafiscal_lined.text()
        print(self.rgc_number, '\n',
        self.cliente, '\n',
        self.Data , '\n',
        self.nota_fiscal
        )
 
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
    
    



# _____Running Code_________#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()