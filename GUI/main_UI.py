import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Cargar el archivo .ui
        loader = QUiLoader()
        file = QFile("./GUI/MainUI.ui")
        file.open(QFile.ReadOnly)
        
        # Cargar la interfaz en la ventana principal
        self.ui = loader.load(file, self)
        file.close()


        # Establecer la interfaz cargada como la ventana central
        self.setCentralWidget(self.ui)

        # Conectar los botones a sus funciones
        self.setup_connections()

    def setup_connections(self):

        stackedWidget = self.ui.findChild(QStackedWidget, 'stackedWidget')
        pushButton = self.ui.findChild(QPushButton, 'btn_4')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
