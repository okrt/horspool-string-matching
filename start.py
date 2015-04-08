#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Oguz Kirat'
__author__ = 'Ferhat Yeşiltarla'
__author__ = 'Gökmen Güreşçi'

import sys
import time
import string
import codecs
import unicodedata

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from main import Ui_MainWindow

global pattern, text, founddict, steps, adimlarchecked, kar_esit, karbool
pattern = ""
text = ""
founddict = {}
steps = ""
adimlarchecked = False
kar_esit = 0
karbool = False


class MyModel(QAbstractListModel):
    def __init__(self, data=[], parent=None):
        QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()]


class PatternPositionsParser(QThread):
    parsedresults = pyqtSignal(str)

    def run(self):
        self.a = ""
        for x in founddict.items():
            self.a = self.a + str(x[0]) + "-" + str(x[1]) + "ms<br>"
        self.parsedresults.emit(self.a)


class BMHorspool(QThread):
    found = pyqtSignal(int)
    completed = pyqtSignal(bool)

    def run(self):
        global kar_esit
        kar_esit = 0
        karbool = False
        self.pattern = pattern
        self.text = text
        self.adimlar = unicode(
            "<html><<head><meta charset=\"UTF-8\"></head><body><div style=\"font-family:'Courier New', Courier, monospace\">",
            "utf-8")
        kontrol = False
        self.founddict = {}
        self.fnd = 0
        start_time = time.clock()
        patterninuzunlugu = len(self.pattern)
        metninuzunlugu = len(self.text)
        if patterninuzunlugu > metninuzunlugu: return -1
        skip = []
        for k in range(256): skip.append(patterninuzunlugu)
        for k in range(patterninuzunlugu - 1): skip[ord(self.pattern[k])] = patterninuzunlugu - k - 1
        skip = tuple(skip)
        k = patterninuzunlugu - 1
        while k < metninuzunlugu:
            j = patterninuzunlugu - 1;
            i = k
            # Adımlar
            if adimlarchecked:
                harf = 0

                self.adimlar = self.adimlar + text + "<br>"
                for c in range(0, (k - patterninuzunlugu) + 1):
                    self.adimlar = self.adimlar + unicode("-", "utf-8")
                for c in range((k - patterninuzunlugu), k):
                    self.adimlar = self.adimlar + unicode(self.pattern[harf], "utf-8")
                    harf = harf + 1
                self.adimlar = self.adimlar + "<br>"
            #Adımlar sonu
            while j >= 0 and self.text[i] == self.pattern[j]:
                j -= 1;
                i -= 1
                kar_esit += 1
                if j != -1:
                    karbool = False
                else:
                    karbool = True
            if j == -1:
                #Burada bulunan pozisyonlar ve sürelerini bir python dictionarysine ekliyorum.
                timepassed = (time.clock() - start_time) * 1000.0
                self.founddict[int(i + 1)] = int(timepassed)
                self.fnd = self.fnd + 1
                self.found.emit(self.fnd)
                #return i + 1
                kontrol = True
            k += skip[ord(self.text[k])]
            if karbool == False:
                kar_esit += 1
            else:
                karbool = False

        global founddict
        founddict = self.founddict
        if (k >= metninuzunlugu):
            self.completed.emit(True)
            global steps
            steps = self.adimlar + "</div></html>"


