from Intern.Design.ui_functions import *
from ui_main import *
from Intern.Database.Connect_Database import connect_db


class MainWindow(QMainWindow):


    # -------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        QMainWindow.__init__(self)
        self.cursor = None
        self.table_model = None
        self.table = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ---------------------------------------------------------------------------------------------------------------------------------------------
        # TOGGLE/ MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btn_page_1.clicked.connect(
            lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.page_1), self.load_table_data()))

        # PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.Home_9.clicked.connect(lambda: self.ui.verticalStackedWidget_2.setCurrentWidget(self.ui.TT_DVT_Page))
        self.Display_DVT()
        # self.ui.Home_9.clicked.connect(lambda: self.load_table_data())
        self.ui.pushButton_9.clicked.connect(self.searchBar)
        # self.search()
        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    def Display_DVT(self):  # Xuất dữ liệu bảng Đơn vị tính
        # ---------------------------------------------------------------------------------------------------------------------------------------------
        self.table_model = QtGui.QStandardItemModel()
        self.cursor = connect_db().cursor()
        self.cursor.execute('SELECT STT, MaDVT, TenDVT, GhiChu, DaXoa FROM Don_Vi_Tinh ORDER BY STT')
        for row_number, row_data in enumerate(self.cursor):
            # Thêm một hàng mới vào bảng
            self.table_model.insertRow(row_number)
            # Thêm dữ liệu vào các cột
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model.setItem(row_number, column_number, item)

        # Truy vấn bảng Don_Vi_Tinh
        self.ui.tableView.setModel(self.table_model)
        self.table_model.setHorizontalHeaderLabels(['STT', 'MaDVT', 'TenDVT', 'GhiChu', 'DaXoa'])

        # Tự động thay đổi kích thước của các cột để phù hợp với dữ liệu
        self.ui.tableView.resizeColumnsToContents()

        # Lấy Header của bảng
        header = self.ui.tableView.horizontalHeader()

        # Đặt tất cả các cột có kích thước bằng nhau và bằng với độ rộng của bảng
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        # ---------------------------------------------------------------------------------------------------------------------------------------------

    def searchBar(self):  # Tìm kiếm dữ liệu bảng Đơn vị tính

        # # Lấy từ khóa tìm kiếm từ thanh tìm kiếm
        search_term = self.ui.lineEdit_2.text()
        # Truy vấn bảng Don_Vi_Tinh
        self.cursor.execute("SELECT STT, MaDVT, TenDVT, GhiChu, DaXoa FROM Don_Vi_Tinh WHERE MaDVT LIKE ?",
                            ('%' + search_term + '%',))

        # Thêm kết quả vào bảng của PyQT
        self.table_model.clear()
        self.table_model.setHorizontalHeaderLabels(['STT', 'MaDVT', 'TenDVT', 'GhiChu', 'DaXoa'])

        for row_number, row_data in enumerate(self.cursor):
            # Thêm một hàng mới vào bảng
            self.table_model.insertRow(row_number)
            # Thêm dữ liệu vào các cột
            for column_number, data in enumerate(row_data):
                item = QtGui.QStandardItem(str(data))
                self.table_model.setItem(row_number, column_number, item)

        # Tự động thay đổi kích thước của các cột để phù hợp với dữ liệu
        self.ui.tableView.resizeColumnsToContents()

        # Lấy Header của bảng
        header = self.ui.tableView.horizontalHeader()

        # Đặt tất cả các cột có kích thước bằng nhau và bằng với độ rộng của bảng
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        # ---------------------------------------------------------------------------------------------------------------------------------------------

    def load_table_data(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
