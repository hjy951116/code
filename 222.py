import numpy as numpy
import cv2
import os
import matplotlib.pyplot as plt
import pandas as pd 

# Open a vidoe
video_path=r"./vtest.mp4"
 

img_path =r'./images'
img_path2 =r'./equimages'

framey = []
i=0

import cv2
import numpy as np
from matplotlib import pyplot as plt

import glob
from PIL import Image
for frames in glob.glob('./2/*.jpg'): 
    img = cv2.imread(frames)

    hist,bins = np.histogram(img.flatten(),256,[0,256])
    
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    
    plt.plot(cdf_normalized, color = 'r')
    plt.hist(img.flatten(),256,[0,256], color = 'b')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

#   gray_levels = 256
#   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   im = Image.open(frames)
#   pix = im.load()
#   width = im.size[0]
#   height = im.size[1]

#   ay = numpy.array(gray).flatten()
# #   plt.hist(ay ,bins = 256, normed = 1, facecolor = 'blue', edgecolor = 'blue')
#   values, base = numpy.histogram(gray, bins=256)
# #evaluate the cumulative
#   cumulative = numpy.cumsum(values)
# # plot the cumulative function
#   plt.plot(base[:-1], cumulative, c='green')
#   plt.show()
#   print(values)
#   y1 = numpy.mean(gray)
#   framey.append(y1)
#   print(i)
#   i += 1
 
