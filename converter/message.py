#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from string import printable
printable = tuple(printable[:-16])


class Message(object):
    """Classe représentant le Message"""
    # Le message en lui même est conservé tout au long du traitement dans self._msg

    def __init__(self, msg):
        self._msg = self.checkASCII(msg)

    def checkASCII(self, msg):
        """Retourne une string conforme ou lève une exception"""
        # TODO: Voir si on ne peut pas transmettre des caractères français via la table ascii (voir fonction ascii())
        pass

    def crypt(self):
        """Retourne le message crypté.
            Cette classe peut être surchargé pour modifié l'algorithme de
            cryptage.
            A chaque algorithme doit être associé un nombre qui doit être retourné avec le message crypté.
        """
        pass

    def charToInt(self, char):
        """Prend en paramètre un charactère et renvoie un int utilisable pour l'encodage"""
        if char not in printable:
            pass
        else:
            return printable.index(char)

    def msg():
        """Propriété controllant l'accès à l'attribut msg"""

        def getMsg(self):
            return self._msg

        def setMsg(self, newMsg):
            self._msg = self.checkASCII(newMsg)

        return locals()
    msg = property(**msg())
