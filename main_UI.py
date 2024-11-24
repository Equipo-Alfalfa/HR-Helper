import sys
from PySide6.QtWidgets import (QApplication,  QMainWindow, QPushButton)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon

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

    def graf_window(self):
        from GUI.select_graf import grafSelUI
        self.graf_form = grafSelUI()
        self.graf_form.ui.show()

    def clean_window(self):
        from GUI.cleaned import cleanedUI, clean
        self.clean_dialog = cleanedUI()
        self.clean_dialog.ui.show()
        clean()

    def busc_window(self):
        from GUI.busc_empl import buscUI
        self.busc_form = buscUI()
        self.busc_form.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./GUI/icons/arraycolors.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
