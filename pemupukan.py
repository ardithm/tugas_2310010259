# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_tugas


class pemupukan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        filenya = QFile('pemupukan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formpupuk = muatfile.load(filenya, self)
        filenya.close()

        self.aksi = crud_tugas()

        self.isiPetani()
        self.isiTanaman()

        self.formpupuk.btnTambah.clicked.connect(self.simpanPemupukan)
        self.formpupuk.btnUbah.clicked.connect(self.ubahPemupukan)
        self.formpupuk.btnHapus.clicked.connect(self.hapusPemupukan)
        self.formpupuk.btnBatal.clicked.connect(self.batalPemupukan)

        self.formpupuk.tblPemupukan.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formpupuk.tblPemupukan.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formpupuk.tblPemupukan.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formpupuk.tblPemupukan.cellClicked.connect(self.pilihBaris)

        self.tampilPemupukan()

    def simpanPemupukan(self):
        idpupuk = self.formpupuk.editId.text()
        idpetani = self.formpupuk.CBPetani.currentData()
        idtanaman = self.formpupuk.CBTanaman.currentData()
        jenis = self.formpupuk.CBJenis.currentText()
        tanggal = self.formpupuk.DE_Tanggal.date().toString("yyyy-MM-dd")
        jumlah = self.formpupuk.SBJumlah.value()
        ket = self.formpupuk.editKet.toPlainText()

        if not idpupuk or not idpetani or not idtanaman or not jenis:
            QMessageBox.warning(self, "Peringatan", "Semua field wajib diisi!")
            return

        try:
            self.aksi.tambahPemupukan(idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket)
            QMessageBox.information(self, "Sukses", "Data pemupukan berhasil ditambahkan.")
            self.tampilPemupukan()
            self.batalPemupukan()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menambah data!\n{e}")

    def ubahPemupukan(self):
        idpupuk = self.formpupuk.editId.text()
        idpetani = self.formpupuk.CBPetani.currentData()
        idtanaman = self.formpupuk.CBTanaman.currentData()
        jenis = self.formpupuk.CBJenis.currentText()
        tanggal = self.formpupuk.DE_Tanggal.date().toString("yyyy-MM-dd")
        jumlah = self.formpupuk.SBJumlah.value()
        ket = self.formpupuk.editKet.toPlainText()

        if not idpupuk:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah!")
            return

        try:
            self.aksi.ubahPemupukan(idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket)
            QMessageBox.information(self, "Sukses", "Data pemupukan berhasil diubah.")
            self.tampilPemupukan()
            self.batalPemupukan()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal mengubah data!\n{e}")

    def hapusPemupukan(self):
        idpupuk = self.formpupuk.editId.text()
        if not idpupuk:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return

        try:
            self.aksi.hapusPemupukan(idpupuk)
            QMessageBox.information(self, "Sukses", "Data pemupukan berhasil dihapus.")
            self.tampilPemupukan()
            self.batalPemupukan()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menghapus data!\n{e}")


    def batalPemupukan(self):
        self.formpupuk.editId.clear()
        self.formpupuk.CBJenis.setCurrentIndex(-1)
        self.formpupuk.CBPetani.setCurrentIndex(-1)
        self.formpupuk.CBTanaman.setCurrentIndex(-1)
        self.formpupuk.DE_Tanggal.setDate(self.formpupuk.DE_Tanggal.minimumDate())
        self.formpupuk.SBJumlah.setValue(0)
        self.formpupuk.editKet.clear()
        self.formpupuk.editId.setFocus()

    def tampilPemupukan(self):
        hasil = self.aksi.tampilPemupukan()
        self.formpupuk.tblPemupukan.setRowCount(len(hasil))
        self.formpupuk.tblPemupukan.setColumnCount(7)
        self.formpupuk.tblPemupukan.setHorizontalHeaderLabels(
            ["ID Pemupukan", "Petani", "Tanaman", "Jenis Pupuk", "Tanggal", "Jumlah (kg)", "Keterangan"]
        )
        for baris, data in enumerate(hasil):
            for kolom, nilai in enumerate(data):
                self.formpupuk.tblPemupukan.setItem(baris, kolom, QTableWidgetItem(str(nilai)))

    def pilihBaris(self, row, column):
        idpupuk = self.formpupuk.tblPemupukan.item(row, 0).text()
        nama_petani = self.formpupuk.tblPemupukan.item(row, 1).text()
        nama_tanaman = self.formpupuk.tblPemupukan.item(row, 2).text()
        jenis = self.formpupuk.tblPemupukan.item(row, 3).text()
        tanggal = self.formpupuk.tblPemupukan.item(row, 4).text()
        jumlah = self.formpupuk.tblPemupukan.item(row, 5).text()
        ket = self.formpupuk.tblPemupukan.item(row, 6).text()

        self.formpupuk.editId.setText(idpupuk)
        self.formpupuk.CBJenis.setCurrentText(jenis)
        self.formpupuk.SBJumlah.setValue(int(float(jumlah)))
        self.formpupuk.editKet.setPlainText(ket)
        self.formpupuk.DE_Tanggal.setDate(self.formpupuk.DE_Tanggal.date().fromString(tanggal, "yyyy-MM-dd"))

        self.formpupuk.CBPetani.setCurrentText(nama_petani)
        self.formpupuk.CBTanaman.setCurrentText(nama_tanaman)

    def isiPetani(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_petani, nama_petani FROM petani")
        hasil = aksi.fetchall()
        self.formpupuk.CBPetani.clear()
        for idp, nama in hasil:
            self.formpupuk.CBPetani.addItem(nama, idp)
        aksi.close()

    def isiTanaman(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_tanaman, nama_tanaman FROM tanaman")
        hasil = aksi.fetchall()
        self.formpupuk.CBTanaman.clear()
        for idt, nama in hasil:
            self.formpupuk.CBTanaman.addItem(nama, idt)
        aksi.close()
