#Xavier Rouleau
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import UI_PY.Dialog_veterinaire
from PyQt5 import QtWidgets
from Classes.Classe_Enclos import *
from Classes.Classe_Veterinaire import *

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
def verifier_vet(vet):
    index = 0
    for v in Veterinaire.ls_veterinaire:
        if v.Numero_emp == vet.Numero_emp:
            return True, index
        index += 1
    return False, index

def remplir_combobox_enclos(objet):
    for enclos in Enclos.ls_enclos:
        objet.comboBox_enclos_animal.addItem(str(enclos.Numero_enclos))

def cacher_labels_erreur(objet):
    objet.label_erreur_numero_employe__existe.setVisible(False)
    objet.label_erreur_numero_employe_invalide.setVisible(False)
    objet.label_erreur_numero_employe_existe_pas.setVisible(False)
    objet.label_erreur_nom_employe.setVisible(False)
    objet.label_erreur_prenom_employe.setVisible(False)
    objet.label_erreur_date_naiss.setVisible(False)

class Fenetreveterinaire(QtWidgets.QDialog, UI_PY.Dialog_veterinaire.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreveterinaire, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Vétérinaire")
        remplir_combobox_enclos(self)
        cacher_labels_erreur(self)
        self.model = QStandardItemModel()
        self.listView_liste_enclos.setModel(self.model)
        self.ls_enclos = []

    @pyqtSlot()
    def on_pushButton_ajouter_enclos_liste_clicked(self):
        item = QStandardItem("L'enclos: "+self.comboBox_enclos_animal.currentText())
        self.model.appendRow(item)
        for e in Enclos.ls_enclos:
            if e.Numero_enclos == self.comboBox_enclos_animal.currentText():
                self.ls_enclos.append(e)


    @pyqtSlot()
    def on_pushButton_ajout_veterinaire_clicked(self):
        vet = Veterinaire()
        vet.Numero_emp = self.lineEdit_numero_employe.text()
        vet.Nom = self.lineEdit_nom_employe.text()
        vet.Prenom = self.lineEdit_prenom_employe.text()
        vet.Date_naiss = self.dateEdit_datenaiss_employe.date()
        vet.list_enclos = self.ls_enclos

        existe, index = verifier_vet(vet)
        if existe:
            self.label_erreur_numero_employe__existe.setVisible(True)
            self.lineEdit_numero_employe.clear()

        if vet.Numero_emp == "":
            self.label_erreur_numero_employe_invalide.setVisible(True)
            self.lineEdit_numero_employe.clear()

        if vet.Nom == "":
            self.label_erreur_nom_employe.setVisible(True)
            self.lineEdit_nom_employe.clear()

        if vet.Prenom == "":
            self.label_erreur_prenom_employe.setVisible(True)
            self.lineEdit_prenom_employe.clear()

        if vet.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible(True)
            self.dateEdit_datenaiss_employe.clear()

        if vet.Numero_emp != "" and vet.Nom != "" and vet.Prenom != "" and vet.Date_naiss != "" and not existe:
            cacher_labels_erreur(self)
            vet.serialiser()
            self.lineEdit_numero_employe.clear()
            self.lineEdit_nom_employe.clear()
            self.lineEdit_prenom_employe.clear()
            self.dateEdit_datenaiss_employe.clear()
