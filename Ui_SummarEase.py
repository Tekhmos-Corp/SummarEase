# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazkfgcjn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_SumarEase(object):
    def setupUi(self, SumarEase):
        if not SumarEase.objectName():
            SumarEase.setObjectName(u"SumarEase")
        SumarEase.resize(480, 640)
        icon = QIcon()
        icon.addFile(u"assets/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SumarEase.setWindowIcon(icon)
        self.centralwidget = QWidget(SumarEase)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(100, 10, 281, 81))
        self.title.setSizeIncrement(QSize(0, 0))
        self.title.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(32)
        self.title.setFont(font)
        self.Input = QTextEdit(self.centralwidget)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(20, 120, 441, 181))
        self.input_text = QLabel(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(20, 90, 101, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.input_text.setFont(font1)
        self.output = QPlainTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(20, 370, 441, 211))
        self.output.setReadOnly(True)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 310, 371, 51))
        self.radio = QHBoxLayout(self.horizontalLayoutWidget)
        self.radio.setObjectName(u"radio")
        self.radio.setContentsMargins(0, 0, 0, 0)
        self.summarizeradio = QRadioButton(self.horizontalLayoutWidget)
        self.summarizeradio.setObjectName(u"summarizeradio")

        self.radio.addWidget(self.summarizeradio)

        self.explainradio = QRadioButton(self.horizontalLayoutWidget)
        self.explainradio.setObjectName(u"explainradio")
        self.explainradio.setEnabled(True)

        self.radio.addWidget(self.explainradio)

        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(20, 340, 101, 31))
        self.output_label.setFont(font1)
        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(190, 590, 80, 30))
        SumarEase.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SumarEase)
        self.statusbar.setObjectName(u"statusbar")
        SumarEase.setStatusBar(self.statusbar)

        self.retranslateUi(SumarEase)

        QMetaObject.connectSlotsByName(SumarEase)
    # setupUi

    def retranslateUi(self, SumarEase):
        SumarEase.setWindowTitle(QCoreApplication.translate("SumarEase", u"SummarEase", None))
        self.title.setText(QCoreApplication.translate("SumarEase", u"SummarEase", None))
        self.input_text.setText(QCoreApplication.translate("SumarEase", u"  Input", None))
        self.summarizeradio.setText(QCoreApplication.translate("SumarEase", u"Summarize", None))
        self.explainradio.setText(QCoreApplication.translate("SumarEase", u"Explain", None))
        self.output_label.setText(QCoreApplication.translate("SumarEase", u"  Output", None))
        self.send.setText(QCoreApplication.translate("SumarEase", u"Send", None))
    # retranslateUi

