#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Image:

    def __init__(self, msgEncode=None, image=None):
        """Prend en paramètres un objet Message ou une image et produit l'autre"""
        if msgEncode and image:
            raise ValueError
        self.msgEncode = msgEncode
        self.algoNumber = self._msgEncode

    def numToPixel(self, nb):
        """Retourne un tuple RGB à partir d'un nombre"""
        pass

    def assemble(self, algoNumber)
