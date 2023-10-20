import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Window_main import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

class Project(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_photo.clicked.connect(self.open_image)
        self.save_photo.clicked.connect(self.save_image)
        self.fname = ''
        self.flag_effect = False

    def open_image(self):
        fname_new = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                                'Картинка (*.jpg);')[0]
        if (self.fname == '' or self.fname != '') and fname_new != '':
            self.fname_const = fname_new
            self.fname = fname_new
            self.pixmap = QPixmap(fname_new)
            if self.pixmap.width() < 750 and self.pixmap.height() < 660:
                new = self.pixmap
            else:
                new = self.pixmap.scaled(750, 660, Qt.KeepAspectRatio)
            self.image.setPixmap(new)
    def save_image(self):
        if self.fname == '':
            self.error_message()
        elif not self.flag_effect:
            QMessageBox.critical(self, 'Ошибка сохранения', 'Выберите хотя бы один эффект', QMessageBox.Ok)
        else:
            saving = QFileDialog.getSaveFileName(self, 'Выбрать место сохранения', 'Картинка.jpg')
            self.pixmap.save(saving[0])
    def error_message(self):
        """Message by using effects without open image"""
        QMessageBox.critical(self, 'Ошибка', 'Необходимо открыть изображение', QMessageBox.Ok)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
