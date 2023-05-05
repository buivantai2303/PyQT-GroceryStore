# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from EnterDHM import EnterDHMClass
from EnterDHB import EnterDHBClass
from PyQt5 import QtCore, QtGui, QtWidgets

class enterDHM(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterDHMClass()
        self.ui.setupUi(self)


class enterDHB(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterDHBClass()
        self.ui.setupUi(self)

class SelectDHClass(object):

    def __init__(self):
        self.enter_DHB = enterDHB()
        self.enter_DHM = enterDHM()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 204)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(399, 204))
        Form.setStyleSheet("\n"
                           "\n"
                           "background-color: rgb(98, 188, 157);\n"
                           "font: 87 10pt \"Shopee Display Black\";\n"
                           "\n"
                           "\n"
                           "background-color: rgb(98, 188, 157);")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalWidget.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                          "    font: 87 11pt \"Shopee Display Black\";\n"
                                          "    background-color: rgb(255, 175, 135);\n"
                                          "border-radius: 10px;\n"
                                          "background-color: rgb(255, 202, 166);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.verticalWidget, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalWidget_2.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "    background-color: rgb(255, 175, 135);\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Shopee Display ExtBd")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    font: 81 11pt \"Shopee Display ExtBd\";\n"
                                        "    border: 1px solid #000000;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "    background-color:  rgb(170, 0, 0);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 81 11pt \"Shopee Display ExtBd\";\n"
                                      "    border: 1px solid #000000;\n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton {\n"
                                      "    background-color:  rgb(170, 0, 0);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.horizontalWidget_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.show_EnterDHM)
        self.pushButton_2.clicked.connect(self.show_EnterDHM)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                   Chọn lọai đơn hàng muốn thêm"))
        self.pushButton_2.setText(_translate("Form", "Đơn hàng bán"))
        self.pushButton.setText(_translate("Form", "Đơn hàng mua"))

    def show_EnterDHM(self):
        self.enter_DHM = enterDHM()
        self.enter_DHM.show()

    def show_EnterDHB(self):
        self.enter_DHB = enterDHB()
        self.enter_DHB.show()

    def show(self):
        pass



