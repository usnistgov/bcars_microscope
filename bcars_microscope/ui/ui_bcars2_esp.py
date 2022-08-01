# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt_designer\qt_bcars2_esp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(174, 158)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.spinBoxVelocity = QtWidgets.QDoubleSpinBox(Dialog)
        self.spinBoxVelocity.setEnabled(True)
        self.spinBoxVelocity.setMaximumSize(QtCore.QSize(80, 16777215))
        self.spinBoxVelocity.setReadOnly(False)
        self.spinBoxVelocity.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBoxVelocity.setMinimum(0.1)
        self.spinBoxVelocity.setMaximum(2.5)
        self.spinBoxVelocity.setSingleStep(0.1)
        self.spinBoxVelocity.setProperty("value", 1.0)
        self.spinBoxVelocity.setObjectName("spinBoxVelocity")
        self.verticalLayout.addWidget(self.spinBoxVelocity)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.spinBoxAcceleration = QtWidgets.QDoubleSpinBox(Dialog)
        self.spinBoxAcceleration.setMaximumSize(QtCore.QSize(80, 16777215))
        self.spinBoxAcceleration.setMaximum(10.0)
        self.spinBoxAcceleration.setSingleStep(0.1)
        self.spinBoxAcceleration.setProperty("value", 1.0)
        self.spinBoxAcceleration.setObjectName("spinBoxAcceleration")
        self.verticalLayout.addWidget(self.spinBoxAcceleration)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Velocity (mm/s)"))
        self.label_3.setText(_translate("Dialog", "Acceleration (mm/s^2)"))

