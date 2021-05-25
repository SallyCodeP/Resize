from time import sleep
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import sys
from Resize.interface import interface
from threading import Thread
from PIL import Image


class Applica(interface.Interface):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resize")
        self.setFixedSize(312, 300)
        self.carregar()
        self.pode = False
        self.pode2 = False
        self.open_foto.clicked.connect(self.pegar_imagem)
        self.resize_b.clicked.connect(self.resize_imagem_conect)

        
    def erro(self):
        self.label.setText("Erro!")
        sleep(3)
        self.label.setText("Resize!")
        self.pode2 = False

    def resize_image(self):
        if self.pode == True:
            height = self.height_i.text()
            width = self.width_i.text()
            new = self.New_name.text()
            try:
                if len(new) <= 0:
                    self.erro()
                else:
                    height = int(height)
                    width = int(width)
                    self.pode2 = True
                    if self.pode2:
                        self.img = self.img.resize((width, height), Image.ANTIALIAS)
                        self.img.save(f'{new}.png')
                        self.close()
            except Exception:
                self.erro()
        else:
            self.erro()

    def pegar_imagem(self):
        try:
            abc = QtWidgets.QFileDialog.getOpenFileUrl()[0].url().split("/")
            abc.remove('file:')
        except Exception:
            self.pode = False
            print("Erro!")

        try:
            for _ in range(0, abc.count('')):
                abc.remove('')
            abc = "\\".join(abc)
            self.img = Image.open(abc)
            print(abc)
            self.pode = True
        except Exception:
            self.pode = False

    def resize_imagem_conect(self):
        Thread(target=self.resize_image).start()


def carregar_interface():
    app = QApplication(sys.argv)
    win = Applica()
    win.show()
    sys.exit(app.exec_())


carregar_interface()
