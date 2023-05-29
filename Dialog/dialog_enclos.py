#Xavier Rouleau
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_enclos
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Classes.Classe_Enclos import *

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

def cacher_labels_erreur(objet):
    objet.label_erreur_numero_enclos_existe.setVisible(False)
    objet.label_erreur_numero_enclos_existe_pas.setVisible(False)
    objet.label_erreur_validation_numero_enclos.setVisible(False)
    objet.label_erreur_nom_enclos.setVisible(False)

def verifier_enclos(enclos):
    index = 0
    for enclos_ls in Enclos.ls_enclos:
        if enclos_ls.Numero_enclos == enclos.Numero_enclos:
            return True, index
        index += 1
    return False, index

class Fenetreenclos(QtWidgets.QDialog, UI_PY.Dialog_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreenclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Enclos")
        cacher_labels_erreur(self)

    @pyqtSlot()
    def on_pushButton_Ajouter_enclos_clicked(self):
        enclos = Enclos()
        enclos.Numero_enclos = self.lineEdit_numero_enclos.text()
        enclos.Nom_enclos = self.lineEdit_nom_enclos.text()
        enclos.Taille = self.comboBox_taille_enclos.currentText()
        enclos.Type = self.comboBox_type_enclos.currentText()
        enclos.Localisation = self.comboBox_localisation.currentText()

        existe, index = verifier_enclos(enclos)
        if existe:
            self.label_erreur_numero_enclos_existe.setVisible(True)

        if enclos.Numero_enclos == "":
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_validation_numero_enclos.setVisible(True)

        if enclos.Nom_enclos == "":
            self.lineEdit_nom_enclos.clear()
            self.label_erreur_nom_enclos.setVisible(True)

        if enclos.Numero_enclos != "" and enclos.Nom_enclos != "" and not existe:
            Enclos.ls_enclos.append(enclos)
            self.lineEdit_numero_enclos.clear()
            self.lineEdit_nom_enclos.clear()
            cacher_labels_erreur(self)

    @pyqtSlot()
    def on_pushButton_supprimer_enclos_clicked(self):
        enclos = Enclos()
        enclos.Numero_enclos = self.lineEdit_numero_enclos.text()

        existe, index = verifier_enclos(enclos)

        if not existe:
            self.label_erreur_numero_enclos_existe_pas.setVisible(True)
        else:
            Enclos.ls_enclos.pop(index)
            cacher_labels_erreur(self)
