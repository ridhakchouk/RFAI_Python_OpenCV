'''
Created on 16 févr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
from _collections import defaultdict

def imgproc16():   
    img = cv2.imread('home.jpg')
    gray= cv2.cvtColor(img,cv.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray,None)
    img=cv2.drawKeypoints(gray,kp,img)
    cv2.imwrite('sift_keypoints.jpg',img)

imgproc16()