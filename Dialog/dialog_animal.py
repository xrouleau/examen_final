#Xavier Rouleau
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
from Classes.Classe_Animal import *
from Classes.Classe_Mammifere import *
from Classes.Classe_Oiseau import *
from Classes.Classe_Reptile import *
from Classes.Classe_Enclos import *

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


def cacher_labels_erreur(objet):
    objet.label_erreur_numero_animal_existe_pas.setVisible(False)
    objet.label_erreur_numero_animal_existe.setVisible(False)
    objet.label_erreur_numero_animal_invalide.setVisible(False)
    objet.label_erreur_poids_animal.setVisible(False)
    objet.label_erreur_longueur_bec.setVisible(False)


def remplir_combobox_enclos(objet):
    for enclos in Enclos.ls_enclos:
        objet.comboBox_enclos_animal.addItem(str(enclos.Nom_enclos))


def verifier_animal(animal):
    index = 0
    for animal_ls in Animal.ls_animaux:
        if animal_ls.Numero_animal == animal.Numero_animal:
            return True, index
        index += 1
    return False, index


class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")
        cacher_labels_erreur(self)
        remplir_combobox_enclos(self)
        self.comboBox_famille_animal.currentIndexChanged.connect(self.gerer_traits_specifiques)
        self.gerer_traits_specifiques()

    def gerer_traits_specifiques(self):
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            mam = True
        else:
            mam = False
        self.label_mammifere.setVisible(mam)
        self.label_couleur_poil.setVisible(mam)
        self.comboBox_couleur_poil.setVisible(mam)

        if self.comboBox_famille_animal.currentText() == "Oiseaux":
            ois = True
        else:
            ois = False
        self.label_oiseau.setVisible(ois)
        self.label_longueur_bec.setVisible(ois)
        self.lineEdit_longueur_bec.setVisible(ois)

        if self.comboBox_famille_animal.currentText() == "Réptiles":
            rep = True
        else:
            rep = False
        self.label_reptile.setVisible(rep)
        self.label_venimeux.setVisible(rep)
        self.comboBox_venimeux.setVisible(rep)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            animal = Mammifere()
            self.label_mammifere.setVisible(True)
            self.label_couleur_poil.setVisible(True)
            self.comboBox_couleur_poil.setVisible(True)
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            animal = Oiseau()
            self.label_oiseau.setVisible(True)
            self.label_longueur_bec.setVisible(True)
            self.lineEdit_longueur_bec.setVisible(True)
        elif self.comboBox_famille_animal.currentText() == "Réptiles":
            animal = Reptile()
            self.label_reptile.setVisible(True)
            self.label_erreur_poids_animal.setVisible(True)
            self.label_erreur_longueur_bec.setVisible(True)

        animal.Numero_animal = self.lineEdit_numero_animal.text()
        animal.Surnom = self.lineEdit_surnom_animal.text()
        animal.Poids = self.lineEdit_poids_animal.text()
        animal.Famille = self.comboBox_famille_animal.currentText()
        animal.Enclos = self.comboBox_enclos_animal.currentText()

        if self.comboBox_famille_animal.currentText() == "Mammifères":
            animal.Couleur_poil = self.comboBox_couleur_poil.currentText()
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            animal.Longueur_bec = self.lineEdit_longueur_bec.text()
        elif self.comboBox_famille_animal.currentText() == "Réptiles":
            animal.Venimeux = self.comboBox_venimeux.currentText()

        existe, index = verifier_animal(animal)

        if existe:
            self.label_erreur_numero_animal_existe.setVisible(True)

        if animal.Numero_animal == "":
            self.lineEdit_numero_animal.clear()
            self.label_erreur_numero_animal_invalide.setVisible(True)

        if animal.Poids == "":
            self.lineEdit_poids_animal.clear()
            self.label_erreur_poids_animal.setVisible(True)

        if self.comboBox_famille_animal == "Oiseaux":
            if animal.Longueur_bec == "":
                self.label_erreur_longueur_bec.setVisible(True)
                self.lineEdit_longueur_bec.clear()

        if animal.Numero_animal != "" and animal.Poids != "" and not existe:
            def terminer_animal():
                Animal.ls_animaux.append(animal)
                cacher_labels_erreur(self)
                self.lineEdit_numero_animal.clear()
                self.lineEdit_surnom_animal.clear()
                self.lineEdit_poids_animal.clear()

            if self.comboBox_famille_animal.currentText() == "Oiseaux":
                if animal.Longueur_bec != "":
                    terminer_animal()
            else:
                terminer_animal()


    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        animal = Animal()
        animal.Numero_animal = self.lineEdit_numero_animal.text()
        existe, index = verifier_animal(animal)

        if not existe:
            self.label_erreur_numero_animal_existe_pas.setVisible(True)
            self.lineEdit_numero_animal.clear()
        else:
            self.lineEdit_surnom_animal.setText(Animal.ls_animaux[index].Surnom)
            self.lineEdit_poids_animal.setText(Animal.ls_animaux[index].Poids)
            self.comboBox_famille_animal.setCurrentText(Animal.ls_animaux[index].Famille)
            self.comboBox_enclos_animal.setCurrentText(Animal.ls_animaux[index].Enclos)
            if self.comboBox_famille_animal.currentText() == "Mammifères":
                self.comboBox_couleur_poil.setCurrentText(Animal.ls_animaux[index].Couleur_poil)
            elif self.comboBox_famille_animal.currentText() == "Oiseaux":
                self.lineEdit_longueur_bec.setText(Animal.ls_animaux[index].Longueur_bec)
            elif self.comboBox_famille_animal.currentText() == "Réptiles":
                self.comboBox_venimeux.setCurrentText(Animal.ls_animaux[index].Venimeux)
