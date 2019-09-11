import numpy as numpy
import cv2
current_frame = cv2.imread('./images/000068.jpg')
current_frame1 = cv2.imread('./images/000067.jpg')
current_frame2 = cv2.imread('./framediff/00068.jpg')
current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
current_frame_gray1 = cv2.cvtColor(current_frame1, cv2.COLOR_BGR2GRAY)
current_frame_gray2 = cv2.cvtColor(current_frame2, cv2.COLOR_BGR2GRAY)   

frame = cv2.absdiff(current_frame_gray,current_frame_gray2)
cv2.imwrite('frame.jpg',current_frame_gray)
cv2.imwrite('frame1.jpg',current_frame_gray1)
cv2.imwrite('frame2.jpg',frame)