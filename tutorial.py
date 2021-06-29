from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt
import webbrowser

o = Image.open("assets/o.png")
pixel = o.load()

for row in range(pixel.size[0]):
    for column in range(pixel.size[1]):
        if pixel[row, column] != (255, 255, 255):
            pixel[row, column] = (0, 0, 0)

