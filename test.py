#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from converter import *
# On créer le message
msg = message.Message(msg="salut le monde!", crypt=utils.cesar, cryptKArgs={"decalage": 1})
# On passe le message à la classe Image
img = image.Image(objMsg=msg, sizeImg=(6, 6))
# On en sort un objet PIL.Image.Image
imageEncode = img.getImage()
# On la sauvegarde
imageEncode.save("img.png")

# On charge l'objet image dans Image
imgBack = image.Image(objImg=imageEncode)
# On passe le message décodé par Image dans Message
msgBack = message.Message(objImg=imgBack, crypt=utils.cesar, cryptKArgs={"decalage": -1})
# On affiche le message initial
print(msgBack.getClearMsg())

# L'IMAGE DOIT ÊTRE SAUVEGARDER AU FORMAT PNG!!
