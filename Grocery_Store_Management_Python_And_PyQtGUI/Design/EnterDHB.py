import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class EnterDHBClass(object):
    def __init__(self):
        self.Dialog = None

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(679, 251)
        Dialog.setMinimumSize(QtCore.QSize(679, 251))
        Dialog.setStyleSheet("font: 87 8pt \"Shopee Display Black\";\n"
                             "background-color: rgb(98, 188, 157);")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_4.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontalWidget_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.horizontalWidget_4.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalWidget_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.horizontalWidget_4)
        self.horizontalWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_3.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalWidget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EnterDHB_NgayDH = QtWidgets.QDateEdit(self.horizontalWidget_3)
        self.EnterDHB_NgayDH.setStyleSheet("\n"
                                           "background-color: rgb(255, 222, 215);\n"
                                           "color: rgb(170, 0, 0);\n"
                                           "border: 1px solid #000000;\n"
                                           "border-radius: 10px;\n"
                                           "")
        self.EnterDHB_NgayDH.setObjectName("EnterDHB_NgayDH")
        self.verticalLayout_2.addWidget(self.EnterDHB_NgayDH)
        self.EnterDHB_MaNV = QtWidgets.QComboBox(self.horizontalWidget_3)
        self.EnterDHB_MaNV.setStyleSheet("\n"
                                         "background-color: rgb(255, 222, 215);\n"
                                         "color: rgb(170, 0, 0);\n"
                                         "border: 1px solid #000000;\n"
                                         "border-radius: 10px;\n"
                                         "")
        self.EnterDHB_MaNV.setObjectName("EnterDHB_MaNV")
        self.verticalLayout_2.addWidget(self.EnterDHB_MaNV)
        self.EnterDHB_MaKH = QtWidgets.QLineEdit(self.horizontalWidget_3)
        self.EnterDHB_MaKH.setStyleSheet("\n"
                                         "background-color: rgb(255, 222, 215);\n"
                                         "color: rgb(170, 0, 0);\n"
                                         "border: 1px solid #000000;\n"
                                         "border-radius: 10px;\n"
                                         "")
        self.EnterDHB_MaKH.setObjectName("EnterDHB_MaKH")
        self.verticalLayout_2.addWidget(self.EnterDHB_MaKH)
        self.EnterDHB_Total = QtWidgets.QLineEdit(self.horizontalWidget_3)
        self.EnterDHB_Total.setStyleSheet("\n"
                                          "background-color: rgb(255, 222, 215);\n"
                                          "color: rgb(170, 0, 0);\n"
                                          "border: 1px solid #000000;\n"
                                          "border-radius: 10px;\n"
                                          "")
        self.EnterDHB_Total.setObjectName("EnterDHB_Total")
        self.verticalLayout_2.addWidget(self.EnterDHB_Total)
        self.horizontalLayout.addWidget(self.horizontalWidget_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_2.setMinimumSize(QtCore.QSize(100, 0))
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalWidget_2.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.horizontalWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EnterButtonDHB = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.EnterButtonDHB.setStyleSheet("QPushButton {\n"
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
        self.EnterButtonDHB.setObjectName("EnterButtonDHB")
        self.verticalLayout_3.addWidget(self.EnterButtonDHB)
        self.ExitButtonDHB = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.ExitButtonDHB.setStyleSheet("QPushButton {\n"
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
        self.ExitButtonDHB.setObjectName("ExitButtonDHB")
        self.verticalLayout_3.addWidget(self.ExitButtonDHB)
        self.horizontalLayout_4.addWidget(self.horizontalWidget_2)
        self.ExitButtonDHB.clicked.connect(self.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.EnterButtonDHB.clicked.connect(self.add_data_to_db)
        self.ExitButtonDHB.clicked.connect(self.CloseTab)

        server = 'BANHMIBIETBAY\\SQLEXPRESS'
        database = 'Sales_Manager'
        username = 'sa'
        password = '180403'

        # Create the database connection
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()

        cursor.execute("SELECT MaNV FROM Nhan_Vien WHERE XoaMem = 1")
        data_2 = cursor.fetchall()
        for item_2 in data_2:
            self.EnterDHB_MaNV.addItem(item_2[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ngày đơn hàng"))
        self.label_3.setText(_translate("Dialog", "Mã nhân viên"))
        self.label_4.setText(_translate("Dialog", "Mã khách hàng"))
        self.label_2.setText(_translate("Dialog", "Tổng giá trị"))
        self.EnterButtonDHB.setText(_translate("Dialog", "Hoàn tất"))
        self.ExitButtonDHB.setText(_translate("Dialog", "Hủy"))

    def add_data_to_db(self):
        print("Hello")
        server = 'BANHMIBIETBAY\\SQLEXPRESS'
        database = 'Sales_Manager'
        username = 'sa'
        password = '180403'

        # Create the database connection
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        MaNV = self.EnterDHB_MaNV.currentText()
        MaKH = self.EnterDHB_MaKH.text()
        Date = self.EnterDHB_NgayDH.date().toString("dd-MM-yyyy")
        Total = self.EnterDHB_Total.text()
        XoaMem = 1
        ThoiGianXoa = None
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO Don_Hang_Ban (NgayDH, MaNV, MaKH, TongGiaTri, XoaMem, ThoiGianXoa) VALUES (?, ?, ?, ?, ?, ?)", (Date, MaNV, MaKH, Total, XoaMem, ThoiGianXoa))
            conn.commit()

            info_box = QMessageBox()
            info_box.setIcon(QMessageBox.Information)
            info_box.setWindowTitle("Thông báo")
            info_box.setText("Thêm dữ liệu thành công!")
            info_box.setStandardButtons(QMessageBox.Ok)
            info_box.exec_()

            # Reset to next import
            self.EnterDHB_MaNV.setText("")
            self.EnterDHB_MaKH.setText("")
            self.EnterDHB_Total.setText("")
            self.EnterDHB_NgayDH.setText("")

        except Exception as e:
            conn.rollback()
            # Handle the exception as needed
        finally:
            conn.close()
            self.Dialog.close()

    def close(self):
        pass

    def CloseTab(self):
        self.Dialog.close()
