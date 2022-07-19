# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_bcars2_main.ui'
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
        MainWindow.resize(1007, 213)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(97, 144))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.radioButtonCCD = QRadioButton(self.frame)
        self.radioButtonCCD.setObjectName(u"radioButtonCCD")
        self.radioButtonCCD.setEnabled(False)
        self.radioButtonCCD.setStyleSheet(u"QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonCCD.setCheckable(True)
        self.radioButtonCCD.setChecked(False)
        self.radioButtonCCD.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.radioButtonCCD, 0, Qt.AlignHCenter)

        self.pushButtonInitCCD = QPushButton(self.frame)
        self.pushButtonInitCCD.setObjectName(u"pushButtonInitCCD")
        self.pushButtonInitCCD.setMinimumSize(QSize(75, 0))
        self.pushButtonInitCCD.setMaximumSize(QSize(75, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        self.pushButtonInitCCD.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButtonInitCCD, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(185, 144))
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.radioButtonSpectrograph = QRadioButton(self.frame_5)
        self.radioButtonSpectrograph.setObjectName(u"radioButtonSpectrograph")
        self.radioButtonSpectrograph.setEnabled(False)
        self.radioButtonSpectrograph.setStyleSheet(u"QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonSpectrograph.setCheckable(True)
        self.radioButtonSpectrograph.setChecked(False)
        self.radioButtonSpectrograph.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.radioButtonSpectrograph, 0, Qt.AlignHCenter)

        self.pushButtonInitSpectrograph = QPushButton(self.frame_5)
        self.pushButtonInitSpectrograph.setObjectName(u"pushButtonInitSpectrograph")
        self.pushButtonInitSpectrograph.setMinimumSize(QSize(75, 0))
        self.pushButtonInitSpectrograph.setMaximumSize(QSize(75, 16777215))
        self.pushButtonInitSpectrograph.setFont(font1)

        self.verticalLayout_5.addWidget(self.pushButtonInitSpectrograph, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(185, 144))
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.radioButtonMicroStage = QRadioButton(self.frame_4)
        self.radioButtonMicroStage.setObjectName(u"radioButtonMicroStage")
        self.radioButtonMicroStage.setEnabled(False)
        self.radioButtonMicroStage.setStyleSheet(u"QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonMicroStage.setCheckable(True)
        self.radioButtonMicroStage.setChecked(False)
        self.radioButtonMicroStage.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.radioButtonMicroStage, 0, Qt.AlignHCenter)

        self.pushButtonInitMicroStage = QPushButton(self.frame_4)
        self.pushButtonInitMicroStage.setObjectName(u"pushButtonInitMicroStage")
        self.pushButtonInitMicroStage.setMinimumSize(QSize(75, 0))
        self.pushButtonInitMicroStage.setMaximumSize(QSize(75, 16777215))
        self.pushButtonInitMicroStage.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButtonInitMicroStage, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_4, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(165, 144))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.radioButtonNanoStage = QRadioButton(self.frame_2)
        self.radioButtonNanoStage.setObjectName(u"radioButtonNanoStage")
        self.radioButtonNanoStage.setEnabled(False)
        self.radioButtonNanoStage.setStyleSheet(u"QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonNanoStage.setCheckable(True)
        self.radioButtonNanoStage.setChecked(False)
        self.radioButtonNanoStage.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.radioButtonNanoStage, 0, Qt.AlignHCenter)

        self.pushButtonInitNanoStage = QPushButton(self.frame_2)
        self.pushButtonInitNanoStage.setObjectName(u"pushButtonInitNanoStage")
        self.pushButtonInitNanoStage.setMinimumSize(QSize(75, 0))
        self.pushButtonInitNanoStage.setMaximumSize(QSize(75, 16777215))
        self.pushButtonInitNanoStage.setFont(font1)

        self.verticalLayout.addWidget(self.pushButtonInitNanoStage, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_2, 0, 3, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(170, 144))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.radioButtonDelayStage = QRadioButton(self.frame_3)
        self.radioButtonDelayStage.setObjectName(u"radioButtonDelayStage")
        self.radioButtonDelayStage.setEnabled(False)
        self.radioButtonDelayStage.setStyleSheet(u"QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonDelayStage.setCheckable(True)
        self.radioButtonDelayStage.setChecked(False)
        self.radioButtonDelayStage.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.radioButtonDelayStage, 0, Qt.AlignHCenter)

        self.pushButtonInitDelayStage = QPushButton(self.frame_3)
        self.pushButtonInitDelayStage.setObjectName(u"pushButtonInitDelayStage")
        self.pushButtonInitDelayStage.setMinimumSize(QSize(75, 0))
        self.pushButtonInitDelayStage.setMaximumSize(QSize(75, 16777215))
        self.pushButtonInitDelayStage.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButtonInitDelayStage, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_3, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox.setFont(font2)
        self.groupBox.setFlat(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonWinSpectroscopy = QPushButton(self.groupBox)
        self.pushButtonWinSpectroscopy.setObjectName(u"pushButtonWinSpectroscopy")
        self.pushButtonWinSpectroscopy.setMaximumSize(QSize(134, 50))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButtonWinSpectroscopy.setFont(font3)

        self.gridLayout.addWidget(self.pushButtonWinSpectroscopy, 0, 0, 1, 1)

        self.pushButtonWinRaster = QPushButton(self.groupBox)
        self.pushButtonWinRaster.setObjectName(u"pushButtonWinRaster")
        self.pushButtonWinRaster.setMaximumSize(QSize(134, 50))
        self.pushButtonWinRaster.setFont(font3)

        self.gridLayout.addWidget(self.pushButtonWinRaster, 1, 0, 1, 1)

        self.pushButtonWinRaster_2 = QPushButton(self.groupBox)
        self.pushButtonWinRaster_2.setObjectName(u"pushButtonWinRaster_2")
        self.pushButtonWinRaster_2.setMaximumSize(QSize(134, 50))
        self.pushButtonWinRaster_2.setFont(font3)

        self.gridLayout.addWidget(self.pushButtonWinRaster_2, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 7, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1007, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CCD", None))
        self.radioButtonCCD.setText("")
        self.pushButtonInitCCD.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Spectrograph", None))
        self.radioButtonSpectrograph.setText("")
        self.pushButtonInitSpectrograph.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Macro Stage", None))
        self.radioButtonMicroStage.setText("")
        self.pushButtonInitMicroStage.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nano Stage", None))
        self.radioButtonNanoStage.setText("")
        self.pushButtonInitNanoStage.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Delay Stage", None))
        self.radioButtonDelayStage.setText("")
        self.pushButtonInitDelayStage.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.pushButtonWinSpectroscopy.setText(QCoreApplication.translate("MainWindow", u"Spectroscopy", None))
        self.pushButtonWinRaster.setText(QCoreApplication.translate("MainWindow", u"Micro Raster", None))
        self.pushButtonWinRaster_2.setText(QCoreApplication.translate("MainWindow", u"Macro Raster", None))
    # retranslateUi

