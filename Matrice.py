# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:54:18 2018

@author: nicolas
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
import os.path
from os import listdir
import pickle
from scipy.spatial import distance
from sklearn.metrics import confusion_matrix

pathDataSet ="./matrix_confusion"
pathDataTest = "./test"
pathDataTrain ="./train"
pathDescripteur="./descripteur"
listDossiers = listdir(pathDataTest)


#Recuperation du descripteur Unpickle
def unpickle_fch_descripteur(fichier):   
    Unpkl=pickle.Unpickler(fichier)
    fic= Unpkl.load()
    return fic
  
def matrix_confusion():
    fi = open((pathDataSet+"/pourcentage.txt"),'rb')
    r = unpickle_fch_descripteur(fi)
    
    fi.close
    
    
    fic = open((pathDataSet+"/prediction.txt"),'rb')
    p = unpickle_fch_descripteur(fic)
    fic.close
    
    fiche = open((pathDataSet+"/label.txt"),'rb')
    l = unpickle_fch_descripteur(fiche)
    fiche.close
    
    fiches = open((pathDataSet+"/realite.txt"),'rb')
    r = unpickle_fch_descripteur(fiches)
    fiches.close
    
    tableau = confusion_matrix(r, p)
    
    #tableau = confusion_matrix(p, r,l)
    print(tableau)
    vegetables = l

    
    
    print(len(l))
    
    #print(vegetables.reverse())
    #print(vegetables)
    
    harvest = tableau
    #print(m[1])
    print(tableau[2])
    #print(tableau[87])
    
    fig, ax = plt.subplots()
    im = ax.imshow(harvest)
    
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(vegetables)))
    ax.set_yticks(np.arange(len(l)))
    # ... and label them with the respective list entries
    #ax.set_xticklabels(l)
    #plt.xticks(fontsize=6.5, rotation=45)
    ax.set_yticklabels(vegetables)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(7,7)
    #ax.get_xticklabels(),
    # Rotate the tick labels and set their alignment.
    plt.setp( rotation=45, ha="right",rotation_mode="anchor")
    
    # Loop over data dimensions and create text annotations.
    """for i in range(len(l)):
        for j in range(len(l)):
            text = ax.text(j, i, harvest[i, j],ha="center", va="center", color="w",fontsize=6)"""
                     
    ax.set_title("   Matrix de confusion  ")
    fig.tight_layout()
    plt.show()
matrix_confusion()