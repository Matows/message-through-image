#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import utils
from utils import printable


class Message:
    """Classe représentant le Message.

        Message d'origine dans self.originMsg
        Message encodé dans self.encodedMsg
        checksum de la fonction de cryptage (si défini) dans self.cryptFuncChecksum
    """

    def __init__(self, msg=None, objImg=None, crypt=None, cryptKArgs=None):
        """Initialie l'objet.
            Paramètres:
            - Le message
            - La fonction de cryptage (optionel)
            - Le dictionnaire de paramètre (optionel) à passer au cryptage
        """
        utils.checkInputs(msg, objImg)  # Un seul des deux paramètres doivent être passé
        self.crypt = crypt
        self.cryptKArgs = cryptKArgs
        if msg:
            self._msgOrigin = self.checkConformity(msg)
        else:
            self._msg, self.parcourirCS, self.cryptCS = objImg.desassemble()
            if self.cryptCS != '0'*32 and self.cryptCS != self.getCryptChecksum():
                print("ATTENTION: L'algorithme de cryptage de départ est différent de celui donné",
                      f"Expected:{self.getCryptChecksum()}", f"Got:{self.cryptCS}", sep="\n")

    def getEncodedMsg(self):
        """Retourne le message sous forme de tableau d'entier"""
        if self.crypt:  # Cryptage si défini
            self._msg = self.crypt(self._msgOrigin, **self.cryptKArgs)
        else:
            self._msg = self._msgOrigin
        self._msg = [self.charToInt(lettre)
                     for lettre in self._msg]  # On convertie en liste de lettre
        return self._msg

    def getClearMsg(self):
        msg = "".join([self.intToChar(nb) for nb in self._msg])
        msgUncrypt = self.crypt(msg, **self.cryptKArgs)
        return msgUncrypt

    def getCryptChecksum(self):
        if self.crypt:
            return utils.funcChecksum(self.crypt)
        else:
            return '0'*32

    def checkConformity(self, msg):
        """Lève une exception ValueError si le message n'est pas conforme"""
        # TODO: Voir si on ne peut pas transmettre des caractères français via la table ascii (voir fonction ascii())
        for lettre in msg:
            if lettre not in printable:
                raise ValueError("Un des caractères n'est pas autorisé")
        return msg.strip()

    def charToInt(self, char):
        """Retourne un int utilisable pour l'encodage"""
        if char in printable:
            return printable.index(char)

    def intToChar(self, nb):
        """Retourne un caractère à partir d'un nombre"""
        return printable[nb]

    def msgOrigin():
        """Propriété controllant l'accès à l'attribut _msgOrigin"""
        # TODO: Géré un nouveau message

        def fget(self):
            return self._msgOrigin

        def fset(self, newMsg):
            self._msgOrigin = self.checkConformity(newMsg)

        return locals()
    msgOrigin = property(**msgOrigin())

    def msg():
        """Propriété empêchant l'écriture de l'attribut _msg"""

        def fget(self):
            return self._msg

        def fset(self):
            print("Il est interdit de changer directement le message final")

        return locals()
    msg = property(**msg())
