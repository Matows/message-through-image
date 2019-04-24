#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from utils import *
from PIL import *


class Image:

    def __init__(self, objMsg=None, image=None):
        """Prend en paramètres un objet Message ou une image et produit l'inverse"""
        checkInputs(msgEncode, image)

        self.msgEncode = objMsg.msg  # Tableau de int
        self.sumAlgoCrypt = None  # Checksum de l'algo ?

    def numToPixel(self, nb):
        """Retourne une liste RGB à partir d'un nombre
            On part du principe qu'il y a 84 charactère (printable[:-16])
        """
        nbR = nb//16
        nbG = int((nb*nb)/300)
        nbV = nb%16
        R = nbR
        G = nbG
        B = nbV
        return [R, G, B]

    def pixelToNum(self, RGB):
        """Retourne un nombre à partir d'un nombre RGB
        """
        nbR = RGB[0]
        nbG = RGB[1]
        nbB = RGB[2]
        nb = nbR*16 + nbV
        return [nb]

    def assemble(self, size, RGBTab, newVal):
        """Prend un tableau de pixel et rajoute les codes d'identifications de l'algorithme"""
        if size in RGBTab[0][1] or size in RGBTab[0][2]:
            return RGBTab.append(newVal)
        else:
            im = Image.new('RGB', size)
            im.append(newVal)

    def lecture(self, imgTab):
        """Retourne des listes de valeurs RGB"""
        R = imgTab[0]
        G = imgTab[1]
        B = imgTab[2]
        return [R, G, B]
