from PySide6.QtWidgets import QMessageBox, QWidget

class LimpDialUI(QWidget):
    def __init__(self):
        super().__init__()


    def show_warning_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Es necesaria una limpieza de datos, puede ejecutarla desde el menú principal")
        msg_box.setWindowTitle("Advertencia")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
