import sys
from PySide6.QtWidgets import (QPushButton,QDialog, QRadioButton, QLineEdit)
from PySide6.QtUiTools import QUiLoader
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos')))



class buscUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('./GUI/.ui/busc_empl.ui')
        self.ui.setWindowTitle("Buscar Empleado")
        self.ui.setModal(True)
        self.setup_connections()

    def setup_connections(self):
        self.lineid = self.ui.findChild(QLineEdit, 'line_id')

        self.bsc_por_id = self.ui.findChild(QRadioButton, 'ID_bsc_btn')
        self.bsc_por_id.toggled.connect(self.setEnabled)

        self.btn_buscar = self.ui.findChild(QPushButton, 'Btn_Ok')
        self.btn_buscar.clicked.connect(self.buscar_empleado)

    def buscar_empleado(self):
        import GUI.mostrar_datos
        id = self.lineid.text()
        self.mostrar_datos = GUI.mostrar_datos.MostrarDatosUI(id)
        self.mostrar_datos.ui.show()
        self.ui.close()

    def setEnabled(self):
        pass
