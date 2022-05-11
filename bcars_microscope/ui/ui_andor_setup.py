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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(714, 561)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(53, 53, 53, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(35, 35, 35, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush4 = QBrush(QColor(42, 130, 218, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush3)
        palette.setBrush(QPalette.Active, QPalette.Link, brush4)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush5 = QBrush(QColor(25, 25, 25, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        brush7 = QBrush(QColor(120, 120, 120, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush8 = QBrush(QColor(0, 120, 215, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
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

        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_3.addWidget(self.comboBox_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 50, 141, 21))
        self.spinBox_Exposure = QDoubleSpinBox(self.groupBox)
        self.spinBox_Exposure.setObjectName(u"spinBox_Exposure")
        self.spinBox_Exposure.setGeometry(QRect(180, 50, 120, 25))
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

        self.comboBox_4 = QComboBox(self.groupBox_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_4)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBox_5 = QComboBox(self.groupBox_2)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_5)


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

        self.comboBox_6 = QComboBox(self.groupBox_3)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_6)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.comboBox_7 = QComboBox(self.groupBox_3)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_7)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)
        self.radioButton.setCheckable(False)
        self.radioButton.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.radioButton_2)


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

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.checkBox)

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

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 714, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Acquisition Mode", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Run Till Abort", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Trigger Mode", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Internal", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"External", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Fast External", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Readout Mode", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Image", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"FVB", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Timings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Exposure Time (sec)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Vertical Pixel Shift", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Shift Speed (us)", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"4.95", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"9.75", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"19.35", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"38.55", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Vertical Clock Voltage Amplitude", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"+1", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"+2", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"+3", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"+4", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Horizontal Pixel Shift", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Readout Rate", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"2.5 MHz", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"1 MHz", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"50 kHz", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Premaplifer Gain", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"1x", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"2x", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"4x", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output Amplifier", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Electron Multiplying (EM)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Conventional", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"EM Multiplier Gain", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.checkBox.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gain Level", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Camera Setup", None))
    # retranslateUi

