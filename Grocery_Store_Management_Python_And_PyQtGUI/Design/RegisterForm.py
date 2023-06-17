from PyQt5 import QtCore, QtGui, QtWidgets

class EnterRegisterFromClass(object):
    def setupUi(self, RegisterFrom):
        RegisterFrom.setObjectName("RegisterFrom")
        RegisterFrom.resize(400, 600)
        RegisterFrom.setMinimumSize(QtCore.QSize(400, 600))
        RegisterFrom.setStyleSheet("font: 87 8pt \"Shopee Display Black\";\n"
"background-color: rgb(98, 188, 157);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(RegisterFrom)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalWidget = QtWidgets.QWidget(RegisterFrom)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(16777215, 180))
        self.verticalWidget_2.setStyleSheet("    color: rgb(170, 0, 0);\n"
"    font: 87 11pt \"Shopee Display Black\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 202, 166);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_5.setStyleSheet("font: 87 29pt \"Shopee Display Black\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.verticalWidget_2)
        self.verticalWidget_3 = QtWidgets.QWidget(self.widget)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget1 = QtWidgets.QWidget(self.verticalWidget_3)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.widget1)
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalFrame_2.setStyleSheet("    color: rgb(170, 0, 0);\n"
"    font: 87 11pt \"Shopee Display Black\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 202, 166);")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_8.setContentsMargins(2, 30, 0, 30)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Shopee Display Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.horizontalFrame_2)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_6.addWidget(self.horizontalFrame_2)
        self.verticalFrame = QtWidgets.QFrame(self.widget1)
        self.verticalFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalFrame.setStyleSheet("    color: rgb(170, 0, 0);\n"
"    font: 87 11pt \"Shopee Display Black\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 202, 166);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.UserNameRegister = QtWidgets.QLineEdit(self.verticalFrame)
        self.UserNameRegister.setMinimumSize(QtCore.QSize(200, 30))
        self.UserNameRegister.setStyleSheet("\n"
"background-color: rgb(255, 222, 215);\n"
"color: rgb(170, 0, 0);\n"
"border: 1px solid #000000;\n"
"border-radius: 10px;\n"
"")
        self.UserNameRegister.setText("")
        self.UserNameRegister.setObjectName("UserNameRegister")
        self.verticalLayout_4.addWidget(self.UserNameRegister)
        self.Password_Register = QtWidgets.QLineEdit(self.verticalFrame)
        self.Password_Register.setMinimumSize(QtCore.QSize(200, 30))
        self.Password_Register.setStyleSheet("\n"
"background-color: rgb(255, 222, 215);\n"
"color: rgb(170, 0, 0);\n"
"border: 1px solid #000000;\n"
"border-radius: 10px;\n"
"")
        self.Password_Register.setText("")
        self.Password_Register.setObjectName("Password_Register")
        self.verticalLayout_4.addWidget(self.Password_Register)
        self.PhoneNumber = QtWidgets.QLineEdit(self.verticalFrame)
        self.PhoneNumber.setMinimumSize(QtCore.QSize(200, 30))
        self.PhoneNumber.setStyleSheet("\n"
"background-color: rgb(255, 222, 215);\n"
"color: rgb(170, 0, 0);\n"
"border: 1px solid #000000;\n"
"border-radius: 10px;\n"
"")
        self.PhoneNumber.setText("")
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.verticalLayout_4.addWidget(self.PhoneNumber)
        self.EmailRegister = QtWidgets.QLineEdit(self.verticalFrame)
        self.EmailRegister.setMinimumSize(QtCore.QSize(200, 30))
        self.EmailRegister.setStyleSheet("\n"
"background-color: rgb(255, 222, 215);\n"
"color: rgb(170, 0, 0);\n"
"border: 1px solid #000000;\n"
"border-radius: 10px;\n"
"")
        self.EmailRegister.setText("")
        self.EmailRegister.setObjectName("EmailRegister")
        self.verticalLayout_4.addWidget(self.EmailRegister)
        self.horizontalLayout_6.addWidget(self.verticalFrame)
        self.verticalLayout_6.addWidget(self.widget1)
        self.label_6 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_6.setMinimumSize(QtCore.QSize(300, 0))
        self.label_6.setMaximumSize(QtCore.QSize(300, 30))
        self.label_6.setStyleSheet("    color: rgb(170, 0, 0);\n"
"    font: 87 11pt \"Shopee Display Black\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 202, 166);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.widget2 = QtWidgets.QWidget(self.verticalWidget_3)
        self.widget2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(100, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SaveRegister = QtWidgets.QPushButton(self.widget2)
        self.SaveRegister.setMinimumSize(QtCore.QSize(0, 0))
        self.SaveRegister.setMaximumSize(QtCore.QSize(150, 50))
        self.SaveRegister.setStyleSheet("QPushButton {\n"
"    font: 81 10pt \"Shopee Display ExtBd\";\n"
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
        self.SaveRegister.setObjectName("SaveRegister")
        self.horizontalLayout_3.addWidget(self.SaveRegister)
        self.horizontalWidget = QtWidgets.QWidget(self.widget2)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.FaceIDButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.FaceIDButton.setGeometry(QtCore.QRect(40, 20, 40, 40))
        self.FaceIDButton.setMaximumSize(QtCore.QSize(40, 40))
        self.FaceIDButton.setStyleSheet("QPushButton {\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:/Icon/cil-smile.png);\n"
"    background-position: center;\n"
"    background-size: cover;\n"
"}\n"
"QPushButton {\n"
"    border: 1px solid #000000;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 81 10pt \"Shopee Display ExtBd\";\n"
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
        self.FaceIDButton.setText("")
        self.FaceIDButton.setIconSize(QtCore.QSize(30, 30))
        self.FaceIDButton.setObjectName("FaceIDButton")
        self.horizontalLayout_3.addWidget(self.horizontalWidget)
        self.verticalLayout_6.addWidget(self.widget2)
        self.verticalLayout_2.addWidget(self.verticalWidget_3)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.verticalWidget)

        self.retranslateUi(RegisterFrom)
        QtCore.QMetaObject.connectSlotsByName(RegisterFrom)

    def retranslateUi(self, RegisterFrom):
        _translate = QtCore.QCoreApplication.translate
        RegisterFrom.setWindowTitle(_translate("RegisterFrom", "Form"))
        self.label_5.setText(_translate("RegisterFrom", "Register"))
        self.label_2.setText(_translate("RegisterFrom", "Tài khoản"))
        self.label_3.setText(_translate("RegisterFrom", "Mật khẩu"))
        self.label_4.setText(_translate("RegisterFrom", "Số điện thoại"))
        self.label.setText(_translate("RegisterFrom", "Email"))
        self.UserNameRegister.setPlaceholderText(_translate("RegisterFrom", "Type here"))
        self.Password_Register.setPlaceholderText(_translate("RegisterFrom", "Type here"))
        self.PhoneNumber.setPlaceholderText(_translate("RegisterFrom", "Type here"))
        self.EmailRegister.setPlaceholderText(_translate("RegisterFrom", "Type here"))
        self.label_6.setText(_translate("RegisterFrom", "    Chọn \"Đăng ký\" để thực hiện đăng ký"))
        self.SaveRegister.setText(_translate("RegisterFrom", "Đăng ký"))

