#!/usr/bin/env python3

import qrcode

# s = https://www.linkedin.com/in/tasos-tzaras-04910b213/
    
def qr_generator(link):
    img = qrcode.make(link)
    img.save("qr.png")
    print("QRCode generated successfully!!")
    
if __name__=='__main__':
    s = input("give the url to QRCode: \n")
    qr_generator(s))
