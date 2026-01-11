# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lahan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1160, 441)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 70, 451, 311))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLahanLabel = QLabel(self.formLayoutWidget)
        self.iDLahanLabel.setObjectName(u"iDLahanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLahanLabel)

        self.editId = QLineEdit(self.formLayoutWidget)
        self.editId.setObjectName(u"editId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editId)

        self.namaPetaniLabel = QLabel(self.formLayoutWidget)
        self.namaPetaniLabel.setObjectName(u"namaPetaniLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPetaniLabel)

        self.CBPetani = QComboBox(self.formLayoutWidget)
        self.CBPetani.setObjectName(u"CBPetani")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.CBPetani)

        self.lokasiLahanLabel = QLabel(self.formLayoutWidget)
        self.lokasiLahanLabel.setObjectName(u"lokasiLahanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lokasiLahanLabel)

        self.editLokasi = QLineEdit(self.formLayoutWidget)
        self.editLokasi.setObjectName(u"editLokasi")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editLokasi)

        self.luasLahanLabel = QLabel(self.formLayoutWidget)
        self.luasLahanLabel.setObjectName(u"luasLahanLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.luasLahanLabel)

        self.SBLuas = QSpinBox(self.formLayoutWidget)
        self.SBLuas.setObjectName(u"SBLuas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.SBLuas)

        self.jenisTanahLabel = QLabel(self.formLayoutWidget)
        self.jenisTanahLabel.setObjectName(u"jenisTanahLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jenisTanahLabel)

        self.CBJenis = QComboBox(self.formLayoutWidget)
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.setObjectName(u"CBJenis")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.CBJenis)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.editKet = QTextEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKet)

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


        self.formLayout.setLayout(6, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 1031, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tblLahan = QTableWidget(Form)
        if (self.tblLahan.columnCount() < 6):
            self.tblLahan.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblLahan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblLahan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblLahan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblLahan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblLahan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblLahan.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblLahan.setObjectName(u"tblLahan")
        self.tblLahan.setGeometry(QRect(500, 130, 641, 191))
        self.comboFilter = QComboBox(Form)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        self.comboFilter.setGeometry(QRect(801, 340, 201, 28))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(732, 80, 411, 28))
        self.btnCetak = QPushButton(Form)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(1029, 340, 101, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDLahanLabel.setText(QCoreApplication.translate("Form", u"ID Lahan", None))
        self.namaPetaniLabel.setText(QCoreApplication.translate("Form", u"Nama Petani", None))
        self.lokasiLahanLabel.setText(QCoreApplication.translate("Form", u"Lokasi Lahan", None))
        self.luasLahanLabel.setText(QCoreApplication.translate("Form", u"Luas Lahan", None))
        self.jenisTanahLabel.setText(QCoreApplication.translate("Form", u"Jenis Tanah", None))
        self.CBJenis.setItemText(0, QCoreApplication.translate("Form", u"Lempung", None))
        self.CBJenis.setItemText(1, QCoreApplication.translate("Form", u"Gembur", None))
        self.CBJenis.setItemText(2, QCoreApplication.translate("Form", u"Berpasir", None))

        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Form", u" KELOLA DATA LAHAN", None))
        ___qtablewidgetitem = self.tblLahan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tblLahan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Petani", None));
        ___qtablewidgetitem2 = self.tblLahan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lokasi", None));
        ___qtablewidgetitem3 = self.tblLahan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Luas", None));
        ___qtablewidgetitem4 = self.tblLahan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Jenis Tanah", None));
        ___qtablewidgetitem5 = self.tblLahan.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Form", u"Lempung", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Form", u"Gembur", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("Form", u"Berpasir", None))

        self.lineCari.setPlaceholderText(QCoreApplication.translate("Form", u"Cari berdasarkan ID/Nama/Lokasi/Jenis Tanah....", None))
        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

