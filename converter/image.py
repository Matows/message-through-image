#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from utils import *


class Image:

    def __init__(self, objMsg=None, image=None):
        """Prend en paramètres un objet Message ou une image et produit l'inverse"""
        checkInputs(msgEncode, image)

        self.msgEncode = objMsg.msg # Tableau de int
        self.sumAlgoCrypt = None  # Checksum de l'algo ?

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
        nb = RGB[0]
        return nb

    def assemble(self, size):
        """Prend un tableau de pixel et rajoute les codes d'identifications de l'algorithme"""
        pass

    def lecture(self, imgTab):
        """Retourne des listes de valeurs RGB"""
        R = imgTab[0]
        G = imgTab[1]
        B = imgTab[2]
        return [R, G, B]
