import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class Welcome(QDialog):
    def __int__(self):
        self.window = QtWidgets.QMainWindow()
        super(Welcome, self).__int__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUI(os.path.join(ui_path, "welcome.ui" ), self)
        self.show()
        # uic.loadUi("welcome.ui", self)
        # uic.load("welcome.ui", self)
        # self.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Welcome()
    app.exec_()

if __name__ == "__main__":
    main()
# app = QApplication(sys.argv)
# welcome = Welcome()
# app.exec_()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(Welcome)
# widget.setFixedHeight(800)
# widget.setFixedWidth(1200)
# widget.show()
# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")
