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
        MainWindow.resize(1511, 950)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tabWidget_3 = QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox = QGroupBox(self.tab_9)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
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
        self.spinBox_fast_steps.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_fast_steps.setMinimum(1)
        self.spinBox_fast_steps.setMaximum(5000)
        self.spinBox_fast_steps.setValue(50)

        self.verticalLayout.addWidget(self.spinBox_fast_steps)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.spinBox_fast_stepsize = QDoubleSpinBox(self.groupBox)
        self.spinBox_fast_stepsize.setObjectName(u"spinBox_fast_stepsize")
        self.spinBox_fast_stepsize.setEnabled(False)
        self.spinBox_fast_stepsize.setMinimumSize(QSize(75, 25))
        self.spinBox_fast_stepsize.setMaximumSize(QSize(200, 40))
        self.spinBox_fast_stepsize.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_fast_stepsize.setReadOnly(True)
        self.spinBox_fast_stepsize.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fast_stepsize.setDecimals(3)
        self.spinBox_fast_stepsize.setMinimum(-200.000000000000000)
        self.spinBox_fast_stepsize.setMaximum(200.000000000000000)
        self.spinBox_fast_stepsize.setValue(1.000000000000000)

        self.verticalLayout.addWidget(self.spinBox_fast_stepsize)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_9.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_9)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
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
        self.spinBox_slow_steps.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_slow_steps.setMinimum(1)
        self.spinBox_slow_steps.setMaximum(5000)
        self.spinBox_slow_steps.setValue(50)

        self.verticalLayout_5.addWidget(self.spinBox_slow_steps)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_5.addWidget(self.label_24)

        self.spinBox_slow_stepsize = QDoubleSpinBox(self.groupBox_2)
        self.spinBox_slow_stepsize.setObjectName(u"spinBox_slow_stepsize")
        self.spinBox_slow_stepsize.setEnabled(False)
        self.spinBox_slow_stepsize.setMinimumSize(QSize(75, 25))
        self.spinBox_slow_stepsize.setMaximumSize(QSize(200, 40))
        self.spinBox_slow_stepsize.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_slow_stepsize.setReadOnly(True)
        self.spinBox_slow_stepsize.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_slow_stepsize.setDecimals(3)
        self.spinBox_slow_stepsize.setMinimum(-200.000000000000000)
        self.spinBox_slow_stepsize.setMaximum(200.000000000000000)
        self.spinBox_slow_stepsize.setValue(1.000000000000000)

        self.verticalLayout_5.addWidget(self.spinBox_slow_stepsize)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
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
        self.spinBox_fixed_steps.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_fixed_steps.setMinimum(1)
        self.spinBox_fixed_steps.setMaximum(5000)
        self.spinBox_fixed_steps.setValue(1)

        self.verticalLayout_3.addWidget(self.spinBox_fixed_steps)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_3.addWidget(self.label_25)

        self.spinBox_fixed_stepsize = QDoubleSpinBox(self.groupBox_3)
        self.spinBox_fixed_stepsize.setObjectName(u"spinBox_fixed_stepsize")
        self.spinBox_fixed_stepsize.setEnabled(False)
        self.spinBox_fixed_stepsize.setMinimumSize(QSize(75, 25))
        self.spinBox_fixed_stepsize.setMaximumSize(QSize(200, 40))
        self.spinBox_fixed_stepsize.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_fixed_stepsize.setReadOnly(True)
        self.spinBox_fixed_stepsize.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_fixed_stepsize.setDecimals(3)
        self.spinBox_fixed_stepsize.setMinimum(-200.000000000000000)
        self.spinBox_fixed_stepsize.setMaximum(200.000000000000000)
        self.spinBox_fixed_stepsize.setValue(1.000000000000000)

        self.verticalLayout_3.addWidget(self.spinBox_fixed_stepsize)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_9.addWidget(self.groupBox_3)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout = QGridLayout(self.tab_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonMacroXZ = QPushButton(self.tab_10)
        self.pushButtonMacroXZ.setObjectName(u"pushButtonMacroXZ")

        self.gridLayout.addWidget(self.pushButtonMacroXZ, 0, 1, 1, 1)

        self.pushButtonMacroXY = QPushButton(self.tab_10)
        self.pushButtonMacroXY.setObjectName(u"pushButtonMacroXY")

        self.gridLayout.addWidget(self.pushButtonMacroXY, 0, 0, 1, 1)

        self.pushButtonMacroHighRes = QPushButton(self.tab_10)
        self.pushButtonMacroHighRes.setObjectName(u"pushButtonMacroHighRes")

        self.gridLayout.addWidget(self.pushButtonMacroHighRes, 1, 1, 1, 1)

        self.pushButtonMacroLowRes = QPushButton(self.tab_10)
        self.pushButtonMacroLowRes.setObjectName(u"pushButtonMacroLowRes")

        self.gridLayout.addWidget(self.pushButtonMacroLowRes, 1, 0, 1, 1)

        self.pushButtonMacroXYRange = QPushButton(self.tab_10)
        self.pushButtonMacroXYRange.setObjectName(u"pushButtonMacroXYRange")

        self.gridLayout.addWidget(self.pushButtonMacroXYRange, 3, 0, 1, 1)

        self.pushButtonMacroXZRange = QPushButton(self.tab_10)
        self.pushButtonMacroXZRange.setObjectName(u"pushButtonMacroXZRange")

        self.gridLayout.addWidget(self.pushButtonMacroXZRange, 3, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab_10, "")

        self.verticalLayout_12.addWidget(self.tabWidget_3)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.formLayout = QFormLayout(self.tab_7)
        self.formLayout.setObjectName(u"formLayout")
        self.label_14 = QLabel(self.tab_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.spinBox_post_image_z_pos = QDoubleSpinBox(self.tab_7)
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

        self.label_16 = QLabel(self.tab_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.spinBoxDelayImaging = QDoubleSpinBox(self.tab_7)
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

        self.label_19 = QLabel(self.tab_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.comboBoxRecNRB = QComboBox(self.tab_7)
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.addItem("")
        self.comboBoxRecNRB.setObjectName(u"comboBoxRecNRB")
        self.comboBoxRecNRB.setMaximumSize(QSize(69, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxRecNRB)

        self.label_17 = QLabel(self.tab_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_17)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxCollectDark = QCheckBox(self.tab_7)
        self.checkBoxCollectDark.setObjectName(u"checkBoxCollectDark")
        self.checkBoxCollectDark.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxCollectDark.sizePolicy().hasHeightForWidth())
        self.checkBoxCollectDark.setSizePolicy(sizePolicy)
        self.checkBoxCollectDark.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")

        self.horizontalLayout.addWidget(self.checkBoxCollectDark)

        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.label_21)

        self.spinBoxDelayDark = QDoubleSpinBox(self.tab_7)
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

        self.label_18 = QLabel(self.tab_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBoxCollectNRB = QCheckBox(self.tab_7)
        self.checkBoxCollectNRB.setObjectName(u"checkBoxCollectNRB")
        self.checkBoxCollectNRB.setEnabled(True)
        sizePolicy.setHeightForWidth(self.checkBoxCollectNRB.sizePolicy().hasHeightForWidth())
        self.checkBoxCollectNRB.setSizePolicy(sizePolicy)
        self.checkBoxCollectNRB.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")

        self.horizontalLayout_3.addWidget(self.checkBoxCollectNRB)

        self.label_22 = QLabel(self.tab_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setTextFormat(Qt.PlainText)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.spinBoxDelayNRB = QDoubleSpinBox(self.tab_7)
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

        self.label_20 = QLabel(self.tab_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_20)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxCollectNRB_Early = QCheckBox(self.tab_7)
        self.checkBoxCollectNRB_Early.setObjectName(u"checkBoxCollectNRB_Early")
        self.checkBoxCollectNRB_Early.setEnabled(True)
        sizePolicy.setHeightForWidth(self.checkBoxCollectNRB_Early.sizePolicy().hasHeightForWidth())
        self.checkBoxCollectNRB_Early.setSizePolicy(sizePolicy)
        self.checkBoxCollectNRB_Early.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")

        self.horizontalLayout_4.addWidget(self.checkBoxCollectNRB_Early)

        self.label_23 = QLabel(self.tab_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setTextFormat(Qt.PlainText)

        self.horizontalLayout_4.addWidget(self.label_23)

        self.spinBoxDelayNRB_Early = QDoubleSpinBox(self.tab_7)
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

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_4 = QGroupBox(self.tab_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_14.addWidget(self.label_31)

        self.comboBox_nrb_fast_axis = QComboBox(self.groupBox_4)
        self.comboBox_nrb_fast_axis.addItem("")
        self.comboBox_nrb_fast_axis.addItem("")
        self.comboBox_nrb_fast_axis.addItem("")
        self.comboBox_nrb_fast_axis.setObjectName(u"comboBox_nrb_fast_axis")
        self.comboBox_nrb_fast_axis.setEnabled(False)

        self.verticalLayout_14.addWidget(self.comboBox_nrb_fast_axis)

        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_14.addWidget(self.label_32)

        self.spinBox_nrb_fast_start = QDoubleSpinBox(self.groupBox_4)
        self.spinBox_nrb_fast_start.setObjectName(u"spinBox_nrb_fast_start")
        self.spinBox_nrb_fast_start.setMinimumSize(QSize(75, 25))
        self.spinBox_nrb_fast_start.setMaximumSize(QSize(200, 40))
        self.spinBox_nrb_fast_start.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_nrb_fast_start.setReadOnly(False)
        self.spinBox_nrb_fast_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_fast_start.setDecimals(3)
        self.spinBox_nrb_fast_start.setMinimum(-1.000000000000000)
        self.spinBox_nrb_fast_start.setMaximum(201.000000000000000)
        self.spinBox_nrb_fast_start.setValue(90.000000000000000)

        self.verticalLayout_14.addWidget(self.spinBox_nrb_fast_start)

        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_14.addWidget(self.label_33)

        self.spinBox_nrb_fast_stop = QDoubleSpinBox(self.groupBox_4)
        self.spinBox_nrb_fast_stop.setObjectName(u"spinBox_nrb_fast_stop")
        self.spinBox_nrb_fast_stop.setMinimumSize(QSize(75, 25))
        self.spinBox_nrb_fast_stop.setMaximumSize(QSize(200, 40))
        self.spinBox_nrb_fast_stop.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_nrb_fast_stop.setReadOnly(False)
        self.spinBox_nrb_fast_stop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_fast_stop.setDecimals(3)
        self.spinBox_nrb_fast_stop.setMinimum(-1.000000000000000)
        self.spinBox_nrb_fast_stop.setMaximum(201.000000000000000)
        self.spinBox_nrb_fast_stop.setValue(110.000000000000000)

        self.verticalLayout_14.addWidget(self.spinBox_nrb_fast_stop)

        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_14.addWidget(self.label_34)

        self.spinBox_nrb_fast_steps = QSpinBox(self.groupBox_4)
        self.spinBox_nrb_fast_steps.setObjectName(u"spinBox_nrb_fast_steps")
        self.spinBox_nrb_fast_steps.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_fast_steps.setMinimum(1)
        self.spinBox_nrb_fast_steps.setMaximum(5000)
        self.spinBox_nrb_fast_steps.setValue(120)

        self.verticalLayout_14.addWidget(self.spinBox_nrb_fast_steps)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)


        self.horizontalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_36 = QLabel(self.groupBox_5)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_16.addWidget(self.label_36)

        self.comboBox_nrb_slow_axis = QComboBox(self.groupBox_5)
        self.comboBox_nrb_slow_axis.addItem("")
        self.comboBox_nrb_slow_axis.addItem("")
        self.comboBox_nrb_slow_axis.addItem("")
        self.comboBox_nrb_slow_axis.setObjectName(u"comboBox_nrb_slow_axis")
        self.comboBox_nrb_slow_axis.setEnabled(False)

        self.verticalLayout_16.addWidget(self.comboBox_nrb_slow_axis)

        self.label_37 = QLabel(self.groupBox_5)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_16.addWidget(self.label_37)

        self.spinBox_nrb_slow_start = QDoubleSpinBox(self.groupBox_5)
        self.spinBox_nrb_slow_start.setObjectName(u"spinBox_nrb_slow_start")
        self.spinBox_nrb_slow_start.setMinimumSize(QSize(75, 25))
        self.spinBox_nrb_slow_start.setMaximumSize(QSize(200, 40))
        self.spinBox_nrb_slow_start.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_nrb_slow_start.setReadOnly(False)
        self.spinBox_nrb_slow_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_slow_start.setDecimals(3)
        self.spinBox_nrb_slow_start.setMinimum(-1.000000000000000)
        self.spinBox_nrb_slow_start.setMaximum(201.000000000000000)
        self.spinBox_nrb_slow_start.setValue(90.000000000000000)

        self.verticalLayout_16.addWidget(self.spinBox_nrb_slow_start)

        self.label_38 = QLabel(self.groupBox_5)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_16.addWidget(self.label_38)

        self.spinBox_nrb_slow_stop = QDoubleSpinBox(self.groupBox_5)
        self.spinBox_nrb_slow_stop.setObjectName(u"spinBox_nrb_slow_stop")
        self.spinBox_nrb_slow_stop.setMinimumSize(QSize(75, 25))
        self.spinBox_nrb_slow_stop.setMaximumSize(QSize(200, 40))
        self.spinBox_nrb_slow_stop.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_nrb_slow_stop.setReadOnly(False)
        self.spinBox_nrb_slow_stop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_slow_stop.setDecimals(3)
        self.spinBox_nrb_slow_stop.setMinimum(-1.000000000000000)
        self.spinBox_nrb_slow_stop.setMaximum(201.000000000000000)
        self.spinBox_nrb_slow_stop.setValue(110.000000000000000)

        self.verticalLayout_16.addWidget(self.spinBox_nrb_slow_stop)

        self.label_39 = QLabel(self.groupBox_5)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_16.addWidget(self.label_39)

        self.spinBox_nrb_slow_steps = QSpinBox(self.groupBox_5)
        self.spinBox_nrb_slow_steps.setObjectName(u"spinBox_nrb_slow_steps")
        self.spinBox_nrb_slow_steps.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_slow_steps.setMinimum(1)
        self.spinBox_nrb_slow_steps.setMaximum(5000)
        self.spinBox_nrb_slow_steps.setValue(5)

        self.verticalLayout_16.addWidget(self.spinBox_nrb_slow_steps)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.horizontalLayout_8.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_18.addWidget(self.label_41)

        self.comboBox_nrb_fixed_axis = QComboBox(self.groupBox_6)
        self.comboBox_nrb_fixed_axis.addItem("")
        self.comboBox_nrb_fixed_axis.addItem("")
        self.comboBox_nrb_fixed_axis.addItem("")
        self.comboBox_nrb_fixed_axis.setObjectName(u"comboBox_nrb_fixed_axis")
        self.comboBox_nrb_fixed_axis.setEnabled(False)

        self.verticalLayout_18.addWidget(self.comboBox_nrb_fixed_axis)

        self.label_42 = QLabel(self.groupBox_6)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_18.addWidget(self.label_42)

        self.spinBox_nrb_fixed_start = QDoubleSpinBox(self.groupBox_6)
        self.spinBox_nrb_fixed_start.setObjectName(u"spinBox_nrb_fixed_start")
        self.spinBox_nrb_fixed_start.setMinimumSize(QSize(75, 25))
        self.spinBox_nrb_fixed_start.setMaximumSize(QSize(200, 40))
        self.spinBox_nrb_fixed_start.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_nrb_fixed_start.setReadOnly(False)
        self.spinBox_nrb_fixed_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nrb_fixed_start.setDecimals(3)
        self.spinBox_nrb_fixed_start.setMinimum(-1.000000000000000)
        self.spinBox_nrb_fixed_start.setMaximum(201.000000000000000)
        self.spinBox_nrb_fixed_start.setValue(100.000000000000000)

        self.verticalLayout_18.addWidget(self.spinBox_nrb_fixed_start)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.horizontalLayout_8.addWidget(self.groupBox_6)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.verticalLayout_12.addWidget(self.tabWidget_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(1000, 70))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButtonStartAcq = QPushButton(self.frame_3)
        self.pushButtonStartAcq.setObjectName(u"pushButtonStartAcq")
        sizePolicy.setHeightForWidth(self.pushButtonStartAcq.sizePolicy().hasHeightForWidth())
        self.pushButtonStartAcq.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.pushButtonStopAcq.sizePolicy().hasHeightForWidth())
        self.pushButtonStopAcq.setSizePolicy(sizePolicy)
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


        self.verticalLayout_12.addWidget(self.frame_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_11 = QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(60, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_30.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_30, 0, Qt.AlignLeft)

        self.checkBoxSave = QCheckBox(self.tab_5)
        self.checkBoxSave.setObjectName(u"checkBoxSave")
        self.checkBoxSave.setEnabled(True)
        sizePolicy.setHeightForWidth(self.checkBoxSave.sizePolicy().hasHeightForWidth())
        self.checkBoxSave.setSizePolicy(sizePolicy)
        self.checkBoxSave.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }\n"
"QCheckBox::indicator:disabled { background-color:rgb(100,100,100);}")
        self.checkBoxSave.setChecked(False)

        self.horizontalLayout_7.addWidget(self.checkBoxSave, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.label_26 = QLabel(self.tab_5)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_11.addWidget(self.label_26)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEditPathFileName = QLineEdit(self.tab_5)
        self.lineEditPathFileName.setObjectName(u"lineEditPathFileName")
        self.lineEditPathFileName.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEditPathFileName)

        self.pushButtonBrowseFiles = QPushButton(self.tab_5)
        self.pushButtonBrowseFiles.setObjectName(u"pushButtonBrowseFiles")
        self.pushButtonBrowseFiles.setMinimumSize(QSize(25, 0))
        self.pushButtonBrowseFiles.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButtonBrowseFiles)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_27 = QLabel(self.tab_5)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_10.addWidget(self.label_27)

        self.lineEditDatasetName = QLineEdit(self.tab_5)
        self.lineEditDatasetName.setObjectName(u"lineEditDatasetName")
        self.lineEditDatasetName.setMinimumSize(QSize(250, 0))

        self.verticalLayout_10.addWidget(self.lineEditDatasetName)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_28 = QLabel(self.tab_5)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_9.addWidget(self.label_28)

        self.spinBoxDatasetIndex = QSpinBox(self.tab_5)
        self.spinBoxDatasetIndex.setObjectName(u"spinBoxDatasetIndex")
        self.spinBoxDatasetIndex.setMaximum(5000)

        self.verticalLayout_9.addWidget(self.spinBoxDatasetIndex)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_11.addWidget(self.label_29)

        self.lineEditGroupName = QLineEdit(self.tab_5)
        self.lineEditGroupName.setObjectName(u"lineEditGroupName")
        self.lineEditGroupName.setMinimumSize(QSize(250, 0))

        self.verticalLayout_11.addWidget(self.lineEditGroupName)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_5 = QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plainTextEditMemo = QPlainTextEdit(self.tab_6)
        self.plainTextEditMemo.setObjectName(u"plainTextEditMemo")

        self.gridLayout_5.addWidget(self.plainTextEditMemo, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_12.addWidget(self.tabWidget)


        self.gridLayout_6.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(739, 0))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget_left = QTabWidget(self.frame_2)
        self.tabWidget_left.setObjectName(u"tabWidget_left")
        self.tabWidget_left.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mpl_widget_left = QWidget(self.tab)
        self.mpl_widget_left.setObjectName(u"mpl_widget_left")
        sizePolicy2.setHeightForWidth(self.mpl_widget_left.sizePolicy().hasHeightForWidth())
        self.mpl_widget_left.setSizePolicy(sizePolicy2)
        self.mpl_widget_left.setMinimumSize(QSize(518, 451))
        self.mpl_widget_left.setAutoFillBackground(False)
        self.mpl_widget_left.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.gridLayout_2.addWidget(self.mpl_widget_left, 0, 0, 1, 1)

        self.tabWidget_left.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.spinBox_left_index = QSpinBox(self.tab_2)
        self.spinBox_left_index.setObjectName(u"spinBox_left_index")
        self.spinBox_left_index.setMaximumSize(QSize(61, 16777215))
        self.spinBox_left_index.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_left_index.setMinimum(0)
        self.spinBox_left_index.setMaximum(1599)
        self.spinBox_left_index.setValue(1000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBox_left_index)


        self.verticalLayout_8.addLayout(self.formLayout_2)

        self.tabWidget_left.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget_left, 0, 0, 1, 1)

        self.tabWidget_right = QTabWidget(self.frame_2)
        self.tabWidget_right.setObjectName(u"tabWidget_right")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mpl_widget_right = QWidget(self.tab_3)
        self.mpl_widget_right.setObjectName(u"mpl_widget_right")
        sizePolicy2.setHeightForWidth(self.mpl_widget_right.sizePolicy().hasHeightForWidth())
        self.mpl_widget_right.setSizePolicy(sizePolicy2)
        self.mpl_widget_right.setMinimumSize(QSize(518, 451))
        self.mpl_widget_right.setAutoFillBackground(False)
        self.mpl_widget_right.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.gridLayout_3.addWidget(self.mpl_widget_right, 0, 0, 1, 1)

        self.tabWidget_right.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_35 = QLabel(self.tab_4)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_35)

        self.spinBox_right_index = QSpinBox(self.tab_4)
        self.spinBox_right_index.setObjectName(u"spinBox_right_index")
        self.spinBox_right_index.setMaximumSize(QSize(61, 16777215))
        self.spinBox_right_index.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_right_index.setMinimum(0)
        self.spinBox_right_index.setMaximum(1599)
        self.spinBox_right_index.setValue(1000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.spinBox_right_index)


        self.gridLayout_7.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.tabWidget_right.addTab(self.tab_4, "")

        self.gridLayout_4.addWidget(self.tabWidget_right, 0, 1, 1, 1)

        self.mpl_widget_spectra = QWidget(self.frame_2)
        self.mpl_widget_spectra.setObjectName(u"mpl_widget_spectra")
        sizePolicy2.setHeightForWidth(self.mpl_widget_spectra.sizePolicy().hasHeightForWidth())
        self.mpl_widget_spectra.setSizePolicy(sizePolicy2)
        self.mpl_widget_spectra.setMinimumSize(QSize(1061, 281))
        self.mpl_widget_spectra.setAutoFillBackground(False)
        self.mpl_widget_spectra.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.gridLayout_4.addWidget(self.mpl_widget_spectra, 1, 0, 1, 2)


        self.gridLayout_6.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1511, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.comboBoxFast, self.spinBox_fast_start)
        QWidget.setTabOrder(self.spinBox_fast_start, self.spinBox_fast_stop)
        QWidget.setTabOrder(self.spinBox_fast_stop, self.spinBox_fast_steps)
        QWidget.setTabOrder(self.spinBox_fast_steps, self.comboBoxSlow)
        QWidget.setTabOrder(self.comboBoxSlow, self.spinBox_slow_start)
        QWidget.setTabOrder(self.spinBox_slow_start, self.spinBox_slow_stop)
        QWidget.setTabOrder(self.spinBox_slow_stop, self.spinBox_slow_steps)
        QWidget.setTabOrder(self.spinBox_slow_steps, self.comboBoxFixed)
        QWidget.setTabOrder(self.comboBoxFixed, self.spinBox_fixed_start)
        QWidget.setTabOrder(self.spinBox_fixed_start, self.spinBox_fixed_stop)
        QWidget.setTabOrder(self.spinBox_fixed_stop, self.spinBox_fixed_steps)
        QWidget.setTabOrder(self.spinBox_fixed_steps, self.spinBox_post_image_z_pos)
        QWidget.setTabOrder(self.spinBox_post_image_z_pos, self.spinBoxDelayImaging)
        QWidget.setTabOrder(self.spinBoxDelayImaging, self.comboBoxRecNRB)
        QWidget.setTabOrder(self.comboBoxRecNRB, self.checkBoxCollectDark)
        QWidget.setTabOrder(self.checkBoxCollectDark, self.spinBoxDelayDark)
        QWidget.setTabOrder(self.spinBoxDelayDark, self.checkBoxCollectNRB)
        QWidget.setTabOrder(self.checkBoxCollectNRB, self.spinBoxDelayNRB)
        QWidget.setTabOrder(self.spinBoxDelayNRB, self.checkBoxCollectNRB_Early)
        QWidget.setTabOrder(self.checkBoxCollectNRB_Early, self.spinBoxDelayNRB_Early)
        QWidget.setTabOrder(self.spinBoxDelayNRB_Early, self.pushButtonStartAcq)
        QWidget.setTabOrder(self.pushButtonStartAcq, self.pushButtonStopAcq)
        QWidget.setTabOrder(self.pushButtonStopAcq, self.tabWidget_left)
        QWidget.setTabOrder(self.tabWidget_left, self.tabWidget_right)
        QWidget.setTabOrder(self.tabWidget_right, self.spinBox_left_index)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(0)
        self.comboBoxSlow.setCurrentIndex(1)
        self.comboBoxFixed.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.comboBoxRecNRB.setCurrentIndex(0)
        self.comboBox_nrb_slow_axis.setCurrentIndex(1)
        self.comboBox_nrb_fixed_axis.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_left.setCurrentIndex(0)
        self.tabWidget_right.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Raster Scanning", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Fast Axis", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBoxFast.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBoxFast.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBoxFast.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Step Size (um)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Slow Axis", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBoxSlow.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBoxSlow.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBoxSlow.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Step Size (um)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Fixed Axis", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBoxFixed.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBoxFixed.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBoxFixed.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Step Size (um)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Raster Parameters", None))
        self.pushButtonMacroXZ.setText(QCoreApplication.translate("MainWindow", u"X-Z", None))
        self.pushButtonMacroXY.setText(QCoreApplication.translate("MainWindow", u"X-Y", None))
        self.pushButtonMacroHighRes.setText(QCoreApplication.translate("MainWindow", u"High Res", None))
        self.pushButtonMacroLowRes.setText(QCoreApplication.translate("MainWindow", u"Low Res", None))
        self.pushButtonMacroXYRange.setText(QCoreApplication.translate("MainWindow", u"Full XY Range", None))
        self.pushButtonMacroXZRange.setText(QCoreApplication.translate("MainWindow", u"XZ Range", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Macros", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Post-Image Z  (um)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Imaging Delay (mm)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Before/After", None))
        self.comboBoxRecNRB.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBoxRecNRB.setItemText(1, QCoreApplication.translate("MainWindow", u"Before", None))
        self.comboBoxRecNRB.setItemText(2, QCoreApplication.translate("MainWindow", u"After", None))
        self.comboBoxRecNRB.setItemText(3, QCoreApplication.translate("MainWindow", u"Both", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Collect Dark", None))
        self.checkBoxCollectDark.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Delay (mm)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Collect NRB", None))
        self.checkBoxCollectNRB.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Delay (mm)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Early-Time NRB", None))
        self.checkBoxCollectNRB_Early.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Delay (mm)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"NRB/Dark Collection", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Fast Axis", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBox_nrb_fast_axis.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_nrb_fast_axis.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_nrb_fast_axis.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Slow Axis", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBox_nrb_slow_axis.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_nrb_slow_axis.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_nrb_slow_axis.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Start (um)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Stop (um)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Fixed Axis", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.comboBox_nrb_fixed_axis.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_nrb_fixed_axis.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_nrb_fixed_axis.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Position (um)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Params", None))
        self.pushButtonStartAcq.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButtonStopAcq.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Save?", None))
        self.checkBoxSave.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Path and Filename", None))
        self.pushButtonBrowseFiles.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Dataset Name", None))
        self.lineEditDatasetName.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Group Name", None))
        self.lineEditGroupName.setText(QCoreApplication.translate("MainWindow", u"/BCARSImage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Save", None))
        self.plainTextEditMemo.setPlainText(QCoreApplication.translate("MainWindow", u"Sample:\n"
"\n"
"Notes:\n"
"\n"
"Probe Power = 21 mW\n"
"SC Power = 11 mW", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Memo", None))
        self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Image", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Frequency Index", None))
        self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Image", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Frequency Index", None))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

