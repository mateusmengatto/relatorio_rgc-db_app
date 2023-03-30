from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QScrollArea, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPainter, QImage
from popplerqt6 import Poppler

class PDFViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.scrollArea = QScrollArea(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.scrollArea)

    def loadDocument(self, fileName):
        self.popplerDoc = Poppler.Document.load(fileName)
        self.pageImages = []
        for i in range(self.popplerDoc.numPages()):
            page = self.popplerDoc.page(i)
            size = page.pageSize()
            img = QImage(size.width(), size.height(), QImage.Format_RGB32)
            painter = QPainter(img)
            page.renderToPainter(painter)
            painter.end()
            self.pageImages.append(img)

    def paintEvent(self, event):
        painter = QPainter(self)
        for i, img in enumerate(self.pageImages):
            painter.drawImage(0, i * img.height(), img)
        painter.end()


'''Instalar o Poppler'''