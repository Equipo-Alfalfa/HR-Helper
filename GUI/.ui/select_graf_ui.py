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

class Ui_graf_form(object):
    def setupUi(self, graf_form):
        if not graf_form.objectName():
            graf_form.setObjectName(u"graf_form")
        graf_form.resize(461, 319)
        self.gridLayout = QGridLayout(graf_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(graf_form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.hGrafBtn = QRadioButton(graf_form)
        self.hGrafBtn.setObjectName(u"hGrafBtn")

        self.gridLayout_2.addWidget(self.hGrafBtn, 2, 0, 1, 1)

        self.bGrafBtn = QRadioButton(graf_form)
        self.bGrafBtn.setObjectName(u"bGrafBtn")

        self.gridLayout_2.addWidget(self.bGrafBtn, 3, 0, 1, 1)

        self.label_2 = QLabel(graf_form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(graf_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.pGrafBtn = QRadioButton(graf_form)
        self.pGrafBtn.setObjectName(u"pGrafBtn")

        self.gridLayout_2.addWidget(self.pGrafBtn, 1, 0, 1, 1)

        self.Btn_Ok = QPushButton(graf_form)
        self.Btn_Ok.setObjectName(u"Btn_Ok")

        self.gridLayout_2.addWidget(self.Btn_Ok, 3, 1, 1, 1)

        self.comboBox = QComboBox(graf_form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_4 = QLabel(graf_form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)


        self.retranslateUi(graf_form)

        QMetaObject.connectSlotsByName(graf_form)
    # setupUi

    def retranslateUi(self, graf_form):
        graf_form.setWindowTitle(QCoreApplication.translate("graf_form", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("graf_form", u"Mostrar un Gr\u00e1fico", None))
        self.hGrafBtn.setText(QCoreApplication.translate("graf_form", u"Mapa de Calor", None))
        self.bGrafBtn.setText(QCoreApplication.translate("graf_form", u"Grafico de Barras", None))
        self.label_2.setText(QCoreApplication.translate("graf_form", u"Tipo de Gr\u00e1fico", None))
        self.label_3.setText(QCoreApplication.translate("graf_form", u"Datos del Gr\u00e1fico", None))
        self.pGrafBtn.setText(QCoreApplication.translate("graf_form", u"Gr\u00e1fico Circular", None))
        self.Btn_Ok.setText(QCoreApplication.translate("graf_form", u"Generar", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("graf_form", u"EducationField", None))

        self.label_4.setText("")
    # retranslateUi

