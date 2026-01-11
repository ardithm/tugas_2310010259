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

        self.formtanaman.lineCari.textChanged.connect(self.cariDataTanaman)
        self.formtanaman.btnCetak.clicked.connect(self.laporanTanaman)

        self.formtanaman.tblTanaman.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formtanaman.tblTanaman.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formtanaman.tblTanaman.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formtanaman.tblTanaman.cellClicked.connect(self.pilihBaris)

        self.tampilTanaman()

    def simpanTanaman(self):
        if not self.formtanaman.editId.text().strip():
            QMessageBox.information(None, "Informasi", "ID Tanaman belum diisi")
            self.formtanaman.editId.setFocus()
        elif not self.formtanaman.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Tanaman belum diisi")
            self.formtanaman.editNama.setFocus()
        else:
            idt = self.formtanaman.editId.text()
            nama = self.formtanaman.editNama.text()
            jenis = self.formtanaman.CBJenis.currentText()
            masa = self.formtanaman.SBMasa.value()
            musim = self.formtanaman.CBMusim.currentText()
            ket = self.formtanaman.editKet.toPlainText()

            self.aksi.tambahTanaman(idt, nama, jenis, masa, musim, ket)
            self.tampilTanaman()
            self.batalTanaman()

            QMessageBox.information(None, "Informasi", "Data tanaman berhasil disimpan")


    def ubahTanaman(self):
        idt = self.formtanaman.editId.text()
        nama = self.formtanaman.editNama.text()
        jenis = self.formtanaman.CBJenis.currentText()
        masa = self.formtanaman.SBMasa.value()
        musim = self.formtanaman.CBMusim.currentText()
        ket = self.formtanaman.editKet.toPlainText()

        self.aksi.ubahTanaman(idt, nama, jenis, masa, musim, ket)
        self.tampilTanaman()
        self.batalTanaman()

        QMessageBox.information(None, "Informasi", "Data tanaman berhasil diubah")


    def hapusTanaman(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            idt = self.formtanaman.editId.text()
            self.aksi.hapusTanaman(idt)
            self.tampilTanaman()
            self.batalTanaman()
        else:
            pass

    def batalTanaman(self):
        self.formtanaman.editId.clear()
        self.formtanaman.editNama.clear()
        self.formtanaman.CBJenis.setCurrentIndex(-1)
        self.formtanaman.SBMasa.setValue(0)
        self.formtanaman.CBMusim.setCurrentIndex(-1)
        self.formtanaman.editKet.clear()
        self.formtanaman.editNama.setFocus()


    def tampilTanaman(self):
        self.formtanaman.tblTanaman.setRowCount(0)
        data = self.aksi.dataTanaman()

        for i, baris in enumerate(data):
            self.formtanaman.tblTanaman.insertRow(i)
            self.formtanaman.tblTanaman.setItem(i, 0, QTableWidgetItem(str(baris["id_tanaman"])))
            self.formtanaman.tblTanaman.setItem(i, 1, QTableWidgetItem(str(baris["nama_tanaman"])))
            self.formtanaman.tblTanaman.setItem(i, 2, QTableWidgetItem(str(baris["jenis_tanaman"])))
            self.formtanaman.tblTanaman.setItem(i, 3, QTableWidgetItem(str(baris["masa_tanam"])))
            self.formtanaman.tblTanaman.setItem(i, 4, QTableWidgetItem(str(baris["musim_tanam"])))
            self.formtanaman.tblTanaman.setItem(i, 5, QTableWidgetItem(str(baris["keterangan"])))


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


    def cariDataTanaman(self):
        varCari = self.formtanaman.lineCari.text()
        self.formtanaman.tblTanaman.setRowCount(0)
        data = self.aksi.filterTanaman(varCari)

        for i, baris in enumerate(data):
            self.formtanaman.tblTanaman.insertRow(i)
            self.formtanaman.tblTanaman.setItem(i, 0, QTableWidgetItem(str(baris["id_tanaman"])))
            self.formtanaman.tblTanaman.setItem(i, 1, QTableWidgetItem(str(baris["nama_tanaman"])))
            self.formtanaman.tblTanaman.setItem(i, 2, QTableWidgetItem(str(baris["jenis_tanaman"])))
            self.formtanaman.tblTanaman.setItem(i, 3, QTableWidgetItem(str(baris["masa_tanam"])))
            self.formtanaman.tblTanaman.setItem(i, 4, QTableWidgetItem(str(baris["musim_tanam"])))
            self.formtanaman.tblTanaman.setItem(i, 5, QTableWidgetItem(str(baris["keterangan"])))

    def laporanTanaman(self):
        filter = self.formtanaman.comboFilter.currentText()

        if filter == "Semua":
            self.aksi.cetakTanaman()
        else:
            self.aksi.cetakFilterTanaman(filter)
