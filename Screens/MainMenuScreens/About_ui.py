# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\about.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#widget{\n"
"background-color: #F8F8F0;\n"
"}\n"
"#label_2, #label_4, #label_6{\n"
"color: #096033\n"
"}\n"
".QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.widget_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(24)
        self.widget_6.setFont(font)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(24)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.widget_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "ABOUT THE SYSTEM"))
        self.label.setText(_translate("MainWindow", "Welcome to the product management system for Ranil\'s Poultry Shop. A poultry shop\'s management tasks, such as product registration, sales management, inventory tracking, and user administration, can be made simpler and more automated with the help of this system. Ranil\'s Poultry Shop can increase overall customer service, decrease manual errors, and improve operational efficiency by utilizing this system. Our user-friendly and secure interface guarantees accurate and efficient completion of all tasks, offering a dependable solution for all your management requirements related to poultry shops."))
        self.label_4.setText(_translate("MainWindow", "ABOUT US"))
        self.label_5.setText(_translate("MainWindow", "Ranil\'s Poultry Shop offers a variety of products for poultry, including bird feed, plant seeds, fertilizers, and poultry accessories. They also provide pet-related items like dog and cat food, pet supplies, pet care products, and pet basics. Located in Rodriguez Rizal, the shop operates from 7:00 a.m. to 7:00 p.m. The current owner Mrs. Rachel Manuel, is the one who oversees all store operations. "))
        self.label_6.setText(_translate("MainWindow", "CONTACT US"))
import assets.All_In_Resource_rc
