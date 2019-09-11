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
video_path=r"./test.mp4"
 

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
count2 = 0
framey = []
i = 0
j = 0
# Open frames in the folder
import glob
from PIL import Image
for frames in glob.glob('./1/*.jpg'):
  img = cv2.imread(frames)
  gray_levels = 256
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  # equ = cv2.equalizeHist(gray)
  # cv2.imwrite(os.path.join(img_path2,'%.6d.jpg'%count2),equ)
  count2 += 1
  im = Image.open(frames)
  pix = im.load()
  width = im.size[0]
  height = im.size[1]


  # Define the window size
  windowsize_r = 16
  windowsize_c = 16
  # The average luminance component (Y) of an entire frame
  # for m in range(width):
  #     for n in range(height):
  #       R, G, B = pix[m, n]
  #       Y = (0.2126*R + 0.7152*G + 0.0722*B)
        # Y =   16 +  65.738*R/256 + 129.057*G/256 +  25.064*B/256
        # Cb = 128 -  37.945*R/256 -  74.494*G/256 + 112.439*B/256
        # Cr = 128 + 112.439*R/256 -  94.154*G/256 -  18.285*B/256
        #print(m,n)
        #print(y)
  # y1 = numpy.mean(Y)
  y1 = numpy.mean(gray)
  # print(y1)
  framey.append(y1)
  print(i)
  
  blocky = []
  blocky2 = []
  # Each frame is partitioned into blocks
  for r in range(0,gray.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,gray.shape[1] - windowsize_c, windowsize_c):
        window = gray[r:r+windowsize_r,c:c+windowsize_c]
        #hist = numpy.histogram(window,bins=gray_levels)
        # The average luminance component of each block 
        w = numpy.mean(window)
        blocky.insert(0,w)
        # The blocks are sorted in decreasing order 
        w1 = numpy.sort(blocky)
        #hist,bins = numpy.histogram(img.flatten(),256,[0,256])
        #print(window)
        #print(blocky)
  if column[i] == 1:
    #plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.plot(w1,'r') # plotting by columns
  else:
    #plt.hist(img.flatten(),256,[0,256], color = 'b')
    plt.plot(w1,'b') # plotting by columns

  i += 1
#plt.show()

  # Each frame is partitioned into blocks
  # for r2 in range(0,equ.shape[0] - windowsize_r, windowsize_r):
  #   for c2 in range(0,equ.shape[1] - windowsize_c, windowsize_c):
  #       window2 = equ[r2:r2+windowsize_r,c2:c2+windowsize_c]
  #       hist2 = numpy.histogram(window2,bins=gray_levels)
  #       # The average luminance component of each block 
  #       w2 = numpy.mean(window2)
  #       blocky2.insert(0,w2)
  #       # The blocks are sorted in decreasing order 
  #       w3 = numpy.sort(blocky2)
  #       #print(blocky2)
  # # if column[i] == 1:
  # #   #plt.hist(img.flatten(),256,[0,256], color = 'r')
  # #   plt.plot(w3,'g') # plotting by columns
  # # else:
  # #   #plt.hist(img.flatten(),256,[0,256], color = 'b')
  # #   plt.plot(w3,'y') # plotting by columns
  # # # plt.plot(w3) # plotting by columns
plt.show()
  
                #print(hist)
plt.axhline(y = 126, color = 'r', linestyle = '-')
plt.plot(framey) # plotting by columns
plt.show()
# print(y2)