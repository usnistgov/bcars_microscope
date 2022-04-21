# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_demo_2_threads.ui'
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
        MainWindow.resize(1007, 518)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 1, 2, 4, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.pushButton_moveCenter_Offset = QPushButton(self.frame)
        self.pushButton_moveCenter_Offset.setObjectName(u"pushButton_moveCenter_Offset")
        self.pushButton_moveCenter_Offset.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveCenter_Offset, 5, 4, 1, 1)

        self.spinBox_z_setpos = QDoubleSpinBox(self.frame)
        self.spinBox_z_setpos.setObjectName(u"spinBox_z_setpos")
        self.spinBox_z_setpos.setMinimumSize(QSize(75, 25))
        self.spinBox_z_setpos.setMaximumSize(QSize(200, 40))
        self.spinBox_z_setpos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_z_setpos.setReadOnly(False)
        self.spinBox_z_setpos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_z_setpos.setDecimals(3)
        self.spinBox_z_setpos.setMinimum(-10.000000000000000)
        self.spinBox_z_setpos.setMaximum(210.000000000000000)
        self.spinBox_z_setpos.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.spinBox_z_setpos, 4, 3, 1, 1)

        self.spinBox_x_setpos = QDoubleSpinBox(self.frame)
        self.spinBox_x_setpos.setObjectName(u"spinBox_x_setpos")
        self.spinBox_x_setpos.setMinimumSize(QSize(75, 25))
        self.spinBox_x_setpos.setMaximumSize(QSize(200, 40))
        self.spinBox_x_setpos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_x_setpos.setReadOnly(False)
        self.spinBox_x_setpos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_x_setpos.setDecimals(3)
        self.spinBox_x_setpos.setMinimum(-10.000000000000000)
        self.spinBox_x_setpos.setMaximum(210.000000000000000)
        self.spinBox_x_setpos.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.spinBox_x_setpos, 2, 3, 1, 1)

        self.pushButton_updatePosition = QPushButton(self.frame)
        self.pushButton_updatePosition.setObjectName(u"pushButton_updatePosition")
        self.pushButton_updatePosition.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_updatePosition, 1, 0, 1, 2)

        self.pushButton_moveX = QPushButton(self.frame)
        self.pushButton_moveX.setObjectName(u"pushButton_moveX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_moveX.sizePolicy().hasHeightForWidth())
        self.pushButton_moveX.setSizePolicy(sizePolicy1)
        self.pushButton_moveX.setMinimumSize(QSize(0, 25))
        self.pushButton_moveX.setMaximumSize(QSize(16777215, 40))
        self.pushButton_moveX.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveX, 2, 4, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_4.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.spinBox_y_pos = QDoubleSpinBox(self.frame)
        self.spinBox_y_pos.setObjectName(u"spinBox_y_pos")
        self.spinBox_y_pos.setMinimumSize(QSize(75, 25))
        self.spinBox_y_pos.setMaximumSize(QSize(200, 40))
        self.spinBox_y_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_y_pos.setReadOnly(True)
        self.spinBox_y_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_y_pos.setDecimals(3)
        self.spinBox_y_pos.setMinimum(-10.000000000000000)
        self.spinBox_y_pos.setMaximum(210.000000000000000)
        self.spinBox_y_pos.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.spinBox_y_pos, 3, 1, 1, 1)

        self.pushButton_moveY = QPushButton(self.frame)
        self.pushButton_moveY.setObjectName(u"pushButton_moveY")
        self.pushButton_moveY.setMinimumSize(QSize(0, 25))
        self.pushButton_moveY.setMaximumSize(QSize(16777215, 40))
        self.pushButton_moveY.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveY, 3, 4, 1, 1)

        self.spinBox_x_pos = QDoubleSpinBox(self.frame)
        self.spinBox_x_pos.setObjectName(u"spinBox_x_pos")
        self.spinBox_x_pos.setMinimumSize(QSize(75, 25))
        self.spinBox_x_pos.setMaximumSize(QSize(200, 40))
        self.spinBox_x_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_x_pos.setReadOnly(True)
        self.spinBox_x_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_x_pos.setDecimals(3)
        self.spinBox_x_pos.setMinimum(-10.000000000000000)
        self.spinBox_x_pos.setMaximum(210.000000000000000)
        self.spinBox_x_pos.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.spinBox_x_pos, 2, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_5.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 2)

        self.pushButton_moveZ = QPushButton(self.frame)
        self.pushButton_moveZ.setObjectName(u"pushButton_moveZ")
        self.pushButton_moveZ.setMinimumSize(QSize(0, 25))
        self.pushButton_moveZ.setMaximumSize(QSize(16777215, 40))
        self.pushButton_moveZ.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveZ, 4, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.pushButton_moveCenter = QPushButton(self.frame)
        self.pushButton_moveCenter.setObjectName(u"pushButton_moveCenter")
        self.pushButton_moveCenter.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveCenter, 5, 3, 1, 1)

        self.spinBox_z_pos = QDoubleSpinBox(self.frame)
        self.spinBox_z_pos.setObjectName(u"spinBox_z_pos")
        self.spinBox_z_pos.setMinimumSize(QSize(75, 25))
        self.spinBox_z_pos.setMaximumSize(QSize(200, 40))
        self.spinBox_z_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_z_pos.setReadOnly(True)
        self.spinBox_z_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_z_pos.setDecimals(3)
        self.spinBox_z_pos.setMinimum(-10.000000000000000)
        self.spinBox_z_pos.setMaximum(210.000000000000000)
        self.spinBox_z_pos.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.spinBox_z_pos, 4, 1, 1, 1)

        self.spinBox_y_setpos = QDoubleSpinBox(self.frame)
        self.spinBox_y_setpos.setObjectName(u"spinBox_y_setpos")
        self.spinBox_y_setpos.setMinimumSize(QSize(75, 25))
        self.spinBox_y_setpos.setMaximumSize(QSize(200, 40))
        self.spinBox_y_setpos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_y_setpos.setReadOnly(False)
        self.spinBox_y_setpos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_y_setpos.setDecimals(3)
        self.spinBox_y_setpos.setMinimum(-10.000000000000000)
        self.spinBox_y_setpos.setMaximum(210.000000000000000)
        self.spinBox_y_setpos.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.spinBox_y_setpos, 3, 3, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_moveAll = QPushButton(self.frame)
        self.pushButton_moveAll.setObjectName(u"pushButton_moveAll")
        self.pushButton_moveAll.setStyleSheet(u"font: 11pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.pushButton_moveAll)

        self.pushButton_setPos_getCurrent = QPushButton(self.frame)
        self.pushButton_setPos_getCurrent.setObjectName(u"pushButton_setPos_getCurrent")
        self.pushButton_setPos_getCurrent.setStyleSheet(u"font: 11pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.pushButton_setPos_getCurrent)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 3, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 1)

        self.spinBox_z_offset = QDoubleSpinBox(self.frame)
        self.spinBox_z_offset.setObjectName(u"spinBox_z_offset")
        self.spinBox_z_offset.setMinimumSize(QSize(50, 25))
        self.spinBox_z_offset.setMaximumSize(QSize(150, 40))
        self.spinBox_z_offset.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_z_offset.setReadOnly(False)
        self.spinBox_z_offset.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_z_offset.setDecimals(3)
        self.spinBox_z_offset.setMinimum(-10.000000000000000)
        self.spinBox_z_offset.setMaximum(210.000000000000000)
        self.spinBox_z_offset.setValue(130.000000000000000)

        self.gridLayout.addWidget(self.spinBox_z_offset, 6, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.mpl_widget = QWidget(self.centralwidget)
        self.mpl_widget.setObjectName(u"mpl_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mpl_widget.sizePolicy().hasHeightForWidth())
        self.mpl_widget.setSizePolicy(sizePolicy2)
        self.mpl_widget.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.mpl_widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Y (um)</span></p></body></html>", None))
        self.pushButton_moveCenter_Offset.setText(QCoreApplication.translate("MainWindow", u"Center + Z-Offset", None))
        self.pushButton_updatePosition.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_moveX.setText(QCoreApplication.translate("MainWindow", u"Move X", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Current</span><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Position</span></p></body></html>", None))
        self.pushButton_moveY.setText(QCoreApplication.translate("MainWindow", u"Move Y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Set Position</span></p></body></html>", None))
        self.pushButton_moveZ.setText(QCoreApplication.translate("MainWindow", u"Move Z", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">X (um)</span></p></body></html>", None))
        self.pushButton_moveCenter.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Z (um)</span></p></body></html>", None))
        self.pushButton_moveAll.setText(QCoreApplication.translate("MainWindow", u"Move All", None))
        self.pushButton_setPos_getCurrent.setText(QCoreApplication.translate("MainWindow", u"Use Current", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Z-Offset</span></p></body></html>", None))
    # retranslateUi

