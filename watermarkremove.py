import cv2 as cv
import numpy as np
from PIL import Image
import cv2

c = input("Please input video directory(like : " "D:\sda.mp4) :")

cap = cv.VideoCapture(c)
n=0

image = input("Please input image directory: " )
while(1):
    ret, frame = cap.read()

    mask = cv.imread(image)
    gr = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    bg = gr.copy()
    framee = cv.inpaint(frame, gr , 3 , cv.INPAINT_TELEA)
    framee = cv.resize(framee, (640,360) , cv.INTER_AREA)
    n+=1

    if n == 1000:
        break
    else:
        cv.imshow('franes' , framee)
        if cv.waitKey(1)==27:
            break

cap.release()
cv.destroyAllWindows()