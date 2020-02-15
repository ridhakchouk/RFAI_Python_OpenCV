'''
Created on 15 févr. 2020

@author: carbo
'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

#Substraction
def imgproc12(img1,img2):
    return cv2.absdiff(img1,img2) 
# retourne la différence entre deux images passé en arguement

while (True):
    imgproc12()
    if cv2.waitKey(1000) | 0xFF == ord('q'):
        break
    break
