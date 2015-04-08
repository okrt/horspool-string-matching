# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Apr 08 10:31:45 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(647, 735)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.teMetin = QtGui.QTextEdit(self.centralwidget)
        self.teMetin.setGeometry(QtCore.QRect(10, 30, 381, 151))
        self.teMetin.setObjectName(_fromUtf8("teMetin"))
        self.lePattern = QtGui.QLineEdit(self.centralwidget)
        self.lePattern.setGeometry(QtCore.QRect(10, 210, 381, 20))
        self.lePattern.setObjectName(_fromUtf8("lePattern"))
        self.teAdimlar = QtGui.QTextEdit(self.centralwidget)
        self.teAdimlar.setGeometry(QtCore.QRect(10, 310, 621, 151))
        self.teAdimlar.setReadOnly(True)
        self.teAdimlar.setObjectName(_fromUtf8("teAdimlar"))
        self.btnBul = QtGui.QPushButton(self.centralwidget)
        self.btnBul.setGeometry(QtCore.QRect(10, 240, 611, 41))
        self.btnBul.setObjectName(_fromUtf8("btnBul"))
        self.btnDosya = QtGui.QPushButton(self.centralwidget)
        self.btnDosya.setGeometry(QtCore.QRect(220, 0, 121, 23))
        self.btnDosya.setObjectName(_fromUtf8("btnDosya"))
        self.lblMetin = QtGui.QLabel(self.centralwidget)
        self.lblMetin.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.lblMetin.setObjectName(_fromUtf8("lblMetin"))
        self.lblPattern = QtGui.QLabel(self.centralwidget)
        self.lblPattern.setGeometry(QtCore.QRect(10, 190, 121, 16))
        self.lblPattern.setObjectName(_fromUtf8("lblPattern"))
        self.lblAdimlar = QtGui.QLabel(self.centralwidget)
        self.lblAdimlar.setGeometry(QtCore.QRect(10, 290, 121, 16))
        self.lblAdimlar.setObjectName(_fromUtf8("lblAdimlar"))
        self.lblHakkinda = QtGui.QLabel(self.centralwidget)
        self.lblHakkinda.setGeometry(QtCore.QRect(440, 480, 181, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHakkinda.sizePolicy().hasHeightForWidth())
        self.lblHakkinda.setSizePolicy(sizePolicy)
        self.lblHakkinda.setObjectName(_fromUtf8("lblHakkinda"))
        self.lblPozisyon = QtGui.QLabel(self.centralwidget)
        self.lblPozisyon.setGeometry(QtCore.QRect(410, 10, 101, 20))
        self.lblPozisyon.setObjectName(_fromUtf8("lblPozisyon"))
        self.lblDurum = QtGui.QLabel(self.centralwidget)
        self.lblDurum.setGeometry(QtCore.QRect(10, 560, 531, 20))
        self.lblDurum.setObjectName(_fromUtf8("lblDurum"))
        self.lblIslem = QtGui.QLabel(self.centralwidget)
        self.lblIslem.setGeometry(QtCore.QRect(10, 590, 621, 71))
        self.lblIslem.setAutoFillBackground(False)
        self.lblIslem.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lblIslem.setTextFormat(QtCore.Qt.RichText)
        self.lblIslem.setScaledContents(False)
        self.lblIslem.setObjectName(_fromUtf8("lblIslem"))
        self.cbAdimlar = QtGui.QCheckBox(self.centralwidget)
        self.cbAdimlar.setGeometry(QtCore.QRect(20, 510, 401, 21))
        self.cbAdimlar.setObjectName(_fromUtf8("cbAdimlar"))
        self.cbThDurumAl = QtGui.QCheckBox(self.centralwidget)
        self.cbThDurumAl.setGeometry(QtCore.QRect(20, 490, 421, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbThDurumAl.sizePolicy().hasHeightForWidth())
        self.cbThDurumAl.setSizePolicy(sizePolicy)
        self.cbThDurumAl.setChecked(True)
        self.cbThDurumAl.setTristate(False)
        self.cbThDurumAl.setObjectName(_fromUtf8("cbThDurumAl"))
        self.lblDurum_2 = QtGui.QLabel(self.centralwidget)
        self.lblDurum_2.setGeometry(QtCore.QRect(10, 470, 531, 20))
        self.lblDurum_2.setObjectName(_fromUtf8("lblDurum_2"))
        self.lvKonumlar = QtGui.QListView(self.centralwidget)
        self.lvKonumlar.setGeometry(QtCore.QRect(410, 30, 211, 201))
        self.lvKonumlar.setObjectName(_fromUtf8("lvKonumlar"))
        self.cbRenklendir = QtGui.QCheckBox(self.centralwidget)
        self.cbRenklendir.setGeometry(QtCore.QRect(20, 530, 391, 21))
        self.cbRenklendir.setObjectName(_fromUtf8("cbRenklendir"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 670, 601, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Horspool String Matching @NKU", None))
        self.btnBul.setText(_translate("MainWindow", "Find", None))
        self.btnDosya.setText(_translate("MainWindow", "Import File", None))
        self.lblMetin.setText(_translate("MainWindow", "Text:", None))
        self.lblPattern.setText(_translate("MainWindow", "Pattern:", None))
        self.lblAdimlar.setText(_translate("MainWindow", "Steps:", None))
        self.lblHakkinda.setText(_translate("MainWindow", "<html><head/><body><p>Ferhat Yeşiltarla</p><p>Gökmen Güreşçi</p><p>Oğuz Kırat</p></body></html>", None))
        self.lblPozisyon.setText(_translate("MainWindow", "Positions Found", None))
        self.lblDurum.setText(_translate("MainWindow", "Status", None))
        self.lblIslem.setText(_translate("MainWindow", "Ready", None))
        self.cbAdimlar.setText(_translate("MainWindow", "Show steps (Not recommended on long texts)", None))
        self.cbThDurumAl.setText(_translate("MainWindow", "Get info from string matching thread while processing.", None))
        self.lblDurum_2.setText(_translate("MainWindow", "Options", None))
        self.cbRenklendir.setText(_translate("MainWindow", "Colorize patterns found. (Not recommended on long texts)", None))
        self.label.setText(_translate("MainWindow", "Quickly developed for \"Pattern Matching in Texts\" course assignment @ nku.edu.tr", None))

