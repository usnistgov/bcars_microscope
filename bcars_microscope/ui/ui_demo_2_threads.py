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
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_pos = QVBoxLayout()
        self.verticalLayout_pos.setObjectName(u"verticalLayout_pos")
        self.pushButton_updatePosition = QPushButton(self.centralwidget)
        self.pushButton_updatePosition.setObjectName(u"pushButton_updatePosition")

        self.verticalLayout_pos.addWidget(self.pushButton_updatePosition)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.spinBox_x_pos = QDoubleSpinBox(self.frame)
        self.spinBox_x_pos.setObjectName(u"spinBox_x_pos")
        self.spinBox_x_pos.setReadOnly(True)
        self.spinBox_x_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_x_pos.setDecimals(3)
        self.spinBox_x_pos.setMinimum(-10.000000000000000)
        self.spinBox_x_pos.setMaximum(210.000000000000000)

        self.verticalLayout.addWidget(self.spinBox_x_pos)


        self.verticalLayout_pos.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.spinBox_y_pos = QDoubleSpinBox(self.frame_2)
        self.spinBox_y_pos.setObjectName(u"spinBox_y_pos")
        self.spinBox_y_pos.setReadOnly(True)
        self.spinBox_y_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_y_pos.setDecimals(3)
        self.spinBox_y_pos.setMinimum(-10.000000000000000)
        self.spinBox_y_pos.setMaximum(210.000000000000000)

        self.verticalLayout_2.addWidget(self.spinBox_y_pos)


        self.verticalLayout_pos.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.frame_3.setLineWidth(2)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.spinBox_z_pos = QDoubleSpinBox(self.frame_3)
        self.spinBox_z_pos.setObjectName(u"spinBox_z_pos")
        self.spinBox_z_pos.setReadOnly(True)
        self.spinBox_z_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_z_pos.setDecimals(3)
        self.spinBox_z_pos.setMinimum(-10.000000000000000)
        self.spinBox_z_pos.setMaximum(210.000000000000000)

        self.verticalLayout_3.addWidget(self.spinBox_z_pos)


        self.verticalLayout_pos.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_pos.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_pos)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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
        self.pushButton_updatePosition.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Z", None))
    # retranslateUi

