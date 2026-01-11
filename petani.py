# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
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

        self.formpetani.lineCari.textChanged.connect(self.cariDataPetani)
        self.formpetani.btnCetak.clicked.connect(self.laporanPetani)

        self.tampilPetani()
        self.formpetani.tblPetani.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formpetani.tblPetani.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formpetani.tblPetani.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formpetani.tblPetani.cellClicked.connect(self.pilihBaris)


    def simpanPetani(self):
        if not self.formpetani.editId.text().strip():
            QMessageBox.information(None, "Informasi", "ID Petani belum diisi")
            self.formpetani.editId.setFocus()
        elif not self.formpetani.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Petani belum diisi")
            self.formpetani.editNama.setFocus()
        elif not self.formpetani.editNo.text().strip():
            QMessageBox.information(None, "Informasi", "No HP belum diisi")
            self.formpetani.editNo.setFocus()
        else:
            id = self.formpetani.editId.text()
            nama = self.formpetani.editNama.text()
            alamat = self.formpetani.editAlamat.text()
            no_hp = self.formpetani.editNo.text()
            jenis_kelamin = self.formpetani.CBJk.currentText()
            umur = self.formpetani.SBUmur.value()

            self.aksi.tambahPetani(id, nama, alamat, no_hp, jenis_kelamin, umur)
            self.tampilPetani()
            self.batalPetani()

            QMessageBox.information(None, "Informasi", "Data petani berhasil disimpan")


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

        QMessageBox.information(None, "Informasi", "Data petani berhasil diubah")


    def hapusPetani(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            id = self.formpetani.editId.text()
            self.aksi.hapusPetani(id)
            self.tampilPetani()
            self.batalPetani()
        else:
            pass


    def batalPetani(self):
        self.formpetani.editId.clear()
        self.formpetani.editNama.clear()
        self.formpetani.editAlamat.clear()
        self.formpetani.editNo.clear()
        self.formpetani.CBJk.setCurrentIndex(-1)
        self.formpetani.SBUmur.setValue(0)
        self.formpetani.editNama.setFocus()


    def tampilPetani(self):
        self.formpetani.tblPetani.setRowCount(0)
        data = self.aksi.dataPetani()

        for i, baris in enumerate(data):
            self.formpetani.tblPetani.insertRow(i)
            self.formpetani.tblPetani.setItem(i, 0, QTableWidgetItem(str(baris["id_petani"])))
            self.formpetani.tblPetani.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formpetani.tblPetani.setItem(i, 2, QTableWidgetItem(str(baris["alamat"])))
            self.formpetani.tblPetani.setItem(i, 3, QTableWidgetItem(str(baris["no_hp"])))
            self.formpetani.tblPetani.setItem(i, 4, QTableWidgetItem(str(baris["jenis_kelamin"])))
            self.formpetani.tblPetani.setItem(i, 5, QTableWidgetItem(str(baris["umur"])))



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

    def cariDataPetani(self):
        varCari = self.formpetani.lineCari.text()
        self.formpetani.tblPetani.setRowCount(0)
        data = self.aksi.filterPetani(varCari)

        for i, baris in enumerate(data):
            self.formpetani.tblPetani.insertRow(i)
            self.formpetani.tblPetani.setItem(i, 0, QTableWidgetItem(str(baris["id_petani"])))
            self.formpetani.tblPetani.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formpetani.tblPetani.setItem(i, 2, QTableWidgetItem(str(baris["alamat"])))
            self.formpetani.tblPetani.setItem(i, 3, QTableWidgetItem(str(baris["no_hp"])))
            self.formpetani.tblPetani.setItem(i, 4, QTableWidgetItem(str(baris["jenis_kelamin"])))
            self.formpetani.tblPetani.setItem(i, 5, QTableWidgetItem(str(baris["umur"])))

    def laporanPetani(self):
        filter = self.formpetani.comboFilter.currentText()

        if filter == "Semua":
            self.aksi.cetakPetani()
        else:
            self.aksi.cetakFilterPetani(filter)




