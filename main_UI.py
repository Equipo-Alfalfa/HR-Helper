import sys
from PySide6.QtWidgets import (QApplication,  QMainWindow, QPushButton)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile,QThread, Signal, Slot
from PySide6.QtGui import QIcon

class limpThread(QThread):
     finished = Signal()
     def run(self):
        import modulos.datacleaning as data
        data.clean()
        self.finished.emit()
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loader = QUiLoader()
        file = QFile("./GUI/.ui/MainUI.ui")
        file.open(QFile.ReadOnly)
        
        self.ui = loader.load(file, self)
        file.close()

        self.setCentralWidget(self.ui)
        self.setWindowTitle("HR Helper")
        self.setWindowIcon(QIcon('./GUI/icons/arraycolors.ico'))
        self.setup_connections()

    def setup_connections(self):

        btn_graf = self.ui.findChild(QPushButton, 'btn_graf')
        btn_graf.clicked.connect(self.graf_window)

        btn_cln = self.ui.findChild(QPushButton, 'btn_cln')
        btn_cln.clicked.connect(self.clean_window)

        btn_busc = self.ui.findChild(QPushButton, 'btn_busc')
        btn_busc.clicked.connect(self.busc_window)

        btn_busc = self.ui.findChild(QPushButton, 'btn_excel')
        btn_busc.clicked.connect(self.gen_excel)

    def graf_window(self):
        from GUI.select_graf import grafSelUI
        self.graf_form = grafSelUI()
        self.graf_form.ui.show()

    def clean_window(self):
        from GUI.cleaned import cleanedUI
        self.clean_dialog = cleanedUI()
        self.thread = limpThread()
        self.thread.finished.connect(self.clean_dialog.ui.show)
        self.thread.start()

    def busc_window(self):
        from GUI.busc_empl import buscUI
        self.busc_form = buscUI()
        self.busc_form.ui.show()

    def gen_excel(self):
        from GUI.gen_excel_pro import excelUI
        self.excel_form = excelUI()
        self.excel_form.ui.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./GUI/icons/arraycolors.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
