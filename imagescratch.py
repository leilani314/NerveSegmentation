# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:18:05 2016

@author: Leilani Pai

Read/show binary image mask and convert to a run-length encoding entry
"""

#to view image
from PIL import Image
img = Image.open('C:\\Users\\Leilani Pai\\Documents\\Nerve Segmentation\\train\\train\\1_1_mask.tif')
img.show()

#to convert image to numpy array
import numpy
array = numpy.asarray(img)

#get array dimensions
dim = array.shape
n = dim[0]
m = dim[1]

#reshape into row vector
rowa = numpy.reshape(array, n*m, order='F')

#try to pull out rle
i = 0
rle = []

while i < n*m:
    if rowa[i] != 0:
        c = 0
        rle = rle + [i+1]
        while rowa[i] != 0:
            c = c + 1
            i = i + 1
        rle = rle + [c]
    i = i + 1