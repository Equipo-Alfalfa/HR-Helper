import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication,  QMainWindow, QPushButton, QDialog)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from GUI.select_graf import grafSelUI

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loader = QUiLoader()
        file = QFile("./GUI/.ui/MainUI.ui")
        file.open(QFile.ReadOnly)
        
        self.ui = loader.load(file, self)
        file.close()

        self.setCentralWidget(self.ui)

        self.setup_connections()

    def setup_connections(self):

        btn_graf = self.ui.findChild(QPushButton, 'btn_graf')
        btn_graf.clicked.connect(self.graf_window)

    def graf_window(self):
        self.graf_form = grafSelUI()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
