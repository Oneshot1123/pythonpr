import qrcode
QR=qrcode.make("https://www.youtube.com/")
QR.save("C:\pythonpr\you.png")
import matplotlib.pyplot as p
p.imshow(QR,cmap="twilight")