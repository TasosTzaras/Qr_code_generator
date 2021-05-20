#!/usr/bin/env python3

import qrcode

# s = https://github.com/TasosTzaras
s = input("give the url to QRCode: \n")
img = qrcode.make(s)
img.save("qr.png")
print("QRCode generated successfully!!")
