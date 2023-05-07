# IMPORT File and Source -----------------------------------------------------------------------------------------------|
import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QWidget, QMessageBox
from Intern.Database.Connect_Database import connect_db
from Intern.Design.EnterBG import EnterBGCLass
from Intern.Design.EnterDHB import EnterDHBClass
from Intern.Design.EnterDHM import EnterDHMClass
from Intern.Design.EnterDSHH import EnterDSHHClass
from Intern.Design.EnterDVT import EnterDVTClass
from Intern.Design.EnterNCC import EnterNCCClas
from Intern.Design.EnterNV import EnterNVClass
from Intern.Design.EnterXacNhan import Xac_Nhan
from Intern.Design.Login import EnterLoginClass
from Intern.Design.RegisterForm import EnterRegisterFromClass
from Intern.Design.SelectDH import SelectDHClass
from Intern.Functions.Animation.ui_functions import *
from Intern.Functions.FaceID.recognition import FaceRecognition
from ui_main import *
import datetime

# Call other class -----------------------------------------------------------------------------------------------------|
class enterDVT(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterDVTClass()
        self.ui.setupUi(self)


class enterNCC(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterNCCClas()
        self.ui.setupUi(self)


class enterDSHH(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterDSHHClass()
        self.ui.setupUi(self)


class enterBG(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterBGCLass()
        self.ui.setupUi(self)


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


# Register class -------------------------------------------------------------------------------------------------------|
class enterRegister(QDialog):
    time = datetime.datetime.now()

    def __init__(self):
        super().__init__()
        self.ui = EnterRegisterFromClass()
        self.ui.setupUi(self)
        self.ui.SaveRegister.clicked.connect(self.insert_data)
        self.ui.SaveRegister.clicked.connect(self.close)

    def insert_data(self):
        ten_nguoi_dung = self.ui.UserNameRegister.text()
        mat_khau = self.ui.Password_Register.text()
        so_dien_thoai = self.ui.PhoneNumber.text()
        R_email = self.ui.EmailRegister.text()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (TenNguoiDung, MatKhau, SoDienThoai, Email) VALUES (?, ?, ?, ?)",
                       ten_nguoi_dung, mat_khau, so_dien_thoai, R_email)
        conn.commit()
        # Thực hiện insert dữ liệu vào bảng login
        cursor = conn.cursor()
        cursor.execute("INSERT INTO login (UserName, Pass) VALUES (?, ?)", ten_nguoi_dung, mat_khau)
        conn.commit()

        # Đóng kết nối
        conn.close()

        from PyQt5.QtWidgets import QMessageBox

        # Đóng UI
        QMessageBox.information(self, "Thông báo", "Đăng ký thành công!")
        self.close()


class enterNV(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = EnterNVClass()
        self.ui.setupUi(self)


class enterSelect(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = SelectDHClass()
        self.ui.setupUi(self)


class xacnhan(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Xac_Nhan()
        self.ui.setupUi(self)


# MAIN -----------------------------------------------------------------------------------------------------------------|

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cursor = None

        # Create Table Model
        self.table_model_DVT = None
        self.table_model_NCC = None
        self.table_model_HH = None
        self.table_model_BG = None
        self.table_model_DHM = None
        self.table_model_DHB = None
        self.table_model_QLNV = None
        self.table_model_QLTK = None
        self.table = None

        # Show data from SQL Server to Table
        self.Display_DVT()
        self.Display_NCC()
        self.Display_Hang_Hoa()
        self.Display_Bang_Gia()
        self.Display_QuanLyTaiKhoan()
        self.Display_NhanVien()

        # Connect to other UI:
        self.enter_dvt = enterDVT()
        self.enter_ncc = enterNCC()
        self.enter_dshh = enterDSHH()
        self.enter_bg = enterBG()
        self.enter_dhm = enterDHM()
        self.enter_dhb = enterDHB()
        self.enter_nv = enterNV()
        self.enter_login = EnterLoginClass()
        self.enter_register = enterRegister()
        self.enter_selectDH = enterSelect()
        self.enter_xacnhan = xacnhan()

        # TOGGLE/ MENU: Include Account and main -----------------------------------------------------------------------|
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btn_page_1.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)))
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGES:
        # PAGE 1: Function of app in left menu -------------------------------------------------------------------------|
        self.ui.Home_9.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_DVT_Page))
        self.ui.Home_8.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_NCC_Page))
        self.ui.Home_7.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_DSHH_Page))
        self.ui.Home_6.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_BG_Page))
        self.ui.Home_5.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_DG_Page))
        self.ui.Home_2.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_QLNV_Page))

        # DVT Page -----------------------------------------------------------------------------------------------------|
        self.ui.AddButtonDSDVT.clicked.connect(self.enter_dvt.exec_)

        # NCC Page -----------------------------------------------------------------------------------------------------|
        self.ui.AddButtonDSNCC.clicked.connect(self.enter_ncc.exec_)

        # DSHH Page ----------------------------------------------------------------------------------------------------|
        self.ui.AddButonDSHH.clicked.connect(self.enter_dshh.exec_)

        # Bang Gia Page ------------------------------------------------------------------------------------------------|
        self.ui.pushButton_22.clicked.connect(self.enter_bg.exec_)

        # Nhan Vien Page -----------------------------------------------------------------------------------------------|
        self.ui.pushButton_13.clicked.connect(self.enter_nv.exec_)

        # Select DH Page -----------------------------------------------------------------------------------------------|
        self.ui.pushButton_2.clicked.connect(self.enter_selectDH.exec_)

        # Delete Function called ---------------------------------------------------------------------------------------|
        self.ui.DeleteButtonDSDVT.clicked.connect(self.removeSelectedRow_DVT)
        self.ui.DeleteButtonDSHH.clicked.connect(self.removeSelectedRow_HangHoa)
        self.ui.DeleteButtonDSNCC.clicked.connect(self.removeSelectedRow_NhaCungCap)
        self.ui.pushButton_23.clicked.connect(self.removeSelectedRow_BangGia)
        self.ui.pushButton.clicked.connect(self.removeSelectedRow_DonHangMUa)
        self.ui.pushButton.clicked.connect(self.removeSelectedRow_DonHangBan)
        self.ui.pushButton_14.clicked.connect(self.removeSelectedRowNhanVien)

    # Radio button used for display DHB/DHM ----------------------------------------------------------------------------|
        self.ui.radioButton_3.clicked.connect(self.radio_button_3_clicked)
        self.ui.radioButton_4.clicked.connect(self.radio_button_4_clicked)

    def radio_button_3_clicked(self):
        if self.ui.radioButton_3.isChecked():
            self.ui.radioButton_4.clicked.disconnect(self.radio_button_4_clicked)
            self.ui.radioButton_4.setChecked(False)
            self.ui.radioButton_4.clicked.connect(self.radio_button_4_clicked)
            self.Display_Don_Hang_Mua()

    def radio_button_4_clicked(self):
        if self.ui.radioButton_4.isChecked():
            self.ui.radioButton_3.clicked.disconnect(self.radio_button_3_clicked)
            self.ui.radioButton_3.setChecked(False)
            self.ui.radioButton_3.clicked.connect(self.radio_button_3_clicked)
            self.Display_Don_Hang_Ban()

    # Display and Search functions -------------------------------------------------------------------------------------|
    def searchBar_DVT(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.LineSearchDSDVT.text().strip()
        self.cursor.execute("SELECT STT, MaDVT, TenDVT, GhiChu FROM Don_Vi_Tinh WHERE MaDVT LIKE ?",
                            ('%' + search_term + '%',))
        self.table_model_DVT.clear()
        self.table_model_DVT.setHorizontalHeaderLabels(['STT', 'Mã Đơn vị tính', 'Tên Đơn vị tính', 'Ghi chú'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_DVT.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_DVT.setItem(row_number, column_number, item)

        self.ui.tableView.resizeColumnsToContents()
        header = self.ui.tableView.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_DVT(self):  # Xuất dữ liệu ra bảng
        self.ui.LineSearchDSDVT.textChanged.connect(self.searchBar_DVT)
        self.table_model_DVT = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute('SELECT STT, MaDVT, TenDVT, GhiChu FROM Don_Vi_Tinh ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_DVT.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_DVT.setItem(row_number, column_number, item)

        self.ui.tableView.setModel(self.table_model_DVT)
        self.table_model_DVT.setHorizontalHeaderLabels(['STT', 'Mã Đơn vị tính', 'Tên Đơn vị tính', 'Ghi chú'])
        self.ui.tableView.resizeColumnsToContents()
        header = self.ui.tableView.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def searchBar_NCC(self):  # Tìm kiếm dữ liệu
        search_term_2 = self.ui.LineSearchDSNCC.text().strip()
        self.cursor.execute(
            "SELECT STT, MaNCC, TenNCC, DienThoai, DiaChi, GhiChu FROM Nha_Cung_Cap WHERE XoaMem = 1 AND TenNCC LIKE ?",
            ('%' + search_term_2 + '%',))
        self.table_model_NCC.clear()
        self.table_model_NCC.setHorizontalHeaderLabels(['STT', 'Mã Nhà cung cấp', 'Tên Nhà cung cấp', 'Điện thoại', 'Địa chỉ', 'Ghi chú'])
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_NCC.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_NCC.setItem(row_number, column_number, item)
        self.ui.tableView_2.resizeColumnsToContents()
        header = self.ui.tableView_2.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_NCC(self):  # Xuất dữ liệu ra bảng
        self.ui.LineSearchDSNCC.textChanged.connect(self.searchBar_NCC)
        self.table_model_NCC = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute(
            'SELECT STT, MaNCC, TenNCC, DienThoai, DiaChi, GhiChu FROM Nha_Cung_Cap WHERE XoaMem = 1 ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_NCC.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_NCC.setItem(row_number, column_number, item)

        self.ui.tableView_2.setModel(self.table_model_NCC)
        self.table_model_NCC.setHorizontalHeaderLabels(['STT', 'Mã Nhà cung cấp', 'Tên Nhà cung cấp', 'Điện thoại', 'Địa chỉ', 'Ghi chú'])
        self.ui.tableView_2.resizeColumnsToContents()
        header = self.ui.tableView_2.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def searchBar_Hang_Hoa(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.LineSearchDSHH.text().strip()
        self.cursor.execute(
            "SELECT STT, MaHang, TenHang, MaDVT, GiaMua, GiaBan, GiaBinhQUan, MaNCC, SoLuongTon, NgayCapNhat, GhiChu "
            "FROM Hang_Hoa WHERE XoaMem = 1 AND TenHang LIKE ?",
            ('%' + search_term + '%',))
        self.table_model_HH.clear()
        self.table_model_HH.setHorizontalHeaderLabels(
            ['STT', 'Mã Hàng', 'Tên Hàng', 'Mã Đơn vị tính', 'Giá mua', 'Giá bán', 'Giá bình quân', 'Mã nhà cung cấp', 'Tồn kho',
             'Ngày cập nhật', 'Ghi chú'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_HH.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_HH.setItem(row_number, column_number, item)

        self.ui.tableView_3.resizeColumnsToContents()
        header = self.ui.tableView_3.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_Hang_Hoa(self):  # Xuất dữ liệu ra bảng
        self.ui.LineSearchDSHH.textChanged.connect(self.searchBar_Hang_Hoa)
        self.table_model_HH = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute(
            'SELECT STT, MaHang, TenHang, MaDVT, GiaMua, GiaBan, GiaBinhQUan, MaNCC, SoLuongTon, NgayCapNhat, GhiChu '
            'FROM Hang_Hoa WHERE XoaMem = 1 ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_HH.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_HH.setItem(row_number, column_number, item)

        self.ui.tableView_3.setModel(self.table_model_HH)
        self.table_model_HH.setHorizontalHeaderLabels(
            ['STT', 'Mã Hàng', 'Tên Hàng', 'Mã Đơn vị tính', 'Giá mua', 'Giá bán', 'Giá bình quân', 'Mã nhà cung cấp',
             'Tồn kho', 'Ngày cập nhật', 'Ghi chú'])
        self.ui.tableView_3.resizeColumnsToContents()
        header = self.ui.tableView_3.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def searchBar_Bang_Gia(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.lineEdit_5.text().strip()
        self.cursor.execute(
            "SELECT STT, MaBangGia, MaHang, MaDVT, SoLuongDVT, GiaMua, GiaBan FROM Bang_Gia WHERE XoaMem = 1 AND MaHang "
            "LIKE ?",
            ('%' + search_term + '%',))
        self.table_model_BG.clear()
        self.table_model_BG.setHorizontalHeaderLabels(
            ['STT', 'Mã giá sản phẩm', 'Mã hàng', 'Mã Đơn vị tính', 'Số lượng', 'Giá mua', 'Giá bán'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_BG.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_BG.setItem(row_number, column_number, item)

        self.ui.tableView_4.resizeColumnsToContents()
        header = self.ui.tableView_4.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_Bang_Gia(self):  # Xuất dữ liệu ra bảng
        self.ui.lineEdit_5.textChanged.connect(self.searchBar_Bang_Gia)
        self.table_model_BG = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute(
            'SELECT STT, MaBangGia, MaHang, MaDVT, SoLuongDVT, GiaMua, GiaBan FROM Bang_Gia ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_BG.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_BG.setItem(row_number, column_number, item)

        self.ui.tableView_4.setModel(self.table_model_BG)
        self.table_model_BG.setHorizontalHeaderLabels(
            ['STT', 'Mã giá sản phẩm', 'Mã hàng', 'Mã Đơn vị tính', 'Số lượng', 'Giá mua', 'Giá bán'])
        self.ui.tableView_4.resizeColumnsToContents()
        header = self.ui.tableView_4.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def searchBar_Don_Hang_Mua(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.lineEdit_8.text().strip()
        self.cursor.execute(
            "SELECT STT, MaDH, NgayDH, MaNV, MaNCC, TongGiaTri FROM Don_Hang_Mua WHERE XoaMem = 1 AND MaDH LIKE ?",
            ('%' + search_term + '%',))
        self.table_model_DHM.clear()
        self.table_model_DHM.setHorizontalHeaderLabels(
            ['STT', 'Mã Đơn hàng mua', 'Thời gian', 'Mã nhân viên', 'Mã nhà cung cấp', 'Tổng giá trị'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_DHM.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_DHM.setItem(row_number, column_number, item)

        self.ui.tableView_6.resizeColumnsToContents()
        header = self.ui.tableView_6.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_Don_Hang_Mua(self):  # Xuất dữ liệu ra bảng
        self.ui.lineEdit_8.textChanged.connect(self.searchBar_Don_Hang_Mua)
        self.table_model_DHM = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute(
            'SELECT STT, MaDH, NgayDH, MaNV, MaNCC, TongGiaTri FROM Don_Hang_Mua WHERE XoaMem = 1 ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_DHM.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_DHM.setItem(row_number, column_number, item)

        self.ui.tableView_6.setModel(self.table_model_DHM)
        self.table_model_DHM.setHorizontalHeaderLabels(
            ['STT', 'Mã Đơn hàng mua', 'Thời gian', 'Mã nhân viên', 'Mã nhà cung cấp', 'Tổng giá trị'])
        self.ui.tableView_6.resizeColumnsToContents()
        header = self.ui.tableView_6.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def searchBar_Don_Hang_Ban(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.lineEdit_8.text().strip()
        self.cursor.execute(
            "SELECT STT, MaDH, NgayDH, MaNV, MaKH, TongGiaTri FROM Don_Hang_Ban WHERE XoaMem = 1 AND MaDH LIKE ?",
            ('%' + search_term + '%',))
        self.table_model_DHB.clear()
        self.table_model_DHB.setHorizontalHeaderLabels(
            ['STT', 'Mã Đơn hàng bán', 'Thời gian', 'Mã nhân viên', 'Mã khách hàng (Nếu có)', 'Tổng giá trị'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_DHB.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_DHB.setItem(row_number, column_number, item)

        self.ui.tableView_6.resizeColumnsToContents()
        header = self.ui.tableView_6.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_Don_Hang_Ban(self):  # Xuất dữ liệu ra bảng
        self.ui.lineEdit_8.textChanged.connect(self.searchBar_Don_Hang_Ban)
        self.table_model_DHB = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute(
            'SELECT STT, MaDH, NgayDH, MaNV, MaKH, TongGiaTri FROM Don_Hang_Ban WHERE XoaMem = 1 ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_DHB.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_DHB.setItem(row_number, column_number, item)

        self.ui.tableView_6.setModel(self.table_model_DHB)
        self.table_model_DHB.setHorizontalHeaderLabels(
            ['STT', 'Mã Đơn hàng bán', 'Thời gian', 'Mã nhân viên', 'Mã khách hàng (Nếu có)', 'Tổng giá trị'])
        self.ui.tableView_6.resizeColumnsToContents()
        header = self.ui.tableView_6.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def SearchBar_QuanLyTaiKhoan(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.LineSearchQLTK.text().strip()
        self.cursor.execute(
            "SELECT TenNguoiDung, MatKhau, SoDienThoai, Email FROM users WHERE XoaMem = 1 AND TenNguoiDung LIKE ?",
            ('%' + search_term + '%',))
        self.table_model_QLTK.clear()
        self.table_model_QLTK.setHorizontalHeaderLabels(
            ['Tên người dùng', 'Mật khẩu', 'Số điện thoại', 'Email'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_QLTK.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_QLTK.setItem(row_number, column_number, item)

        self.ui.TableQLTK.resizeColumnsToContents()
        header = self.ui.TableQLTK.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_QuanLyTaiKhoan(self):  # Xuất dữ liệu ra bảng
        self.ui.LineSearchQLTK.textChanged.connect(self.SearchBar_QuanLyTaiKhoan)
        self.table_model_QLTK = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute('SELECT TenNguoiDung, MatKhau, SoDienThoai, Email FROM users ORDER BY TenNguoiDung')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_QLTK.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_QLTK.setItem(row_number, column_number, item)

        self.ui.TableQLTK.setModel(self.table_model_QLTK)
        self.table_model_QLTK.setHorizontalHeaderLabels(
            ['Tên người dùng', 'Mật khẩu', 'Số điện thoại', 'Email'])
        self.ui.TableQLTK.resizeColumnsToContents()
        header = self.ui.TableQLTK.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def searchBar_Nhan_Vien(self):  # Tìm kiếm dữ liệu
        search_term = self.ui.lineEdit_10.text().strip()
        self.cursor.execute(
            "SELECT STT, MaNV, TenNV, DienThoai, DiaChi, TaiKhoan, Quyen, GhiChu, DaXoa FROM Nhan_Vien WHERE "
            "XoaMem = 1 AND TenNV LIKE ?",
            ('%' + search_term + '%',))
        self.table_model_QLNV.clear()
        self.table_model_QLNV.setHorizontalHeaderLabels(
            ['STT', 'Mã nhân viên', 'Tên nhân viên', 'Số điện thoại', 'Địa chỉ', 'Tài khoản mail', 'Quyền',
             'Ghi chú',
             'Trạng thái'])

        for row_number, row_data in enumerate(self.cursor):
            self.table_model_QLNV.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_QLNV.setItem(row_number, column_number, item)

        self.ui.tableView_10.resizeColumnsToContents()
        header = self.ui.tableView_10.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def Display_NhanVien(self):  # Xuất dữ liệu ra bảng
        self.ui.lineEdit_10.textChanged.connect(self.searchBar_Nhan_Vien)
        self.table_model_QLNV = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute(
            'SELECT STT, MaNV, TenNV, DienThoai, DiaChi, TaiKhoan, Quyen, GhiChu, DaXoa FROM Nhan_Vien WHERE '
            'XoaMem = 1 ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            self.table_model_QLNV.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model_QLNV.setItem(row_number, column_number, item)

        self.ui.tableView_10.setModel(self.table_model_QLNV)
        self.table_model_QLNV.setHorizontalHeaderLabels(
            ['STT', 'Mã nhân viên', 'Tên nhân viên', 'Số điện thoại', 'Địa chỉ', 'Tài khoản mail', 'Quyền',
             'Ghi chú', 'Trạng thái'])
        self.ui.tableView_10.resizeColumnsToContents()
        header = self.ui.tableView_10.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    # Remove element in table ------------------------------------------------------------------------------------------|

    def removeSelectedRow_DVT(self):
        selection_model = self.ui.tableView.selectionModel()
        indexes = selection_model.selectedIndexes()
        if indexes:
            reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row_numbers = sorted(set(index.row() for index in indexes))
                conn = connect_db()
                cursor = conn.cursor()
                for row_number in reversed(row_numbers):
                    if row_number < 0:
                        continue
                    # Lấy giá trị của cột MaDVT tại hàng được chọn
                    selected_index = self.table_model_DVT.index(row_number, 1)
                    MaDVT = selected_index.data()
                    # Xóa hàng trong tableView
                    self.table_model_DVT.removeRow(row_number)
                    # Xóa mềm dữ liệu trong SQL Server
                    ThoiGianXoa = datetime.datetime.now()
                    cursor.execute(f"UPDATE Don_Vi_Tinh SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaDVT = '{MaDVT}'")
                    conn.commit()
                cursor.close()
                conn.close()

    def removeSelectedRow_HangHoa(self):
        selection_model = self.ui.tableView_3.selectionModel()
        indexes = selection_model.selectedIndexes()
        if indexes:
            reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row_numbers = sorted(set(index.row() for index in indexes))
                conn = connect_db()
                cursor = conn.cursor()
                for row_number in reversed(row_numbers):
                    if row_number < 0:
                        continue
                    # Lấy giá trị của cột MaDVT tại hàng được chọn
                    selected_index = self.table_model_HH.index(row_number, 1)
                    HangHoa = selected_index.data()
                    # Xóa hàng trong tableView
                    self.table_model_HH.removeRow(row_number)
                    # Xóa mềm dữ liệu trong SQL Server
                    ThoiGianXoa = datetime.datetime.now()
                    cursor.execute(f"UPDATE Hang_Hoa SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaHang = '{HangHoa}'")
                    conn.commit()
                cursor.close()
                conn.close()

    def removeSelectedRow_NhaCungCap(self):
        selection_model = self.ui.tableView_2.selectionModel()
        indexes = selection_model.selectedIndexes()
        if indexes:
            reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row_numbers = sorted(set(index.row() for index in indexes))
                conn = connect_db()
                cursor = conn.cursor()
                for row_number in reversed(row_numbers):
                    if row_number < 0:
                        continue
                    # Lấy giá trị của cột MaDVT tại hàng được chọn
                    selected_index = self.table_model_NCC.index(row_number, 1)
                    NCC = selected_index.data()
                    # Xóa hàng trong tableView
                    self.table_model_NCC.removeRow(row_number)
                    # Xóa mềm dữ liệu trong SQL Server
                    ThoiGianXoa = datetime.datetime.now()
                    cursor.execute(f"UPDATE Nha_Cung_Cap SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaNCC  = '{NCC}'")
                    conn.commit()
                cursor.close()
                conn.close()

    def removeSelectedRow_BangGia(self):
        selection_model = self.ui.tableView_4.selectionModel()
        indexes = selection_model.selectedIndexes()
        if indexes:
            reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row_numbers = sorted(set(index.row() for index in indexes))
                conn = connect_db()
                cursor = conn.cursor()
                for row_number in reversed(row_numbers):
                    if row_number < 0:
                        continue
                    # Lấy giá trị của cột MaDVT tại hàng được chọn
                    selected_index = self.table_model_BG.index(row_number, 1)
                    MaBangGia = selected_index.data()
                    # Xóa hàng trong tableView
                    self.table_model_BG.removeRow(row_number)
                    # Xóa mềm dữ liệu trong SQL Server
                    ThoiGianXoa = datetime.datetime.now()
                    cursor.execute(f"UPDATE Bang_Gia SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaBangGia  = '{MaBangGia}'")
                    conn.commit()
                cursor.close()
                conn.close()

    def removeSelectedRow_DonHangMUa(self):
        if self.ui.radioButton_3.isChecked():
            selection_model = self.ui.tableView_6.selectionModel()
            indexes = selection_model.selectedIndexes()
            if indexes:
                reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    row_numbers = sorted(set(index.row() for index in indexes))
                    conn = connect_db()
                    cursor = conn.cursor()
                    for row_number in reversed(row_numbers):
                        # Lấy giá trị của cột MaDVT tại hàng được chọn
                        if row_number < 0:
                            continue
                        selected_index = self.table_model_DHM.index(row_number, 1)
                        MaDH = selected_index.data()
                        # Xóa hàng trong tableView
                        self.table_model_DHM.removeRow(row_number)
                        # Xóa mềm dữ liệu trong SQL Server
                        ThoiGianXoa = datetime.datetime.now()
                        cursor.execute(f"UPDATE Don_Hang_Mua SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaDH  = '{MaDH}'")
                        conn.commit()
                    cursor.close()
                    conn.close()
            else:
                QMessageBox.warning(self, 'Thông báo', 'Chưa chọn hàng để xóa.')

    def removeSelectedRow_DonHangBan(self):
        if self.ui.radioButton_4.isChecked():
            selection_model = self.ui.tableView_6.selectionModel()
            indexes = selection_model.selectedIndexes()
            if indexes:
                reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    row_numbers = sorted(set(index.row() for index in indexes))
                    conn = connect_db()
                    cursor = conn.cursor()
                    for row_number in reversed(row_numbers):
                        # Lấy giá trị của cột MaDVT tại hàng được chọn
                        if row_number < 0:
                            continue
                        selected_index = self.table_model_DHB.index(row_number, 1)
                        MaDH = selected_index.data()
                        # Xóa hàng trong tableView
                        self.table_model_DHB.removeRow(row_number)
                        # Xóa mềm dữ liệu trong SQL Server
                        ThoiGianXoa = datetime.datetime.now()
                        cursor.execute(f"UPDATE Don_Hang_Ban SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaDH  = '{MaDH}'")
                        conn.commit()
                    cursor.close()
                    conn.close()
            else:
                QMessageBox.warning(self, 'Thông báo', 'Chưa chọn hàng để xóa.')

    def removeSelectedRowNhanVien(self):
        selection_model = self.ui.tableView_10.selectionModel()
        indexes = selection_model.selectedIndexes()
        if indexes:
            reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn chắc chắn muốn xóa?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row_numbers = sorted(set(index.row() for index in indexes))
                conn = connect_db()
                cursor = conn.cursor()
                for row_number in reversed(row_numbers):
                    if row_number < 0:
                        continue
                    # Lấy giá trị của cột MaDVT tại hàng được chọn
                    selected_index = self.table_model_QLNV.index(row_number, 1)
                    MaNV = selected_index.data()
                    # Xóa hàng trong tableView
                    self.table_model_QLNV.removeRow(row_number)
                    # Xóa mềm dữ liệu trong SQL Server
                    ThoiGianXoa = datetime.datetime.now()
                    cursor.execute(f"UPDATE Nhan_Vien SET XoaMem = 0, ThoiGianXoa = '{ThoiGianXoa}' WHERE MaNV  = '{MaNV}'")
                    conn.commit()
                cursor.close()
                conn.close()

    # Show Connect Button ----------------------------------------------------------------------------------------------|

    def show_enter_dvt(self):
        self.enter_dvt.show()

    def show_enter_ncc(self):
        self.enter_ncc.show()

    def show_enter_dshh(self):
        self.enter_dshh.show()

    def show_enter_ng(self):
        self.enter_bg.show()

    def show_enter_nv(self):
        self.enter_nv.show()

    def show_enter_login(self):
        self.enter_login.show()

    def show_enter_selectDH(self):
        self.enter_selectDH.show()

    def show_xacnhan(self):
        self.enter_xacnhan.show()


# Login ----------------------------------------------------------------------------------------------------------------|

class Login(QWidget):

    def Face_reg(self):
        dd = FaceRecognition()
        Chek = dd.run_recognition()
        if Chek:
            self.close()
            main_win = MainWindow()
            main_win.show()

    def show_enter_register(self):
        self.enter_register.show()

    def __init__(self):
        super(Login, self).__init__()
        self.cur = None
        self.conn = None
        self.ui = EnterLoginClass()
        self.ui.setupUi(self)
        self.enter_register = enterRegister()
        self.ui.LoginButton.clicked.connect(self.Handel_Login)
        self.ui.FaceIDButton.clicked.connect(self.Face_reg)
        self.ui.RegisterButton.clicked.connect(self.show_enter_register)

    def Handel_Login(self):
        self.conn = connect_db()
        self.cur = self.conn.cursor()

        admin_name = self.ui.LineUserName.text()
        admin_password = self.ui.LinePassword.text()

        sql = f"SELECT TenNguoiDung, MatKhau FROM users WHERE TenNguoiDung='{admin_name}' AND MatKhau='{admin_password}'"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        if len(data) > 0:
            self.close()
            main_win = MainWindow()
            main_win.show()
        else:
            self.ui.label.setText('Make Sure You Entered Correctly')


# Run file -------------------------------------------------------------------------------------------------------------|

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_win = Login()
    login_win.show()
    sys.exit(app.exec())
