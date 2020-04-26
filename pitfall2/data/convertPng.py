#!/usr/bin/env python3
# coding: utf-8

from PIL import Image, ImageDraw

SCRWIDTH = 280
SCRHEIGHT = 192


def convert(file):
    data = bytearray(8192)
    img = Image.open(file)
    pixels = img.load()
    for y in range(SCRHEIGHT):
        offset = ((y & 7) << 10) + ((y & 0x38) << 4) + (y >> 6) * 40
        for x in range(0, SCRWIDTH, 7):
            byte = 0
            if pixels[x, y] in ((255, 255, 255), (10, 10, 10)):
                byte = 0x80
            for j in range(7):
                posX = (x + j)
                posY = y
                pixel = pixels[posX, posY]
                if pixel in ((128, 128, 128), (255, 255, 255)):
                    byte |= (1 << j)
            data[offset + int(x / 7)] = byte
    return data


data = convert('OpenScreen.png')
with open('OpenScreen.bin', 'wb') as file:
    file.write(data)
