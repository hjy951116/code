import cv2

#-----Reading the image-----------------------------------------------------
img = cv2.imread('1.png')
fimg= cv2.imread('2.png')
cv2.imshow("img",img)
cv2.imshow("fimg",fimg) 

#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
flab= cv2.cvtColor(fimg, cv2.COLOR_BGR2LAB)
cv2.imshow("lab",lab)

#-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
cv2.imshow('l_channel', l)
cv2.imshow('a_channel', a)
cv2.imshow('b_channel', b)

fl, fa, fb = cv2.split(flab)
cv2.imshow('fl_channel', fl)
cv2.imshow('fa_channel', fa)
cv2.imshow('fb_channel', fb)

#-----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
cv2.imshow('CLAHE output', cl)

fcl = clahe.apply(fl)
cv2.imshow('fCLAHE output', fcl)

#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl,a,b))
cv2.imshow('limg', limg)

flimg = cv2.merge((fcl,fa,fb))
cv2.imshow('flimg', flimg)

#-----Converting image from LAB Color model to RGB model--------------------
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('final', final)

ffinal = cv2.cvtColor(flimg, cv2.COLOR_LAB2BGR)
cv2.imshow('ffinal', ffinal)

cv2.waitKey(0)
#cv2.destroyAllWindows()
#_____END_____