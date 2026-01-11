# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QFile, QDate
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

        self.formpupuk.DE_Tanggal.setDate(QDate.currentDate())
        self.aksi = crud_tugas()

        self.isiPetani()
        self.isiTanaman()

        self.formpupuk.btnTambah.clicked.connect(self.simpanPemupukan)
        self.formpupuk.btnUbah.clicked.connect(self.ubahPemupukan)
        self.formpupuk.btnHapus.clicked.connect(self.hapusPemupukan)
        self.formpupuk.btnBatal.clicked.connect(self.batalPemupukan)

        self.formpupuk.lineCari.textChanged.connect(self.cariDataPemupukan)
        self.formpupuk.btnCetak.clicked.connect(self.laporanPemupukan)

        self.formpupuk.tblPemupukan.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formpupuk.tblPemupukan.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.formpupuk.tblPemupukan.setSelectionMode(QAbstractItemView.SingleSelection)
        self.formpupuk.tblPemupukan.cellClicked.connect(self.pilihBaris)

        self.tampilPemupukan()


    def simpanPemupukan(self):
        if not self.formpupuk.editId.text().strip():
            QMessageBox.information(None, "Informasi", "ID Pemupukan belum diisi")
            self.formpupuk.editId.setFocus()
        elif self.formpupuk.CBPetani.currentIndex() == -1:
            QMessageBox.information(None, "Informasi", "Petani belum dipilih")
            self.formpupuk.CBPetani.setFocus()
        elif self.formpupuk.CBTanaman.currentIndex() == -1:
            QMessageBox.information(None, "Informasi", "Tanaman belum dipilih")
            self.formpupuk.CBTanaman.setFocus()
        elif not self.formpupuk.CBJenis.currentText():
            QMessageBox.information(None, "Informasi", "Jenis pupuk belum dipilih")
            self.formpupuk.CBJenis.setFocus()
        else:
            idpupuk = self.formpupuk.editId.text()
            idpetani = self.formpupuk.CBPetani.currentData()
            idtanaman = self.formpupuk.CBTanaman.currentData()
            jenis = self.formpupuk.CBJenis.currentText()
            tanggal = self.formpupuk.DE_Tanggal.date().toString("yyyy-MM-dd")
            jumlah = self.formpupuk.SBJumlah.value()
            ket = self.formpupuk.editKet.toPlainText()

            self.aksi.tambahPemupukan(idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket)
            self.tampilPemupukan()
            self.batalPemupukan()

            QMessageBox.information(None, "Informasi", "Data pemupukan berhasil disimpan")


    def ubahPemupukan(self):
        idpupuk = self.formpupuk.editId.text()
        idpetani = self.formpupuk.CBPetani.currentData()
        idtanaman = self.formpupuk.CBTanaman.currentData()
        jenis = self.formpupuk.CBJenis.currentText()
        tanggal = self.formpupuk.DE_Tanggal.date().toString("yyyy-MM-dd")
        jumlah = self.formpupuk.SBJumlah.value()
        ket = self.formpupuk.editKet.toPlainText()

        self.aksi.ubahPemupukan(idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket)
        self.tampilPemupukan()
        self.batalPemupukan()

        QMessageBox.information(None, "Informasi", "Data pemupukan berhasil diubah")


    def hapusPemupukan(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            idpupuk = self.formpupuk.editId.text()
            self.aksi.hapusPemupukan(idpupuk)
            self.tampilPemupukan()
            self.batalPemupukan()

    def batalPemupukan(self):
        self.formpupuk.editId.clear()
        self.formpupuk.CBJenis.setCurrentIndex(0)
        self.formpupuk.CBPetani.setCurrentIndex(0)
        self.formpupuk.CBTanaman.setCurrentIndex(0)
        self.formpupuk.DE_Tanggal.setDate(QDate.currentDate())
        self.formpupuk.SBJumlah.setValue(0)
        self.formpupuk.editKet.clear()
        self.formpupuk.editId.setFocus()


    def tampilPemupukan(self):
        data = self.aksi.dataPemupukan()

        self.formpupuk.tblPemupukan.setRowCount(0)
        self.formpupuk.tblPemupukan.setColumnCount(7)
        self.formpupuk.tblPemupukan.setHorizontalHeaderLabels(
            ["ID Pemupukan", "Petani", "Tanaman", "Jenis Pupuk", "Tanggal", "Jumlah (kg)", "Keterangan"]
        )

        for i, baris in enumerate(data):
            self.formpupuk.tblPemupukan.insertRow(i)
            self.formpupuk.tblPemupukan.setItem(i, 0, QTableWidgetItem(str(baris["id_pemupukan"])))
            self.formpupuk.tblPemupukan.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formpupuk.tblPemupukan.setItem(i, 2, QTableWidgetItem(str(baris["nama_tanaman"])))
            self.formpupuk.tblPemupukan.setItem(i, 3, QTableWidgetItem(str(baris["jenis_pupuk"])))
            self.formpupuk.tblPemupukan.setItem(i, 4, QTableWidgetItem(str(baris["tanggal_pupuk"])))
            self.formpupuk.tblPemupukan.setItem(i, 5, QTableWidgetItem(str(baris["jumlah_kg"])))
            self.formpupuk.tblPemupukan.setItem(i, 6, QTableWidgetItem(str(baris["keterangan"])))


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

    def cariDataPemupukan(self):
        varCari = self.formpupuk.lineCari.text()
        self.formpupuk.tblPemupukan.setRowCount(0)
        data = self.aksi.filterPemupukan(varCari)

        for i, baris in enumerate(data):
            self.formpupuk.tblPemupukan.insertRow(i)
            self.formpupuk.tblPemupukan.setItem(i, 0, QTableWidgetItem(str(baris["id_pemupukan"])))
            self.formpupuk.tblPemupukan.setItem(i, 1, QTableWidgetItem(str(baris["nama_petani"])))
            self.formpupuk.tblPemupukan.setItem(i, 2, QTableWidgetItem(str(baris["nama_tanaman"])))
            self.formpupuk.tblPemupukan.setItem(i, 3, QTableWidgetItem(str(baris["jenis_pupuk"])))
            self.formpupuk.tblPemupukan.setItem(i, 4, QTableWidgetItem(str(baris["tanggal_pupuk"])))
            self.formpupuk.tblPemupukan.setItem(i, 5, QTableWidgetItem(str(baris["jumlah_kg"])))
            self.formpupuk.tblPemupukan.setItem(i, 6, QTableWidgetItem(str(baris["keterangan"])))

    def laporanPemupukan(self):
        filter = self.formpupuk.comboFilter.currentText()

        if filter == "Semua":
            self.aksi.cetakPemupukan()
        else:
            self.aksi.cetakFilterPemupukan(filter)


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
