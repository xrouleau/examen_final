#Xavier Rouleau
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItem, QStandardItemModel

import UI_PY.DialogRecherche
from PyQt5 import QtWidgets
from Classes.Classe_Enclos import *
from Classes.Classe_Animal import *

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


def remplir_combobox(objet):
    for enclos in Enclos.ls_enclos:
        objet.comboBox_enclos_animal.addItem(str(enclos.Numero_enclos))


class Fenetrerecherche(QtWidgets.QDialog, UI_PY.DialogRecherche.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrerecherche, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Recherche")
        remplir_combobox(self)


    @pyqtSlot()
    def on_pushButton_afficher_clicked(self):
        model = QStandardItemModel()
        self.listView_list_animaux.setModel(model)
        for e in Animal.ls_animaux:
            if e.Enclos == self.comboBox_enclos_animal.currentText():
                item = QStandardItem(e.Numero_animal+" nommé: "+e.Surnom)
                model.appendRow(item)
