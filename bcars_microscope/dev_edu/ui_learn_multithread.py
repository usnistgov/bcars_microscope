# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_learn_multithread.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mpl_widget = QWidget(self.centralwidget)
        self.mpl_widget.setObjectName(u"mpl_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_widget.sizePolicy().hasHeightForWidth())
        self.mpl_widget.setSizePolicy(sizePolicy)
        self.mpl_widget.setMinimumSize(QSize(518, 451))
        self.mpl_widget.setAutoFillBackground(False)
        self.mpl_widget.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.verticalLayout.addWidget(self.mpl_widget)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(321, 16777215))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButtonStartAcq = QPushButton(self.frame_3)
        self.pushButtonStartAcq.setObjectName(u"pushButtonStartAcq")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonStartAcq.sizePolicy().hasHeightForWidth())
        self.pushButtonStartAcq.setSizePolicy(sizePolicy2)
        self.pushButtonStartAcq.setMinimumSize(QSize(50, 50))
        self.pushButtonStartAcq.setMaximumSize(QSize(75, 50))
        self.pushButtonStartAcq.setBaseSize(QSize(50, 50))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButtonStartAcq.setFont(font)
        self.pushButtonStartAcq.setStyleSheet(u"color: white;\n"
"font: 87 14pt \"Arial Black\";")

        self.horizontalLayout_2.addWidget(self.pushButtonStartAcq)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButtonStopAcq = QPushButton(self.frame_3)
        self.pushButtonStopAcq.setObjectName(u"pushButtonStopAcq")
        sizePolicy2.setHeightForWidth(self.pushButtonStopAcq.sizePolicy().hasHeightForWidth())
        self.pushButtonStopAcq.setSizePolicy(sizePolicy2)
        self.pushButtonStopAcq.setMinimumSize(QSize(50, 50))
        self.pushButtonStopAcq.setMaximumSize(QSize(75, 50))
        self.pushButtonStopAcq.setBaseSize(QSize(50, 50))
        self.pushButtonStopAcq.setFont(font)
        self.pushButtonStopAcq.setStyleSheet(u"color:red;\n"
"font: 87 14pt \"Arial Black\";")
        self.pushButtonStopAcq.setCheckable(True)
        self.pushButtonStopAcq.setChecked(False)

        self.horizontalLayout_2.addWidget(self.pushButtonStopAcq)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonStartAcq.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButtonStopAcq.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

