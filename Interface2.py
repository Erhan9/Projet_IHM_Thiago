#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kapucu
"""

from PyQt5.QtGui import QIntValidator, QPixmap, QFont
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup,
                             QTextEdit, QApplication, QLabel, QWidget, QRadioButton, QToolTip)



class View2(QWidget):
    def __init__(self, precedent):
        super().__init__()

        self.prec = precedent

        self.nom1 = QLabel(self)
        self.nom1.setText('Nom')
        self.prenom1 = QLabel(self)
        self.prenom1.setText('Prenom')
        self.age1 = QLabel(self)
        self.age1.setText('Age')
        self.sexe1 = QLabel('Sexe')
        self.btnM = QRadioButton('M')
        self.btnF = QRadioButton('F')

        self.nom = QLineEdit(self)
        self.prenom = QLineEdit(self)
        self.age = QLineEdit(self)
        self.sexe = QButtonGroup()
        self.sexe.addButton(self.btnM)
        self.sexe.addButton(self.btnF)

        self.docteur=QTextEdit(self)
        self.propositionmedicament=QTextEdit(self)
        
        self.medicament = {"Doliprane":['douleur','fievre','paracetamol','gelules']}

        QToolTip.setFont(QFont('Calibri', 13))
        self.enregis1 = QPushButton('Sauvegarder')
        self.enregis1.setToolTip('Enregistrer les informations dans le fichier du patient')

        self.quit1 = QPushButton('Fermer')
        self.quit1.setToolTip('Revenir au menu principal')
        
        self.btnHistorik = QPushButton('Historique')
        self.btnHistorik.setToolTip('Afficher l historique du patient')


        self.init_ui()

    def init_ui(self):

        h_box_nom = QHBoxLayout()
        h_box_nom.addWidget(self.nom1)
        h_box_nom.addWidget(self.nom)

        h_box_prenom = QHBoxLayout()
        h_box_prenom.addWidget(self.prenom1)
        h_box_prenom.addWidget(self.prenom)

        h_box_age = QHBoxLayout()
        h_box_age.addWidget(self.age1)
        h_box_age.addWidget(self.age)

        h_box_sexe = QHBoxLayout()
        h_box_sexe.addWidget(self.sexe1)
        h_box_sexe.addWidget(self.btnM)
        h_box_sexe.addWidget(self.btnF)

        h_box_historik = QHBoxLayout()
        h_box_historik.addWidget(self.btnHistorik)

        v_box_1 = QVBoxLayout()
        v_box_1.addLayout(h_box_nom)
        v_box_1.addLayout(h_box_prenom)
        v_box_1.addLayout(h_box_age)
        v_box_1.addLayout(h_box_sexe)

        h_box_2 = QHBoxLayout()
        h_box_2.addLayout(h_box_historik)

        h_box_3 = QHBoxLayout()
        h_box_3.addLayout(v_box_1)
        h_box_3.addLayout(h_box_2)

        h_box_4 = QHBoxLayout()
        h_box_4.addWidget(self.docteur)
        h_box_4.addWidget(self.propositionmedicament)

        h_box_btn = QHBoxLayout()
        h_box_btn.addWidget(self.quit1)
        h_box_btn.addWidget(self.enregis1)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box_3)
        v_box.addLayout(h_box_4)
        v_box.addLayout(h_box_btn)
        
        self.docteur.setDisabled(False)
        self.propositionmedicament.setDisabled(True)

        self.setLayout(v_box)
        self.setWindowTitle('Dossier patient')

        self.quit1.clicked.connect(self.quit2)
        self.enregis1.clicked.connect(self.enregis2)

    def quit2(self):
        self.hide()
        self.prec.show()

    def enregis2(self):
        self.nomstr = self.nom.text()
        self.prenomstr = self.prenom.text()
        self.agestr = self.age.text()
        
        if self.btnF.isChecked():
            self.sexe = 'F'

        elif self.btnM.isChecked():
            self.sexe = 'H'
            
        else:
            self.sexe = ''
        
        print(self.nomstr)
        print(self.prenomstr)
        fichier=open(self.nomstr+' '+self.prenomstr+'.txt','a')
        fichier.write(self.nomstr+','+self.prenomstr+','+self.agestr+','+self.sexe)
        fichier.close()
        