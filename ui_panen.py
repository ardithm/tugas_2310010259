# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1249, 640)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 110, 471, 337))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPanenLabel = QLabel(self.formLayoutWidget)
        self.iDPanenLabel.setObjectName(u"iDPanenLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPanenLabel)

        self.editId = QLineEdit(self.formLayoutWidget)
        self.editId.setObjectName(u"editId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editId)

        self.namaPetaniLabel = QLabel(self.formLayoutWidget)
        self.namaPetaniLabel.setObjectName(u"namaPetaniLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPetaniLabel)

        self.CBPetani = QComboBox(self.formLayoutWidget)
        self.CBPetani.setObjectName(u"CBPetani")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.CBPetani)

        self.namaTanamanLabel = QLabel(self.formLayoutWidget)
        self.namaTanamanLabel.setObjectName(u"namaTanamanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.namaTanamanLabel)

        self.CBTanaman = QComboBox(self.formLayoutWidget)
        self.CBTanaman.setObjectName(u"CBTanaman")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.CBTanaman)

        self.tanggalPanenLabel = QLabel(self.formLayoutWidget)
        self.tanggalPanenLabel.setObjectName(u"tanggalPanenLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalPanenLabel)

        self.editTanggal = QDateEdit(self.formLayoutWidget)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTanggal)

        self.jumlahHasilKgLabel = QLabel(self.formLayoutWidget)
        self.jumlahHasilKgLabel.setObjectName(u"jumlahHasilKgLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jumlahHasilKgLabel)

        self.SBHasil = QSpinBox(self.formLayoutWidget)
        self.SBHasil.setObjectName(u"SBHasil")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.SBHasil)

        self.kualitasLabel = QLabel(self.formLayoutWidget)
        self.kualitasLabel.setObjectName(u"kualitasLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.kualitasLabel)

        self.CBKualitas = QComboBox(self.formLayoutWidget)
        self.CBKualitas.addItem("")
        self.CBKualitas.addItem("")
        self.CBKualitas.addItem("")
        self.CBKualitas.setObjectName(u"CBKualitas")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.CBKualitas)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnTambah = QPushButton(self.formLayoutWidget)
        self.btnTambah.setObjectName(u"btnTambah")

        self.horizontalLayout.addWidget(self.btnTambah)

        self.btnUbah = QPushButton(self.formLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.horizontalLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(self.formLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout.addWidget(self.btnHapus)

        self.btnBatal = QPushButton(self.formLayoutWidget)
        self.btnBatal.setObjectName(u"btnBatal")

        self.horizontalLayout.addWidget(self.btnBatal)


        self.formLayout.setLayout(7, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.editKet = QTextEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 1171, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tblPanen = QTableWidget(Form)
        if (self.tblPanen.columnCount() < 7):
            self.tblPanen.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tblPanen.setObjectName(u"tblPanen")
        self.tblPanen.setGeometry(QRect(560, 180, 651, 192))
        self.comboFilter = QComboBox(Form)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        self.comboFilter.setGeometry(QRect(860, 390, 191, 28))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(752, 130, 461, 28))
        self.btnCetak = QPushButton(Form)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(1089, 390, 121, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPanenLabel.setText(QCoreApplication.translate("Form", u"ID Panen", None))
        self.namaPetaniLabel.setText(QCoreApplication.translate("Form", u"Nama Petani", None))
        self.namaTanamanLabel.setText(QCoreApplication.translate("Form", u"Nama Tanaman", None))
        self.tanggalPanenLabel.setText(QCoreApplication.translate("Form", u"Tanggal Panen", None))
        self.jumlahHasilKgLabel.setText(QCoreApplication.translate("Form", u"Jumlah Hasil (Kg)", None))
        self.kualitasLabel.setText(QCoreApplication.translate("Form", u"Kualitas", None))
        self.CBKualitas.setItemText(0, QCoreApplication.translate("Form", u"Bagus", None))
        self.CBKualitas.setItemText(1, QCoreApplication.translate("Form", u"Sedang", None))
        self.CBKualitas.setItemText(2, QCoreApplication.translate("Form", u"Buruk", None))

        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA PANEN", None))
        ___qtablewidgetitem = self.tblPanen.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tblPanen.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Petani", None));
        ___qtablewidgetitem2 = self.tblPanen.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nama Tanaman", None));
        ___qtablewidgetitem3 = self.tblPanen.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tanggal Panen", None));
        ___qtablewidgetitem4 = self.tblPanen.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Jumlah (kg)", None));
        ___qtablewidgetitem5 = self.tblPanen.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Kualitas", None));
        ___qtablewidgetitem6 = self.tblPanen.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Form", u"Bagus", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Form", u"Sedang", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("Form", u"Buruk", None))

        self.lineCari.setPlaceholderText(QCoreApplication.translate("Form", u"Cari berdasarkan ID/Nama Petani/Nama Tanaman/Kualitas...", None))
        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

