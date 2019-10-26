# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_py.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os 


class Ui_MainWindow(object):

    def cagir(self): 
        global dosyayolu, yol, dosyaadi, klasoryolu

        if self.lineEditDosyaAdi.text()=="" or self.lineEditDosyaAdi.text()=="PY Olacak Dosyanın Adını Yazınız.":
            self.textBrowserDosyaYolu.setText("Lütfen PY dosyanızın adını giriniz.")
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            dosyayolu, _ = QFileDialog.getOpenFileName(filter="*.ui")
            yol = dosyayolu.split("/")
            dosyaadi = yol[-1]
            yol.remove(dosyaadi)
            klasoryolu = str("\\".join(yol))
            if dosyaadi=="":
                self.textBrowserDosyaYolu.setText("DOSYA SEÇMEDINIZ!")
                return

            self.textBrowserDosyaYolu.setText("Seçilen Dosya = " + dosyaadi + "\n" + "Dosya Yolu: " + dosyayolu+"\nÇıkacak PY Dosya Adı: "+self.lineEditDosyaAdi.text())
            self.btnDonustur.show()
    
    def donusturucu(self):
        global yeniisim
        yeniisim = self.lineEditDosyaAdi.text()
        os.chdir(klasoryolu)
        os.system('python -m PyQt5.uic.pyuic -x' + dosyaadi + ' -o ' + yeniisim + '.py')
        self.textBrowserDosyaYolu.setText("Dosya Dönüştürüldü.\nDosya Yolu: " + klasoryolu + "\nPy Dosya Adı: " + yeniisim)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(593, 349)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnDosyaSec = QtWidgets.QPushButton(self.centralwidget)
        self.btnDosyaSec.setGeometry(QtCore.QRect(280, 90, 72, 23))
        self.btnDosyaSec.setObjectName("btnDosyaSec")
        self.btnDosyaSec.clicked.connect(self.cagir) 

        self.labelDosyaAdi = QtWidgets.QLabel(self.centralwidget)
        self.labelDosyaAdi.setGeometry(QtCore.QRect(170, 30, 131, 20))
        self.labelDosyaAdi.setObjectName("labelDosyaAdi")

        self.lineEditDosyaAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDosyaAdi.setGeometry(QtCore.QRect(300, 30, 170, 20))
        self.lineEditDosyaAdi.setObjectName("lineEditDosyaAdi")
        self.lineEditDosyaAdi.setText("PY Olacak Dosyanın Adını Yazınız.") 

        self.btnCikis = QtWidgets.QPushButton(self.centralwidget)
        self.btnCikis.setGeometry(QtCore.QRect(360, 90, 75, 23))
        self.btnCikis.setObjectName("btnCikis")
        self.btnCikis.clicked.connect(self.cikis) 
        

        self.btnDonustur = QtWidgets.QPushButton(self.centralwidget)
        self.btnDonustur.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.btnDonustur.setObjectName("btnDonustur")
        self.btnDonustur.clicked.connect(self.donusturucu) 

        
        self.textBrowserDosyaYolu = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserDosyaYolu.setGeometry(QtCore.QRect(170, 140, 261, 71))
        self.textBrowserDosyaYolu.setObjectName("textBrowserDosyaYolu")
        self.textBrowserDosyaYolu.setText("Lütfet UI dosyanızı Seçiniz.\nLütfen Dosyanızı seçmeden önce PY dosyanızın adını belirleyiniz.") 

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")

        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.statusbar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionAc = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("Open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        self.actionAc.setIcon(icon) 
        self.actionAc.setObjectName("actionAc")
        self.actionAc.triggered.connect(self.ac) 

        self.actionKaydet = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        self.actionKaydet.setIcon(icon) 
        self.actionKaydet.setObjectName("actionKaydet")
        self.actionKaydet.triggered.connect(self.kaydet) 

        self.actionCikis = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        self.actionCikis.setIcon(icon)
        self.actionCikis.setObjectName("actionCikis")
        self.actionCikis.triggered.connect(self.cikis) 
        

        self.menuDosya.addAction(self.actionAc)
        self.menuDosya.addAction(self.actionKaydet)
        self.menuDosya.addAction(self.actionCikis)  
        
        self.menuDosya.addSeparator()
        self.menubar.addAction(self.menuDosya.menuAction())

             
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MenkapSoft-UI yi PY Dönüştürme"))
        self.btnDosyaSec.setText(_translate("MainWindow", "Dosya Seç"))
        self.labelDosyaAdi.setText(_translate("MainWindow", "Python Dosya Adı Giriniz:"))
        self.btnCikis.setText(_translate("MainWindow", "Çıkış"))
        self.btnDonustur.setText(_translate("MainWindow", "Dönüştür"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.actionAc.setText(_translate("MainWindow", "Aç"))
        self.actionAc.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.actionKaydet.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCikis.setText(_translate("MainWindow", "Çıkış"))
        self.actionCikis.setShortcut(_translate("MainWindow","Ctrl+F4"))

        
    

    def ac(self):
        pass

    def kaydet(self):
        pass

    def cikis(self):
        sys.exit()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
