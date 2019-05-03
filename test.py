import message
import image
import utils
msg = message.Message(msg="salut le monde!", crypt=utils.cesar, cryptKArgs={"decalage": 1})
print(msg.getEncodedMsg())
img = image.Image(objMsg=msg, sizeImg=(6, 6))
imageEncode = img.getImage()

imgBack = image.Image(objImg=imageEncode)
msgBack = message.Message(objImg=imgBack, crypt=utils.cesar, cryptKArgs={"decalage": -1})
print(msgBack.getClearMsg())


# DOIT ÊTRE SAUVEGARDER AU FORMAT PNG!!
