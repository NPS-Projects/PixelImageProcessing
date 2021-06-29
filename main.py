from PIL import Image
import numpy as np
from list_of_colours import colours
from list_of_colours import colour_keywords

"""Converts image to pixel art, then assigned with minecraft blocks"""

"""Convert image to pixel art"""


def toPixelArt(image, xlen=100, ylen=75):
    print(image.width, image.height)
    small_image = image.resize((xlen, ylen), Image.BILINEAR)
    getImagePixelRGB(small_image)
    small_image.save('new_image.png')


"""loop through each pixel"""


def getImagePixelRGB(image):
    # a large matrix - list that shows colour of each pixel
    code_list = []
    for y in range(image.height):
        # list that shows colour of pixel in y'th row
        inner_list = []
        for x in range(image.width):
            r, g, b, a = image.getpixel((x, y))
            colour_key_f, colour_rgb_f = find_nearest_dist(r, g, b)
            nr, ng, nb = colour_rgb_f
            image.putpixel((x, y), (nr, ng, nb))
            inner_list.append(str(x+1) + " " + colour_key_f)
        code_list.append(inner_list)
        print(image.height-y, inner_list)


def find_nearest_dist(r, g, b, colours=colours, colour_key=colour_keywords):
    index = 0
    dist = ((colours[0][0] - r) * 0.25) ** 2 + ((colours[0][1] - g) * 0.25) ** 2 + ((colours[0][2] - b) * 0.5) ** 2
    for i in range(1, len(colours)):
        d = ((colours[i][0] - r) * 0.25) ** 2 + ((colours[i][1] - g) * 0.25) ** 2 + ((colours[i][2] - b) * 0.5) ** 2
        if d < dist:
            dist = d
            index = i
    return colour_key[index], colours[index]


if __name__ == "__main__":
    # image = Image.open('Screenshot (67).png')
    image = Image.open('cutelongears3.png')
    toPixelArt(image, 80,90)
