'''
Created on 11 févr. 2020

@author: carbo
'''
'''
Created on 7 fevr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Gradient function
def imgproc5():
    img = cv2.imread('parrot.png',0) # Lecture image
    laplacian = cv2.Laplacian(img,cv2.CV_64F) # Filtrage laplacien
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray') #affichage img original
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')# affichage laplacien
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray') # Sobel derivatives
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])# affichage titre
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])# affichage titre
    plt.show()# affichage

#Canny Edges
def imgproc6():
    img = cv2.imread('parrot.png',1) # lecture image
    edges = cv2.Canny(img,100,200) # canny edge detection 
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()


while (True):
    #img = cv2.imread('parrot.png',1) #original
    #imgproc5()
    imgproc6()
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
    break
