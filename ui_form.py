# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionPETANI = QAction(main)
        self.actionPETANI.setObjectName(u"actionPETANI")
        self.actionLAHAN = QAction(main)
        self.actionLAHAN.setObjectName(u"actionLAHAN")
        self.actionTANAMAN = QAction(main)
        self.actionTANAMAN.setObjectName(u"actionTANAMAN")
        self.actionPEMUPUKAN = QAction(main)
        self.actionPEMUPUKAN.setObjectName(u"actionPEMUPUKAN")
        self.actionPANEN = QAction(main)
        self.actionPANEN.setObjectName(u"actionPANEN")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuKELOLA_PETANI = QMenu(self.menubar)
        self.menuKELOLA_PETANI.setObjectName(u"menuKELOLA_PETANI")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuKELOLA_PETANI.menuAction())
        self.menuKELOLA_PETANI.addAction(self.actionPETANI)
        self.menuKELOLA_PETANI.addAction(self.actionLAHAN)
        self.menuKELOLA_PETANI.addAction(self.actionTANAMAN)
        self.menuKELOLA_PETANI.addAction(self.actionPEMUPUKAN)
        self.menuKELOLA_PETANI.addAction(self.actionPANEN)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionPETANI.setText(QCoreApplication.translate("main", u"PETANI", None))
        self.actionLAHAN.setText(QCoreApplication.translate("main", u"LAHAN", None))
        self.actionTANAMAN.setText(QCoreApplication.translate("main", u"TANAMAN", None))
        self.actionPEMUPUKAN.setText(QCoreApplication.translate("main", u"PEMUPUKAN", None))
        self.actionPANEN.setText(QCoreApplication.translate("main", u"PANEN", None))
        self.menuKELOLA_PETANI.setTitle(QCoreApplication.translate("main", u"KELOLA MENU", None))
    # retranslateUi

