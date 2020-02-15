'''
Created on 7 fevr. 2020

@author: carbo
'''
#Importation des librairies
import numpy as np
import cv2

# Cette fonction retourne l'image passé en paramètre
def imgproc(imgc):
    return imgc


#Variable qui contient les images capturé à partir d'une source
cap = cv2.VideoCapture('parrot.mp4')

#boucle infini le programme continuera à tourner tant qu'il y a capture
while (True):
    #Deux variable déclaré: ret(apres) et frame(avant) pour afficher
    #les images capturé  avant et après l'application des filtres
    ret, frame = cap.read()
    #Si ret contient toujour une image (if true) alors on rentre dans la boucle
    if ret == True:
        # la variable img reçoit l'image qui est copié à partir de la variable frame
        #gray convertie l'image contenue dans la variable img en niveau de gris
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #gray reçoit l'image retourner par la fonction imgproc
        gray = imgproc(gray)
        
        #Affichage des images contenue dans frame et img dans deux fenêtre distincte
        cv2.imshow('MavideoAvant', frame)
        cv2.imshow('MavideoApres', gray)
    else:
        print('video ended')
        break
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

###COMPLETED OK 
    