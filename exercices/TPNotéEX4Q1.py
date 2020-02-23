'''
Created on 15 fevr. 2020

@author: carbo
'''
import cv2
import numpy as np
#from matplotlib import pyplot as plt

def imgproc13():
    src = cv2.VideoCapture('sunrise.mp4') # acquisition vidéo
    ret, img_prec = src.read()# chargement premiere img pour faire des comparaison après
    img_prec = cv2.cvtColor(img_prec,cv2.COLOR_BGR2GRAY)# conversion en niv de gris
    img_prec = cv2.resize(img_prec,(480,320))
    #entre dans la boucle infini pour lire la vidéo
    i = 0 # compteur de changement de scene
    seuil_diff = 151000
    while ret == True:
        ret , img_suiv = src.read()#image suivante
        img_suiv = cv2.cvtColor(img_suiv,cv2.COLOR_BGR2GRAY) # pour facilité les comparaison
        img_suiv = cv2.resize(img_suiv,(480,320))
        diff = cv2.absdiff(img_prec,img_suiv) # soustraction afin de voir les différence
        non_zero_val = np.count_nonzero(diff) # compte le nombre de valeurs différentes de 0 dans un tableau
        #Seuil max de val différente 151000
        if non_zero_val > seuil_diff: #si beaucoup de différence alors il y a changement de plan
            print('changement de scene :',i)
            i+=1
        cv2.imshow('premiere image',img_prec)
        cv2.imshow('image_suiv', img_suiv)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            src.release()
            cv2.destroyAllWindows()
            break
        print("fin iteration") # affichage dans la console pour 
        #savoir quand une itération est terminé
        print(non_zero_val)
imgproc13()