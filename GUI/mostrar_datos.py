import sys
from PySide6.QtWidgets import (QWidget, QLineEdit)
from PySide6.QtUiTools import QUiLoader

class MostrarDatosUI(QWidget):
    def __init__(self, id):
        super().__init__()
        self.ui = QUiLoader().load('./GUI/.ui/ver_datos.ui')
        self.ui.setWindowTitle("Buscar Empleado")
        self.emp_id = id
        self.setup_connections()
        self.mostrar_datos()
        
    def setup_connections(self):
        self.line_id = self.ui.findChild(QLineEdit, 'line_id')
        self.line_nombre = self.ui.findChild(QLineEdit, 'line_nombre')
        self.line_edad = self.ui.findChild(QLineEdit, 'line_edad')
        self.line_puesto = self.ui.findChild(QLineEdit, 'line_puesto')
        self.line_sueldo = self.ui.findChild(QLineEdit, 'line_sueldo')
        self.line_area = self.ui.findChild(QLineEdit, 'line_area')
        self.line_comp = self.ui.findChild(QLineEdit, 'yrs_comp')
        self.line_prom = self.ui.findChild(QLineEdit, 'yrs_prom')

    def mostrar_datos(self):
        from modulos.buscar_empl import buscar_usuarios_por_id

        empleado = buscar_usuarios_por_id(self.emp_id)

        index = empleado.index[empleado['EmpID'] == 'RM108'].tolist()       
        self.line_id.setText(str(empleado['EmpID'][index[0]]))
        self.line_edad.setText(str(empleado['Age'][index[0]]))
        self.line_puesto.setText(str(empleado['JobRole'][index[0]]))
        self.line_sueldo.setText(str(empleado['MonthlyIncome'][index[0]]))
        self.line_area.setText(str(empleado['Department'][index[0]]))
        self.line_comp.setText(str(empleado['YearsAtCompany'][index[0]]))
        self.line_prom.setText(str(empleado['YearsSinceLastPromotion'][index[0]]))

