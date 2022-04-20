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
        MainWindow.resize(996, 763)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_pos = QVBoxLayout()
        self.verticalLayout_pos.setObjectName(u"verticalLayout_pos")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_4.setTextFormat(Qt.RichText)

        self.verticalLayout_pos.addWidget(self.label_4)

        self.pushButton_updatePosition = QPushButton(self.centralwidget)
        self.pushButton_updatePosition.setObjectName(u"pushButton_updatePosition")
        self.pushButton_updatePosition.setStyleSheet(u"font: 11pt \"Arial\";")

        self.verticalLayout_pos.addWidget(self.pushButton_updatePosition)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font: 11pt \"Arial\";")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 11pt \"Arial\";")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinBox_x_pos = QDoubleSpinBox(self.frame)
        self.spinBox_x_pos.setObjectName(u"spinBox_x_pos")
        self.spinBox_x_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_x_pos.setReadOnly(True)
        self.spinBox_x_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_x_pos.setDecimals(3)
        self.spinBox_x_pos.setMinimum(-10.000000000000000)
        self.spinBox_x_pos.setMaximum(210.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBox_x_pos)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"Arial\";")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinBox_y_pos = QDoubleSpinBox(self.frame)
        self.spinBox_y_pos.setObjectName(u"spinBox_y_pos")
        self.spinBox_y_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_y_pos.setReadOnly(True)
        self.spinBox_y_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_y_pos.setDecimals(3)
        self.spinBox_y_pos.setMinimum(-10.000000000000000)
        self.spinBox_y_pos.setMaximum(210.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.spinBox_y_pos)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 11pt \"Arial\";")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.spinBox_z_pos = QDoubleSpinBox(self.frame)
        self.spinBox_z_pos.setObjectName(u"spinBox_z_pos")
        self.spinBox_z_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_z_pos.setReadOnly(True)
        self.spinBox_z_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_z_pos.setDecimals(3)
        self.spinBox_z_pos.setMinimum(-10.000000000000000)
        self.spinBox_z_pos.setMaximum(210.000000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spinBox_z_pos)


        self.verticalLayout.addLayout(self.formLayout_2)


        self.verticalLayout_pos.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_pos.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_pos)

        self.verticalLayout_pos_2 = QVBoxLayout()
        self.verticalLayout_pos_2.setObjectName(u"verticalLayout_pos_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_5.setTextFormat(Qt.RichText)

        self.verticalLayout_pos_2.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_moveAll = QPushButton(self.centralwidget)
        self.pushButton_moveAll.setObjectName(u"pushButton_moveAll")
        self.pushButton_moveAll.setStyleSheet(u"font: 11pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.pushButton_moveAll)

        self.pushButton_setPos_getCurrent = QPushButton(self.centralwidget)
        self.pushButton_setPos_getCurrent.setObjectName(u"pushButton_setPos_getCurrent")
        self.pushButton_setPos_getCurrent.setStyleSheet(u"font: 11pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.pushButton_setPos_getCurrent)


        self.verticalLayout_pos_2.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font: 11pt \"Arial\";")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.spinBox_y_setpos = QDoubleSpinBox(self.frame_2)
        self.spinBox_y_setpos.setObjectName(u"spinBox_y_setpos")
        self.spinBox_y_setpos.setMaximumSize(QSize(50, 16777215))
        self.spinBox_y_setpos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_y_setpos.setReadOnly(True)
        self.spinBox_y_setpos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_y_setpos.setDecimals(3)
        self.spinBox_y_setpos.setMinimum(-10.000000000000000)
        self.spinBox_y_setpos.setMaximum(210.000000000000000)

        self.gridLayout.addWidget(self.spinBox_y_setpos, 1, 1, 1, 1)

        self.spinBox_x_setpos = QDoubleSpinBox(self.frame_2)
        self.spinBox_x_setpos.setObjectName(u"spinBox_x_setpos")
        self.spinBox_x_setpos.setMaximumSize(QSize(50, 16777215))
        self.spinBox_x_setpos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_x_setpos.setReadOnly(True)
        self.spinBox_x_setpos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_x_setpos.setDecimals(3)
        self.spinBox_x_setpos.setMinimum(-10.000000000000000)
        self.spinBox_x_setpos.setMaximum(210.000000000000000)

        self.gridLayout.addWidget(self.spinBox_x_setpos, 0, 1, 1, 1)

        self.spinBox_z_setpos = QDoubleSpinBox(self.frame_2)
        self.spinBox_z_setpos.setObjectName(u"spinBox_z_setpos")
        self.spinBox_z_setpos.setMaximumSize(QSize(50, 16777215))
        self.spinBox_z_setpos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_z_setpos.setReadOnly(True)
        self.spinBox_z_setpos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_z_setpos.setDecimals(3)
        self.spinBox_z_setpos.setMinimum(-10.000000000000000)
        self.spinBox_z_setpos.setMaximum(210.000000000000000)

        self.gridLayout.addWidget(self.spinBox_z_setpos, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.pushButton_moveX = QPushButton(self.frame_2)
        self.pushButton_moveX.setObjectName(u"pushButton_moveX")
        self.pushButton_moveX.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveX, 0, 2, 1, 1)

        self.pushButton_moveY = QPushButton(self.frame_2)
        self.pushButton_moveY.setObjectName(u"pushButton_moveY")
        self.pushButton_moveY.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveY, 1, 2, 1, 1)

        self.pushButton_moveZ = QPushButton(self.frame_2)
        self.pushButton_moveZ.setObjectName(u"pushButton_moveZ")
        self.pushButton_moveZ.setStyleSheet(u"font: 11pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_moveZ, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_pos_2.addWidget(self.frame_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_pos_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_pos_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 996, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Current Position</span></p></body></html>", None))
        self.pushButton_updatePosition.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Set Position</span></p></body></html>", None))
        self.pushButton_moveAll.setText(QCoreApplication.translate("MainWindow", u"Move All", None))
        self.pushButton_setPos_getCurrent.setText(QCoreApplication.translate("MainWindow", u"Load Current", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_moveX.setText(QCoreApplication.translate("MainWindow", u"Move X", None))
        self.pushButton_moveY.setText(QCoreApplication.translate("MainWindow", u"Move Y", None))
        self.pushButton_moveZ.setText(QCoreApplication.translate("MainWindow", u"Move Z", None))
    # retranslateUi

