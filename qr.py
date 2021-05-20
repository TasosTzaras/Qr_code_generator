#!/usr/bin/env python3

import qrcode
import time

# s = https://github.com/TasosTzaras
s = input("give the url to QRCode: \n")
img = qrcode.make(s)
time.sleep(5)
img.save("qr.png")
print("QRCode generated successfully!!")
