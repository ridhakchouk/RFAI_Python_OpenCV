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
    liste_img = []
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
            liste_de_plan.append([i,img_prec])
            #print("Plan N°",i,"-->",nb_img,"images")
            nb_img=0
        liste_img.append([i,img_suiv])
        nb_img+=1
    
        if i == 30:
            break    
    for j in range(0,len(liste_de_plan)):
        for k in range(0,len(liste_img)):
            if(j == liste_img[k][0]):
                print(j,k)
                     
imgproc15()