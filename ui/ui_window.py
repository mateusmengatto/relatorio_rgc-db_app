# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.notafiscal_lbl = QLabel(self.centralwidget)
        self.notafiscal_lbl.setObjectName(u"notafiscal_lbl")
        font = QFont()
        font.setPointSize(12)
        self.notafiscal_lbl.setFont(font)
        self.notafiscal_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.notafiscal_lbl, 4, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 11, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout.addLayout(self.gridLayout_3, 11, 1, 1, 1)

        self.cliente_lbl = QLabel(self.centralwidget)
        self.cliente_lbl.setObjectName(u"cliente_lbl")
        self.cliente_lbl.setFont(font)
        self.cliente_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.cliente_lbl, 2, 0, 1, 1)

        self.cliente_lined = QLineEdit(self.centralwidget)
        self.cliente_lined.setObjectName(u"cliente_lined")
        self.cliente_lined.setFont(font)

        self.gridLayout.addWidget(self.cliente_lined, 2, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.encaminhado_lined = QLineEdit(self.centralwidget)
        self.encaminhado_lined.setObjectName(u"encaminhado_lined")

        self.gridLayout_2.addWidget(self.encaminhado_lined, 0, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout_2.addWidget(self.dateTimeEdit, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 9, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addline_btn = QPushButton(self.centralwidget)
        self.addline_btn.setObjectName(u"addline_btn")

        self.verticalLayout_2.addWidget(self.addline_btn)

        self.removeline_btn = QPushButton(self.centralwidget)
        self.removeline_btn.setObjectName(u"removeline_btn")

        self.verticalLayout_2.addWidget(self.removeline_btn)

        self.gerarrelatorio_btn = QPushButton(self.centralwidget)
        self.gerarrelatorio_btn.setObjectName(u"gerarrelatorio_btn")

        self.verticalLayout_2.addWidget(self.gerarrelatorio_btn)


        self.gridLayout.addLayout(self.verticalLayout_2, 7, 2, 1, 1)

        self.date_lined = QDateEdit(self.centralwidget)
        self.date_lined.setObjectName(u"date_lined")
        self.date_lined.setFont(font)

        self.gridLayout.addWidget(self.date_lined, 3, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.notafiscal_lined = QLineEdit(self.centralwidget)
        self.notafiscal_lined.setObjectName(u"notafiscal_lined")
        self.notafiscal_lined.setFont(font)

        self.gridLayout.addWidget(self.notafiscal_lined, 4, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 608, 245))
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 1, 611, 401))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 7, 1, 1, 1)

        self.rgc_check_btn = QPushButton(self.centralwidget)
        self.rgc_check_btn.setObjectName(u"rgc_check_btn")

        self.gridLayout.addWidget(self.rgc_check_btn, 1, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)

        self.data_lbl = QLabel(self.centralwidget)
        self.data_lbl.setObjectName(u"data_lbl")
        self.data_lbl.setFont(font)
        self.data_lbl.setLayoutDirection(Qt.LeftToRight)
        self.data_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.data_lbl, 3, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.guiafornecedor_btn = QPushButton(self.centralwidget)
        self.guiafornecedor_btn.setObjectName(u"guiafornecedor_btn")

        self.verticalLayout_3.addWidget(self.guiafornecedor_btn)

        self.guiapecas_btn = QPushButton(self.centralwidget)
        self.guiapecas_btn.setObjectName(u"guiapecas_btn")

        self.verticalLayout_3.addWidget(self.guiapecas_btn)


        self.gridLayout.addLayout(self.verticalLayout_3, 7, 0, 1, 1)

        self.rgc_lined = QLineEdit(self.centralwidget)
        self.rgc_lined.setObjectName(u"rgc_lined")
        self.rgc_lined.setFont(font)

        self.gridLayout.addWidget(self.rgc_lined, 1, 1, 1, 1)

        self.rgc_lbl = QLabel(self.centralwidget)
        self.rgc_lbl.setObjectName(u"rgc_lbl")
        self.rgc_lbl.setFont(font)
        self.rgc_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.rgc_lbl, 1, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(16777215, 85))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 608, 83))
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 0, 611, 91))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_2, 10, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RGC", None))
        self.notafiscal_lbl.setText(QCoreApplication.translate("MainWindow", u"Nota Fiscal:", None))
        self.cliente_lbl.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Data (hora):", None))
        self.addline_btn.setText(QCoreApplication.translate("MainWindow", u"Adicionar\n"
"Linha", None))
        self.removeline_btn.setText(QCoreApplication.translate("MainWindow", u"Remover\n"
"Linha", None))
        self.gerarrelatorio_btn.setText(QCoreApplication.translate("MainWindow", u"Gerar\n"
" e Imprimir \n"
"Relat\u00f3rio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio de Garantia - Db Truck", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"COD PRODUTO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DEFEITO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ULTIMA COMPRA", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"GARANTIA", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.rgc_check_btn.setText(QCoreApplication.translate("MainWindow", u"Check-RGC", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es:", None))
        self.data_lbl.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Tutorial \n"
"Garantias", None))
        self.guiafornecedor_btn.setText(QCoreApplication.translate("MainWindow", u"Guia\n"
"Fornecedor", None))
        self.guiapecas_btn.setText(QCoreApplication.translate("MainWindow", u"Guia Pe\u00e7as", None))
        self.rgc_lbl.setText(QCoreApplication.translate("MainWindow", u"RGC:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Encaminhado:", None))
    # retranslateUi

