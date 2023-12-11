# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:11:56 2023

@author: adfw980
"""

import pandas as pd
import csv
import sys
import matplotlib.pyplot as plt

import urllib.request

from PIL import Image

from skimage import data, io, filters
from skimage import  color


image_path_blood = r"C:\Users\adfw980\Downloads\SEM_blood_cells.jpg"
image_path_monet = r"C:\Users\adfw980\Downloads\Claude_Monet,_Impression,_soleil_levant.jpg"

image_blood = io.imread(image_path_blood)

image_monet = io.imread(image_path_monet)

io.imshow(image_blood)
io.show()


io.imshow(image_monet)
io.show()

#we will try different filters on the images we have

gray_monet = color.rgb2gray(image_monet)
io.show()                            


filters_list = [
    
    (filters.sobel, 'Sobel Filter'),
    (filters.gaussian, 'Gaussian Filter'),
    (filters.median, 'Median Filter'),
    ] 

for i, (filter_func, title) in enumerate(filters_list, start=2):
    filtered_image = filter_func(gray_monet)
    plt.subplot(1, 3, i)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(title)

plt.tight_layout()
plt.show()
