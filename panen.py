# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class panen(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('panen.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formpanen = muatfile.load(filenya,self)
