# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_bcars2_spectrometer.ui'
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
        Dialog.resize(442, 342)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setFocusPolicy(Qt.NoFocus)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBoxGratings = QComboBox(Dialog)
        self.comboBoxGratings.setObjectName(u"comboBoxGratings")
        self.comboBoxGratings.setMinimumSize(QSize(200, 0))
        self.comboBoxGratings.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout.addWidget(self.comboBoxGratings)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.spinBoxWL = QDoubleSpinBox(Dialog)
        self.spinBoxWL.setObjectName(u"spinBoxWL")
        self.spinBoxWL.setEnabled(True)
        self.spinBoxWL.setMinimumSize(QSize(150, 0))
        self.spinBoxWL.setFocusPolicy(Qt.StrongFocus)
        self.spinBoxWL.setReadOnly(False)
        self.spinBoxWL.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxWL.setDecimals(3)
        self.spinBoxWL.setMaximum(1200.000000000000000)

        self.verticalLayout_2.addWidget(self.spinBoxWL)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 7):
            self.tableWidget.setRowCount(7)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(200, 0))
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Spectrometer Settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Grating", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Wavelength (nm)", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Wavelength (nm)", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"CARS (New)", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"CARS (Old)", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"CARS (Older)", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"SHG (Probe)", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"SHG (SC)", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"SHG (Both)", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"GFP", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"675", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"700", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"730", None));
        ___qtablewidgetitem11 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"385", None));
        ___qtablewidgetitem12 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"500", None));
        ___qtablewidgetitem13 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"400", None));
        ___qtablewidgetitem14 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"500", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

