# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader
from crud import crud_tugas


class panen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        filenya = QFile('panen.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formpanen = muatfile.load(filenya, self)
        filenya.close()

        self.formpanen.editTanggal.setDate(QDate.currentDate())
        self.aksi = crud_tugas()

        self.isiPetani()
        self.isiTanaman()

        self.formpanen.btnTambah.clicked.connect(self.simpanPanen)
        self.formpanen.btnUbah.clicked.connect(self.ubahPanen)
        self.formpanen.btnHapus.clicked.connect(self.hapusPanen)
        self.formpanen.btnBatal.clicked.connect(self.batalPanen)

        self.formpanen.lineCari.textChanged.connect(self.cariDataPanen)
        self.formpanen.btnCetak.clicked.connect(self.laporanPanen)

        self.formpanen.tblPanen.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formpanen.tblPanen.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formpanen.tblPanen.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formpanen.tblPanen.cellClicked.connect(self.pilihBaris)

        self.tampilPanen()


    def simpanPanen(self):
        if not self.formpanen.editId.text().strip():
            QMessageBox.information(None, "Informasi", "ID Panen belum diisi")
            self.formpanen.editId.setFocus()
        elif self.formpanen.CBPetani.currentIndex() == -1:
            QMessageBox.information(None, "Informasi", "Petani belum dipilih")
            self.formpanen.CBPetani.setFocus()
        elif self.formpanen.CBTanaman.currentIndex() == -1:
            QMessageBox.information(None, "Informasi", "Tanaman belum dipilih")
            self.formpanen.CBTanaman.setFocus()
        elif self.formpanen.CBKualitas.currentIndex() == -1:
            QMessageBox.information(None, "Informasi", "Kualitas belum dipilih")
            self.formpanen.CBKualitas.setFocus()
        else:
            idp = self.formpanen.editId.text()
            idpetani = self.formpanen.CBPetani.currentData()
            idtanaman = self.formpanen.CBTanaman.currentData()
            tgl = self.formpanen.editTanggal.date().toString("yyyy-MM-dd")
            hasil = self.formpanen.SBHasil.value()
            kualitas = self.formpanen.CBKualitas.currentText()
            ket = self.formpanen.editKet.toPlainText()

            self.aksi.tambahPanen(idp, idpetani, idtanaman, tgl, hasil, kualitas, ket)
            self.tampilPanen()
            self.batalPanen()

            QMessageBox.information(None, "Informasi", "Data panen berhasil disimpan")


    def ubahPanen(self):
        idp = self.formpanen.editId.text()
        idpetani = self.formpanen.CBPetani.currentData()
        idtanaman = self.formpanen.CBTanaman.currentData()
        tgl = self.formpanen.editTanggal.date().toString("yyyy-MM-dd")
        hasil = self.formpanen.SBHasil.value()
        kualitas = self.formpanen.CBKualitas.currentText()
        ket = self.formpanen.editKet.toPlainText()

        self.aksi.ubahPanen(idp, idpetani, idtanaman, tgl, hasil, kualitas, ket)
        self.tampilPanen()
        self.batalPanen()

        QMessageBox.information(None, "Informasi", "Data panen berhasil diubah")

    def hapusPanen(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            idp = self.formpanen.editId.text()
            self.aksi.hapusPanen(idp)
            self.tampilPanen()
            self.batalPanen()


    def batalPanen(self):
        self.formpanen.editId.clear()
        self.formpanen.CBPetani.setCurrentIndex(-1)
        self.formpanen.CBTanaman.setCurrentIndex(-1)
        self.formpanen.editTanggal.setDate(QDate.currentDate())
        self.formpanen.SBHasil.setValue(0)
        self.formpanen.CBKualitas.setCurrentIndex(-1)
        self.formpanen.editKet.clear()
        self.formpanen.editId.setFocus()


    def tampilPanen(self):
        data = self.aksi.dataPanen()

        self.formpanen.tblPanen.setRowCount(0)
        self.formpanen.tblPanen.setColumnCount(7)
        self.formpanen.tblPanen.setHorizontalHeaderLabels(
            ["ID Panen", "Petani", "Tanaman", "Tanggal", "Hasil", "Kualitas", "Keterangan"]
        )

        for i, baris in enumerate(data):
            self.formpanen.tblPanen.insertRow(i)
            self.formpanen.tblPanen.setItem(i, 0, QTableWidgetItem(str(baris["id_panen"])))
            self.formpanen.tblPanen.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formpanen.tblPanen.setItem(i, 2, QTableWidgetItem(str(baris["nama_tanaman"])))
            self.formpanen.tblPanen.setItem(i, 3, QTableWidgetItem(str(baris["tanggal_panen"])))
            self.formpanen.tblPanen.setItem(i, 4, QTableWidgetItem(str(baris["jumlah_hasil"])))
            self.formpanen.tblPanen.setItem(i, 5, QTableWidgetItem(str(baris["kualitas"])))
            self.formpanen.tblPanen.setItem(i, 6, QTableWidgetItem(str(baris["keterangan"])))



    def pilihBaris(self, row, column):
        idp = self.formpanen.tblPanen.item(row, 0).text()
        nama_petani = self.formpanen.tblPanen.item(row, 1).text()
        nama_tanaman = self.formpanen.tblPanen.item(row, 2).text()
        tgl = self.formpanen.tblPanen.item(row, 3).text()
        hasil = self.formpanen.tblPanen.item(row, 4).text()
        kualitas = self.formpanen.tblPanen.item(row, 5).text()
        ket = self.formpanen.tblPanen.item(row, 6).text()

        self.formpanen.editId.setText(idp)
        self.formpanen.SBHasil.setValue(int(float(hasil)))
        self.formpanen.CBKualitas.setCurrentText(kualitas)
        self.formpanen.editKet.setPlainText(ket)

        self.formpanen.editTanggal.setDate(
            self.formpanen.editTanggal.date().fromString(tgl, "yyyy-MM-dd")
        )

        self.formpanen.CBPetani.setCurrentText(nama_petani)
        self.formpanen.CBTanaman.setCurrentText(nama_tanaman)

    def cariDataPanen(self):
        varCari = self.formpanen.lineCari.text()
        self.formpanen.tblPanen.setRowCount(0)
        data = self.aksi.filterPanen(varCari)

        for i, baris in enumerate(data):
            self.formpanen.tblPanen.insertRow(i)
            self.formpanen.tblPanen.setItem(i, 0, QTableWidgetItem(str(baris["id_panen"])))
            self.formpanen.tblPanen.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formpanen.tblPanen.setItem(i, 2, QTableWidgetItem(str(baris["nama_tanaman"])))
            self.formpanen.tblPanen.setItem(i, 3, QTableWidgetItem(str(baris["tanggal_panen"])))
            self.formpanen.tblPanen.setItem(i, 4, QTableWidgetItem(str(baris["jumlah_hasil"])))
            self.formpanen.tblPanen.setItem(i, 5, QTableWidgetItem(str(baris["kualitas"])))
            self.formpanen.tblPanen.setItem(i, 6, QTableWidgetItem(str(baris["keterangan"])))

    def laporanPanen(self):
        filter = self.formpanen.comboFilter.currentText()

        if filter == "Semua":
            self.aksi.cetakPanen()
        else:
            self.aksi.cetakFilterPanen(filter)


    def isiPetani(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_petani, nama_petani FROM petani")
        hasil = aksi.fetchall()
        self.formpanen.CBPetani.clear()
        for idp, nama in hasil:
            self.formpanen.CBPetani.addItem(nama, idp)
        aksi.close()

    def isiTanaman(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_tanaman, nama_tanaman FROM tanaman")
        hasil = aksi.fetchall()
        self.formpanen.CBTanaman.clear()
        for idt, nama in hasil:
            self.formpanen.CBTanaman.addItem(nama, idt)
        aksi.close()

