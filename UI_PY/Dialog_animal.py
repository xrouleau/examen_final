#Xavier Rouleau
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Brouillon2\Dialog_animal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog_Animal):
        Dialog_Animal.setObjectName("Dialog_Animal")
        Dialog_Animal.resize(1080, 578)
        self.label_numero_animal = QtWidgets.QLabel(Dialog_Animal)
        self.label_numero_animal.setGeometry(QtCore.QRect(40, 60, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numero_animal.setFont(font)
        self.label_numero_animal.setObjectName("label_numero_animal")
        self.lineEdit_numero_animal = QtWidgets.QLineEdit(Dialog_Animal)
        self.lineEdit_numero_animal.setGeometry(QtCore.QRect(40, 90, 191, 41))
        self.lineEdit_numero_animal.setObjectName("lineEdit_numero_animal")
        self.label_erreur_numero_animal_existe_pas = QtWidgets.QLabel(Dialog_Animal)
        self.label_erreur_numero_animal_existe_pas.setGeometry(QtCore.QRect(40, 140, 261, 16))
        self.label_erreur_numero_animal_existe_pas.setObjectName("label_erreur_numero_animal_existe_pas")
        self.label_erreur_numero_animal_existe = QtWidgets.QLabel(Dialog_Animal)
        self.label_erreur_numero_animal_existe.setGeometry(QtCore.QRect(40, 150, 261, 16))
        self.label_erreur_numero_animal_existe.setObjectName("label_erreur_numero_animal_existe")
        self.label_erreur_numero_animal_invalide = QtWidgets.QLabel(Dialog_Animal)
        self.label_erreur_numero_animal_invalide.setGeometry(QtCore.QRect(40, 160, 381, 16))
        self.label_erreur_numero_animal_invalide.setObjectName("label_erreur_numero_animal_invalide")
        self.lineEdit_surnom_animal = QtWidgets.QLineEdit(Dialog_Animal)
        self.lineEdit_surnom_animal.setGeometry(QtCore.QRect(40, 240, 191, 41))
        self.lineEdit_surnom_animal.setObjectName("lineEdit_surnom_animal")
        self.label_surnom_animal = QtWidgets.QLabel(Dialog_Animal)
        self.label_surnom_animal.setGeometry(QtCore.QRect(40, 210, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_surnom_animal.setFont(font)
        self.label_surnom_animal.setObjectName("label_surnom_animal")
        self.lineEdit_poids_animal = QtWidgets.QLineEdit(Dialog_Animal)
        self.lineEdit_poids_animal.setGeometry(QtCore.QRect(50, 350, 191, 41))
        self.lineEdit_poids_animal.setObjectName("lineEdit_poids_animal")
        self.label_poids_animal = QtWidgets.QLabel(Dialog_Animal)
        self.label_poids_animal.setGeometry(QtCore.QRect(50, 320, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_poids_animal.setFont(font)
        self.label_poids_animal.setObjectName("label_poids_animal")
        self.label_erreur_poids_animal = QtWidgets.QLabel(Dialog_Animal)
        self.label_erreur_poids_animal.setGeometry(QtCore.QRect(50, 390, 261, 16))
        self.label_erreur_poids_animal.setObjectName("label_erreur_poids_animal")
        self.label_famille_animal = QtWidgets.QLabel(Dialog_Animal)
        self.label_famille_animal.setGeometry(QtCore.QRect(490, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_famille_animal.setFont(font)
        self.label_famille_animal.setObjectName("label_famille_animal")
        self.comboBox_famille_animal = QtWidgets.QComboBox(Dialog_Animal)
        self.comboBox_famille_animal.setGeometry(QtCore.QRect(490, 100, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_famille_animal.setFont(font)
        self.comboBox_famille_animal.setObjectName("comboBox_famille_animal")
        self.comboBox_famille_animal.addItem("")
        self.comboBox_famille_animal.addItem("")
        self.comboBox_famille_animal.addItem("")
        self.comboBox_enclos_animal = QtWidgets.QComboBox(Dialog_Animal)
        self.comboBox_enclos_animal.setGeometry(QtCore.QRect(490, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_enclos_animal.setFont(font)
        self.comboBox_enclos_animal.setObjectName("comboBox_enclos_animal")
        self.comboBox_enclos_animal.addItem("")
        self.comboBox_enclos_animal.setItemText(0, "")
        self.comboBox_enclos_animal.addItem("")
        self.comboBox_enclos_animal.setItemText(1, "")
        self.comboBox_enclos_animal.addItem("")
        self.comboBox_enclos_animal.setItemText(2, "")
        self.label_enclos_animal = QtWidgets.QLabel(Dialog_Animal)
        self.label_enclos_animal.setGeometry(QtCore.QRect(490, 220, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enclos_animal.setFont(font)
        self.label_enclos_animal.setObjectName("label_enclos_animal")
        self.pushButton_ajouter = QtWidgets.QPushButton(Dialog_Animal)
        self.pushButton_ajouter.setGeometry(QtCore.QRect(110, 480, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter.setFont(font)
        self.pushButton_ajouter.setObjectName("pushButton_ajouter")
        self.pushButton_rechercher = QtWidgets.QPushButton(Dialog_Animal)
        self.pushButton_rechercher.setGeometry(QtCore.QRect(470, 480, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_rechercher.setFont(font)
        self.pushButton_rechercher.setObjectName("pushButton_rechercher")
        self.comboBox_couleur_poil = QtWidgets.QComboBox(Dialog_Animal)
        self.comboBox_couleur_poil.setGeometry(QtCore.QRect(760, 120, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_couleur_poil.setFont(font)
        self.comboBox_couleur_poil.setObjectName("comboBox_couleur_poil")
        self.comboBox_couleur_poil.addItem("")
        self.comboBox_couleur_poil.addItem("")
        self.comboBox_couleur_poil.addItem("")
        self.label_couleur_poil = QtWidgets.QLabel(Dialog_Animal)
        self.label_couleur_poil.setGeometry(QtCore.QRect(760, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_couleur_poil.setFont(font)
        self.label_couleur_poil.setObjectName("label_couleur_poil")
        self.label_longueur_bec = QtWidgets.QLabel(Dialog_Animal)
        self.label_longueur_bec.setGeometry(QtCore.QRect(770, 220, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_longueur_bec.setFont(font)
        self.label_longueur_bec.setObjectName("label_longueur_bec")
        self.comboBox_venimeux = QtWidgets.QComboBox(Dialog_Animal)
        self.comboBox_venimeux.setGeometry(QtCore.QRect(760, 400, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_venimeux.setFont(font)
        self.comboBox_venimeux.setObjectName("comboBox_venimeux")
        self.comboBox_venimeux.addItem("")
        self.comboBox_venimeux.addItem("")
        self.comboBox_venimeux.addItem("")
        self.comboBox_venimeux.setItemText(2, "")
        self.label_venimeux = QtWidgets.QLabel(Dialog_Animal)
        self.label_venimeux.setGeometry(QtCore.QRect(760, 370, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_venimeux.setFont(font)
        self.label_venimeux.setObjectName("label_venimeux")
        self.lineEdit_longueur_bec = QtWidgets.QLineEdit(Dialog_Animal)
        self.lineEdit_longueur_bec.setGeometry(QtCore.QRect(770, 250, 161, 41))
        self.lineEdit_longueur_bec.setObjectName("lineEdit_longueur_bec")
        self.label_erreur_longueur_bec = QtWidgets.QLabel(Dialog_Animal)
        self.label_erreur_longueur_bec.setGeometry(QtCore.QRect(770, 300, 381, 16))
        self.label_erreur_longueur_bec.setObjectName("label_erreur_longueur_bec")
        self.line_2 = QtWidgets.QFrame(Dialog_Animal)
        self.line_2.setGeometry(QtCore.QRect(710, 50, 20, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_mammifere = QtWidgets.QLabel(Dialog_Animal)
        self.label_mammifere.setGeometry(QtCore.QRect(760, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_mammifere.setFont(font)
        self.label_mammifere.setObjectName("label_mammifere")
        self.label_oiseau = QtWidgets.QLabel(Dialog_Animal)
        self.label_oiseau.setGeometry(QtCore.QRect(760, 190, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_oiseau.setFont(font)
        self.label_oiseau.setObjectName("label_oiseau")
        self.label_reptile = QtWidgets.QLabel(Dialog_Animal)
        self.label_reptile.setGeometry(QtCore.QRect(760, 330, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_reptile.setFont(font)
        self.label_reptile.setObjectName("label_reptile")

        self.retranslateUi(Dialog_Animal)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Animal)

    def retranslateUi(self, Dialog_Animal):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Animal.setWindowTitle(_translate("Dialog_Animal", "Dialog Animal"))
        self.label_numero_animal.setText(_translate("Dialog_Animal", "Numéro d\'animal"))
        self.label_erreur_numero_animal_existe_pas.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Le numéro d\'animal n\'existe pas</span></p></body></html>"))
        self.label_erreur_numero_animal_existe.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Le numéro d\'animal existe déjà</span></p></body></html>"))
        self.label_erreur_numero_animal_invalide.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" font-family:\'Arial,sans-serif\'; font-size:9pt; color:#ff0000;\">Entrer deux lettres suivies d’un tiret puis de cinq chiffres.</span></p></body></html>"))
        self.label_surnom_animal.setText(_translate("Dialog_Animal", "Surnom de l\'animal"))
        self.label_poids_animal.setText(_translate("Dialog_Animal", "Poids de l\'animal"))
        self.label_erreur_poids_animal.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" font-family:\'Arial,sans-serif\'; font-size:8pt; color:#ff0000;\">doit être un nombre entier supérieur à 15 lb.</span></p></body></html>"))
        self.label_famille_animal.setText(_translate("Dialog_Animal", "Famille de l\'animal"))
        self.comboBox_famille_animal.setItemText(0, _translate("Dialog_Animal", "Mammifères"))
        self.comboBox_famille_animal.setItemText(1, _translate("Dialog_Animal", "Oiseaux"))
        self.comboBox_famille_animal.setItemText(2, _translate("Dialog_Animal", "Réptiles"))
        self.label_enclos_animal.setText(_translate("Dialog_Animal", "Enclos de l\'animal"))
        self.pushButton_ajouter.setText(_translate("Dialog_Animal", "Ajouter"))
        self.pushButton_rechercher.setText(_translate("Dialog_Animal", "Rechercher"))
        self.comboBox_couleur_poil.setItemText(0, _translate("Dialog_Animal", "Blanc"))
        self.comboBox_couleur_poil.setItemText(1, _translate("Dialog_Animal", "Gris"))
        self.comboBox_couleur_poil.setItemText(2, _translate("Dialog_Animal", "Brun"))
        self.label_couleur_poil.setText(_translate("Dialog_Animal", "Couleur poil"))
        self.label_longueur_bec.setText(_translate("Dialog_Animal", "Longueur bec"))
        self.comboBox_venimeux.setItemText(0, _translate("Dialog_Animal", "True"))
        self.comboBox_venimeux.setItemText(1, _translate("Dialog_Animal", "False"))
        self.label_venimeux.setText(_translate("Dialog_Animal", "Venimeux"))
        self.label_erreur_longueur_bec.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Doit être une valeur réelle positive</span></p></body></html>"))
        self.label_mammifere.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" color:#0000ff;\">Mammifère</span></p></body></html>"))
        self.label_oiseau.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" color:#0000ff;\">Oiseau</span></p></body></html>"))
        self.label_reptile.setText(_translate("Dialog_Animal", "<html><head/><body><p><span style=\" color:#0000ff;\">Réptile</span></p></body></html>"))
