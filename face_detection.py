import cv2
import numpy as np


face_cascade = cv2.CascadeClassfier("haarcascade_frontalface_default.xml")

img = cv2.imread("D:/PlayMirror/pf/IMAG0623.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h) in faces:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('img', img)