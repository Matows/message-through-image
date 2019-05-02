#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import utils
from string import printable
printable = tuple(printable[:-16])


class Message:
    """Classe représentant le Message.

        Message d'origine dans self.originMsg
        Message encodé dans self.encodedMsg
        checksum de la fonction de cryptage (si défini) dans self.cryptFuncChecksum
    """
    def __init__(self, msg=None, msgEncode=None, crypt=None, cryptKArgs=None):
        """Initialie l'objet.
            Paramètres:
            - Le message
            - La fonction de cryptage (optionel)
            - Le dictionnaire de paramètre (optionel) à passer au cryptage
        """
        utils.checkInputs(msg, msgEncode)  # Un seul des deux paramètres doivent être passé
        self._msgOrigin = self.checkConformity(msg)

        self.crypt = crypt
        self.cryptKArgs = cryptKArgs

    def getEncodedMsg(self):
        """Retourne le message sous forme de tableau d'entier"""
        if self.crypt: # Cryptage si défini
            self._msg = self.crypt(self._msgOrigin, **self.cryptKArgs)
        else:
            self._msg=self._msgOrigin
        self._msg = [self.charToInt(lettre) for lettre in self._msg] # On convertie en liste de lettre
        return self._msg

    def getCryptChecksum(self):
        return utils.funcChecksum(self.crypt)

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
