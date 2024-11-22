import sys
from PySide6.QtWidgets import (QPushButton,QDialog)
from PySide6.QtUiTools import QUiLoader
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos')))
import modulos.datacleaning as data


class cleanedUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('./GUI/.ui/cleaned.ui')
        self.ui.setWindowTitle("Información")
        self.ui.setModal(True)
        self.setup_connections()
        self.ui.show()
    def setup_connections(self):
        self.btn_ok = self.ui.findChild(QPushButton, 'btn')
        self.btn_ok.clicked.connect(self.ui.close)

def clean():
    data.clean()
