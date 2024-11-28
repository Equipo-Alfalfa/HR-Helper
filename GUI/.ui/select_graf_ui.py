# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_graf.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_QDialog(object):
    def setupUi(self, QDialog):
        if not QDialog.objectName():
            QDialog.setObjectName(u"QDialog")
        QDialog.resize(461, 268)
        self.gridLayout = QGridLayout(QDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(QDialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.vGrafBtn = QRadioButton(QDialog)
        self.vGrafBtn.setObjectName(u"vGrafBtn")

        self.gridLayout_2.addWidget(self.vGrafBtn, 8, 0, 1, 1)

        self.bGrafBtn = QRadioButton(QDialog)
        self.bGrafBtn.setObjectName(u"bGrafBtn")

        self.gridLayout_2.addWidget(self.bGrafBtn, 7, 0, 1, 1)

        self.pGrafBtn = QRadioButton(QDialog)
        self.pGrafBtn.setObjectName(u"pGrafBtn")

        self.gridLayout_2.addWidget(self.pGrafBtn, 1, 0, 1, 1)

        self.label_2 = QLabel(QDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.Btn_Ok = QPushButton(QDialog)
        self.Btn_Ok.setObjectName(u"Btn_Ok")

        self.gridLayout_2.addWidget(self.Btn_Ok, 8, 2, 1, 1)

        self.hGrafBtn = QRadioButton(QDialog)
        self.hGrafBtn.setObjectName(u"hGrafBtn")

        self.gridLayout_2.addWidget(self.hGrafBtn, 4, 0, 1, 1)

        self.comboBox = QComboBox(QDialog)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.comboBox, 1, 2, 1, 1)

        self.notilabel = QLabel(QDialog)
        self.notilabel.setObjectName(u"notilabel")

        self.gridLayout_2.addWidget(self.notilabel, 7, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.label = QLabel(QDialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 1))
        self.label.setMaximumSize(QSize(16777215, 70))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(QDialog)

        QMetaObject.connectSlotsByName(QDialog)
    # setupUi

    def retranslateUi(self, QDialog):
        QDialog.setWindowTitle(QCoreApplication.translate("QDialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("QDialog", u"Datos del Gr\u00e1fico", None))
        self.vGrafBtn.setText(QCoreApplication.translate("QDialog", u"Gr\u00e1fico Viol\u00edn", None))
        self.bGrafBtn.setText(QCoreApplication.translate("QDialog", u"Grafico de Barras", None))
        self.pGrafBtn.setText(QCoreApplication.translate("QDialog", u"Gr\u00e1fico Circular", None))
        self.label_2.setText(QCoreApplication.translate("QDialog", u"Tipo de Gr\u00e1fico", None))
        self.Btn_Ok.setText(QCoreApplication.translate("QDialog", u"Generar", None))
        self.hGrafBtn.setText(QCoreApplication.translate("QDialog", u"Mapa de Calor", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("QDialog", u"EducationField", None))

        self.notilabel.setText("")
        self.label.setText(QCoreApplication.translate("QDialog", u"Mostrar un Gr\u00e1fico", None))
    # retranslateUi

