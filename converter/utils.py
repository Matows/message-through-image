#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from inspect import getsource
from hashlib import md5
from string import printable
printable = tuple(printable[:-16]) + tuple(" ")


def checkInputs(a, b):
    if a == None and b == None:
        raise ValueError("Un des deux paramètres doit être renseigné")
    elif a != None and b != None:
        raise ValueError("Seulement un des deux paramètres doit être renseigné")
    else:
        pass


def funcChecksum(func):
    """Renvoie le hash md5 d'une fonction"""
    code = getsource(func)
    code = "".join([line.strip() for line in code.split("\n") if line != ''])
    hash = md5(code.encode())
    return hash.hexdigest()


def lineaire(largeur, hauteur):
    """Générateur qui renvoie un ordre de gauche à droite et de haut en bas

        - Yield les coordonnées sous forme X, Y.
        - Les coordonnées de l'image sont considéré ainsi:

            ┌───────> X (largeur)
            │PPPPPPP
            │PPPPPPP
            │PPPPPPP
            V Y (hauteur)

            P : pixel
    """
    for y in range(hauteur):
        for x in range(largeur):
            yield x, y


def cesar(msg, decalage):
    if decalage >= len(printable):
        raise ValueError("Décalage hors limite")
    msgCrypt = ""
    for char in msg:
        nouvelleLettre = printable.index(char) + decalage
        if nouvelleLettre >= len(printable):
            nouvelleLettre -= len(printable)
        if nouvelleLettre < 0:
            nouvelleLettre += len(printable)
        finalLettre = printable[nouvelleLettre]
        msgCrypt += finalLettre
    return msgCrypt
