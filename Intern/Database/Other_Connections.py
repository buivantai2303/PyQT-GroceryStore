import pyodbc
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor

# Kết nối tới database SQL Server
server = 'BANHMIBIETBAY\SQLEXPRESS'
database = 'Sales_Manager'
username = 'sa'
password = '180403'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Tạo bảng PyQT và thiết lập thuộc tính
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Danh sách đơn vị tính")
        self.setGeometry(100, 100, 800, 600)

        # Tạo table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)

        # Thiết lập header cho table widget
        self.tableWidget.setHorizontalHeaderLabels(['STT', 'Mã đơn vị tính', 'Tên đơn vị tính', 'Ghi chú'])

        # Lấy dữ liệu từ SQL Server và hiển thị lên table widget
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Don_Vi_Tinh")
        rows = cursor.fetchall()
        for row_number, row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        # Thiết lập màu nền cho table widget
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                self.tableWidget.item(row, column).setBackground(QColor(225, 225, 225))

        # Thiết lập table widget là widget chính của main window
        self.setCentralWidget(self.tableWidget)

# Chạy chương trình
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
