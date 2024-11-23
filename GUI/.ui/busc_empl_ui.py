# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busc_empl.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_graf_form(object):
    def setupUi(self, graf_form):
        if not graf_form.objectName():
            graf_form.setObjectName(u"graf_form")
        graf_form.resize(461, 290)
        self.gridLayout = QGridLayout(graf_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.hGrafBtn = QRadioButton(graf_form)
        self.hGrafBtn.setObjectName(u"hGrafBtn")
        self.hGrafBtn.setEnabled(False)
        font = QFont()
        font.setWeight(QFont.Light)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.hGrafBtn.setFont(font)
        self.hGrafBtn.setCheckable(False)

        self.gridLayout_2.addWidget(self.hGrafBtn, 3, 0, 1, 1)

        self.ID_bsc_btn = QRadioButton(graf_form)
        self.ID_bsc_btn.setObjectName(u"ID_bsc_btn")
        self.ID_bsc_btn.setChecked(True)

        self.gridLayout_2.addWidget(self.ID_bsc_btn, 1, 0, 1, 1)

        self.label_2 = QLabel(graf_form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.bGrafBtn = QRadioButton(graf_form)
        self.bGrafBtn.setObjectName(u"bGrafBtn")
        self.bGrafBtn.setEnabled(False)
        self.bGrafBtn.setFont(font)

        self.gridLayout_2.addWidget(self.bGrafBtn, 5, 0, 1, 1)

        self.Btn_Ok = QPushButton(graf_form)
        self.Btn_Ok.setObjectName(u"Btn_Ok")

        self.gridLayout_2.addWidget(self.Btn_Ok, 5, 1, 1, 1)

        self.label_3 = QLabel(graf_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.line_id = QLineEdit(graf_form)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.line_id.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.line_id, 3, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.label = QLabel(graf_form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(15)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(graf_form)

        QMetaObject.connectSlotsByName(graf_form)
    # setupUi

    def retranslateUi(self, graf_form):
        graf_form.setWindowTitle(QCoreApplication.translate("graf_form", u"Dialog", None))
        self.hGrafBtn.setText(QCoreApplication.translate("graf_form", u"Est\u00e1mos trabajando en esta funci\u00f3n", None))
        self.ID_bsc_btn.setText(QCoreApplication.translate("graf_form", u"ID de empleado", None))
        self.label_2.setText(QCoreApplication.translate("graf_form", u"Encontrar por:", None))
        self.bGrafBtn.setText(QCoreApplication.translate("graf_form", u"Est\u00e1mos trabajando en esta funci\u00f3n", None))
        self.Btn_Ok.setText(QCoreApplication.translate("graf_form", u"Buscar", None))
        self.label_3.setText(QCoreApplication.translate("graf_form", u"Datos del empleado a encontrar", None))
        self.line_id.setText("")
        self.label.setText(QCoreApplication.translate("graf_form", u"Buscar Empleados", None))
    # retranslateUi

