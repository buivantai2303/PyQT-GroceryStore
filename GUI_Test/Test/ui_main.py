from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, QPropertyAnimation


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(600, 70, 91, 31))
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(600, 120, 91, 31))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(600, 170, 91, 31))
        self.btn_delete.setObjectName("btn_delete")
        self.lbl_order = QtWidgets.QLabel(self.centralwidget)
        self.lbl_order.setGeometry(QtCore.QRect(20, 220, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_order.setFont(font)
        self.lbl_order.setObjectName("lbl_order")
        self.table_order = QtWidgets.QTableWidget(self.centralwidget)
        self.table_order.setGeometry(QtCore.QRect(20, 260, 751, 251))
        self.table_order.setObjectName("table_order")
        self.table_order.setColumnCount(4)
        self.table_order.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(3, item)
        self.lbl_product = QtWidgets.QLabel(self.centralwidget)
        self.lbl_product.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_product.setFont(font)
        self.lbl_product.setObjectName("lbl_product")
        self.table_product = QtWidgets.QTableWidget(self.centralwidget)
        self.table_product.setGeometry(QtCore.QRect(20, 70, 551, 141))
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(4)
        self.table_product.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        self.label_animation = QtWidgets.QLabel(self.centralwidget)
        self.label_animation.setGeometry(QtCore.QRect(360, 520, 91, 51))
        self.label_animation.setStyleSheet("background-image:url(\"/path/to/animation.gif\")")
        self.label_animation.setText("")
        self.label_animation.setObjectName("label_animation")
        self.label_animation.show()
        self.animation = QPropertyAnimation(self.label_animation, b"pos")
        self.animation.setDuration(3000)
        self.animation.setStartValue(QPoint(0, 0))
        var = self.animation.setEnd
        # Add product button
        self.btn_add.setText("Add")
        self.btn_add.clicked.connect(self.add_product)

        # Edit product button
        self.btn_edit.setText("Edit")
        self.btn_edit.clicked.connect(self.edit_product)

        # Delete product button
        self.btn_delete.setText("Delete")
        self.btn_delete.clicked.connect(self.delete_product)

        # Order table
        self.table_order.setHorizontalHeaderLabels(["Product Name", "Quantity", "Price", "Total"])
        self.table_order.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Product table
        self.table_product.setHorizontalHeaderLabels(["ID", "Name", "Price", "Stock"])
        self.table_product.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Start animation
        self.animation.setEndValue(QPoint(360, 520))
        self.animation.setLoopCount(-1)
        self.animation.start()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.list_functions = QtWidgets.QListWidget(self.centralwidget)
        self.list_functions.setGeometry(QtCore.QRect(0, 0, 150, 500))
        self.list_functions.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.list_functions.setObjectName("list_functions")
        MainWindow.setCentralWidget(self.centralwidget)

        # Add items to list
        self.list_functions.addItem("Product")
        self.list_functions.addItem("Order")

        # Connect list item clicked signal to slot
        self.list_functions.itemClicked.connect(self.change_panel)

    def add_product(self):
        # Add new product to product table
        pass

    def edit_product(self):
        # Edit product in product table
        pass

    def delete_product(self):
        # Delete product from product table
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sales Management"))
        self.lbl_order.setText(_translate("MainWindow", "Order Information"))
        self.lbl_product.setText(_translate("MainWindow", "Product Information"))

    def change_panel(self, item):
        """
        Slot to handle list item clicked signal.
        """
        # Change to product panel
        if item.text() == "Product":
            self.stackedWidget.setCurrentIndex(0)

        # Change to order panel
        elif item.text() == "Order":
            self.stackedWidget.setCurrentIndex(1)