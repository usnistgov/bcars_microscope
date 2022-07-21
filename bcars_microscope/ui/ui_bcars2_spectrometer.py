# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt_bcars2_spectrometer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 342)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBoxGratings = QtWidgets.QComboBox(Dialog)
        self.comboBoxGratings.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxGratings.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBoxGratings.setObjectName("comboBoxGratings")
        self.verticalLayout.addWidget(self.comboBoxGratings)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.spinBoxWL = QtWidgets.QDoubleSpinBox(Dialog)
        self.spinBoxWL.setEnabled(True)
        self.spinBoxWL.setMinimumSize(QtCore.QSize(150, 0))
        self.spinBoxWL.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.spinBoxWL.setReadOnly(False)
        self.spinBoxWL.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBoxWL.setDecimals(3)
        self.spinBoxWL.setMaximum(1200.0)
        self.spinBoxWL.setObjectName("spinBoxWL")
        self.verticalLayout_2.addWidget(self.spinBoxWL)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Spectrometer Settings"))
        self.label.setText(_translate("Dialog", "Grating"))
        self.label_2.setText(_translate("Dialog", "Wavelength (nm)"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "CARS (New)"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "CARS (Old)"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "CARS (Older)"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "SHG (Probe)"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "SHG (SC)"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "SHG (Both)"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "GFP"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Wavelength (nm)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "675"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "700"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog", "730"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Dialog", "385"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Dialog", "500"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Dialog", "400"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Dialog", "500"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

