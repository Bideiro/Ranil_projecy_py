# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Transaction\Dialog\DLog_CashAmount.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 199)
        Dialog.setStyleSheet("#widget{\n"
"background-color: #F8F8F0;\n"
"border: 3px solid #ABE27D;\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 3px solid #096033;\n"
"color: white\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #ABE27D;\n"
"background-color:rgba(0,0,0,0);\n"
"color: gray\n"
"}\n"
".QLabel{\n"
"color: black;\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Input_LE = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_LE.sizePolicy().hasHeightForWidth())
        self.Input_LE.setSizePolicy(sizePolicy)
        self.Input_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(11)
        self.Input_LE.setFont(font)
        self.Input_LE.setObjectName("Input_LE")
        self.verticalLayout.addWidget(self.Input_LE)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ok_btn = QtWidgets.QPushButton(self.widget_2)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(14)
        font.setBold(True)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_2.addWidget(self.ok_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_3.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "INPUT PAYMENT"))
        self.Input_LE.setPlaceholderText(_translate("Dialog", "Enter Amount Paid"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
