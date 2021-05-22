#!/usr/bin/env python3

import qrcode

# example of s: s = https://github.com/TasosTzaras
# s can be any URL we would like to make a QR code of

s = input("give the url to QRCode: \n")
img = qrcode.make(s)
img.save("qr.png")
print("QRCode generated successfully!!")