# Formdan generate edilmiş olan sınıfımıza subclassing uyguluyoruz.
class MainWindow(QMainWindow, Ui_MainWindow):
    def removetrchars(self, text):
        return text.replace(u"ş", "s").replace(u"Ş", "S").replace(u"Ü", "U").replace(u"ü", "u").replace(u"Ç","C").replace(u"ğ", "g").replace(u"ç", "c").replace(u"Ğ", "G").replace(u"İ", "I").replace(u"ı", "i")

    def warning_dialog(self, title, text):
        QMessageBox.warning(self, title, text, QMessageBox.Ok)

    #Türkçe karakterlerin düzgün görüntülenmesi için bu fonksiyonu kullanın.
    def str2utf8(self, msg):
        return unicode(msg, "utf-8")

    def parsecompleted(self, var):
        self.teKonumlar.setText(self.str2utf8(var))

    def updatefoundcount(self, val):
        self.lblIslem.setText(self.str2utf8("Processing...<br>Found " + str(val) + " so far."))

    def operationcompleted(self):
        passed = (time.clock() - started) * 1000.0
        self.lblIslem.setText(self.str2utf8(
            "String matching completed.<br>Total " + str(len(founddict)) + " matches." + "<br>It took " + str(
                passed) + " ms. <br>Listing data might have taken more time...<br>Comparison: " + str(
                kar_esit)))
        self.ui = Ui_MainWindow
        self.ui.thread = PatternPositionsParser()
        #self.ui.thread.start()
        #self.ui.thread.parsedresults.connect(self.parsecompleted)
        data = founddict.keys()
        data.sort()
        model = MyModel(data)
        self.lvKonumlar.setModel(model)
        if adimlarchecked:
            self.teAdimlar.setText(steps)
        if (self.cbRenklendir.isChecked()):
            self.teMetin.setAcceptRichText(False)
            stdformat = QTextCharFormat()
            stdformat.setBackground(Qt.white)
            self.teMetin.setCurrentCharFormat(stdformat)
            self.teMetin.setAcceptRichText(True)

            self.teMetin.setText(self.teMetin.toPlainText())
            format = QTextCharFormat()
            format.setBackground(Qt.yellow)
            cursor = self.teMetin.textCursor()
            cursor.setPosition(0)
            for x in data:
                self.teMetin.textCursor()
                cursor.setPosition(x)
                cursor.movePosition(QTextCursor.Right, 1, len(pattern))
                cursor.mergeCharFormat(format)

    @pyqtSlot()
    def adimlarchanged(self):
        global adimlarchecked
        if self.cbAdimlar.isChecked():
            adimlarchecked = True
        else:
            adimlarchecked = False

    @pyqtSlot()
    def openfile(self):
        self.selected = QFileDialog.getOpenFileName(self, self.str2utf8("Select a text file"))
        if string.lower(unicode(self.selected)).endswith('.txt'):
            f = codecs.open(self.selected, 'r', "utf-8")
            text = f.read()
            self.lblIslem.setText(self.str2utf8("File imported..."))
            self.teMetin.setText(text)
        else:
            self.warning_dialog(self.tr("Error"), self.str2utf8(("You should select a txt file")))



    @pyqtSlot()
    def stringmatcher(self):

        if (len(self.lePattern.text()) > 0 and len(self.teMetin.toPlainText()) > 0):
            if (len(self.lePattern.text()) <= len(self.teMetin.toPlainText())):
                self.lblIslem.setText(self.str2utf8("Processing..."))
                global pattern, text

                pattern = self.removetrchars(unicodedata.normalize('NFKC', unicode(self.lePattern.text()))).encode(
                    'ascii', 'replace')
                text = self.removetrchars(unicodedata.normalize('NFKC', unicode(self.teMetin.toPlainText()))).encode(
                    'ascii', 'replace')

                global started
                started = time.clock()

                self.ui = Ui_MainWindow
                self.ui.thread = BMHorspool();
                self.ui.thread.start()
                self.ui.thread.completed.connect(self.operationcompleted)
                if (self.cbThDurumAl.isChecked()):
                    self.ui.thread.found.connect(self.updatefoundcount)

            else:
                self.warning_dialog(self.tr("Error"),
                                    self.str2utf8(("Pattern should be smaller than text")))
        else:
            self.warning_dialog(self.tr("Hata"), self.str2utf8(("Please enter a text and a pattern")))

    def __init__(self):
        QMainWindow.__init__(self)

        # kullanici arayuzunu olustur
        self.setupUi(self)
        # istege bagli slot baglantilari
        #QObject.connect(self.btnDosya,SIGNAL("released()"),self.openfile()) # signal/slot connection
        self.btnDosya.released.connect(self.openfile)
        self.btnBul.released.connect(self.stringmatcher)
        self.cbAdimlar.stateChanged.connect(self.adimlarchanged)



        #


# Main fonk
def main(argv):
    # Qt uygulamasini olustur
    app = QApplication(argv, True)

    # ana ekrani olustur
    wnd = MainWindow()  # classname
    wnd.show()

    # bitis sinyali
    # app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))

    # Uygulamayi baslar
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)