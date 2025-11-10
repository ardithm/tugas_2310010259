# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_tugas


class lahan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        filenya = QFile('lahan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formLahan = muatfile.load(filenya, self)
        filenya.close()

        self.aksi = crud_tugas()

        self.formLahan.btnTambah.clicked.connect(self.simpanLahan)
        self.formLahan.btnUbah.clicked.connect(self.ubahLahan)
        self.formLahan.btnHapus.clicked.connect(self.hapusLahan)
        self.formLahan.btnBatal.clicked.connect(self.batalLahan)

        self.formLahan.tblLahan.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formLahan.tblLahan.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formLahan.tblLahan.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formLahan.tblLahan.cellClicked.connect(self.pilihBaris)

        self.isiPetani()
        self.tampilLahan()

    def simpanLahan(self):
        idlahan = self.formLahan.editId.text()
        idpetani = self.formLahan.CBPetani.currentData()
        lokasi = self.formLahan.editLokasi.text()
        luas = self.formLahan.SBLuas.value()
        jenis = self.formLahan.CBJenis.currentText()
        keterangan = self.formLahan.editKet.toPlainText()
        self.aksi.tambahLahan(idlahan, idpetani, lokasi, luas, jenis, keterangan)
        self.tampilLahan()
        self.batalLahan()

    def ubahLahan(self):
        idlahan = self.formLahan.editId.text()
        idpetani = self.formLahan.CBPetani.currentData()
        lokasi = self.formLahan.editLokasi.text()
        luas = self.formLahan.SBLuas.value()
        jenis = self.formLahan.CBJenis.currentText()
        keterangan = self.formLahan.editKet.toPlainText()
        self.aksi.ubahLahan(idlahan, idpetani, lokasi, luas, jenis, keterangan)
        self.tampilLahan()
        self.batalLahan()

    def hapusLahan(self):
        idlahan = self.formLahan.editId.text()
        self.aksi.hapusLahan(idlahan)
        self.tampilLahan()
        self.batalLahan()

    def isiPetani(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_petani, nama_petani FROM petani")
        hasil = aksi.fetchall()
        self.formLahan.CBPetani.clear()
        for idp, nama in hasil:
            self.formLahan.CBPetani.addItem(f"{idp} - {nama}", idp)
        aksi.close()

    def batalLahan(self):
        self.formLahan.editId.clear()
        self.formLahan.editLokasi.clear()
        self.formLahan.SBLuas.setValue(0)
        self.formLahan.CBJenis.setCurrentIndex(-1)
        self.formLahan.editKet.clear()
        self.formLahan.CBPetani.setCurrentIndex(-1)
        self.formLahan.editId.setFocus()

    def tampilLahan(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT * FROM lahan")
        hasil = aksi.fetchall()

        self.formLahan.tblLahan.setRowCount(len(hasil))
        self.formLahan.tblLahan.setColumnCount(6)
        self.formLahan.tblLahan.setHorizontalHeaderLabels(
            ["ID Lahan", "ID Petani", "Lokasi", "Luas", "Jenis Tanah", "Keterangan"]
        )

        for baris, data in enumerate(hasil):
            for kolom, nilai in enumerate(data):
                self.formLahan.tblLahan.setItem(baris, kolom, QTableWidgetItem(str(nilai)))
        aksi.close()

    def pilihBaris(self, row, column):
        id_lahan = self.formLahan.tblLahan.item(row, 0).text()
        id_petani = self.formLahan.tblLahan.item(row, 1).text()
        lokasi = self.formLahan.tblLahan.item(row, 2).text()
        luas = self.formLahan.tblLahan.item(row, 3).text()
        jenis = self.formLahan.tblLahan.item(row, 4).text()
        ket = self.formLahan.tblLahan.item(row, 5).text()

        self.formLahan.editId.setText(id_lahan)
        self.formLahan.editLokasi.setText(lokasi)
        self.formLahan.SBLuas.setValue(float(luas))
        self.formLahan.CBJenis.setCurrentText(jenis)
        self.formLahan.editKet.setPlainText(ket)

        for i in range(self.formLahan.CBPetani.count()):
            if str(self.formLahan.CBPetani.itemData(i)) == str(id_petani):
                self.formLahan.CBPetani.setCurrentIndex(i)
                break

