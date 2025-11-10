# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tanaman.ui'
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
        Form.resize(731, 595)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 70, 571, 301))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDTanamanLabel = QLabel(self.formLayoutWidget)
        self.iDTanamanLabel.setObjectName(u"iDTanamanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDTanamanLabel)

        self.editId = QLineEdit(self.formLayoutWidget)
        self.editId.setObjectName(u"editId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editId)

        self.namaTanamanLabel = QLabel(self.formLayoutWidget)
        self.namaTanamanLabel.setObjectName(u"namaTanamanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaTanamanLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.jenisTanamanLabel = QLabel(self.formLayoutWidget)
        self.jenisTanamanLabel.setObjectName(u"jenisTanamanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jenisTanamanLabel)

        self.CBJenis = QComboBox(self.formLayoutWidget)
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.addItem("")
        self.CBJenis.setObjectName(u"CBJenis")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.CBJenis)

        self.masaTanamHariLabel = QLabel(self.formLayoutWidget)
        self.masaTanamHariLabel.setObjectName(u"masaTanamHariLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.masaTanamHariLabel)

        self.SBMasa = QSpinBox(self.formLayoutWidget)
        self.SBMasa.setObjectName(u"SBMasa")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.SBMasa)

        self.musimTanamLabel = QLabel(self.formLayoutWidget)
        self.musimTanamLabel.setObjectName(u"musimTanamLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.musimTanamLabel)

        self.CBMusim = QComboBox(self.formLayoutWidget)
        self.CBMusim.addItem("")
        self.CBMusim.addItem("")
        self.CBMusim.setObjectName(u"CBMusim")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.CBMusim)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

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

        self.editKet = QTextEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")
        self.editKet.setEnabled(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 30, 571, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tblTanaman = QTableWidget(Form)
        self.tblTanaman.setObjectName(u"tblTanaman")
        self.tblTanaman.setGeometry(QRect(80, 390, 621, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDTanamanLabel.setText(QCoreApplication.translate("Form", u"ID Tanaman", None))
        self.namaTanamanLabel.setText(QCoreApplication.translate("Form", u"Nama Tanaman", None))
        self.jenisTanamanLabel.setText(QCoreApplication.translate("Form", u"Jenis Tanaman", None))
        self.CBJenis.setItemText(0, QCoreApplication.translate("Form", u"Padi", None))
        self.CBJenis.setItemText(1, QCoreApplication.translate("Form", u"Palawija", None))
        self.CBJenis.setItemText(2, QCoreApplication.translate("Form", u"Sayuran", None))
        self.CBJenis.setItemText(3, QCoreApplication.translate("Form", u"Padi-padian", None))

        self.masaTanamHariLabel.setText(QCoreApplication.translate("Form", u"Masa Tanam (Hari)", None))
        self.musimTanamLabel.setText(QCoreApplication.translate("Form", u"Musim Tanam", None))
        self.CBMusim.setItemText(0, QCoreApplication.translate("Form", u"Hujan", None))
        self.CBMusim.setItemText(1, QCoreApplication.translate("Form", u"Kemarau", None))

        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBatal.setText(QCoreApplication.translate("Form", u"Batal", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA TANAMAN", None))
    # retranslateUi

