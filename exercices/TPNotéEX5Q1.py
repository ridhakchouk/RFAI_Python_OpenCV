'''
Created on 15 févr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
from _collections import defaultdict

def imgproc15():   
    src = cv2.VideoCapture('sunrise.mp4')   #capture vidéo
    ret, img_prec = src.read()              #aquisition image
    img_prec = cv2.cvtColor(img_prec,cv2.COLOR_BGR2GRAY) # Convertion en niveau de gris pour comparaison
    img_prec = cv2.resize(img_prec,(480,320)) # redemensionnement de l'image pour reduire la taille des fenetres
    
    i = 0 #compteur de plan
    
    seuil_diff = 100000 # seuil de tolérance
    
    liste_de_plan = [] # Liste de plan
    liste_img = [] # liste d'image
    nb_img = 0 # compteur image 
    
    while ret  == True:# tant qu'il y a une trame
        ret , img_suiv = src.read() # lecture de la nouvelle trame
        if ret : # si il ya une trame alors :
            img_suiv = cv2.cvtColor(img_suiv,cv2.COLOR_BGR2GRAY) # covertie en niv de gris la trame suivante
            img_suiv = cv2.resize(img_suiv,(480,320))# redimensionne la
            diff = cv2.absdiff(img_prec,img_suiv) # et fait une soustraction pour voir les différence
            non_zero_val = np.count_nonzero(diff) # pour une trame regarde chaque pixel et compte les différence (permet de calculer si le seuil est respecté)
            if non_zero_val > seuil_diff:# Si noombre de pixel différent au seuil autorisé alors c'est un nouveau plan
                img_prec = img_suiv # mise a jour du nouveau plan par la trame
                i+=1 # compteur de plan +1
                liste_de_plan.append([i,img_prec])# ajout de ce plan a la liste de plan
                print("Plan N°",i-1,"-->",nb_img,"images") # affichage
                nb_img=0 # réinitialise le compteur d'image
            liste_img.append([i,img_suiv])# compte le nombre d'image pour les trames qui vont suivre
            nb_img+=1 # compteur ++
    
    for j in range(0,len(liste_de_plan)): #AFFICHAGE
        for k in range(0,len(liste_img)): #AFFICHAGE
            if(j == liste_img[k][0]): #AFFICHAGE
                print("Plan N°",j,"--> Image N°",k) #AFFICHAGE
                     
imgproc15()