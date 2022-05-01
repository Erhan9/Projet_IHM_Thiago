#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kapucu
"""

import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QTextEdit, QFormLayout, QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPixmap

from Interface2 import View2
#from Interface3 import View3


class View1(QWidget):
    def __init__(self, ctrl):
        super().__init__()

        self.myCtrl = ctrl

        self.Interface2 = View2(self)

        self.labelImage = QLabel(self)

        self.pixmap = QPixmap('image1.JPEG')

        self.labelImage.setPixmap(self.pixmap)
        self.labelImage.resize(self.pixmap.width(), self.pixmap.height())

        self.labelNom = QLabel(self)
        self.labelNom.setText('Erhanolib')

        self.labelMsg = QLabel(self)
        self.labelMsg.setText('Bienvenue ;-)')

        self.creer = QPushButton('Creer')
        self.creer.setToolTip('Modifier le dossier d un patient')
        
        self.charger = QPushButton('Charger')
        self.charger.setToolTip('Charger le dossier d un patient')

        self.init_ui()

        self.show()

    def init_ui(self):

        h_box_image = QHBoxLayout()
        h_box_image.addWidget(self.labelImage)

        h_box_label = QHBoxLayout()
        h_box_label.addWidget(self.labelNom)

        h_box_msg = QHBoxLayout()
        h_box_msg.addWidget(self.labelMsg)

        v_box_b = QVBoxLayout()
        v_box_b.addWidget(self.creer)
        v_box_b.addWidget(self.charger)

        v_box = QVBoxLayout()

        v_box.addLayout(h_box_image)
        v_box.addLayout(h_box_label)
        v_box.addLayout(h_box_msg)
        v_box.addLayout(v_box_b)

        self.labelNom.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMsg.setAlignment(QtCore.Qt.AlignCenter)

        self.creer.clicked.connect(self.creer1)

        self.setLayout(v_box)
        self.setWindowTitle('Fenêtre d accueil')

        self.show()

    def creer1(self):
        self.hide()
        self.Interface2.show()


# %%

class Controller:
    def __init__(self, model):
        self.myModel = model

    def creer2(self, name):
        pass

# %%

class Model:
    def __init__(self):
        pass

    def creer3(self, name):
        pass

print(__name__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    ctrl = Controller(model)
    view = View1(ctrl)
    sys.exit(app.exec_())
