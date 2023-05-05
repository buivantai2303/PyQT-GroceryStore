from datetime import datetime

import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets


class EnterDHMClass(object):
    def __init__(self):
            self.Dialog = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 245)
        Dialog.setMinimumSize(QtCore.QSize(652, 240))
        Dialog.setStyleSheet("font: 87 8pt \"Shopee Display Black\";\n"
                             "background-color: rgb(98, 188, 157);")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.horizontalWidget_3.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.horizontalWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.horizontalWidget_3)
        self.horizontalWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_2.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalWidget_2)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EnterDHM_NDH = QtWidgets.QDateEdit(self.horizontalWidget_2)
        self.EnterDHM_NDH.setStyleSheet("\n"
                                        "background-color: rgb(255, 222, 215);\n"
                                        "color: rgb(170, 0, 0);\n"
                                        "border: 1px solid #000000;\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.EnterDHM_NDH.setObjectName("EnterDHM_NDH")
        self.verticalLayout.addWidget(self.EnterDHM_NDH)
        self.EnterDHM_MNV = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.EnterDHM_MNV.setStyleSheet("\n"
                                        "background-color: rgb(255, 222, 215);\n"
                                        "color: rgb(170, 0, 0);\n"
                                        "border: 1px solid #000000;\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.EnterDHM_MNV.setObjectName("EnterDHM_MNV")
        self.verticalLayout.addWidget(self.EnterDHM_MNV)
        self.EnterDHM_NCC = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.EnterDHM_NCC.setStyleSheet("\n"
                                        "background-color: rgb(255, 222, 215);\n"
                                        "color: rgb(170, 0, 0);\n"
                                        "border: 1px solid #000000;\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.EnterDHM_NCC.setObjectName("EnterDHM_NCC")
        self.verticalLayout.addWidget(self.EnterDHM_NCC)
        self.EnterDHM_Total = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.EnterDHM_Total.setStyleSheet("\n"
                                          "background-color: rgb(255, 222, 215);\n"
                                          "color: rgb(170, 0, 0);\n"
                                          "border: 1px solid #000000;\n"
                                          "border-radius: 10px;\n"
                                          "")
        self.EnterDHM_Total.setObjectName("EnterDHM_Total")
        self.verticalLayout.addWidget(self.EnterDHM_Total)
        self.horizontalLayout.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalWidget_21 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_21.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalWidget_21.setStyleSheet("\n"
                                               "background-color: rgb(255, 222, 215);\n"
                                               "color: rgb(170, 0, 0);\n"
                                               "border: 1px solid #000000;\n"
                                               "border-radius: 10px;\n"
                                               "")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalWidget_21)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EnterButtonDHM = QtWidgets.QPushButton(self.horizontalWidget_21)
        self.EnterButtonDHM.setStyleSheet("QPushButton {\n"
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
        self.EnterButtonDHM.setObjectName("EnterButtonDHM")
        self.verticalLayout_2.addWidget(self.EnterButtonDHM)
        self.ExitButtonDHM = QtWidgets.QPushButton(self.horizontalWidget_21)
        self.ExitButtonDHM.setStyleSheet("QPushButton {\n"
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
        self.ExitButtonDHM.setObjectName("ExitButtonDHM")
        self.verticalLayout_2.addWidget(self.ExitButtonDHM)
        self.horizontalLayout_3.addWidget(self.horizontalWidget_21)
        self.EnterButtonDHM.clicked.connect(self.add_data_to_db)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        server = 'BANHMIBIETBAY\\SQLEXPRESS'
        database = 'Sales_Manager'
        username = 'sa'
        password = '180403'

        # Create the database connection
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()

        cursor.execute("SELECT TenNCC FROM Nha_Cung_Cap WHERE XoaMem = 1")
        data = cursor.fetchall()
        for item in data:
            self.EnterDHM_NCC.addItem(item[0])

        cursor.execute("SELECT TenNV FROM Nhan_Vien WHERE XoaMem = 1")
        data_2 = cursor.fetchall()
        for item_2 in data_2:
            self.EnterDHM_MNV.addItem(item_2[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ngày đơn hàng"))
        self.label_3.setText(_translate("Dialog", "Mã nhân viên"))
        self.label_4.setText(_translate("Dialog", "Mã nhà cung cấp"))
        self.label_2.setText(_translate("Dialog", "Tổng giá trị"))
        self.EnterButtonDHM.setText(_translate("Dialog", "Hoàn tất"))
        self.ExitButtonDHM.setText(_translate("Dialog", "Hủy"))

    def add_data_to_db(self):
        server = 'BANHMIBIETBAY\\SQLEXPRESS'
        database = 'Sales_Manager'
        username = 'sa'
        password = '180403'

        # Create the database connection
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        Date = self.EnterDHM_NDH.date().toString("dd-MM-yyyy")
        MaNV = self.EnterDHM_MNV.currentText()
        NCC = self.EnterDHM_NCC.currentText()
        Total = self.EnterDHM_Total.text()
        XoaMem = 1
        ThoiGianXoa = datetime.today()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO Don_Hang_Mua (NgayDH, MaNV, MaNCC, TongGiaTri, XoaMem, ThoiGianXoa) VALUES (?, ?, ?, ?, ?, ?)",
                           (Date, MaNV, NCC, Total, XoaMem, ThoiGianXoa))
            conn.commit()
        except Exception as e:
            conn.rollback()
            # Handle the exception as needed
        finally:
            conn.close()
            # self.Dialog.close()

    def close(self):
        # self.close()
        pass