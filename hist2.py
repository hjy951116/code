import numpy as numpy
import cv2
import os
import matplotlib.pyplot as plt

# Open a vidoe
video_path=r"./vtest.mp4"
 

img_path =r'./images'
img_path2 =r'./equimages'

# if not os.path.isdir(img_path):
#    mkdir(img_path)

# # Divide the video into frames
# vidcap = cv2.VideoCapture(video_path)
# (cap,frame)= vidcap.read()
 
# if cap==False:
#     print('cannot open video file')
# count = 0

# # Save the frames in a folder
# while cap:
#   cv2.imwrite(os.path.join(img_path,'%.6d.jpg'%count),frame)

#   count += 1
#   # Every 100 frames get 1
#   for i in range(1):
#     (cap,frame)= vidcap.read()

framey = []
i=0

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

  ay = numpy.array(gray).flatten()
  plt.hist(ay ,bins = 256, density = 1, facecolor = 'blue', edgecolor = 'blue')
  plt.show()
  values, base = numpy.histogram(gray, bins=256)
#evaluate the cumulative
  cumulative = numpy.cumsum(values)
# plot the cumulative function
  # plt.plot(base[:-1], cumulative, c='green')
  # plt.show()
  print(values)
  y1 = numpy.mean(gray)
  framey.append(y1)
  print(i)
  i += 1

