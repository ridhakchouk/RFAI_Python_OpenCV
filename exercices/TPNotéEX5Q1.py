'''
Created on 15 févr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
from _collections import defaultdict

def imgproc15():
    src = cv2.VideoCapture('sunrise.mp4')
    ret, img_prec = src.read()
    img_prec = cv2.cvtColor(img_prec,cv2.COLOR_BGR2GRAY)
    img_prec = cv2.resize(img_prec,(480,320))
    
    i = 0 
    
    seuil_diff = 100000
    
    liste_de_plan = []
    liste_img_de_plan = []
    nb_img = 0
    while ret == True:
        
        ret , img_suiv = src.read()
        img_suiv = cv2.cvtColor(img_suiv,cv2.COLOR_BGR2GRAY)
        img_suiv = cv2.resize(img_suiv,(480,320))
        diff = cv2.absdiff(img_prec,img_suiv)
        non_zero_val = np.count_nonzero(diff)
        if non_zero_val > seuil_diff:#plan ici 
            img_prec = img_suiv
            i+=1
            print("Plan N°",i,"-->",nb_img,"images")
            nb_img=0
        #liste_img_de_plan.append(img_suiv)
        nb_img+=1
        
                 
imgproc15()