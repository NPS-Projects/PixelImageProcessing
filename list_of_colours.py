# Color pallete from https://colorswall.com/palette/3847/
import numpy as np
import pandas as pd

df = pd.read_csv('color_data.csv', sep=',')
colour_keywords = df['ColorName'].to_numpy()
colours = df['ColorRGBCode'].to_numpy()

for i in range(len(colours)):
    colours[i] = colours[i][1:-1]
    colours[i] = colours[i].split(',')
    colours[i] = list(map(int, colours[i]))