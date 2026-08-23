#!/usr/bin/env python3

from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import sys, os

register_heif_opener()

targetRatio = 16 / 9
x = 0
imageDir = os.listdir("/home/srogue/epaper/friends/newImages")
cropDir = os.listdir("/home/srogue/epaper/friends/cropped")
lengthD = len(cropDir) + 1


while (x < len(imageDir)):
    (os.listdir())
    #tester = "IMG_" + str(x)
    filename = imageDir[x]
    tester = "/home/srogue/epaper/friends/newImages/" + imageDir[x]
    print(tester + "\n")
    outfile = "/home/srogue/epaper/friends/cropped/crop" + str(lengthD) + ".jpg"
    try:
        im = Image.open(tester)
        im = ImageOps.exif_transpose(im)
        im = im.convert("L")
        print(im.format, im.size, im.mode)

        im = im.copy()
        #im.show()
        try:
            im.save(outfile)
        except:
            print("\n Failed to save file\n")
        width, height = im.size
        ratio = width / height
        if width != 960 or height != 540:
            if ratio > targetRatio:
                # Too wide → crop left and right
                new_width = height * targetRatio
                left = (width - new_width) / 2
                box = (left, 0, left + new_width, height)

            else:
                # Too tall → crop top and bottom
                new_height = width / targetRatio
                top = (height - new_height) / 2
                box = (0, top, width, top + new_height)

            print(box)

            y = im.crop(box)

            print("\nAfter crop:", y.size)

            #y.show()

            y = y.resize((960, 540), Image.Resampling.LANCZOS)

            print("\nAfter resize:", y.size)

            #y.show()
            try:
                y.save(outfile)
            except:
                print("\nFailed to save file\n")
            imageW = 960
            imageH = 540
            data = bytearray()
            pixel1 = None
            for pixelX in range(540):
                for pixelY in range(960):
                    value = y.getpixel((pixelY, pixelX))
                    avgGreyVal = value * 15 / 255
                    greyVal = round(avgGreyVal)
                    displayVal = round(greyVal * 255 / 15)
                    y.putpixel((pixelY, pixelX), displayVal)
                    if pixel1 is None:
                        pixel1 = greyVal
                    else:
                        byte = (pixel1 << 4) | greyVal
                        data.append(byte)
                        pixel1 = None

            binaryOut = "/home/srogue/epaper/friends/binaries/IMG_" + str(lengthD) + ".bin"
            with open(binaryOut, "wb") as f:
                f.write(data)
            print(sorted(set(y.get_flattened_data())))
            newFileSpot = "/home/srogue/epaper/friends/originals/" + filename
            os.rename(tester, newFileSpot)
            y.save(outfile)

    except Exception as e:
        print("\nError:", e)
    x += 1
    lengthD += 1
