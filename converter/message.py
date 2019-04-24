#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from string import printable
from utils import *
printable = tuple(printable[:-16])


class Message:
    """Classe représentant le Message"""
    # Le message en lui même est conservé tout au long du traitement dans self._msg

    def __init__(self, msg=None, msgEncode=None):
        """Prend en paramètres un objet message encodé ou une image et produit l'inverse"""
        checkInputs(msg, msgEncode)  # Un seul des deux paramètres doivent être passé
        self._msg = self.checkConformity(msg)

        ### Paramètres ####
        # cryptage
        self._key = 0
        self.algoNumber = 0

    def checkConformity(self, msg):
        """Retourne une string conforme (ascii) ou lève une exception"""
        # TODO: Voir si on ne peut pas transmettre des caractères français via la table ascii (voir fonction ascii())
        for i in range(0,len(msg)):
            if msg[i] in printable :
                pass
            else:
                print ("Erreur, charactère invalide en ", i)
        return msg

    def crypt(self, key=None, algoNumber=None):
        """Crypte le message contenu dans _msg. Ne retourne rien
            Cette classe peut être surchargé pour modifié l'algorithme de
            cryptage.
            A chaque algorithme doit être associé un nombre qui doit être retourné avec le message crypté.
        """
        # On peut imaginer que les algorithmes de cryptage sois stocké dans un fichier
        # Si on veut qu'une méthode sois forcément écrite par un dev, il faut raise NotImplementedError
        if not key:
            key = self._key
        if not algoNumber:
            algoNumber = self.algoNumber

        pass

    def charToInt(self, char):
        """Retourne un int utilisable pour l'encodage"""
        if char not in printable:
            pass
        else:
            return printable.index(char)

    def cleanMessage(self, msg):
        """Sert à nettoyer le message avant qu'il soit utilisé."""
        return msg.strip()

    def msg():
        """Propriété controllant l'accès à l'attribut msg"""

        def fget(self):
            return self._msg

        def fset(self, newMsg):
            self._msg = self.checkConformity(newMsg)

        return locals()
    msg = property(**msg())
