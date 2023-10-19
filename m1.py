import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Window_main import Ui_MainWindow




class Project(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Open window
        """
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
