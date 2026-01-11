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

        self.isiPetani()

        self.formLahan.btnTambah.clicked.connect(self.simpanLahan)
        self.formLahan.btnUbah.clicked.connect(self.ubahLahan)
        self.formLahan.btnHapus.clicked.connect(self.hapusLahan)
        self.formLahan.btnBatal.clicked.connect(self.batalLahan)

        self.formLahan.lineCari.textChanged.connect(self.cariDataLahan)
        self.formLahan.btnCetak.clicked.connect(self.laporanLahan)

        self.formLahan.tblLahan.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formLahan.tblLahan.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formLahan.tblLahan.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formLahan.tblLahan.cellClicked.connect(self.pilihBaris)


        self.tampilLahan()

    def simpanLahan(self):
        if not self.formLahan.editId.text().strip():
            QMessageBox.information(None, "Informasi", "ID Lahan belum diisi")
            self.formLahan.editId.setFocus()
        elif self.formLahan.CBPetani.currentIndex() == -1:
            QMessageBox.information(None, "Informasi", "Petani belum dipilih")
            self.formLahan.CBPetani.setFocus()
        elif not self.formLahan.editLokasi.text().strip():
            QMessageBox.information(None, "Informasi", "Lokasi belum diisi")
            self.formLahan.editLokasi.setFocus()
        else:
            idlahan = self.formLahan.editId.text()
            idpetani = self.formLahan.CBPetani.currentData()
            lokasi = self.formLahan.editLokasi.text()
            luas = self.formLahan.SBLuas.value()
            jenis = self.formLahan.CBJenis.currentText()
            keterangan = self.formLahan.editKet.toPlainText()

            self.aksi.tambahLahan(idlahan, idpetani, lokasi, luas, jenis, keterangan)
            self.tampilLahan()
            self.batalLahan()

            QMessageBox.information(None, "Informasi", "Data lahan berhasil disimpan")


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

        QMessageBox.information(None, "Informasi", "Data lahan berhasil diubah")


    def hapusLahan(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            idlahan = self.formLahan.editId.text()
            self.aksi.hapusLahan(idlahan)
            self.tampilLahan()
            self.batalLahan()


    def batalLahan(self):
        self.formLahan.editId.clear()
        self.formLahan.editLokasi.clear()
        self.formLahan.SBLuas.setValue(0)
        self.formLahan.CBJenis.setCurrentIndex(0)
        self.formLahan.editKet.clear()
        self.formLahan.CBPetani.setCurrentIndex(0)
        self.formLahan.editId.setFocus()

    def tampilLahan(self):
        data = self.aksi.dataLahan()

        self.formLahan.tblLahan.setRowCount(0)
        self.formLahan.tblLahan.setColumnCount(6)
        self.formLahan.tblLahan.setHorizontalHeaderLabels(
            ["ID Lahan", "Petani", "Lokasi", "Luas", "Jenis Tanah", "Keterangan"]
        )

        for i, baris in enumerate(data):
            self.formLahan.tblLahan.insertRow(i)
            self.formLahan.tblLahan.setItem(i, 0, QTableWidgetItem(str(baris["id_lahan"])))
            self.formLahan.tblLahan.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formLahan.tblLahan.setItem(i, 2, QTableWidgetItem(str(baris["lokasi"])))
            self.formLahan.tblLahan.setItem(i, 3, QTableWidgetItem(str(baris["luas_lahan"])))
            self.formLahan.tblLahan.setItem(i, 4, QTableWidgetItem(str(baris["jenis_tanah"])))
            self.formLahan.tblLahan.setItem(i, 5, QTableWidgetItem(str(baris["keterangan"])))


    def pilihBaris(self, row, column):
        id_lahan = self.formLahan.tblLahan.item(row, 0).text()
        nama_petani = self.formLahan.tblLahan.item(row, 1).text()
        lokasi = self.formLahan.tblLahan.item(row, 2).text()
        luas = self.formLahan.tblLahan.item(row, 3).text()
        jenis = self.formLahan.tblLahan.item(row, 4).text()
        ket = self.formLahan.tblLahan.item(row, 5).text()

        self.formLahan.editId.setText(id_lahan)
        self.formLahan.editLokasi.setText(lokasi)
        self.formLahan.SBLuas.setValue(int(float(luas)))
        self.formLahan.CBJenis.setCurrentText(jenis)
        self.formLahan.editKet.setPlainText(ket)

        self.formLahan.CBPetani.setCurrentText(nama_petani)

    def cariDataLahan(self):
        varCari = self.formLahan.lineCari.text()
        self.formLahan.tblLahan.setRowCount(0)
        data = self.aksi.filterLahan(varCari)

        for i, baris in enumerate(data):
            self.formLahan.tblLahan.insertRow(i)
            self.formLahan.tblLahan.setItem(i, 0, QTableWidgetItem(str(baris["id_lahan"])))
            self.formLahan.tblLahan.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formLahan.tblLahan.setItem(i, 2, QTableWidgetItem(str(baris["lokasi"])))
            self.formLahan.tblLahan.setItem(i, 3, QTableWidgetItem(str(baris["luas_lahan"])))
            self.formLahan.tblLahan.setItem(i, 4, QTableWidgetItem(str(baris["jenis_tanah"])))
            self.formLahan.tblLahan.setItem(i, 5, QTableWidgetItem(str(baris["keterangan"])))

    def laporanLahan(self):
        filter = self.formLahan.comboFilter.currentText()

        if filter == "Semua":
            self.aksi.cetakLahan()
        else:
            self.aksi.cetakFilterLahan(filter)


    def isiPetani(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_petani, nama_petani FROM petani")
        hasil = aksi.fetchall()
        self.formLahan.CBPetani.clear()
        for idp, nama in hasil:
            self.formLahan.CBPetani.addItem(nama, idp)
        aksi.close()
