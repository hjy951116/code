import cv2
import os
import numpy as np

video_path=r"./vtest.mp4"
 

img_path=r'./images'
 

if not os.path.isdir(img_path):
   mkdir(img_path)
 

vidcap = cv2.VideoCapture(video_path)
(cap,frame)= vidcap.read()

if cap==False:
    print('cannot open video file')
count = 0


while cap:
  cv2.imwrite(os.path.join(img_path,'%.6d.jpg'%count),frame)

  count += 1
  for i in range(100):
    (cap,frame)= vidcap.read()
i=0
j=0
from PIL import Image
im = Image.open('000000.jpg')
pix = im.load()
width = im.size[0]
height = im.size[1]
i=i+1
print(i)
for m in range(width):
    for n in range(height):
        r, g, b = pix[m, n]
        y= (0.2126*r + 0.7152*g + 0.0722*b)
        print(m,n)
        print(y)
y1= np.mean(y)
print(y1)
