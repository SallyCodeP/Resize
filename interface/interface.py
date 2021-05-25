
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

    def carregar(self):
        self.setObjectName("MainWindow")
        self.resize(312, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(172, 229, 255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.box_1 = QtWidgets.QFrame(self.centralwidget)
        self.box_1.setGeometry(QtCore.QRect(10, 10, 291, 61))
        self.box_1.setStyleSheet("#box_1{\n"
                                 "    background-color: rgb(148, 180, 255);\n"
                                 "    border-radius: 5px;\n"
                                 "    border: 1px solid;\n"
                                 "}")
        self.box_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_1.setObjectName("box_1")
        self.label = QtWidgets.QLabel(self.box_1)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.box_2 = QtWidgets.QFrame(self.centralwidget)
        self.box_2.setGeometry(QtCore.QRect(10, 80, 291, 211))
        self.box_2.setStyleSheet("#box_2{\n"
                                 "    background-color: rgb(148, 180, 255);\n"
                                 "    border-radius: 5px;\n"
                                 "    border: 1px solid;\n"
                                 "}")
        self.box_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_2.setObjectName("box_2")
        self.width_i = QtWidgets.QLineEdit(self.box_2)
        self.width_i.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.width_i.setStyleSheet("border-radius: 5px;\n"
                                   "background-color: rgb(190, 213, 255);\n"
                                   "border: 1px solid;\n"
                                   "border-color: black;")
        self.width_i.setAlignment(QtCore.Qt.AlignCenter)
        self.width_i.setObjectName("width_i")
        self.height_i = QtWidgets.QLineEdit(self.box_2)
        self.height_i.setGeometry(QtCore.QRect(190, 50, 71, 31))
        self.height_i.setStyleSheet("border-radius: 5px;\n"
                                    "background-color: rgb(190, 213, 255);\n"
                                    "border: 1px solid;\n"
                                    "border-color: black;")
        self.height_i.setAlignment(QtCore.Qt.AlignCenter)
        self.height_i.setObjectName("height_i")
        self.label_2 = QtWidgets.QLabel(self.box_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.box_2)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: none;")
        self.label_3.setObjectName("label_3")
        self.resize_b = QtWidgets.QPushButton(self.box_2)
        self.resize_b.setGeometry(QtCore.QRect(20, 160, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.resize_b.setFont(font)
        self.resize_b.setStyleSheet("background-color: rgb(80, 103, 255);\n"
                                    "border-radius: 5px;\n"
                                    "border: 1px solid;\n"
                                    "border-color: black;\n"
                                    "color: white;")
        self.resize_b.setObjectName("resize_b")
        self.New_name = QtWidgets.QLineEdit(self.box_2)
        self.New_name.setGeometry(QtCore.QRect(20, 100, 241, 41))
        self.New_name.setStyleSheet("border-radius: 5px;\n"
                                    "background-color: rgb(190, 213, 255);\n"
                                    "border: 1px solid;\n"
                                    "border-color: black;")
        self.New_name.setAlignment(QtCore.Qt.AlignCenter)
        self.New_name.setObjectName("New_name")
        self.open_foto = QtWidgets.QPushButton(self.box_2)
        self.open_foto.setGeometry(QtCore.QRect(100, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.open_foto.setFont(font)
        self.open_foto.setStyleSheet("background-color: rgb(80, 103, 255);\n"
                                     "border-radius: 5px;\n"
                                     "border: 1px solid;\n"
                                     "border-color: black;\n"
                                     "color: white;")
        self.open_foto.setObjectName("open_foto")
        self.setCentralWidget(self.centralwidget)

        self.retranslateui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Resize"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", "Height"))
        self.resize_b.setText(_translate("MainWindow", "Resize"))
        self.New_name.setText(_translate("MainWindow", "Novo nome"))
        self.open_foto.setText(_translate("MainWindow", "Abrir foto"))