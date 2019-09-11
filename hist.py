import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('000067.jpg',0)
img2 = cv2.imread('000068.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
hist2,bins = np.histogram(img2.flatten(),256,[0,256])
cdf = hist.cumsum()
print(cdf)
cdf_normalized = cdf * hist.max()/ cdf.max()
cdf2 = hist2.cumsum()
print(cdf2)
cdf_normalized2 = cdf2 * hist2.max()/ cdf2.max()
# for i in range 256
#   if cdf < cdf2
#     cdf2 =  cdf2

 
plt.plot(cdf_normalized, color = 'r')
plt.hist(img.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


# cdf_m = np.ma.masked_equal(cdf,0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# cdf = np.ma.filled(cdf_m,0).astype('uint8')
# img2 = cdf[img]
# cv2.imwrite('img2.jpg',img2)
# histm,binsm = np.histogram(img2.flatten(),256,[0,256])
 
# cdfm = histm.cumsum()
# cdfm_normalized = cdfm * histm.max()/ cdfm.max()
 
# plt.plot(cdfm_normalized, color = 'r')
# plt.hist(img2.flatten(),256,[0,256], color = 'b')
# plt.xlim([0,256])
# plt.legend(('cdfm','histogram'), loc = 'upper left')
# plt.show()
