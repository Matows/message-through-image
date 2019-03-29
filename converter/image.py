 #!/usr/bin/env python3
# -*- coding:utf-8 -*-

from utils import *


class Image:

    def __init__(self, msgEncode=None, image=None):
        """Prend en paramètres un objet Message ou une image et produit l'inverse"""
        checkInputs(msgEncode, image)

        self.msgEncode = msgEncode
        self.algoNumber = None  # Checksum de l'algo ?

    def numToPixel(self, nb):
        """Retourne un tuple RGB à partir d'un nombre"""
        with open("valeurs_RGB.csv",'r') as file:

        pass

    def assemble(self, algoNumber):
        """Prend un tableau de pixel et rajoute les codes d'identifications de l'algorithme"""
        pass
