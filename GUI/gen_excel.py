from PySide6.QtWidgets import QMessageBox, QWidget

class excelUI(QWidget):
    def __init__(self):
        super().__init__()


    def show_warning_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText('Se ha generado el archivo excel con los datos limpios\npuedes encontrarlo en la carpeta "Salidas"')
        msg_box.setWindowTitle("Información")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
