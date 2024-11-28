from PySide6.QtCore import QThread, Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos')))

class ExcelThread(QThread):
    finished = Signal()
    def run(self):
        import modulos.payroll_calc as excel
        excel.calculate_payroll("./source/datos/payroll.xlsx")
        self.finished.emit()

    def stop(self):
        self.quit()

class excelUI(QDialog):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('./GUI/.ui/gen_exl_prg.ui')
        self.ui.setWindowTitle("Generar Excel")
        self.ui.setModal(True)
        self.thread = ExcelThread()
        self.thread.finished.connect(self.task_finished)
        self.thread.start()
    def task_finished(self):
        self.ui.close()

        

        