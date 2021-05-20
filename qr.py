#!/usr/bin/env python3

import qrcode
import time

# s = https://drive.google.com/file/d/1fKmPDV_c7XqxAmQPulaj_Gm7s_DdiQqv/view?usp=sharing
s = input("give the url to QRCode: \n")
img = qrcode.make(s)
time.sleep(5)
img.save("qr.png")
print("QRCode generated successfully!!")
