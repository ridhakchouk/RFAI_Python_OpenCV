'''
Created on 7 fevr. 2020

@author: carbo
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Flou gaussien
def imgproc(imgc):
    imgc = cv2.GaussianBlur(imgc,(5,5),0)
    return imgc

#Flou median
def imgproc2(imgc):
    imgc = cv2.medianBlur(imgc,5)
    return imgc

#Bilateral Filtering
def imgproc3(imgc):
    imgc = cv2.bilateralFilter(imgc,9,75,75)
    return imgc

#Averaging
def imgproc4(imgc):
    imgc = cv2.blur(imgc,(5,5))
    return imgc


cap = cv2.VideoCapture('parrot.mp4')
while (True):
    ret, frame = cap.read()
    
    if ret == True:
        img1 = frame.copy()    
        img1 = imgproc(img1)
        
        img2 = frame.copy()
        img2 = imgproc2(img2)
        
        img3 = frame.copy()
        img3 = imgproc3(img3)
        
        img4 = frame.copy()
        img4 = imgproc4(img4)
        
        img5 = frame.copy()    
        img5 = imgproc(img5)
        
        cv2.imshow('MavideoAvant', frame)
        cv2.imshow('Flou gaussien', img1)
        cv2.imshow('Flou median', img2)
        cv2.imshow('Bilateral Filtering', img3)
        cv2.imshow('Averaging', img4)
    else:
        print('video ended')
        break
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
