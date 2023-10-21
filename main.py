import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QInputDialog, QColorDialog, QMessageBox
from Window_main import Ui_MainWindow
from PIL import Image, ImageFilter

class Project(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_photo.clicked.connect(self.open_image)
        self.border.clicked.connect(self.set_border)
        self.save_photo.clicked.connect(self.save_image)
        self.negative.clicked.connect(self.creat_negative)
        self.cancell_action.clicked.connect(self.cancel_effects)
        self.collage.clicked.connect(self.preparation_effects)
        self.kvant.clicked.connect(self.preparation_effects)
        self.grid.clicked.connect(self.preparation_effects)
        self.refl.clicked.connect(self.reflection)
        self.bluring.clicked.connect(self.blur_photo)
        self.rotate.clicked.connect(self.preparation_effects)
        self.size_btn.clicked.connect(self.preparation_effects)
        self.rgb_btn.clicked.connect(self.rgb_set)
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
    def cancel_effects(self):
        if self.fname == '':
            self.error_message()
        else:
            self.pixmap = QPixmap(self.fname_const)
            if self.flag_effect:
                if self.pixmap.width() < 750 and self.pixmap.height() < 660:
                    new = self.pixmap
                else:
                    new = self.pixmap.scaled(750, 660, Qt.KeepAspectRatio)
                self.image.setPixmap(new)
                self.fname = self.fname_const
                self.flag_effect = False
    def set_border(self):
        try:
            if self.fname == '':
                self.error_message()
            else:
                self.im = Image.open(self.fname)
                self.pix = self.im.load()
                border_size = QInputDialog.getInt(self, 'Выбор толщины', "Выберите толщину рамки и ее цвет", 0, 1, 14,
                                                  1)
                color = QColorDialog().getColor(Qt.white, None, 'Выбор цвета рамки')
                r, g, b = color.getRgb()[0:3]

                self.creat_border(int(border_size[0]), (r, g, b))
                self.im.save('buffer/oc.jpg')
                self.set_image()
        except:
            QMessageBox.critical(self, 'Неизвестная ошибка', 'Ошибка!')



    def creat_border(self, thickness, color):
        """Creating border around image"""
        x, y = self.im.size
        for i in range(thickness):
            for j in range(y):
                self.pix[i, j] = color[0], color[1], color[2]
                self.pix[x - i - 1, y - j - 1] = color[0], color[1], color[2]
        for i in range(x):
            for j in range(thickness):
                self.pix[i, j] = color[0], color[1], color[2]
                self.pix[x - i - 1, y - j - 1] = color[0], color[1], color[2]

    def creat_negative(self):
        try:
            if self.fname == '':
                self.error_message()
            else:
                im = Image.open(self.fname)
                pix = im.load()
                mode = \
                    QInputDialog.getItem(self, 'Настройка', 'Выберите режим обработки',
                                         ('Черно-белое', 'Цветное', 'Нет изменений'), 2,
                                         False)[0]
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        r, g, b = pix[i, j]
                        if mode == 'Нет изменений':
                            break
                        elif mode == 'Черно-белое':
                            sr = (r + g + b) // 3
                            pix[i, j] = 255 - sr, 255 - sr, 255 - sr
                        else:
                            pix[i, j] = 255 - r, 255 - g, 255 - b
                im.save('buffer/oc.jpg')
                self.set_image()
        except:
            QMessageBox.critical(self, 'Неизвестная ошибка', 'Ошибка!')

    def delet(self):
        x, y = self.im.size
        im1 = Image.new('RGB', (x, y), (0, 0, 0))
        # pixel matrix pictures
        pict = im1.load()
        for i in range(0, x, 2):
            for j in range(0, y, 2):
                r, g, b = self.pix[i, j]
                pict[i, j] = r, g, b
        im1.save('buffer/oc.jpg')



    def reflection(self):

        try:
            if self.fname == '':
                self.error_message()
            else:
                im = Image.open(self.fname)
                pix = im.load()
                x, y = im.size
                mode = ('Отражение вверх', 'Отражение вправо', 'Нет изменений')
                parametrs = QInputDialog.getItem(self, 'Настройка', 'Выберите направление отражения',
                                                 mode, 2, False)[0]
                if parametrs == mode[2]:
                    pass
                elif parametrs == mode[0]:
                    for i in range(x):
                        for j in range(y // 2):
                            pix[i, j], pix[i, y - j - 1] = pix[i, y - 1 - j], pix[i, j]
                else:
                    for i in range(x // 2):
                        for j in range(y):
                            pix[i, j], pix[x - i - 1, j] = pix[x - 1 - i, j], pix[i, j]
                im.save('buffer/oc.jpg')
                self.set_image()
        except:
            QMessageBox.critical(self, 'Неизвестная ошибка', 'Ошибка!')

    def rgb_set(self):

        try:
            if self.fname == '':
                self.error_message()
            else:

                im = Image.open(self.fname)
                level_r = \
                    QInputDialog.getInt(self, 'Выбор уровня изменения',
                                        "Выберите уровень изменения для парметра R(red)", 0,
                                        0,
                                        255,
                                        1)[0]
                level_g = \
                    QInputDialog.getInt(self, 'Выбор уровня изменения',
                                        "Выберите уровень изменения для парметра G(green)",
                                        0,
                                        0,
                                        255,
                                        1)[0]
                level_b = \
                    QInputDialog.getInt(self, 'Выбор уровня изменения',
                                        "Выберите уровень изменения для парметра B(blue)",
                                        0, 0,
                                        255,
                                        1)[0]
                pix = im.load()
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        r, g, b = pix[i, j]
                        pix[i, j] = abs(r - int(level_r)) % 255, abs(g - int(level_g)) % 255, abs(
                            b - int(level_b)) % 255
                im.save('buffer/oc.jpg')
                self.set_image()

        except:
            QMessageBox.critical(self, 'Неизвестная fdnbjkbjошибка', 'Ошибка!')



    def blur_photo(self):
        """blur effect"""
        if self.fname == '':
            self.error_message()
        else:
            self.im = Image.open(self.fname)
            im2 = self.im.filter(ImageFilter.GaussianBlur(radius=5))
            im2.save('buffer/oc.jpg')
            self.set_image()


    def preparation_effects(self):
        """Setting effects without arguments"""
        try:
            if self.fname == '':
                self.error_message()
            else:
                self.im = Image.open(self.fname)
                self.pix = self.im.load()
                if self.sender().text() == 'Коллаж':
                    self.creat_collage()
                elif self.sender().text() == 'Сетка':
                    self.delet()
                elif self.sender().text() == 'Поворот':
                    im2 = self.im.transpose(Image.Transpose.ROTATE_90)
                    im2.save('buffer/oc.jpg')
                elif self.sender().text() == 'Размер':
                    # image width selection
                    size_inform1 = QInputDialog.getInt(self, 'Выбор размера изображения', "Выберите ширину",
                                                       self.im.size[0], 100, self.im.size[0] + 200,
                                                       1)
                    # image lenth selection
                    size_inform2 = QInputDialog.getInt(self, 'Выбор размера изображения', "Выберите длину",
                                                       self.im.size[1], 100, self.im.size[1] + 200,
                                                       1)
                    im2 = self.im.resize((size_inform1[0], size_inform2[0]))
                    im2.save('buffer/oc.jpg')
                else:
                    self.color_reduct()

                self.set_image()
        except:
            QMessageBox.critical(self, 'Неизвестная ошибка', 'Ошибка!')

    def creat_collage(self):
        """Creating collage by cutting image on 4 parts"""
        x, y = self.im.size
        im1 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
        im2 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
        im3 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
        im4 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
        pict1, pict2, pict3, pict4 = im1.load(), im2.load(), im3.load(), im4.load()
        for i in range(x // 2):
            for j in range(y // 2):
                r, g, b = self.pix[i, j]
                pict1[i, j] = r, g, b
        for i in range(x // 2, x):
            for j in range(y // 2):
                r, g, b = self.pix[i, j]
                pict2[i - 1 - x // 2, j] = r, g, b
        for i in range(x // 2):
            for j in range(y // 2, y):
                r, g, b = self.pix[i, j]
                pict3[i, j - y // 2 - 1] = r, g, b
        for i in range(x // 2, x):
            for j in range(y // 2, y):
                r, g, b = self.pix[i, j]
                pict4[i - 1 - x // 2, j - y // 2 - 1] = r, g, b
        self.im.paste(im4, (0, 0))
        self.im.paste(im1, (x // 2, y // 2))
        self.im.paste(im3, (x // 2, 0))
        self.im.paste(im2, (0, y // 2))
        self.im.save('buffer/oc.jpg')

    def color_reduct(self):
        """Reduction numbers of colors"""
        from math import log2, ceil
        x, y = self.im.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pix[i, j]
                if r != 0 and b != 0 and g != 0:
                    self.pix[i, j] = ceil(log2(r)) * 32, int(log2(g)) * 32, int(log2(b)) * 32
        self.im.save('buffer/oc.jpg')
    def set_image(self):
        """Setting image"""
        self.pixmap = QPixmap('buffer/oc.jpg')
        if self.pixmap.width() < 750 and self.pixmap.height() < 660:
            new = self.pixmap
        else:
            new = self.pixmap.scaled(750, 660, Qt.KeepAspectRatio)
        self.image.setPixmap(new)
        self.fname = 'buffer/oc.jpg'
        self.flag_effect = True

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
