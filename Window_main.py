# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 882)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QPushButton {\n"
"            background: #f5edff;\n"
"font-style:italic}\n"
"            QMainWindow {\n"
"            background-color:#cecece;}\n"
"  ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(330, 20, 750, 660))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.image.setFont(font)
        self.image.setStyleSheet("background-color:#958da3;\n"
"color:white")
        self.image.setFrameShape(QtWidgets.QFrame.Box)
        self.image.setObjectName("image")
        self.open_photo = QtWidgets.QPushButton(self.centralwidget)
        self.open_photo.setGeometry(QtCore.QRect(860, 710, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.open_photo.setFont(font)
        self.open_photo.setObjectName("open_photo")
        self.cancell_action = QtWidgets.QPushButton(self.centralwidget)
        self.cancell_action.setGeometry(QtCore.QRect(340, 710, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.cancell_action.setFont(font)
        self.cancell_action.setObjectName("cancell_action")
        self.border = QtWidgets.QPushButton(self.centralwidget)
        self.border.setGeometry(QtCore.QRect(30, 70, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.border.setFont(font)
        self.border.setStyleSheet("")
        self.border.setObjectName("border")
        self.save_photo = QtWidgets.QPushButton(self.centralwidget)
        self.save_photo.setGeometry(QtCore.QRect(600, 710, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.save_photo.setFont(font)
        self.save_photo.setObjectName("save_photo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#958da3")
        self.label.setObjectName("label")
        self.collage = QtWidgets.QPushButton(self.centralwidget)
        self.collage.setGeometry(QtCore.QRect(140, 70, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.collage.setFont(font)
        self.collage.setObjectName("collage")
        self.negative = QtWidgets.QPushButton(self.centralwidget)
        self.negative.setGeometry(QtCore.QRect(30, 170, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.negative.setFont(font)
        self.negative.setObjectName("negative")
        self.kvant = QtWidgets.QPushButton(self.centralwidget)
        self.kvant.setGeometry(QtCore.QRect(140, 170, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.kvant.setFont(font)
        self.kvant.setObjectName("kvant")
        self.grid = QtWidgets.QPushButton(self.centralwidget)
        self.grid.setGeometry(QtCore.QRect(30, 270, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.grid.setFont(font)
        self.grid.setObjectName("grid")
        self.refl = QtWidgets.QPushButton(self.centralwidget)
        self.refl.setGeometry(QtCore.QRect(140, 270, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.refl.setFont(font)
        self.refl.setObjectName("refl")
        self.rotate = QtWidgets.QPushButton(self.centralwidget)
        self.rotate.setGeometry(QtCore.QRect(30, 370, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.rotate.setFont(font)
        self.rotate.setObjectName("rotate")
        self.size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.size_btn.setGeometry(QtCore.QRect(140, 370, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.size_btn.setFont(font)
        self.size_btn.setObjectName("size_btn")
        self.rgb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rgb_btn.setGeometry(QtCore.QRect(30, 460, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.rgb_btn.setFont(font)
        self.rgb_btn.setObjectName("rgb_btn")
        self.bluring = QtWidgets.QPushButton(self.centralwidget)
        self.bluring.setGeometry(QtCore.QRect(140, 460, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.bluring.setFont(font)
        self.bluring.setObjectName("bluring")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image.setText(_translate("MainWindow", "     Изображение отсутсвует"))
        self.open_photo.setText(_translate("MainWindow", "Открыть изображение"))
        self.cancell_action.setText(_translate("MainWindow", "Отмена изменений"))
        self.border.setText(_translate("MainWindow", "Рамка"))
        self.save_photo.setText(_translate("MainWindow", "Сохранить изменения"))
        self.label.setText(_translate("MainWindow", "Доступные эффекты"))
        self.collage.setText(_translate("MainWindow", "Коллаж"))
        self.negative.setText(_translate("MainWindow", "Негатив"))
        self.kvant.setText(_translate("MainWindow", "Квантизация"))
        self.grid.setText(_translate("MainWindow", "Сетка"))
        self.refl.setText(_translate("MainWindow", "Отражение"))
        self.rotate.setText(_translate("MainWindow", "Поворот"))
        self.size_btn.setText(_translate("MainWindow", "Размер"))
        self.rgb_btn.setText(_translate("MainWindow", "RGB"))
        self.bluring.setText(_translate("MainWindow", "Размытие"))
