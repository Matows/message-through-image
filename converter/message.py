#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from string import printable
printable = tuple(printable[:-16])


class Message:
    """Classe représentant le Message"""
    # Le message en lui même est conservé tout au long du traitement dans self._msg

    def __init__(self, msg=False):
        self._msg = self.checkConformity(msg)

        ### Paramètres ####
        # cryptage
        self._key = 0
        self.algoNumber = 0

    def checkConformity(self, msg):
        """Retourne une string conforme (ascii) ou lève une exception"""
        # TODO: Voir si on ne peut pas transmettre des caractères français via la table ascii (voir fonction ascii())
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

    def msg():
        """Propriété controllant l'accès à l'attribut msg"""

        def fget(self):
            return self._msg

        def fset(self, newMsg):
            self._msg = self.checkConformity(newMsg)

        return locals()
    msg = property(**msg())
