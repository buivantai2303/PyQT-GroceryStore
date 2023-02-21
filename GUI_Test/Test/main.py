import sys
from PyQt5 import QtWidgets
from ui_main import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    # Create application object
    app = QtWidgets.QApplication(sys.argv)

    # Create main window object
    main_window = MainWindow()

    # Show main window
    main_window.show()

    # Execute application
    sys.exit(app.exec())
