'''
Created on 12 févr. 2020

@author: carbo
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Seuillage Simple
def imgproc7():
    img = cv2.imread('degrade.jpg',0) # Chargement image
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#Seuillage
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#Seuillage
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#Seuillage
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#Seuillage
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)#Seuillage
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']# Titre img
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]#Liste img
    for i in range(6):#affichage des image dans l'ordre
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    
#Seuillage Adaptif
def imgproc8():
    img = cv2.imread('ombre.jpg',0)#chargement
    img = cv2.medianBlur(img,5)#filtrage median flou
    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#seuillage
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)#seuillage
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)#seuillage
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in  range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    
#Binarisation
def imgproc9():
    img = cv2.imread('noisy.jpg',0)
    # global thresholding
    ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    # Otsu's thresholding
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # plot all the images and their histograms
    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
              'Original Noisy Image','Histogram',"Otsu's Thresholding",
              'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()

#Erosion
def imgproc10():
    img = cv2.imread('a_letter.png',0) # Chargement image
    img = cv2.bitwise_not(img) # inversemment img couleur
    kernel = np.ones((6,6),np.uint8)# Config du noyau
    erosion = cv2.erode(img,kernel,iterations = 1) # Erosion de l'image avec la fonction cv2.erode()
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(erosion,cmap = 'gray')
    plt.title('Erosion Image'), plt.xticks([]), plt.yticks([])
    plt.show()#Affichage

#Dilatation
def imgproc11():
    img = cv2.imread('a_letter.png',0) # Chargement image
    img = cv2.bitwise_not(img) # inversemment img couleur
    kernel = np.ones((10,10),np.uint8)# Config du noyau
    dilation = cv2.dilate(img,kernel,iterations = 1) # dilatation img
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dilation,cmap = 'gray')
    plt.title('Erosion Image'), plt.xticks([]), plt.yticks([])
    plt.show()#Affichage


while (True):
    #imgproc7()
    #imgproc8()
    #imgproc9()
    #imgproc10()
    imgproc11()
    if cv2.waitKey(1000) | 0xFF == ord('q'):
        break
    break
