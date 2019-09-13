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


framey = []
i = 0
frameindex = 0

# Open frames in the folder
import glob
from PIL import Image
for frames in glob.glob('./1/*.jpg'):
  img = cv2.imread(frames)
  gray_levels = 256
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  im = Image.open(frames)
  pix = im.load()
  width = im.size[0]
  height = im.size[1]
  
  # Define the window size
  windowsize_r = 16
  windowsize_c = 16

  blocky = numpy.zeros((height/windowsize_r, width/windowsize_c))

  # The average luminance component (Y) of an entire frame
  y1 = numpy.mean(gray)

  framey.append(y1)

  

  # Each frame is partitioned into blocks
  # for r in range(0,gray.shape[0] - windowsize_r, windowsize_r):
  #   for c in range(0,gray.shape[1] - windowsize_c, windowsize_c):
  for r in range(0,gray.shape[0], windowsize_r):
    for c in range(0,gray.shape[1], windowsize_c):
      window = gray[r:r+windowsize_r,c:c+windowsize_c]
      w = numpy.mean(window)
      i = r/windowsize_r
      j = c/windowsize_c
      blocky[i][j] = blocky[i][j] + w
        
      # The blocks are sorted in decreasing order 
      w1 = numpy.sort(blocky)
  
  print(frameindex)  
  frameindex += 1   
  
  print(blocky)
