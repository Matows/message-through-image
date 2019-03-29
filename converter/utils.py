#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def checkInputs(a, b):
    if a == None and b == None:
        raise ValueError("Un des deux paramètres doit être renseigné")
    elif a != None and b != None:
        raise ValueError("Seulement un des deux paramètres doit être renseigné")
    else:
        pass
