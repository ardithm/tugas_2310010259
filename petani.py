# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_tugas


class petani(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        filenya = QFile('petani.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formpetani = muatfile.load(filenya,self)
        self.aksi = crud_tugas()

        self.formpetani.btnTambah.clicked.connect(self.simpanPetani)
        self.formpetani.btnUbah.clicked.connect(self.ubahPetani)
        self.formpetani.btnHapus.clicked.connect(self.hapusPetani)
        self.formpetani.btnBatal.clicked.connect(self.batalPetani)

        self.tampilPetani()
        self.formpetani.tblPetani.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formpetani.tblPetani.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formpetani.tblPetani.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formpetani.tblPetani.cellClicked.connect(self.pilihBaris)


    def simpanPetani(self):
        id = self.formpetani.editId.text()
        nama = self.formpetani.editNama.text()
        alamat = self.formpetani.editAlamat.text()
        no_hp = self.formpetani.editNo.text()
        jenis_kelamin = self.formpetani.CBJk.currentText()
        umur = self.formpetani.SBUmur.value()
        self.aksi.tambahPetani(id, nama, alamat, no_hp, jenis_kelamin, umur)
        self.tampilPetani()
        self.batalPetani()

    def ubahPetani(self):
        id = self.formpetani.editId.text()
        nama = self.formpetani.editNama.text()
        alamat = self.formpetani.editAlamat.text()
        no_hp = self.formpetani.editNo.text()
        jenis_kelamin = self.formpetani.CBJk.currentText()
        umur = self.formpetani.SBUmur.value()
        self.aksi.ubahPetani(id, nama, alamat, no_hp, jenis_kelamin, umur)
        self.tampilPetani()
        self.batalPetani()

    def hapusPetani(self):
        id = self.formpetani.editId.text()
        self.aksi.hapusPetani(id,)
        self.tampilPetani()
        self.batalPetani()


    def batalPetani(self):
        self.formpetani.editId.clear()
        self.formpetani.editNama.clear()
        self.formpetani.editAlamat.clear()
        self.formpetani.editNo.clear()
        self.formpetani.CBJk.setCurrentIndex(-1)
        self.formpetani.SBUmur.setValue(0)
        self.formpetani.editNama.setFocus()


    def tampilPetani(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT * FROM petani")
        hasil = aksi.fetchall()

        self.formpetani.tblPetani.setRowCount(len(hasil))
        self.formpetani.tblPetani.setColumnCount(6)
        self.formpetani.tblPetani.setHorizontalHeaderLabels(["ID", "Nama", "Alamat", "No HP", "Jenis Kelamin", "Umur"])

        for baris, data in enumerate(hasil):
            for kolom, nilai in enumerate(data):
                self.formpetani.tblPetani.setItem(baris, kolom, QTableWidgetItem(str(nilai)))

        aksi.close()

    def pilihBaris(self, row, column):
        id_petani = self.formpetani.tblPetani.item(row, 0).text()
        nama = self.formpetani.tblPetani.item(row, 1).text()
        alamat = self.formpetani.tblPetani.item(row, 2).text()
        no_hp = self.formpetani.tblPetani.item(row, 3).text()
        jk = self.formpetani.tblPetani.item(row, 4).text()
        umur = self.formpetani.tblPetani.item(row, 5).text()

        self.formpetani.editId.setText(id_petani)
        self.formpetani.editNama.setText(nama)
        self.formpetani.editAlamat.setText(alamat)
        self.formpetani.editNo.setText(no_hp)
        self.formpetani.CBJk.setCurrentText(jk)
        self.formpetani.SBUmur.setValue(int(umur))

