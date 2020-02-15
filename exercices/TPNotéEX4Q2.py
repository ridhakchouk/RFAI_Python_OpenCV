'''
Created on 15 févr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

def imgproc14():
    src = cv2.VideoCapture('sunrise.mp4')
    ret, img_prec = src.read()
    img_prec = cv2.cvtColor(img_prec,cv2.COLOR_BGR2GRAY)
    img_prec = cv2.resize(img_prec,(480,320))
    i = 0 
    seuil_diff = 151000
    while ret == True:
        ret , img_suiv = src.read()
        img_suiv = cv2.cvtColor(img_suiv,cv2.COLOR_BGR2GRAY)
        img_suiv = cv2.resize(img_suiv,(480,320))
        diff = cv2.absdiff(img_prec,img_suiv)
        non_zero_val = np.count_nonzero(diff)
        if non_zero_val > seuil_diff: 
            cv2.imshow("img_prec", img_prec)
            cv2.imshow("img_suiv", img_suiv)
            img_prec = img_suiv
            i+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            src.release()
            cv2.destroyAllWindows()
            break
        print("fin iteration")
         
imgproc14()
        
