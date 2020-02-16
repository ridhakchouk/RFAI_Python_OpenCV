'''
Created on 16 f�vr. 2020

@author: carbo
'''

import numpy as np
import cv2 as cv

def imgproc16():
    img = cv.imread('castle.jpg') # chargement image
    gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)# conversion en niveau de gris
    sift = cv.xfeatures2d.SIFT_create()#calcul des points 
    kp = sift.detect(gray,None)#détection des points cle
    img=cv.drawKeypoints(gray,kp,img)#encerclement des points cle
    cv.imwrite('sift_keypoints.jpg',img)#sauvegarde resultat
    
imgproc16()