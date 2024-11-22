# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(697, 477)
        Form.setMinimumSize(QSize(0, 150))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        font.setWeight(QFont.Light)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(19)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_calc = QPushButton(Form)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy1.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy1)
        self.btn_calc.setMinimumSize(QSize(0, 130))
        self.btn_calc.setMaximumSize(QSize(16777215, 500))
        icon = QIcon()
        icon.addFile(u"../../source/icon/calculator.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_calc.setIcon(icon)
        self.btn_calc.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.btn_calc, 1, 0, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setMinimumSize(QSize(0, 130))
        self.btn_4.setMaximumSize(QSize(16777215, 500))

        self.gridLayout_3.addWidget(self.btn_4, 1, 1, 1, 1)

        self.btn_busc = QPushButton(Form)
        self.btn_busc.setObjectName(u"btn_busc")
        sizePolicy1.setHeightForWidth(self.btn_busc.sizePolicy().hasHeightForWidth())
        self.btn_busc.setSizePolicy(sizePolicy1)
        self.btn_busc.setMinimumSize(QSize(0, 130))
        self.btn_busc.setMaximumSize(QSize(16777215, 500))
        icon1 = QIcon()
        icon1.addFile(u"../../source/icon/magnifier.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_busc.setIcon(icon1)
        self.btn_busc.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.btn_busc, 0, 1, 1, 1)

        self.btn_graf = QPushButton(Form)
        self.btn_graf.setObjectName(u"btn_graf")
        sizePolicy1.setHeightForWidth(self.btn_graf.sizePolicy().hasHeightForWidth())
        self.btn_graf.setSizePolicy(sizePolicy1)
        self.btn_graf.setMinimumSize(QSize(0, 130))
        self.btn_graf.setMaximumSize(QSize(16777215, 500))
        icon2 = QIcon()
        icon2.addFile(u"../../source/icon/sales.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_graf.setIcon(icon2)
        self.btn_graf.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.btn_graf, 0, 0, 1, 1)

        self.gridLayout_3.setColumnMinimumWidth(0, 10)
        self.gridLayout_3.setColumnMinimumWidth(1, 10)
        self.gridLayout_3.setRowMinimumHeight(0, 10)
        self.gridLayout_3.setRowMinimumHeight(1, 10)

        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.label)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Seleccione una Herramienta", None))
        self.label.setText(QCoreApplication.translate("Form", u"Bienvenido a la Herramienta de Recursos Humanos", None))
        self.btn_calc.setText(QCoreApplication.translate("Form", u"Calcular N\u00f3mina", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.btn_busc.setText(QCoreApplication.translate("Form", u"Buscar Trabajadores", None))
        self.btn_graf.setText(QCoreApplication.translate("Form", u"Generar Graficos", None))
    # retranslateUi

