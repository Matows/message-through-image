#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import utils
from PIL import *
from random import randint


class Image:

    def __init__(self, objMsg=None, image=None, sizeImg=None, parcourir=utils.lineaire):
        """Prend en paramètres un objet Message ou une image et produit l'inverse
            A besoin d'un générateur pour connaître l'ordre de lecture
            A besoin d'un tuple sizeImg (largeur,hauteur) > nb_caractères/3 + 2 (pixels de positions) +
        """
        checkInputs(msgEncode, image)
        if type(sizeImg) != tuple:
            raise ValueError("Il manque la valeur de sizeImg")

        #if sizeImg[0]*sizeImg[1] < len()
        self.sizeImg = sizeImg
        self.parcourir = parcourir
        self.msgEncode = objMsg.getEncodedMsg()  # Tableau de int
        self.cryptChecksum = objMsg.getCryptChecksum

    def numToPixel(self, nb):
        """Retourne une liste RGB à partir d'un nombre
            On part du principe qu'il y a 84 charactère (printable[:-16])
        """
        R = nb//16
        G = int((nb*nb)/300)
        V = nb % 16
        return [R, G, B]

    def pixelToNum(self, RGB):
        """Retourne un nombre à partir d'un nombre RGB
        """
        nbR = RGB[0]
        nbG = RGB[1]
        nbB = RGB[2]
        nb = nbR*16 + nbV
        return [nb]

    def assemble(self, RGBTab):
        """Prend un tableau de pixel et rajoute un pixel au debut (position début checksums) et 11 à la fin (checksums)
            Retourne un tableau de pixel (une dimension)
            size: tuple (largeur,hauteur)
            RGBTab: liste sous la forme [[r1, g1, b1], [r2, g2, b2], ...]
        """

        positionDebutChecksums = 1 + len(RGBTab)
        # On convertie en liste de bit
        positionDebutChecksums = list(bin(positionDebutChecksums)[2:])
        # On remplie avec des 0 si besoin
        while len(positionDebutChecksums) < 16:
            positionDebutChecksums.insert(0, "0")
        # On écrit les valeurs du premier pixel
        Rposition = int("".join(positionDebutChecksums[:8]), 2)
        Gposition = int("".join(positionDebutChecksums[8:]), 2)
        Bposition = randint(0, 255)
        position = [Rposition, Gposition, Bposition]
        # Par déduction:
        # px[0] > lire position debut params
        # msg = px[1]...px[positionDebutParams-1]
        # checksums = px[positionDebutParams]..px[positionDebutParams+6*2]

        parcourirChecksum = utils.funcChecksum(self.parcourir)
        checksums = list(parcourirChecksum + self.cryptChecksum)
        # Convertion en tableau de valeurs entre 0 et 255
        pxChecksums = [ int(checksums[x] + checksums[x+1], 16)
                       for x in range(len(checksums))
                       if x % 2 == 0]
        # Regroupement par 3
        pxChecksumsFinal = [ [ pxChecksums[x], pxChecksums[x+1], pxChecksums[x+2] ]
                        for x in range(len(pxChecksums)-2)
                        if x % 3 == 0]
        # Ajout des deux pixels menquant
        pxChecksumsFinal.append([ pxChecksums[-2], pxChecksums[-1], randint(0, 255) ])



        final = []
        final.extend(position)
        final.extend(RGBTab)
        final.extend(pxChecksumsFinal)


    def lecture(self, imgTab):
        """Retourne des listes de valeurs RGB"""
        R = imgTab[0]
        G = imgTab[1]
        B = imgTab[2]
        return [R, G, B]
