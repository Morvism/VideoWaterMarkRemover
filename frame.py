from tkinter import Frame
import cv2 as cv
import fileinput

c = input("Please input video directory(like : " "D:\sda.mp4) :")

cap = cv.VideoCapture(c)
n = 0
framer = int(input("Please input frame of your watermark :"))

while(1):
    ret, frame = cap.read()
    n += 1


    if n == framer:
        cv.imwrite('frame.jpg', frame)
        break

cap.release()
cv.destroyAllWindows()