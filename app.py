#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:28:48 2018

@author: nicolas
"""
import  sift 
import  Matrice 
import matplotlib.pyplot as plt
import cv2

def menu():
    print("=================================================================================")
    print("                                      ")
    print("                                      ")
    print("                   RECONNAISSANCE DES OBJETS                   ")
    print(" Auteur: Worn777                                     ")
    print("                                      ")
    print("=================================================================================")
    print("                                      ")
    print("                                      ")
    print("1- Catégoriser une image.")
    print("2- Matrice de confusion pour un ratio de 0.6.")
    print("3- Phase de test avec dataset de test.")
    print("4- Matching entre deux images.")
    print("0- Quitter.")
    
    
def main():
    menu()
    choix = input("Votre choix")
    while (choix !=0 ):
        if str(choix) == str(3):
            ratio=0
            ratio= float(input("Veuillez renseigner le paramètre ratio"))
            print("Veuiller patienter.....")
            sift.test_dataset(ratio)
            #while (ratio<=0 and ratio>1):
             #   ratio= float(input("Veuillez renseigner le paramètre ratio"))
              #  sift.test_dataset(ratio)
        if str(choix)== str(2):
            print("Veuiller patienter.....")
            Matrice.matrix_confusion()
        if str(choix)== str(1):
            lien=input("Entrer le lien de l'image de test : ")
            ratio=3
            ratio= (input("Veuillez renseigner le paramètre ration(0<ratio<1) "))
            print("Veuiller patienter le modèle recherche la classe de l'image.....")
            if (sift.test_image(lien,float(ratio))==""):
                print("Recommencer l'opération en augmentant le ration (0<ratio<1) ")
            else:   
                print( " La catégorie de l'image est : ", sift.test_image(lien,float(ratio)))
        if str(choix)== str(4):
            lien_i1=input("Entrer le lien de l'image 1 de test :")
            lien_i2=input("Entrer le lien de l'image  2 de test :")
            image = sift.affichage_PI_image(lien_i1,lien_i2)
        menu()
        choix = int(input("Votre choix : "))   
       
        
if __name__ == '__main__':
    main()

            
            
        
        