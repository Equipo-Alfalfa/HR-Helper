import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication,  QMainWindow, QPushButton,QDialog, QRadioButton)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos')))
import modulos.gen_graf as graf

class grafSelUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('./GUI/.ui/select_graf.ui')
        self.setup_connections()
        self.ui.show()

    def setup_connections(self):
        self.rad_1 = self.ui.findChild(QRadioButton, 'pGrafBtn')
        self.rad_1.value = 1
        self.rad_1.toggled.connect(self.graf_selected)

        self.rad_2 = self.ui.findChild(QRadioButton, 'hGrafBtn')
        self.rad_2.value = 2
        self.rad_2.toggled.connect(self.graf_selected)

        self.rad_3 = self.ui.findChild(QRadioButton, 'bGrafBtn')
        self.rad_3.value = 3
        self.rad_3.toggled.connect(self.graf_selected)

        self.btn_ok = self.ui.findChild(QPushButton, 'Btn_Ok')
        self.btn_ok.clicked.connect(self.graficar)
    
    def graf_selected(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.graf_selecc = selected_button.value

        
    def graficar(self):
        graf.graf_bar(1)
        