import cv2
import os
img_path =r'./framediff'
cap = cv2.VideoCapture('vtest.mp4')
ret, current_frame = cap.read()
previous_frame = current_frame
count = 0

while(cap.isOpened()):
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)    

    frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray)

  
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    cv2.imwrite(os.path.join(img_path,'%.5d.jpg'%count),frame_diff)

    count += 1
    previous_frame = current_frame.copy()
    ret, current_frame = cap.read()

# cap.release()
# cv2.destroyAllWindows()


