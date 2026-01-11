# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'petani.ui'
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
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1154, 462)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 100, 441, 261))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPetaniLabel = QLabel(self.formLayoutWidget)
        self.iDPetaniLabel.setObjectName(u"iDPetaniLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPetaniLabel)

        self.editId = QLineEdit(self.formLayoutWidget)
        self.editId.setObjectName(u"editId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editId)

        self.namaPetaniLabel = QLabel(self.formLayoutWidget)
        self.namaPetaniLabel.setObjectName(u"namaPetaniLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPetaniLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.editAlamat = QLineEdit(self.formLayoutWidget)
        self.editAlamat.setObjectName(u"editAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editAlamat)

        self.noHPLabel = QLabel(self.formLayoutWidget)
        self.noHPLabel.setObjectName(u"noHPLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.noHPLabel)

        self.editNo = QLineEdit(self.formLayoutWidget)
        self.editNo.setObjectName(u"editNo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editNo)

        self.jenisKelaminLabel = QLabel(self.formLayoutWidget)
        self.jenisKelaminLabel.setObjectName(u"jenisKelaminLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jenisKelaminLabel)

        self.CBJk = QComboBox(self.formLayoutWidget)
        self.CBJk.addItem("")
        self.CBJk.addItem("")
        self.CBJk.setObjectName(u"CBJk")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.CBJk)

        self.umurLabel = QLabel(self.formLayoutWidget)
        self.umurLabel.setObjectName(u"umurLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.umurLabel)

        self.SBUmur = QSpinBox(self.formLayoutWidget)
        self.SBUmur.setObjectName(u"SBUmur")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.SBUmur)

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
        self.label.setGeometry(QRect(10, 30, 1101, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tblPetani = QTableWidget(Form)
        if (self.tblPetani.columnCount() < 6):
            self.tblPetani.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblPetani.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblPetani.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblPetani.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblPetani.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblPetani.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblPetani.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblPetani.setObjectName(u"tblPetani")
        self.tblPetani.setGeometry(QRect(520, 140, 601, 221))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(720, 90, 401, 28))
        self.comboFilter = QComboBox(Form)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        self.comboFilter.setGeometry(QRect(750, 380, 241, 28))
        self.btnCetak = QPushButton(Form)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(1010, 380, 111, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPetaniLabel.setText(QCoreApplication.translate("Form", u"ID Petani", None))
        self.namaPetaniLabel.setText(QCoreApplication.translate("Form", u"Nama Petani", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.noHPLabel.setText(QCoreApplication.translate("Form", u"No HP", None))
        self.jenisKelaminLabel.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None))
        self.CBJk.setItemText(0, QCoreApplication.translate("Form", u"Laki-Laki", None))
        self.CBJk.setItemText(1, QCoreApplication.translate("Form", u"Perempuan", None))

        self.umurLabel.setText(QCoreApplication.translate("Form", u"Umur", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA PETANI", None))
        ___qtablewidgetitem = self.tblPetani.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Petani", None));
        ___qtablewidgetitem1 = self.tblPetani.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama ", None));
        ___qtablewidgetitem2 = self.tblPetani.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem3 = self.tblPetani.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"No HP", None));
        ___qtablewidgetitem4 = self.tblPetani.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem5 = self.tblPetani.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Umur", None));
        self.lineCari.setPlaceholderText(QCoreApplication.translate("Form", u"Cari berdasarkan ID/Nama/Alamat/JenisKelamin.....", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Form", u"Laki-Laki", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Form", u"Perempuan", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

