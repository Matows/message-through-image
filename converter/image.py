#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from utils import *


class Image:

    def __init__(self, msgEncode=None, image=None):
        """Prend en paramètres un objet Message ou une image et produit l'autre"""
        checkInputs(msgEncode, image)

        self.msgEncode = msgEncode
        self.algoNumber = self._msgEncode

    def numToPixel(self, nb):
        """Retourne un tuple RGB à partir d'un nombre"""
        pass

    def assemble(self, algoNumber):
        """Prend un tableau de pixel et rajoute les codes d'identifications de l'algorithme"""
        pass
