# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QDialogSpeicherzellen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Speicher(object):
    def setupUi(self, Dialog_Speicher):
        Dialog_Speicher.setObjectName("Dialog_Speicher")
        Dialog_Speicher.setWindowModality(QtCore.Qt.NonModal)
        Dialog_Speicher.resize(218, 111)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_Speicher.sizePolicy().hasHeightForWidth())
        Dialog_Speicher.setSizePolicy(sizePolicy)
        Dialog_Speicher.setMinimumSize(QtCore.QSize(0, 0))
        Dialog_Speicher.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Speicher)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBox = QtWidgets.QSpinBox(Dialog_Speicher)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setWrapping(False)
        self.spinBox.setFrame(True)
        self.spinBox.setReadOnly(False)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setAccelerated(False)
        self.spinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(512)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 64)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Speicher)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_Speicher)
        self.buttonBox.accepted.connect(Dialog_Speicher.accept)
        self.buttonBox.rejected.connect(Dialog_Speicher.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Speicher)

    def retranslateUi(self, Dialog_Speicher):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Speicher.setWindowTitle(_translate("Dialog_Speicher", "angezeigte Speicherzellen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Speicher = QtWidgets.QDialog()
    ui = Ui_Dialog_Speicher()
    ui.setupUi(Dialog_Speicher)
    Dialog_Speicher.show()
    sys.exit(app.exec_())
