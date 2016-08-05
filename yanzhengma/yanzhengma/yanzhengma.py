#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import pytesseract
from PIL import Image


def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table



im = Image.open('Captcha.jpg')


im = im.convert('L')
binaryImage = im.point(initTable(),'1')
#binaryImage.show()

print(pytesseract.image_to_string(binaryImage , config='-psm 7'))