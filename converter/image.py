#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import utils
from random import randint
from PIL import Image as PILImage


class Image:

    def __init__(self, objMsg=None, objImg=None, sizeImg=None, parcourir=utils.lineaire):
        """Prend en paramètres un objet Message ou une image et produit l'inverse
            A besoin d'un générateur pour connaître l'ordre de lecture
            A besoin d'un tuple sizeImg (largeur,hauteur) > nb_caractères + 1 (pixels de position) + 11 (checksums)
        """
        utils.checkInputs(objMsg, objImg)
        self.parcourir = parcourir

        # Partie dépendante de si on encode ou décode
        if objMsg:
            if type(sizeImg) != tuple:
                raise ValueError("Il manque la valeur de sizeImg")

            self.sizeImg = sizeImg
            self.msgEncode = objMsg.getEncodedMsg()  # Tableau de int
            self.cryptChecksum = objMsg.getCryptChecksum()

            if sizeImg[0]*sizeImg[1] < len(self.msgEncode) + 12:
                raise ValueError("La taille de l'image choisi est trop petite. Elle doit faire plus de {} pixels".format(
                    len(self.msgEncode) + 12))
        else:
            self.sizeImg = objImg.size
            self.image = objImg

    def numToPixel(self, nb):
        """Retourne une liste RGB à partir d'un nombre
            On part du principe qu'il y a 84 charactères (printable[:-16])
        """
        R = nb//16
        G = int((nb*nb)/300)
        B = nb % 16
        return [R, G, B]

    def pixelToNum(self, RGB):
        """Retourne un nombre à partir d'un nombre RGB"""
        nbR = RGB[0]
        nbG = RGB[1]
        nbB = RGB[2]
        nb = nbR*16 + nbB
        return nb

    def assemble(self):
        """Prend un tableau de pixel et rajoute un pixel au debut (position début checksums) et 11 à la fin (checksums)
            Retourne un tableau de pixel (une dimension)
        """
        # Par déduction:
        # px[0] > lire position debut params
        # msg = px[1]...px[positionDebutParams-1]
        # checksums = px[positionDebutParams]..px[positionDebutParams+6*2]

        positionDebutChecksums = 1 + len(self.msgEncode)
        # On convertie en liste de bit
        positionDebutChecksums = list(bin(positionDebutChecksums)[2:])
        # On remplie avec des 0 si besoin
        while len(positionDebutChecksums) < 16:
            positionDebutChecksums.insert(0, '0')
        # On écrit les valeurs du premier pixel
        Rposition = int("".join(positionDebutChecksums[:8]), 2)
        Gposition = int("".join(positionDebutChecksums[8:]), 2)
        Bposition = randint(0, 255)
        position = [Rposition, Gposition, Bposition]

        parcourirChecksum = utils.funcChecksum(self.parcourir)
        checksums = list(parcourirChecksum + self.cryptChecksum)
        # Convertion en tableau de valeurs entre 0 et 255
        pxChecksums = [int(checksums[x] + checksums[x+1], 16)
                       for x in range(len(checksums))
                       if x % 2 == 0]
        # Regroupement par 3
        pxChecksumsFinal = [[pxChecksums[x], pxChecksums[x+1], pxChecksums[x+2]]
                            for x in range(len(pxChecksums)-2)
                            if x % 3 == 0]
        # Ajout des deux pixels menquant
        pxChecksumsFinal.append([pxChecksums[-2], pxChecksums[-1], randint(0, 255)])

        final = []  # Liste à une dimenstion représentant les pixels
        final.append(position)
        final.extend(self.formatMsg(self.msgEncode))
        final.extend(pxChecksumsFinal)

        nbPxManquant = self.sizeImg[0] * self.sizeImg[1] - len(final)
        while nbPxManquant > 0:
            final.append([randint(0, 255), randint(0, 255), randint(0, 255)])
            nbPxManquant = self.sizeImg[0] * self.sizeImg[1] - len(final)

        return final

    def desassemble(self):
        listePx = self.getListePx()
        position = listePx[0]
        positionDebutChecksums = int(self._tupleToBinary(position[0], position[1]), 2)

        msg = listePx[1:positionDebutChecksums]
        msg = [self.pixelToNum(lettre) for lettre in msg]

        checksums = listePx[positionDebutChecksums:positionDebutChecksums+11]
        checksumsFinal = []
        for pixel in checksums:
            checksumsFinal.extend(pixel)
        checksumsFinal.pop()  # on enlève le nombre aléatoire
        checksumsFinal = [hex(nb)[2:] for nb in checksumsFinal]  # on convertie en hexa
        # Dans le cas ou on a "0" au lieu de "00"...
        checksumsFinal = ["0" + nb for nb in checksums if len(nb) == 1]

        parcourirCS = "".join(checksumsFinal[:16])
        cryptCS = "".join(checksumsFinal[16:])

        if parcourirCS != self.getParcourirChecksum():
            print("ATTENTION: le générateur que vous utiliser pour parcourir l'image n'est pas le même que l'original")

        return msg, parcourirCS, cryptCS

    def _tupleToBinary(self, r, g):
        r = bin(r)[2:]
        g = bin(g)[2:]

        while len(r) < 4:
            r = '0' + r
        while len(g) < 4:
            g = '0' + g
        return r + g

    def formatMsg(self, msg):
        """Transforme le message (liste d'entiers) en liste de pixel"""
        return [self.numToPixel(nb) for nb in msg]

    def unformatMsg(self, msgPx):
        """Transforme le pixel [R,G,B] en un entier"""
        return [self.pixelToNum(RGB) for RGB in msgPx]

    def getImage(self):
        """Retourne un objet Image"""
        imgFinal = PILImage.new("RGB", self.sizeImg)
        listePx = self.assemble()
        for n, (x, y) in enumerate(self.parcourir(*self.sizeImg)):
            imgFinal.putpixel((x, y), tuple(listePx[n]))
        return imgFinal

    def getListePx(self):
        """Retourne une liste de pixel (position + message + checksums + aléatoire)"""
        listePx = []
        for x, y in self.parcourir(*self.sizeImg):
            listePx.append(list(self.image.getpixel((x, y))))
        return listePx

    def getParcourirChecksum(self):
        return utils.funcChecksum(self.parcourir)
