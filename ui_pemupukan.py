# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pemupukan.ui'
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
        Form.resize(676, 640)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 90, 571, 337))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPemupukanLabel = QLabel(self.formLayoutWidget)
        self.iDPemupukanLabel.setObjectName(u"iDPemupukanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPemupukanLabel)

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

        self.jenisPupukLabel = QLabel(self.formLayoutWidget)
        self.jenisPupukLabel.setObjectName(u"jenisPupukLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jenisPupukLabel)

        self.CBJenis = QComboBox(self.formLayoutWidget)
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.setObjectName(u"CBJenis")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.CBJenis)

        self.tanggalPemupukanLabel = QLabel(self.formLayoutWidget)
        self.tanggalPemupukanLabel.setObjectName(u"tanggalPemupukanLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tanggalPemupukanLabel)

        self.DE_Tanggal = QDateEdit(self.formLayoutWidget)
        self.DE_Tanggal.setObjectName(u"DE_Tanggal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.DE_Tanggal)

        self.jumlahKgLabel = QLabel(self.formLayoutWidget)
        self.jumlahKgLabel.setObjectName(u"jumlahKgLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.jumlahKgLabel)

        self.SBJumlah = QSpinBox(self.formLayoutWidget)
        self.SBJumlah.setObjectName(u"SBJumlah")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.SBJumlah)

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
        self.label.setGeometry(QRect(50, 40, 571, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tblPemupukan = QTableWidget(Form)
        self.tblPemupukan.setObjectName(u"tblPemupukan")
        self.tblPemupukan.setGeometry(QRect(50, 440, 591, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPemupukanLabel.setText(QCoreApplication.translate("Form", u"ID Pemupukan", None))
        self.namaPetaniLabel.setText(QCoreApplication.translate("Form", u"Nama Petani", None))
        self.namaTanamanLabel.setText(QCoreApplication.translate("Form", u"Nama Tanaman", None))
        self.jenisPupukLabel.setText(QCoreApplication.translate("Form", u"Jenis Pupuk", None))
        self.CBJenis.setItemText(0, QCoreApplication.translate("Form", u"Urea", None))
        self.CBJenis.setItemText(1, QCoreApplication.translate("Form", u"NPK", None))
        self.CBJenis.setItemText(2, QCoreApplication.translate("Form", u"Kandang", None))
        self.CBJenis.setItemText(3, QCoreApplication.translate("Form", u"Organik", None))

        self.tanggalPemupukanLabel.setText(QCoreApplication.translate("Form", u"Tanggal Pemupukan", None))
        self.jumlahKgLabel.setText(QCoreApplication.translate("Form", u"Jumlah (Kg)", None))
        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA PEMUPUKAN", None))
    # retranslateUi

