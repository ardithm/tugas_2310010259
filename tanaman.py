# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_tugas


class tanaman(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        filenya = QFile('tanaman.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formtanaman = muatfile.load(filenya, self)
        filenya.close()

        self.aksi = crud_tugas()

        self.formtanaman.btnTambah.clicked.connect(self.simpanTanaman)
        self.formtanaman.btnUbah.clicked.connect(self.ubahTanaman)
        self.formtanaman.btnHapus.clicked.connect(self.hapusTanaman)
        self.formtanaman.btnBatal.clicked.connect(self.batalTanaman)

        self.formtanaman.tblTanaman.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formtanaman.tblTanaman.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formtanaman.tblTanaman.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formtanaman.tblTanaman.cellClicked.connect(self.pilihBaris)

        self.tampilTanaman()

    def simpanTanaman(self):
        idt = self.formtanaman.editId.text()
        nama = self.formtanaman.editNama.text()
        jenis = self.formtanaman.CBJenis.currentText()
        masa = self.formtanaman.SBMasa.value()
        musim = self.formtanaman.CBMusim.currentText()
        ket = self.formtanaman.editKet.toPlainText()

        if not idt or not nama or not jenis:
            QMessageBox.warning(self, "Peringatan", "Semua field wajib diisi!")
            return

        try:
            self.aksi.tambahTanaman(idt, nama, jenis, masa, musim, ket)
            QMessageBox.information(self, "Sukses", "Data tanaman berhasil ditambahkan.")
            self.tampilTanaman()
            self.batalTanaman()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menambah data!\n{e}")

    def ubahTanaman(self):
        idt = self.formtanaman.editId.text()
        nama = self.formtanaman.editNama.text()
        jenis = self.formtanaman.CBJenis.currentText()
        masa = self.formtanaman.SBMasa.value()
        musim = self.formtanaman.CBMusim.currentText()
        ket = self.formtanaman.editKet.toPlainText()

        if not idt:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah!")
            return

        try:
            self.aksi.ubahTanaman(idt, nama, jenis, masa, musim, ket)
            QMessageBox.information(self, "Sukses", "Data tanaman berhasil diubah.")
            self.tampilTanaman()
            self.batalTanaman()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal mengubah data!\n{e}")

    def hapusTanaman(self):
        idt = self.formtanaman.editId.text()
        if not idt:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return

        try:
            self.aksi.hapusTanaman(idt)
            QMessageBox.information(self, "Sukses", "Data tanaman berhasil dihapus.")
            self.tampilTanaman()
            self.batalTanaman()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menghapus data!\n{e}")

    def batalTanaman(self):
        self.formtanaman.editId.clear()
        self.formtanaman.editNama.clear()
        self.formtanaman.CBJenis.setCurrentIndex(-1)
        self.formtanaman.SBMasa.setValue(0)
        self.formtanaman.CBMusim.setCurrentIndex(-1)
        self.formtanaman.editKet.clear()
        self.formtanaman.editNama.setFocus()

    def tampilTanaman(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT * FROM tanaman")
        hasil = aksi.fetchall()

        self.formtanaman.tblTanaman.setRowCount(len(hasil))
        self.formtanaman.tblTanaman.setColumnCount(6)
        self.formtanaman.tblTanaman.setHorizontalHeaderLabels(
            ["ID Tanaman", "Nama Tanaman", "Jenis Tanaman", "Masa Tanam", "Musim Tanam", "Keterangan"]
        )

        for baris, data in enumerate(hasil):
            for kolom, nilai in enumerate(data):
                self.formtanaman.tblTanaman.setItem(baris, kolom, QTableWidgetItem(str(nilai)))
        aksi.close()

    def pilihBaris(self, row, column):
        idt = self.formtanaman.tblTanaman.item(row, 0).text()
        nama = self.formtanaman.tblTanaman.item(row, 1).text()
        jenis = self.formtanaman.tblTanaman.item(row, 2).text()
        masa = self.formtanaman.tblTanaman.item(row, 3).text()
        musim = self.formtanaman.tblTanaman.item(row, 4).text()
        ket = self.formtanaman.tblTanaman.item(row, 5).text()

        self.formtanaman.editId.setText(idt)
        self.formtanaman.editNama.setText(nama)
        self.formtanaman.CBJenis.setCurrentText(jenis)
        self.formtanaman.SBMasa.setValue(int(masa))
        self.formtanaman.CBMusim.setCurrentText(musim)
        self.formtanaman.editKet.setPlainText(ket)
