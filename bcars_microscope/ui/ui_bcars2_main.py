# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt_designer\qt_bcars2_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(97, 144))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.radioButtonCCD = QtWidgets.QRadioButton(self.frame)
        self.radioButtonCCD.setEnabled(False)
        self.radioButtonCCD.setStyleSheet("QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonCCD.setText("")
        self.radioButtonCCD.setCheckable(True)
        self.radioButtonCCD.setChecked(False)
        self.radioButtonCCD.setAutoExclusive(False)
        self.radioButtonCCD.setObjectName("radioButtonCCD")
        self.verticalLayout_4.addWidget(self.radioButtonCCD, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonInitCCD = QtWidgets.QPushButton(self.frame)
        self.pushButtonInitCCD.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButtonInitCCD.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButtonInitCCD.setFont(font)
        self.pushButtonInitCCD.setObjectName("pushButtonInitCCD")
        self.verticalLayout_4.addWidget(self.pushButtonInitCCD, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMaximumSize(QtCore.QSize(185, 144))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.radioButtonSpectrograph = QtWidgets.QRadioButton(self.frame_5)
        self.radioButtonSpectrograph.setEnabled(False)
        self.radioButtonSpectrograph.setStyleSheet("QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonSpectrograph.setText("")
        self.radioButtonSpectrograph.setCheckable(True)
        self.radioButtonSpectrograph.setChecked(False)
        self.radioButtonSpectrograph.setAutoExclusive(False)
        self.radioButtonSpectrograph.setObjectName("radioButtonSpectrograph")
        self.verticalLayout_5.addWidget(self.radioButtonSpectrograph, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonInitSpectrograph = QtWidgets.QPushButton(self.frame_5)
        self.pushButtonInitSpectrograph.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButtonInitSpectrograph.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButtonInitSpectrograph.setFont(font)
        self.pushButtonInitSpectrograph.setObjectName("pushButtonInitSpectrograph")
        self.verticalLayout_5.addWidget(self.pushButtonInitSpectrograph, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_5, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(185, 144))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.radioButtonMicroStage = QtWidgets.QRadioButton(self.frame_4)
        self.radioButtonMicroStage.setEnabled(False)
        self.radioButtonMicroStage.setStyleSheet("QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonMicroStage.setText("")
        self.radioButtonMicroStage.setCheckable(True)
        self.radioButtonMicroStage.setChecked(False)
        self.radioButtonMicroStage.setAutoExclusive(False)
        self.radioButtonMicroStage.setObjectName("radioButtonMicroStage")
        self.verticalLayout_3.addWidget(self.radioButtonMicroStage, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonInitMicroStage = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonInitMicroStage.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButtonInitMicroStage.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButtonInitMicroStage.setFont(font)
        self.pushButtonInitMicroStage.setObjectName("pushButtonInitMicroStage")
        self.verticalLayout_3.addWidget(self.pushButtonInitMicroStage, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_4, 0, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(165, 144))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.radioButtonNanoStage = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonNanoStage.setEnabled(False)
        self.radioButtonNanoStage.setStyleSheet("QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonNanoStage.setText("")
        self.radioButtonNanoStage.setCheckable(True)
        self.radioButtonNanoStage.setChecked(False)
        self.radioButtonNanoStage.setAutoExclusive(False)
        self.radioButtonNanoStage.setObjectName("radioButtonNanoStage")
        self.verticalLayout.addWidget(self.radioButtonNanoStage, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonInitNanoStage = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonInitNanoStage.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButtonInitNanoStage.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButtonInitNanoStage.setFont(font)
        self.pushButtonInitNanoStage.setObjectName("pushButtonInitNanoStage")
        self.verticalLayout.addWidget(self.pushButtonInitNanoStage, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_2, 0, 3, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(170, 144))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.radioButtonDelayStage = QtWidgets.QRadioButton(self.frame_3)
        self.radioButtonDelayStage.setEnabled(False)
        self.radioButtonDelayStage.setStyleSheet("QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonDelayStage.setText("")
        self.radioButtonDelayStage.setCheckable(True)
        self.radioButtonDelayStage.setChecked(False)
        self.radioButtonDelayStage.setAutoExclusive(False)
        self.radioButtonDelayStage.setObjectName("radioButtonDelayStage")
        self.verticalLayout_2.addWidget(self.radioButtonDelayStage, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonInitDelayStage = QtWidgets.QPushButton(self.frame_3)
        self.pushButtonInitDelayStage.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButtonInitDelayStage.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButtonInitDelayStage.setFont(font)
        self.pushButtonInitDelayStage.setObjectName("pushButtonInitDelayStage")
        self.verticalLayout_2.addWidget(self.pushButtonInitDelayStage, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_3, 0, 4, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMaximumSize(QtCore.QSize(170, 144))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.radioButtonLaser = QtWidgets.QRadioButton(self.frame_6)
        self.radioButtonLaser.setEnabled(False)
        self.radioButtonLaser.setStyleSheet("QRadioButton { color: white}\n"
"QRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\n"
"QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n"
"QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}")
        self.radioButtonLaser.setText("")
        self.radioButtonLaser.setCheckable(True)
        self.radioButtonLaser.setChecked(False)
        self.radioButtonLaser.setAutoExclusive(False)
        self.radioButtonLaser.setObjectName("radioButtonLaser")
        self.verticalLayout_6.addWidget(self.radioButtonLaser, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonInitLaser = QtWidgets.QPushButton(self.frame_6)
        self.pushButtonInitLaser.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButtonInitLaser.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButtonInitLaser.setFont(font)
        self.pushButtonInitLaser.setObjectName("pushButtonInitLaser")
        self.verticalLayout_6.addWidget(self.pushButtonInitLaser, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_6, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 6, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonWinRaster = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonWinRaster.setMaximumSize(QtCore.QSize(134, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonWinRaster.setFont(font)
        self.pushButtonWinRaster.setObjectName("pushButtonWinRaster")
        self.gridLayout.addWidget(self.pushButtonWinRaster, 1, 1, 1, 1)
        self.pushButtonWinSpectroscopy = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonWinSpectroscopy.setMaximumSize(QtCore.QSize(134, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonWinSpectroscopy.setFont(font)
        self.pushButtonWinSpectroscopy.setObjectName("pushButtonWinSpectroscopy")
        self.gridLayout.addWidget(self.pushButtonWinSpectroscopy, 1, 0, 1, 1)
        self.pushButtonWinRasterMacro = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonWinRasterMacro.setMaximumSize(QtCore.QSize(134, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonWinRasterMacro.setFont(font)
        self.pushButtonWinRasterMacro.setObjectName("pushButtonWinRasterMacro")
        self.gridLayout.addWidget(self.pushButtonWinRasterMacro, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CCD"))
        self.pushButtonInitCCD.setText(_translate("MainWindow", "Initialize"))
        self.label_5.setText(_translate("MainWindow", "Spectrograph"))
        self.pushButtonInitSpectrograph.setText(_translate("MainWindow", "Initialize"))
        self.label_4.setText(_translate("MainWindow", "Macro Stage"))
        self.pushButtonInitMicroStage.setText(_translate("MainWindow", "Initialize"))
        self.label_2.setText(_translate("MainWindow", "Nano Stage"))
        self.pushButtonInitNanoStage.setText(_translate("MainWindow", "Initialize"))
        self.label_3.setText(_translate("MainWindow", "Delay Stage"))
        self.pushButtonInitDelayStage.setText(_translate("MainWindow", "Initialize"))
        self.label_6.setText(_translate("MainWindow", "Laser"))
        self.pushButtonInitLaser.setText(_translate("MainWindow", "Initialize"))
        self.groupBox.setTitle(_translate("MainWindow", "Widgets"))
        self.pushButtonWinRaster.setText(_translate("MainWindow", "Small Raster"))
        self.pushButtonWinSpectroscopy.setText(_translate("MainWindow", "Spectroscopy"))
        self.pushButtonWinRasterMacro.setText(_translate("MainWindow", "Macro Raster"))

