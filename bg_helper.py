# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bg_helper.ui'
#
# Created: Sat Jul 18 01:33:00 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(719, 591)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxAge = QtGui.QSpinBox(self.groupBox)
        self.spinBoxAge.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spinBoxAge.setMinimum(16)
        self.spinBoxAge.setObjectName(_fromUtf8("spinBoxAge"))
        self.horizontalLayout.addWidget(self.spinBoxAge)
        self.pushButtonGenerate = QtGui.QPushButton(self.groupBox)
        self.pushButtonGenerate.setObjectName(_fromUtf8("pushButtonGenerate"))
        self.horizontalLayout.addWidget(self.pushButtonGenerate)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEditResults = QtGui.QPlainTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(13)
        self.plainTextEditResults.setFont(font)
        self.plainTextEditResults.setObjectName(_fromUtf8("plainTextEditResults"))
        self.verticalLayout.addWidget(self.plainTextEditResults)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Background Helper", None))
        self.groupBox.setTitle(_translate("Dialog", "Generator", None))
        self.label.setText(_translate("Dialog", "Age:", None))
        self.pushButtonGenerate.setText(_translate("Dialog", "Generate", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Results", None))

