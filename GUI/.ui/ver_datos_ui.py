# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ver_datos.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(618, 359)
        font = QFont()
        font.setKerning(True)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 2)

        self.Encabezado = QLabel(Form)
        self.Encabezado.setObjectName(u"Encabezado")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Encabezado.sizePolicy().hasHeightForWidth())
        self.Encabezado.setSizePolicy(sizePolicy)
        self.Encabezado.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setKerning(True)
        self.Encabezado.setFont(font1)

        self.gridLayout.addWidget(self.Encabezado, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 6, 0, 1, 1)

        self.line_edad = QLineEdit(Form)
        self.line_edad.setObjectName(u"line_edad")
        self.line_edad.setReadOnly(True)
        self.line_edad.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_edad, 4, 1, 1, 1)

        self.line_area = QLineEdit(Form)
        self.line_area.setObjectName(u"line_area")
        self.line_area.setReadOnly(True)
        self.line_area.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_area, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)

        self.line_sueldo = QLineEdit(Form)
        self.line_sueldo.setObjectName(u"line_sueldo")
        self.line_sueldo.setReadOnly(True)
        self.line_sueldo.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_sueldo, 6, 1, 1, 1)

        self.lab_ar = QLabel(Form)
        self.lab_ar.setObjectName(u"lab_ar")

        self.gridLayout_3.addWidget(self.lab_ar, 3, 0, 1, 1)

        self.line_puesto = QLineEdit(Form)
        self.line_puesto.setObjectName(u"line_puesto")
        self.line_puesto.setReadOnly(True)
        self.line_puesto.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_puesto, 5, 1, 1, 1)

        self.lab_idd = QLabel(Form)
        self.lab_idd.setObjectName(u"lab_idd")

        self.gridLayout_3.addWidget(self.lab_idd, 2, 0, 1, 1)

        self.lab_n = QLabel(Form)
        self.lab_n.setObjectName(u"lab_n")

        self.gridLayout_3.addWidget(self.lab_n, 0, 0, 1, 1)

        self.line_nombre = QLineEdit(Form)
        self.line_nombre.setObjectName(u"line_nombre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_nombre.sizePolicy().hasHeightForWidth())
        self.line_nombre.setSizePolicy(sizePolicy1)
        self.line_nombre.setMinimumSize(QSize(110, 0))
        self.line_nombre.setReadOnly(True)
        self.line_nombre.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_nombre, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 5, 0, 1, 1)

        self.lab_ed = QLabel(Form)
        self.lab_ed.setObjectName(u"lab_ed")

        self.gridLayout_3.addWidget(self.lab_ed, 4, 0, 1, 1)

        self.line_id = QLineEdit(Form)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setReadOnly(True)
        self.line_id.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_id, 1, 1, 1, 1)

        self.lab_id = QLabel(Form)
        self.lab_id.setObjectName(u"lab_id")

        self.gridLayout_3.addWidget(self.lab_id, 1, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)

        self.yrs_comp = QLineEdit(Form)
        self.yrs_comp.setObjectName(u"yrs_comp")

        self.gridLayout_3.addWidget(self.yrs_comp, 0, 3, 1, 1)

        self.yrs_prom = QLineEdit(Form)
        self.yrs_prom.setObjectName(u"yrs_prom")

        self.gridLayout_3.addWidget(self.yrs_prom, 1, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 10, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Encabezado.setText(QCoreApplication.translate("Form", u"Visualizador de datos", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Sueldo Mensual ($)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"a\u00f1os en la compa\u00f1ia", None))
        self.lab_ar.setText(QCoreApplication.translate("Form", u"Area de trabajo", None))
        self.lab_idd.setText(QCoreApplication.translate("Form", u"Nro de Documento de identidad", None))
        self.lab_n.setText(QCoreApplication.translate("Form", u"Nombre Empleado", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"puesto", None))
        self.lab_ed.setText(QCoreApplication.translate("Form", u"Edad", None))
        self.lab_id.setText(QCoreApplication.translate("Form", u"ID de empleado", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"a\u00f1os desde la ultima promoci\u00f3n", None))
    # retranslateUi

