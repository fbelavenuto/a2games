#!/usr/bin/env python3
# coding: utf-8

import argparse
from PIL import Image, ImageDraw

SCRWIDTH = 280
SCRHEIGHT = 192
HGRSIZE = 8192

def hgr2png(binFile, pngFile):
    with open(binFile, 'rb') as file:
        data = file.read(HGRSIZE);
    img = Image.new('RGB', (SCRWIDTH, SCRHEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
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
    img.save(pngFile, 'PNG')


def png2hgr(pngFile, binFile):
    data = bytearray(HGRSIZE)
    img = Image.open(pngFile)
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
    with open(binFile, 'wb') as file:
        file.write(data)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Apple2 HGR utils')
    parser.add_argument('-i', '--input', help='input filename')
    parser.add_argument('-o', '--output', help='output filename')
    parser.add_argument('-b', '--bin', help='bin to png', action='store_true', default=False)
    parser.add_argument('-p', '--png', help='png to bin', action='store_true', default=False)

    args = parser.parse_args()

    if not args.bin and not args.png:
        parser.print_help()
        exit(0)

    if args.input is None or args.output is None:
        parser.print_help()
        exit(0)

    if args.bin:
        hgr2png(args.input, args.output)
    elif args.png:
        png2hgr(args.input, args.output)

