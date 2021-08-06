from time import sleep
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import sys
from Resize.interface import interface
from threading import Thread
from cv2 import imwrite, imread, resize, INTER_AREA
from pyautogui import alert


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

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Localiza o endereço da foto e retorna suas informações uint-8
    def pegar_imagem(self):
        try:
            file_local = QtWidgets.QFileDialog.getOpenFileUrl()[0].url().split("/")
            file_local.remove('file:')
            for _ in range(0, file_local.count('')):
                file_local.remove('')
            self.image = imread("\\".join(file_local))
            self.pode = True

        except Exception:
            self.pode = False
            alert("Erro!")

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Captura os inputs dos valores na interface grafica e realiza o resize da foto
    # Ultiliza a foto capturadas pela função pegar "imagem"
    def resize_image(self):
        if self.pode:
            height = self.height_i.text()
            width = self.width_i.text()
            new = self.New_name.text()
            try:
                if len(new) > 0:
                    height = int(height)
                    width = int(width)
                    self.pode2 = True
                    if self.pode2:
                        imwrite(f"{new}.png", resize(self.image, (width, height), interpolation=INTER_AREA))
                        self.close()

                else:
                    self.erro()
            except Exception:
                print("Errado")
                self.erro()
        else:
            self.erro()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Executar em Thread a função resize imagem
    def resize_imagem_conect(self):
        Thread(target=self.resize_image).start()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def erro(self):
        self.label.setText("Erro!")
        sleep(3)
        self.label.setText("Resize!")
        self.pode2 = False

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Applica()
    win.show()
    sys.exit(app.exec_())
