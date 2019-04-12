#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from utils import *


class Image:

    def __init__(self, objMsg=None, image=None):
        """Prend en paramètres un objet Message ou une image et produit l'inverse"""
        checkInputs(msgEncode, image)

        self.msgEncode = objMsg.msg # Tableau de int
        self.algoNumber = None  # Checksum de l'algo ?

    def numToPixel(self, nb):
        """Retourne une liste RGB à partir d'un nombre
            On part du principe qu'il y a 84 charactère (printable[:-16])
        """
        R = nb
        G = nb
        B = nb
        return [R, G, B]

    def pixelToNum(self, RGB):
        """Retourne un nombre à partir d'un nombre RGB
        """
        #nbR = RGB[0]
        #nbG = RGB[1]
        #nbB = RGB[2]
        #return [nbR, nbG, nbB]
        return RGB[0]

    def assemble(self, algoNumber):
        """Prend un tableau de pixel et rajoute les codes d'identifications de l'algorithme"""
        pass
