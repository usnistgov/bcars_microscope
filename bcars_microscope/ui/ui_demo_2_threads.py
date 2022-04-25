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
        MainWindow.resize(1141, 753)
        MainWindow.setMinimumSize(QSize(800, 400))
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
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(391, 0))
        self.frame.setMaximumSize(QSize(391, 16777215))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_moveY = QPushButton(self.frame)
        self.pushButton_moveY.setObjectName(u"pushButton_moveY")
        self.pushButton_moveY.setMinimumSize(QSize(0, 25))
        self.pushButton_moveY.setMaximumSize(QSize(16777215, 40))
        self.pushButton_moveY.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_moveY, 3, 4, 1, 1)

        self.pushButton_moveZ = QPushButton(self.frame)
        self.pushButton_moveZ.setObjectName(u"pushButton_moveZ")
        self.pushButton_moveZ.setMinimumSize(QSize(0, 25))
        self.pushButton_moveZ.setMaximumSize(QSize(16777215, 40))
        self.pushButton_moveZ.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_moveZ, 4, 4, 1, 1)

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

        self.pushButton_moveX = QPushButton(self.frame)
        self.pushButton_moveX.setObjectName(u"pushButton_moveX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_moveX.sizePolicy().hasHeightForWidth())
        self.pushButton_moveX.setSizePolicy(sizePolicy1)
        self.pushButton_moveX.setMinimumSize(QSize(0, 25))
        self.pushButton_moveX.setMaximumSize(QSize(16777215, 40))
        self.pushButton_moveX.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_moveX, 2, 4, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_moveAll = QPushButton(self.frame)
        self.pushButton_moveAll.setObjectName(u"pushButton_moveAll")
        self.pushButton_moveAll.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_moveAll)

        self.pushButton_setPos_getCurrent = QPushButton(self.frame)
        self.pushButton_setPos_getCurrent.setObjectName(u"pushButton_setPos_getCurrent")
        self.pushButton_setPos_getCurrent.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_setPos_getCurrent)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 3, 1, 2)

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

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_4.setTextFormat(Qt.PlainText)

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

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")
        self.label_5.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 2)

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

        self.pushButton_moveCenter = QPushButton(self.frame)
        self.pushButton_moveCenter.setObjectName(u"pushButton_moveCenter")
        self.pushButton_moveCenter.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_moveCenter, 5, 3, 1, 1)

        self.pushButton_updatePosition = QPushButton(self.frame)
        self.pushButton_updatePosition.setObjectName(u"pushButton_updatePosition")

        self.gridLayout.addWidget(self.pushButton_updatePosition, 1, 0, 1, 2)

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

        self.pushButton_moveCenter_Offset = QPushButton(self.frame)
        self.pushButton_moveCenter_Offset.setObjectName(u"pushButton_moveCenter_Offset")
        self.pushButton_moveCenter_Offset.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_moveCenter_Offset, 5, 4, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 0, 2, 5, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.checkBoxAvgOn = QCheckBox(self.frame_2)
        self.checkBoxAvgOn.setObjectName(u"checkBoxAvgOn")
        sizePolicy.setHeightForWidth(self.checkBoxAvgOn.sizePolicy().hasHeightForWidth())
        self.checkBoxAvgOn.setSizePolicy(sizePolicy)
        self.checkBoxAvgOn.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.checkBoxAvgOn)

        self.spinBoxNAverages = QSpinBox(self.frame_2)
        self.spinBoxNAverages.setObjectName(u"spinBoxNAverages")
        self.spinBoxNAverages.setMaximumSize(QSize(100, 16777215))
        self.spinBoxNAverages.setStyleSheet(u"font: 11pt \"Arial\";")
        self.spinBoxNAverages.setMinimum(1)
        self.spinBoxNAverages.setMaximum(1000)
        self.spinBoxNAverages.setValue(1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBoxNAverages)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.checkBoxShowStdDev = QCheckBox(self.frame_2)
        self.checkBoxShowStdDev.setObjectName(u"checkBoxShowStdDev")
        sizePolicy.setHeightForWidth(self.checkBoxShowStdDev.sizePolicy().hasHeightForWidth())
        self.checkBoxShowStdDev.setSizePolicy(sizePolicy)
        self.checkBoxShowStdDev.setStyleSheet(u"QCheckBox::indicator { width: 25; height: 25 }")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.checkBoxShowStdDev)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(391, 0))
        self.frame_3.setMaximumSize(QSize(391, 16777215))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setBaseSize(QSize(50, 50))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color:black")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setBaseSize(QSize(50, 50))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"color:red")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.mpl_widget = QWidget(self.centralwidget)
        self.mpl_widget.setObjectName(u"mpl_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mpl_widget.sizePolicy().hasHeightForWidth())
        self.mpl_widget.setSizePolicy(sizePolicy4)
        self.mpl_widget.setAutoFillBackground(False)
        self.mpl_widget.setStyleSheet(u"background-color: rgb(53,53,53)")

        self.horizontalLayout_3.addWidget(self.mpl_widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1141, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_moveY.setText(QCoreApplication.translate("MainWindow", u"Move Y", None))
        self.pushButton_moveZ.setText(QCoreApplication.translate("MainWindow", u"Move Z", None))
        self.pushButton_moveX.setText(QCoreApplication.translate("MainWindow", u"Move X", None))
        self.pushButton_moveAll.setText(QCoreApplication.translate("MainWindow", u"Move All", None))
        self.pushButton_setPos_getCurrent.setText(QCoreApplication.translate("MainWindow", u"Use Current", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Current Position", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Set Position", None))
        self.pushButton_moveCenter.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.pushButton_updatePosition.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_moveCenter_Offset.setText(QCoreApplication.translate("MainWindow", u"Center + Z-Offset", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y (um)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X (um)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Z (um)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z-Offset", None))
        self.checkBoxAvgOn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Averages ON", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"N Averages", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Show Standard Deviation", None))
        self.checkBoxShowStdDev.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

