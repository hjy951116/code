import numpy as numpy
import cv2
import os
import matplotlib.pyplot as plt
import csv

with open('./test.csv','rb') as csvfile:
  reader = csv.reader(csvfile)
  column = [row[1] for row in reader]
  column.pop(0)
  column = list(map(int,column))
# Open a vidoe

framey = []
i = 0
j = 0
# Open frames in the folder
import glob
from PIL import Image
for frames in glob.glob('./2/*.jpg'):
  img = cv2.imread(frames)
  gray_levels = 256
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  hist,bins = numpy.histogram(img.flatten(),256,[0,256])
  cdf = hist.cumsum()
  print(i)
  


  if column[i+100] == 1:
    plt.plot(cdf, color = 'r')
    #plt.hist(img.flatten(),256,[0,256], color = 'r')
    #plt.show()
  else:
    plt.plot(cdf, color = 'b')
    #plt.hist(img.flatten(),256,[0,256], color = 'b')
    #plt.show()
  i += 1

plt.show()
  
                #print(hist)
#plt.axhline(y = 126, color = 'r', linestyle = '-')
#plt.plot(framey) # plotting by columns
#plt.show()
# print(y2)