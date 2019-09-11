import numpy as numpy
import cv2
import os
import matplotlib.pyplot as plt
import csv
import pywt
import pywt.data


frameindex = []
xa = []
xb = []
xc = []
with open('./test2.csv','rb') as csvfile:
  reader = csv.reader(csvfile)
  column = [row[1] for row in reader]
  column.pop(0)
  column = list(map(int,column))

with open('./test3.csv','rb') as csvfile1:
  reader1 = csv.reader(csvfile1)
  column1 = [row[1] for row in reader1]
  column1.pop(0)
  column1 = list(map(int,column1))

count2 = 0
framey = []
cAm = []
cHm = []
cVm = []
cDm = []
i = 0
j = 0
# Open frames in the folder
import glob
from PIL import Image
for frames in glob.glob('./1/*.jpg'):
  img = cv2.imread(frames)
  gray_levels = 256
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

  y1 = numpy.mean(gray)
  framey.append(y1)
  print(i)
  coeffs = pywt.dwt2(gray, 'haar')
  cA, (cH, cV, cD) = coeffs
  cAmean = numpy.mean(cA)
  cAm.append(cAmean)
  cHmean = numpy.mean(cH)
  cHm.append(cHmean)
  cVmean = numpy.mean(cV)
  cVm.append(cVmean)
  cDmean = numpy.mean(cD)
  cDm.append(cDmean)
  print(cAmean)
  # print(cA)
  print(cHmean)
  print(cVmean)
  print(cDmean)


  i += 1

  if column[i] == 1:
    xa.append(i)
  elif column1[i] == 1:    
    xb.append(i)
  else:
    xc.append(i)
n = len(cAm)
x = range(0,n)

for j in range (n):

  if cAm[j]>253:
    frameindex.append(j)

print(frameindex)
print(xa)
print(xb)

plt.plot(cAm)
plt.show()
plt.plot(cDm)
plt.plot(cHm)
plt.plot(cVm)
plt.show()
# print(y2)