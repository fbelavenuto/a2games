#!/usr/bin/env python3
# coding: utf-8

from PIL import Image, ImageDraw

SCRWIDTH = 280
SCRHEIGHT = 192


def plotImg(data):
    img = Image.new('RGB', (SCRWIDTH, SCRHEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    p = 0
    for y in range(SCRHEIGHT):
        offset = ((y & 7) << 10) + ((y & 0x38) << 4) + (y >> 6) * 40
        for x in range(0, SCRWIDTH, 7):
            byte = data[offset + int(x / 7)]
            colorMod = (byte & 0x80) == 0x80
            for j in range(7):
                color = (10, 10, 10) if colorMod else (0, 0, 0)
                if byte & (1 << j):
                    color = (255, 255, 255) if colorMod else (128, 128, 128)
                posX = (x + j)
                posY = y
                draw.point([posX,   posY],   fill=color)
    img.save('out.png', 'PNG')


with open('OpenScreen.bin', 'rb') as file:
    data = file.read(8192);
plotImg(data)
