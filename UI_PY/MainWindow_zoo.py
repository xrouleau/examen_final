#Xavier Rouleau
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Brouillon2\MainWindow_zoo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_enclos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enclos.setGeometry(QtCore.QRect(170, 160, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_enclos.setFont(font)
        self.pushButton_enclos.setObjectName("pushButton_enclos")
        self.pushButton_animal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_animal.setGeometry(QtCore.QRect(460, 160, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_animal.setFont(font)
        self.pushButton_animal.setObjectName("pushButton_animal")
        self.pushButton_veterinaire = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_veterinaire.setGeometry(QtCore.QRect(170, 300, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_veterinaire.setFont(font)
        self.pushButton_veterinaire.setObjectName("pushButton_veterinaire")
        self.pushButton_recherche = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recherche.setGeometry(QtCore.QRect(460, 300, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_recherche.setFont(font)
        self.pushButton_recherche.setObjectName("pushButton_recherche")
        self.label_titre = QtWidgets.QLabel(self.centralwidget)
        self.label_titre.setGeometry(QtCore.QRect(230, 20, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestion du zoo Safari"))
        self.pushButton_enclos.setText(_translate("MainWindow", "Enclos"))
        self.pushButton_animal.setText(_translate("MainWindow", "Animal"))
        self.pushButton_veterinaire.setText(_translate("MainWindow", "Vétérinaire"))
        self.pushButton_recherche.setText(_translate("MainWindow", "Recherche"))
        self.label_titre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">Bienvenue au zoo Safari !</span></p></body></html>"))
