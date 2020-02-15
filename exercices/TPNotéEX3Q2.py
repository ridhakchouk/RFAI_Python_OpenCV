'''
Created on 15 fevr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Substraction
def imgproc12(img1,img2):
    return cv2.absdiff(img1,img2) 
# retourne la difference entre deux images passe en arguement

def imgproc12_v2(img1,img2):
    img_resu = cv2.absdiff(img1,img2)
    titles = ['Roi de pique','Roi de carreau', 'Différence']# Titre imgss
    images = [img1, img2, img_resu]#Liste img
    for i in range(3):#affichage des image dans l'ordre
        plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    

while (True):
    img1 = cv2.imread('diff1.png',0)
    img2 = cv2.imread('diff2.png',0)
    #cv2.imshow('Differences',imgproc12(img1,img2))
    imgproc12_v2(img1,img2)
    if cv2.waitKey(1000) | 0xFF == ord('q'):
        break
    break
