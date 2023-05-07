# -*- coding: utf-8 -*-
from datetime import datetime

import pyodbc
# Form implementation generated from reading ui file 'C:\Users\BanhMiBietBay\Documents\Code\Python\Intern\User_Interface\EnterDSHH.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Intern.Database.Connect_Database import connect_db


class EnterDSHHClass(object):
    def __init__(self):
        self.Dialog = None

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(763, 510)
        Dialog.setMinimumSize(QtCore.QSize(763, 510))
        Dialog.setStyleSheet("font: 87 8pt \"Shopee Display Black\";\n"
                             "background-color: rgb(98, 188, 157);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Menu_EnterDSHH = QtWidgets.QWidget(self.widget)
        self.Menu_EnterDSHH.setMinimumSize(QtCore.QSize(150, 0))
        self.Menu_EnterDSHH.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Menu_EnterDSHH.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                          "    font: 87 11pt \"Shopee Display Black\";\n"
                                          "border-radius: 10px;\n"
                                          "background-color: rgb(255, 202, 166);")
        self.Menu_EnterDSHH.setObjectName("Menu_EnterDSHH")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Menu_EnterDSHH)
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_6 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.Menu_EnterDSHH)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_4.addWidget(self.Menu_EnterDSHH)
        self.Context_EnterDSHH = QtWidgets.QWidget(self.widget)
        self.Context_EnterDSHH.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                             "    font: 87 11pt \"Shopee Display Black\";\n"
                                             "border-radius: 10px;\n"
                                             "background-color: rgb(255, 202, 166);")
        self.Context_EnterDSHH.setObjectName("Context_EnterDSHH")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Context_EnterDSHH)
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EnterDSHH_MH = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_MH.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_MH.setStyleSheet("\n"
                                        "background-color: rgb(255, 222, 215);\n"
                                        "color: rgb(170, 0, 0);\n"
                                        "border: 1px solid #000000;\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.EnterDSHH_MH.setText("")
        self.EnterDSHH_MH.setObjectName("EnterDSHH_MH")
        self.verticalLayout_3.addWidget(self.EnterDSHH_MH)
        self.EnterDSHH_TenHang = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_TenHang.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_TenHang.setStyleSheet("\n"
                                             "background-color: rgb(255, 222, 215);\n"
                                             "color: rgb(170, 0, 0);\n"
                                             "border: 1px solid #000000;\n"
                                             "border-radius: 10px;\n"
                                             "")
        self.EnterDSHH_TenHang.setText("")
        self.EnterDSHH_TenHang.setObjectName("EnterDSHH_TenHang")
        self.verticalLayout_3.addWidget(self.EnterDSHH_TenHang)
        self.EnterDSHH_MaDVT = QtWidgets.QComboBox(self.Context_EnterDSHH)
        self.EnterDSHH_MaDVT.setStyleSheet("\n"
                                           "background-color: rgb(255, 222, 215);\n"
                                           "color: rgb(170, 0, 0);\n"
                                           "border: 1px solid #000000;\n"
                                           "border-radius: 10px;\n"
                                           "")
        self.EnterDSHH_MaDVT.setObjectName("EnterDSHH_MaDVT")
        self.verticalLayout_3.addWidget(self.EnterDSHH_MaDVT)
        self.EnterDSHH_GiaMua = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_GiaMua.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_GiaMua.setStyleSheet("\n"
                                            "background-color: rgb(255, 222, 215);\n"
                                            "color: rgb(170, 0, 0);\n"
                                            "border: 1px solid #000000;\n"
                                            "border-radius: 10px;\n"
                                            "")
        self.EnterDSHH_GiaMua.setText("")
        self.EnterDSHH_GiaMua.setObjectName("EnterDSHH_GiaMua")
        self.verticalLayout_3.addWidget(self.EnterDSHH_GiaMua)
        self.EnterDSHH_GiaBan = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_GiaBan.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_GiaBan.setStyleSheet("\n"
                                            "background-color: rgb(255, 222, 215);\n"
                                            "color: rgb(170, 0, 0);\n"
                                            "border: 1px solid #000000;\n"
                                            "border-radius: 10px;\n"
                                            "")
        self.EnterDSHH_GiaBan.setText("")
        self.EnterDSHH_GiaBan.setObjectName("EnterDSHH_GiaBan")
        self.verticalLayout_3.addWidget(self.EnterDSHH_GiaBan)
        self.EnterDSHH_GiaBinhQuan = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_GiaBinhQuan.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_GiaBinhQuan.setStyleSheet("\n"
                                                 "background-color: rgb(255, 222, 215);\n"
                                                 "color: rgb(170, 0, 0);\n"
                                                 "border: 1px solid #000000;\n"
                                                 "border-radius: 10px;\n"
                                                 "")
        self.EnterDSHH_GiaBinhQuan.setText("")
        self.EnterDSHH_GiaBinhQuan.setObjectName("EnterDSHH_GiaBinhQuan")
        self.verticalLayout_3.addWidget(self.EnterDSHH_GiaBinhQuan)
        self.EnterDSHH_MaNCC = QtWidgets.QComboBox(self.Context_EnterDSHH)
        self.EnterDSHH_MaNCC.setStyleSheet("\n"
                                           "background-color: rgb(255, 222, 215);\n"
                                           "color: rgb(170, 0, 0);\n"
                                           "border: 1px solid #000000;\n"
                                           "border-radius: 10px;\n"
                                           "")
        self.EnterDSHH_MaNCC.setObjectName("EnterDSHH_MaNCC")
        self.verticalLayout_3.addWidget(self.EnterDSHH_MaNCC)
        self.EnterDSHH_SoLuonTon = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_SoLuonTon.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_SoLuonTon.setStyleSheet("\n"
                                               "background-color: rgb(255, 222, 215);\n"
                                               "color: rgb(170, 0, 0);\n"
                                               "border: 1px solid #000000;\n"
                                               "border-radius: 10px;\n"
                                               "")
        self.EnterDSHH_SoLuonTon.setText("")
        self.EnterDSHH_SoLuonTon.setObjectName("EnterDSHH_SoLuonTon")
        self.verticalLayout_3.addWidget(self.EnterDSHH_SoLuonTon)
        self.EnterDSHH_NgayCapNhat = QtWidgets.QDateEdit(self.Context_EnterDSHH)
        self.EnterDSHH_NgayCapNhat.setStyleSheet("\n"
                                                 "background-color: rgb(255, 222, 215);\n"
                                                 "color: rgb(170, 0, 0);\n"
                                                 "border: 1px solid #000000;\n"
                                                 "border-radius: 10px;\n"
                                                 "")
        self.EnterDSHH_NgayCapNhat.setObjectName("EnterDSHH_NgayCapNhat")
        self.verticalLayout_3.addWidget(self.EnterDSHH_NgayCapNhat)
        self.EnterDSHH_GhiChu = QtWidgets.QLineEdit(self.Context_EnterDSHH)
        self.EnterDSHH_GhiChu.setMinimumSize(QtCore.QSize(0, 30))
        self.EnterDSHH_GhiChu.setStyleSheet("\n"
                                            "background-color: rgb(255, 222, 215);\n"
                                            "color: rgb(170, 0, 0);\n"
                                            "border: 1px solid #000000;\n"
                                            "border-radius: 10px;\n"
                                            "")
        self.EnterDSHH_GhiChu.setText("")
        self.EnterDSHH_GhiChu.setObjectName("EnterDSHH_GhiChu")
        self.verticalLayout_3.addWidget(self.EnterDSHH_GhiChu)
        self.EnterDSHH_TrangThai = QtWidgets.QComboBox(self.Context_EnterDSHH)
        self.EnterDSHH_TrangThai.setMinimumSize(QtCore.QSize(441, 0))
        self.EnterDSHH_TrangThai.setStyleSheet("\n"
                                               "background-color: rgb(255, 222, 215);\n"
                                               "color: rgb(170, 0, 0);\n"
                                               "border: 1px solid #000000;\n"
                                               "border-radius: 10px;\n"
                                               "")
        self.EnterDSHH_TrangThai.setObjectName("EnterDSHH_TrangThai")
        self.EnterDSHH_TrangThai.addItem("")
        self.EnterDSHH_TrangThai.addItem("")
        self.verticalLayout_3.addWidget(self.EnterDSHH_TrangThai)
        self.horizontalLayout_4.addWidget(self.Context_EnterDSHH)
        self.horizontalWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalWidget_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalWidget_3.setStyleSheet("    color: rgb(170, 0, 0);\n"
                                              "    font: 87 11pt \"Shopee Display Black\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(255, 202, 166);")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalWidget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EnterButtonDSHH = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.EnterButtonDSHH.setMinimumSize(QtCore.QSize(70, 0))
        self.EnterButtonDSHH.setStyleSheet("QPushButton {\n"
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
        self.EnterButtonDSHH.setObjectName("EnterButtonDSHH")
        self.verticalLayout.addWidget(self.EnterButtonDSHH)
        self.ExitButtomDSHH = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.ExitButtomDSHH.setMinimumSize(QtCore.QSize(70, 0))
        self.ExitButtomDSHH.setStyleSheet("QPushButton {\n"
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
        self.ExitButtomDSHH.setObjectName("ExitButtomDSHH")
        self.verticalLayout.addWidget(self.ExitButtomDSHH)
        self.horizontalLayout_4.addWidget(self.horizontalWidget_3)
        self.horizontalLayout.addWidget(self.widget)
        self.ExitButtomDSHH.clicked.connect(self.CloseTab)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.EnterButtonDSHH.clicked.connect(self.add_data_to_db)

        cursor = connect_db().cursor()
        cursor.execute("SELECT TenNCC, MaNCC FROM Nha_Cung_Cap WHERE XoaMem = 1")
        data_2 = cursor.fetchall()
        for item_2 in data_2:
            self.EnterDSHH_MaNCC.addItem(item_2[1])

        cursor.execute("SELECT TenDVT, MaDVT FROM Don_Vi_Tinh WHERE XoaMem = 1")
        data_3 = cursor.fetchall()
        for item_3 in data_3:
            self.EnterDSHH_MaDVT.addItem(item_3[1])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Mã Hàng"))
        self.label_3.setText(_translate("Dialog", "Tên Hàng"))
        self.label_4.setText(_translate("Dialog", "Mã Đơn Vị tính"))
        self.label_5.setText(_translate("Dialog", "Giá mua"))
        self.label_2.setText(_translate("Dialog", "Giá bán"))
        self.label_7.setText(_translate("Dialog", "Giá bình quân"))
        self.label_8.setText(_translate("Dialog", "Mã nhà cung cấp"))
        self.label_9.setText(_translate("Dialog", "Số lượng tồn kho"))
        self.label_11.setText(_translate("Dialog", "Ngày cập nhật"))
        self.label_6.setText(_translate("Dialog", "Ghi chú"))
        self.label_10.setText(_translate("Dialog", "Trạng thái"))
        self.EnterDSHH_MH.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_TenHang.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_GiaMua.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_GiaBan.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_GiaBinhQuan.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_SoLuonTon.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_GhiChu.setPlaceholderText(_translate("Dialog", "Type here"))
        self.EnterDSHH_TrangThai.setItemText(0, _translate("Dialog", "Hoạt động"))
        self.EnterDSHH_TrangThai.setItemText(1, _translate("Dialog", "Không hoạt động"))
        self.EnterButtonDSHH.setText(_translate("Dialog", "Hoàn tất"))
        self.ExitButtomDSHH.setText(_translate("Dialog", "Hủy"))

    def add_data_to_db(self):
        Ma_Hang = self.EnterDSHH_MH.text()
        Ten_Hang = self.EnterDSHH_TenHang.text()
        MaDVT = self.EnterDSHH_MaDVT.currentText()
        GiaMua = self.EnterDSHH_GiaMua.text()
        GiaBan = self.EnterDSHH_GiaBan.text()
        GiaBinhQuan = self.EnterDSHH_GiaBinhQuan.text()
        MaNCC = self.EnterDSHH_MaNCC.currentText()
        SoLuong_Ton = self.EnterDSHH_SoLuonTon.text()
        NgayCapNhat = self.EnterDSHH_NgayCapNhat.date().toString("yyyy/dd/MM")
        GhiChu = self.EnterDSHH_GhiChu.text()
        TrangThai = self.EnterDSHH_TrangThai.currentText()

        server = 'BANHMIBIETBAY\\SQLEXPRESS'
        database = 'Sales_Manager'
        username = 'sa'
        password = '180403'

        # Create the database connection
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Hang_Hoa (MaHang, TenHang, MaDVT, GiaMua, GiaBan, GiaBinhQuan, MaNCC, SoLuongTon, NgayCapNhat, GhiChu, DaXoa) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (Ma_Hang, Ten_Hang, MaDVT, GiaMua, GiaBan, GiaBinhQuan, MaNCC, SoLuong_Ton, NgayCapNhat, GhiChu, TrangThai))
            conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            conn.close()
            self.Dialog.close()

    def close(self):
        pass

    def CloseTab(self):
        self.Dialog.close()
