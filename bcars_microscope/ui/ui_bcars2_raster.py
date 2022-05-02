# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_bcars2_raster.ui'
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
        MainWindow.resize(1511, 848)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 323, 263))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.comboBoxSlow = QComboBox(self.groupBox_2)
        self.comboBoxSlow.addItem("")
        self.comboBoxSlow.addItem("")
        self.comboBoxSlow.addItem("")
        self.comboBoxSlow.setObjectName(u"comboBoxSlow")

        self.verticalLayout_5.addWidget(self.comboBoxSlow)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.spinBox_slow_start = QDoubleSpinBox(self.groupBox_2)
        self.spinBox_slow_start.setObjectName(u"spinBox_slow_start")
        self.spinBox_slow_start.setMinimumSize(QSize(75, 25))
        self.spinBox_slow_start.setMaximumSize(QSize(200, 40))
        self.spinBox_slow_start.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_slow_start.setReadOnly(False)
        self.spinBox_slow_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_slow_start.setDecimals(3)
        self.spinBox_slow_start.setMinimum(-1.000000000000000)
        self.spinBox_slow_start.setMaximum(201.000000000000000)
        self.spinBox_slow_start.setValue(1.000000000000000)

        self.verticalLayout_5.addWidget(self.spinBox_slow_start)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.spinBox_slow_stop = QDoubleSpinBox(self.groupBox_2)
        self.spinBox_slow_stop.setObjectName(u"spinBox_slow_stop")
        self.spinBox_slow_stop.setMinimumSize(QSize(75, 25))
        self.spinBox_slow_stop.setMaximumSize(QSize(200, 40))
        self.spinBox_slow_stop.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_slow_stop.setReadOnly(False)
        self.spinBox_slow_stop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_slow_stop.setDecimals(3)
        self.spinBox_slow_stop.setMinimum(-1.000000000000000)
        self.spinBox_slow_stop.setMaximum(201.000000000000000)
        self.spinBox_slow_stop.setValue(199.000000000000000)

        self.verticalLayout_5.addWidget(self.spinBox_slow_stop)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.spinBox_slow_steps = QSpinBox(self.groupBox_2)
        self.spinBox_slow_steps.setObjectName(u"spinBox_slow_steps")
        self.spinBox_slow_steps.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_slow_steps.setMinimum(1)
        self.spinBox_slow_steps.setMaximum(5000)
        self.spinBox_slow_steps.setValue(50)

        self.verticalLayout_5.addWidget(self.spinBox_slow_steps)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.comboBoxFixed = QComboBox(self.groupBox_3)
        self.comboBoxFixed.addItem("")
        self.comboBoxFixed.addItem("")
        self.comboBoxFixed.addItem("")
        self.comboBoxFixed.setObjectName(u"comboBoxFixed")

        self.verticalLayout_3.addWidget(self.comboBoxFixed)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.spinBox_fixed_start = QDoubleSpinBox(self.groupBox_3)
        self.spinBox_fixed_start.setObjectName(u"spinBox_fixed_start")
        self.spinBox_fixed_start.setMinimumSize(QSize(75, 25))
        self.spinBox_fixed_start.setMaximumSize(QSize(200, 40))
        self.spinBox_fixed_start.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_fixed_start.setReadOnly(False)
        self.spinBox_fixed_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fixed_start.setDecimals(3)
        self.spinBox_fixed_start.setMinimum(-1.000000000000000)
        self.spinBox_fixed_start.setMaximum(201.000000000000000)
        self.spinBox_fixed_start.setValue(100.000000000000000)

        self.verticalLayout_3.addWidget(self.spinBox_fixed_start)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.spinBox_fixed_stop = QDoubleSpinBox(self.groupBox_3)
        self.spinBox_fixed_stop.setObjectName(u"spinBox_fixed_stop")
        self.spinBox_fixed_stop.setMinimumSize(QSize(75, 25))
        self.spinBox_fixed_stop.setMaximumSize(QSize(200, 40))
        self.spinBox_fixed_stop.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_fixed_stop.setReadOnly(False)
        self.spinBox_fixed_stop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fixed_stop.setDecimals(3)
        self.spinBox_fixed_stop.setMinimum(-1.000000000000000)
        self.spinBox_fixed_stop.setMaximum(201.000000000000000)
        self.spinBox_fixed_stop.setValue(100.000000000000000)

        self.verticalLayout_3.addWidget(self.spinBox_fixed_stop)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_3.addWidget(self.label_12)

        self.spinBox_fixed_steps = QSpinBox(self.groupBox_3)
        self.spinBox_fixed_steps.setObjectName(u"spinBox_fixed_steps")
        self.spinBox_fixed_steps.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fixed_steps.setMinimum(1)
        self.spinBox_fixed_steps.setMaximum(5000)
        self.spinBox_fixed_steps.setValue(1)

        self.verticalLayout_3.addWidget(self.spinBox_fixed_steps)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.comboBoxFast = QComboBox(self.groupBox)
        self.comboBoxFast.addItem("")
        self.comboBoxFast.addItem("")
        self.comboBoxFast.addItem("")
        self.comboBoxFast.setObjectName(u"comboBoxFast")

        self.verticalLayout.addWidget(self.comboBoxFast)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.spinBox_fast_start = QDoubleSpinBox(self.groupBox)
        self.spinBox_fast_start.setObjectName(u"spinBox_fast_start")
        self.spinBox_fast_start.setMinimumSize(QSize(75, 25))
        self.spinBox_fast_start.setMaximumSize(QSize(200, 40))
        self.spinBox_fast_start.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_fast_start.setReadOnly(False)
        self.spinBox_fast_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fast_start.setDecimals(3)
        self.spinBox_fast_start.setMinimum(-1.000000000000000)
        self.spinBox_fast_start.setMaximum(201.000000000000000)
        self.spinBox_fast_start.setValue(1.000000000000000)

        self.verticalLayout.addWidget(self.spinBox_fast_start)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.spinBox_fast_stop = QDoubleSpinBox(self.groupBox)
        self.spinBox_fast_stop.setObjectName(u"spinBox_fast_stop")
        self.spinBox_fast_stop.setMinimumSize(QSize(75, 25))
        self.spinBox_fast_stop.setMaximumSize(QSize(200, 40))
        self.spinBox_fast_stop.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_fast_stop.setReadOnly(False)
        self.spinBox_fast_stop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fast_stop.setDecimals(3)
        self.spinBox_fast_stop.setMinimum(-1.000000000000000)
        self.spinBox_fast_stop.setMaximum(201.000000000000000)
        self.spinBox_fast_stop.setValue(199.000000000000000)

        self.verticalLayout.addWidget(self.spinBox_fast_stop)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.spinBox_fast_steps = QSpinBox(self.groupBox)
        self.spinBox_fast_steps.setObjectName(u"spinBox_fast_steps")
        self.spinBox_fast_steps.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fast_steps.setMinimum(1)
        self.spinBox_fast_steps.setMaximum(5000)
        self.spinBox_fast_steps.setValue(50)

        self.verticalLayout.addWidget(self.spinBox_fast_steps)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 500, 321, 72))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonStartAcq.sizePolicy().hasHeightForWidth())
        self.pushButtonStartAcq.setSizePolicy(sizePolicy1)
        self.pushButtonStartAcq.setMinimumSize(QSize(50, 50))
        self.pushButtonStartAcq.setMaximumSize(QSize(75, 50))
        self.pushButtonStartAcq.setBaseSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(10)
        self.pushButtonStartAcq.setFont(font1)
        self.pushButtonStartAcq.setStyleSheet(u"color: white;\n"
"font: 87 14pt \"Arial Black\";")

        self.horizontalLayout_2.addWidget(self.pushButtonStartAcq)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButtonStopAcq = QPushButton(self.frame_3)
        self.pushButtonStopAcq.setObjectName(u"pushButtonStopAcq")
        sizePolicy1.setHeightForWidth(self.pushButtonStopAcq.sizePolicy().hasHeightForWidth())
        self.pushButtonStopAcq.setSizePolicy(sizePolicy1)
        self.pushButtonStopAcq.setMinimumSize(QSize(50, 50))
        self.pushButtonStopAcq.setMaximumSize(QSize(75, 50))
        self.pushButtonStopAcq.setBaseSize(QSize(50, 50))
        self.pushButtonStopAcq.setFont(font1)
        self.pushButtonStopAcq.setStyleSheet(u"color:red;\n"
"font: 87 14pt \"Arial Black\";")
        self.pushButtonStopAcq.setCheckable(True)
        self.pushButtonStopAcq.setChecked(False)

        self.horizontalLayout_2.addWidget(self.pushButtonStopAcq)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 280, 342, 185))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.spinBox_post_image_z_pos = QDoubleSpinBox(self.layoutWidget)
        self.spinBox_post_image_z_pos.setObjectName(u"spinBox_post_image_z_pos")
        self.spinBox_post_image_z_pos.setMinimumSize(QSize(75, 25))
        self.spinBox_post_image_z_pos.setMaximumSize(QSize(75, 40))
        self.spinBox_post_image_z_pos.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_post_image_z_pos.setReadOnly(False)
        self.spinBox_post_image_z_pos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_post_image_z_pos.setDecimals(3)
        self.spinBox_post_image_z_pos.setMinimum(-1.000000000000000)
        self.spinBox_post_image_z_pos.setMaximum(201.000000000000000)
        self.spinBox_post_image_z_pos.setValue(130.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_post_image_z_pos)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.spinBoxDelayImaging = QDoubleSpinBox(self.layoutWidget)
        self.spinBoxDelayImaging.setObjectName(u"spinBoxDelayImaging")
        self.spinBoxDelayImaging.setMinimumSize(QSize(75, 25))
        self.spinBoxDelayImaging.setMaximumSize(QSize(75, 40))
        self.spinBoxDelayImaging.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBoxDelayImaging.setReadOnly(False)
        self.spinBoxDelayImaging.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxDelayImaging.setDecimals(3)
        self.spinBoxDelayImaging.setMinimum(-10000.000000000000000)
        self.spinBoxDelayImaging.setMaximum(10000.000000000000000)
        self.spinBoxDelayImaging.setValue(-0.290000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBoxDelayImaging)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.comboBoxRecNRB = QComboBox(self.layoutWidget)
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.setObjectName(u"comboBoxRecNRB")
        self.comboBoxRecNRB.setMaximumSize(QSize(69, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxRecNRB)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_17)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxCollectDark = QCheckBox(self.layoutWidget)
        self.checkBoxCollectDark.setObjectName(u"checkBoxCollectDark")
        self.checkBoxCollectDark.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.checkBoxCollectDark.sizePolicy().hasHeightForWidth())
        self.checkBoxCollectDark.setSizePolicy(sizePolicy1)
        self.checkBoxCollectDark.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")

        self.horizontalLayout.addWidget(self.checkBoxCollectDark)

        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.label_21)

        self.spinBoxDelayDark = QDoubleSpinBox(self.layoutWidget)
        self.spinBoxDelayDark.setObjectName(u"spinBoxDelayDark")
        self.spinBoxDelayDark.setMinimumSize(QSize(75, 25))
        self.spinBoxDelayDark.setMaximumSize(QSize(75, 40))
        self.spinBoxDelayDark.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBoxDelayDark.setReadOnly(False)
        self.spinBoxDelayDark.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxDelayDark.setDecimals(3)
        self.spinBoxDelayDark.setMinimum(-10000.000000000000000)
        self.spinBoxDelayDark.setMaximum(10000.000000000000000)
        self.spinBoxDelayDark.setValue(0.300000000000000)

        self.horizontalLayout.addWidget(self.spinBoxDelayDark)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBoxCollectNRB = QCheckBox(self.layoutWidget)
        self.checkBoxCollectNRB.setObjectName(u"checkBoxCollectNRB")
        self.checkBoxCollectNRB.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.checkBoxCollectNRB.sizePolicy().hasHeightForWidth())
        self.checkBoxCollectNRB.setSizePolicy(sizePolicy1)
        self.checkBoxCollectNRB.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")

        self.horizontalLayout_3.addWidget(self.checkBoxCollectNRB)

        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setTextFormat(Qt.PlainText)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.spinBoxDelayNRB = QDoubleSpinBox(self.layoutWidget)
        self.spinBoxDelayNRB.setObjectName(u"spinBoxDelayNRB")
        self.spinBoxDelayNRB.setMinimumSize(QSize(75, 25))
        self.spinBoxDelayNRB.setMaximumSize(QSize(75, 40))
        self.spinBoxDelayNRB.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBoxDelayNRB.setReadOnly(False)
        self.spinBoxDelayNRB.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxDelayNRB.setDecimals(3)
        self.spinBoxDelayNRB.setMinimum(-10000.000000000000000)
        self.spinBoxDelayNRB.setMaximum(10000.000000000000000)
        self.spinBoxDelayNRB.setValue(-0.290000000000000)

        self.horizontalLayout_3.addWidget(self.spinBoxDelayNRB)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_20)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxCollectNRB_Early = QCheckBox(self.layoutWidget)
        self.checkBoxCollectNRB_Early.setObjectName(u"checkBoxCollectNRB_Early")
        self.checkBoxCollectNRB_Early.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.checkBoxCollectNRB_Early.sizePolicy().hasHeightForWidth())
        self.checkBoxCollectNRB_Early.setSizePolicy(sizePolicy1)
        self.checkBoxCollectNRB_Early.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")

        self.horizontalLayout_4.addWidget(self.checkBoxCollectNRB_Early)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setTextFormat(Qt.PlainText)

        self.horizontalLayout_4.addWidget(self.label_23)

        self.spinBoxDelayNRB_Early = QDoubleSpinBox(self.layoutWidget)
        self.spinBoxDelayNRB_Early.setObjectName(u"spinBoxDelayNRB_Early")
        self.spinBoxDelayNRB_Early.setMinimumSize(QSize(75, 25))
        self.spinBoxDelayNRB_Early.setMaximumSize(QSize(75, 40))
        self.spinBoxDelayNRB_Early.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBoxDelayNRB_Early.setReadOnly(False)
        self.spinBoxDelayNRB_Early.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxDelayNRB_Early.setDecimals(3)
        self.spinBoxDelayNRB_Early.setMinimum(-10000.000000000000000)
        self.spinBoxDelayNRB_Early.setMaximum(10000.000000000000000)
        self.spinBoxDelayNRB_Early.setValue(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.spinBoxDelayNRB_Early)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(350, 11, 1063, 760))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(739, 0))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mpl_widget_left = QWidget(self.frame_2)
        self.mpl_widget_left.setObjectName(u"mpl_widget_left")
        sizePolicy2.setHeightForWidth(self.mpl_widget_left.sizePolicy().hasHeightForWidth())
        self.mpl_widget_left.setSizePolicy(sizePolicy2)
        self.mpl_widget_left.setMinimumSize(QSize(518, 451))
        self.mpl_widget_left.setAutoFillBackground(False)
        self.mpl_widget_left.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.horizontalLayout_5.addWidget(self.mpl_widget_left)

        self.mpl_widget_right = QWidget(self.frame_2)
        self.mpl_widget_right.setObjectName(u"mpl_widget_right")
        sizePolicy2.setHeightForWidth(self.mpl_widget_right.sizePolicy().hasHeightForWidth())
        self.mpl_widget_right.setSizePolicy(sizePolicy2)
        self.mpl_widget_right.setMinimumSize(QSize(517, 451))
        self.mpl_widget_right.setAutoFillBackground(False)
        self.mpl_widget_right.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.horizontalLayout_5.addWidget(self.mpl_widget_right)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.mpl_widget_spectra = QWidget(self.widget)
        self.mpl_widget_spectra.setObjectName(u"mpl_widget_spectra")
        sizePolicy2.setHeightForWidth(self.mpl_widget_spectra.sizePolicy().hasHeightForWidth())
        self.mpl_widget_spectra.setSizePolicy(sizePolicy2)
        self.mpl_widget_spectra.setMinimumSize(QSize(1061, 281))
        self.mpl_widget_spectra.setAutoFillBackground(False)
        self.mpl_widget_spectra.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.verticalLayout_8.addWidget(self.mpl_widget_spectra)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1511, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBoxSlow.setCurrentIndex(1)
        self.comboBoxFixed.setCurrentIndex(2)
        self.comboBoxRecNRB.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Slow Axis", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBoxSlow.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBoxSlow.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBoxSlow.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Fixed Axis", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBoxFixed.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBoxFixed.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBoxFixed.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Fast Axis", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBoxFast.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBoxFast.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBoxFast.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.pushButtonStartAcq.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButtonStopAcq.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Post-Image Z  (um)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Imaging Delay (mm)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Collect Before/After", None))
        self.comboBoxRecNRB.setItemText(0, QCoreApplication.translate("MainWindow", u"Before", None))
        self.comboBoxRecNRB.setItemText(1, QCoreApplication.translate("MainWindow", u"After", None))
        self.comboBoxRecNRB.setItemText(2, QCoreApplication.translate("MainWindow", u"Both", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Collect Dark", None))
        self.checkBoxCollectDark.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Delay (mm)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Collect NRB/Ref", None))
        self.checkBoxCollectNRB.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Delay (mm)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Early-Time NRB/Ref", None))
        self.checkBoxCollectNRB_Early.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Delay (mm)", None))
    # retranslateUi

