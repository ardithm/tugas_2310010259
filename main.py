# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from petani import petani
from lahan import lahan
from tanaman import tanaman
from pemupukan import pemupukan
from panen import panen


class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('form.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())
        self.formutama.actionPETANI.triggered.connect(self.bukapetani)
        self.formutama.actionLAHAN.triggered.connect(self.bukalahan)
        self.formutama.actionTANAMAN.triggered.connect(self.bukatanaman)
        self.formutama.actionPEMUPUKAN.triggered.connect(self.bukapemupukan)
        self.formutama.actionPANEN.triggered.connect(self.bukapanen)

    def bukapetani(self):
            self.formpetani = petani()
            self.formpetani.show()

    def bukalahan(self):
            self.formlahan = lahan()
            self.formlahan.show()

    def bukatanaman(self):
            self.formtanaman = tanaman()
            self.formtanaman.show()

    def bukapemupukan(self):
            self.formpemupukan = pemupukan()
            self.formpemupukan.show()

    def bukapanen(self):
            self.formpanen = panen()
            self.formpanen.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
