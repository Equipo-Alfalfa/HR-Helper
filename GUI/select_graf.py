import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication,  QMainWindow, QPushButton,QDialog, QRadioButton, QComboBox)
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
        self.graf_selecc = 0
  
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

        self.combbox = self.ui.findChild(QComboBox, 'comboBox')
        self.combbox.clear()

    
    def graf_selected(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.graf_selecc = selected_button.value

        if self.graf_selecc == 1:
            self.combbox.clear()
            self.combbox.addItems(['Campo de Educación','2'])
        elif self.graf_selecc == 2:
            self.combbox.clear()
            self.combbox.addItems(['3','4'])
        elif self.graf_selecc == 3:
            self.combbox.clear()
            self.combbox.addItems(['Relación Edad/Departamento','6'])        
        else:
            self.combbox.clear()
    
    def graficar(self):
        graf.graficar(self.graf_selecc, self.combbox.currentText())
        