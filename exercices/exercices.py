'''
Created on 4 févr. 2020

@author: Ridha
'''


#Exercice 1 installation de openCV



#Exercice 2

import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.pyplot import gray
import matplotlib.pyplot as plt 
from _overlapped import NULL

def exercice2():
    # chargement de l'image dans la variable img
    #imread(path_to_file,flag) flag = if color 
    img = cv2.imread('messi5.jpg',1)
    
    # Affichage de l'image dans la fenetre
    cv2.imshow('Window',img)
    
    # Attent une entrée clavier pour continuer l'execution du code
    cv2.waitKey(0)
    
    #detruit toutes les fenêtres
    cv2.destroyAllWindows()
    
    #ecoute les entrée au clavier
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('messigray.png',img)
        cv2.destroyAllWindows()
    
    #cmap = palette de couleur
    #interpolation = agit sur le contour des formes
    plt.imshow(img, cmap = 'inferno', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    
    # REPONSE A LA QUESTION SUR LE TD
    #l'image est en niveau de gris car :
    '''
    1 l'image est charger avec un flag = 0 donc l'image par defaut est en niveau de gris
    2 plt.imshow contient un parametre cmap qui contient un ensemble de couleur celui ci
    a pour valeur gray donc l'image sera en gris.
    '''

def exercice3():
    #Chargemet image en couleur
    img = cv2.imread('messi5.jpg',1)
    img = cv2.resize(img,(800,600))
    
    gray = cv2.imread('messi5.jpg',1)
    gray = cv2.resize(gray,(800,600))
    
    largeur = gray.shape[0]
    hauteur = gray.shape[1]
    for i in range(0,largeur):
        for j in range(0,hauteur):
                val = gray[i][j]
                #print(val[0],val[1],val[2])
                #x = (val[0]+val[1]+val[2])/3
                x = val[0]*0.299 + val[1]*0.587 + val[2]*0.114
                gray[i][j] = x
                

    
    
    #Avec cvtColor
    #gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('original',img)
    cv2.imshow('gray',gray)
    
    # Attent une entrée clavier pour continuer l'execution du code
    cv2.waitKey(0)
    
    #detruit toutes les fenêtres
    cv2.destroyAllWindows()
    
#exercice3()

def exercice4(img):
    liste = [0] * 256
    largeur = img.shape[0]
    hauteur = img.shape[1]
    for i in range(0,largeur):
        for j in range(0,hauteur):
            val = img[i][j]
            tmp = liste[val]
            liste[val]= tmp + 1
    return liste

#exec ex  

#CHECK OK
'''
gray = cv2.imread('messi5.jpg',0)
print(exercice4(gray))
print("taille de la liste : ",len(exercice4(gray)))
plt.plot(exercice4(gray)) #X et Y sont les listes (ou tableaux numpy) d'abscisses et d'ordonnées des points à tracer
plt.show() #pour afficher
'''


