# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_andor_setup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(794, 553)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBoxAcquisitionMode = QComboBox(self.tab)
        self.comboBoxAcquisitionMode.setObjectName(u"comboBoxAcquisitionMode")
        self.comboBoxAcquisitionMode.setMinimumSize(QSize(188, 0))

        self.verticalLayout.addWidget(self.comboBoxAcquisitionMode)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBoxTriggerMode = QComboBox(self.tab)
        self.comboBoxTriggerMode.setObjectName(u"comboBoxTriggerMode")
        self.comboBoxTriggerMode.setMinimumSize(QSize(270, 0))

        self.verticalLayout_2.addWidget(self.comboBoxTriggerMode)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.comboBoxReadoutMode = QComboBox(self.tab)
        self.comboBoxReadoutMode.setObjectName(u"comboBoxReadoutMode")
        self.comboBoxReadoutMode.setMinimumSize(QSize(250, 0))

        self.verticalLayout_3.addWidget(self.comboBoxReadoutMode)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.formLayout_4 = QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.spinBox_Exposure = QDoubleSpinBox(self.groupBox)
        self.spinBox_Exposure.setObjectName(u"spinBox_Exposure")
        self.spinBox_Exposure.setMinimumSize(QSize(75, 25))
        self.spinBox_Exposure.setMaximumSize(QSize(200, 40))
        self.spinBox_Exposure.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_Exposure.setReadOnly(False)
        self.spinBox_Exposure.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_Exposure.setDecimals(6)
        self.spinBox_Exposure.setMinimum(0.000000000000000)
        self.spinBox_Exposure.setMaximum(300.000000000000000)
        self.spinBox_Exposure.setSingleStep(0.001000000000000)
        self.spinBox_Exposure.setValue(0.003500000000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.spinBox_Exposure)

        self.checkBoxBaselineClamping = QCheckBox(self.groupBox)
        self.checkBoxBaselineClamping.setObjectName(u"checkBoxBaselineClamping")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxBaselineClamping.sizePolicy().hasHeightForWidth())
        self.checkBoxBaselineClamping.setSizePolicy(sizePolicy)
        self.checkBoxBaselineClamping.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.checkBoxBaselineClamping)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 3, 2)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.comboBoxVS = QComboBox(self.groupBox_2)
        self.comboBoxVS.setObjectName(u"comboBoxVS")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBoxVS)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBoxVoltage = QComboBox(self.groupBox_2)
        self.comboBoxVoltage.setObjectName(u"comboBoxVoltage")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBoxVoltage)


        self.verticalLayout_6.addLayout(self.formLayout_2)


        self.gridLayout.addWidget(self.groupBox_2, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.comboBoxHSRate = QComboBox(self.groupBox_3)
        self.comboBoxHSRate.setObjectName(u"comboBoxHSRate")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxHSRate)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.comboBoxPreAmpGain = QComboBox(self.groupBox_3)
        self.comboBoxPreAmpGain.setObjectName(u"comboBoxPreAmpGain")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxPreAmpGain)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBoxAmpType = QComboBox(self.groupBox_3)
        self.comboBoxAmpType.addItem("")
        self.comboBoxAmpType.addItem("")
        self.comboBoxAmpType.setObjectName(u"comboBoxAmpType")
        self.comboBoxAmpType.setEnabled(False)
        self.comboBoxAmpType.setMinimumSize(QSize(110, 0))

        self.verticalLayout_4.addWidget(self.comboBoxAmpType)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.formLayout)


        self.gridLayout.addWidget(self.groupBox_3, 2, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 11pt \"Arial\";")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.checkBoxEM = QCheckBox(self.groupBox_4)
        self.checkBoxEM.setObjectName(u"checkBoxEM")
        sizePolicy.setHeightForWidth(self.checkBoxEM.sizePolicy().hasHeightForWidth())
        self.checkBoxEM.setSizePolicy(sizePolicy)
        self.checkBoxEM.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.checkBoxEM)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 11pt \"Arial\";")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.spinBox_averages = QSpinBox(self.groupBox_4)
        self.spinBox_averages.setObjectName(u"spinBox_averages")
        self.spinBox_averages.setMaximumSize(QSize(100, 16777215))
        self.spinBox_averages.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBox_averages.setMinimum(1)
        self.spinBox_averages.setMaximum(100)
        self.spinBox_averages.setValue(1)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBox_averages)


        self.verticalLayout_7.addLayout(self.formLayout_3)


        self.gridLayout.addWidget(self.groupBox_4, 3, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)
        self.comboBoxPreAmpGain.setCurrentIndex(-1)
        self.comboBoxAmpType.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Acquisition Mode", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Trigger Mode", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Readout Mode", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Exposure Time (sec)", None))
        self.checkBoxBaselineClamping.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Baseline Clamping", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Vertical Pixel Shift", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Shift Speed (us)", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Vertical Clock Voltage Amplitude (V)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Horizontal Pixel Shift", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Readout Rate (MHz)", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Premaplifer Gain", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Output Amplifier", None))
        self.comboBoxAmpType.setItemText(0, QCoreApplication.translate("Dialog", u"EM", None))
        self.comboBoxAmpType.setItemText(1, QCoreApplication.translate("Dialog", u"Conventional", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"EM Multiplier Gain", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Enabled", None))
        self.checkBoxEM.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Gain Level", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Camera Setup", None))
    # retranslateUi

