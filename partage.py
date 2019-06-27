# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 01:00:22 2018

@author: nicolas
"""
import shutil
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os.path
from os import listdir
import pickle
from scipy.spatial import distance

pathDataSet ="./dataset"
pathDataTest = "./test"
pathDataTrain ="./train"

#PARTAGE DU DATASET

#print(len(listDossier))
# """for i in ran"ge(1,101):
   #cheminTest=pathDataTest+"/"+"obj"+str(i)
    #"suffixe="obj"+str(i)+"_"
    #print(cheminTest)
    #print(suffixe)
    #if not os.path.exists(cheminTest):
     #   os.mkdir(cheminTest)
    #for file in  listDossier:
     #   fichier =(str(file))
      #  if(fichier.find(suffixe)!=-1):
       #     shutil.copy((pathDataSet+"/"+file),cheminTest)"""
         
        
        
i=0       
 #PARTAGE DU DATASET
listDossier = listdir(pathDataSet)
for file in  listDossier:
    listImage = os.listdir(pathDataSet+"/"+file)
    cheminTest=pathDataTest+"/"+file
    cheminTrain = pathDataTrain + "/" + file
    i+=len(listImage)
print(i)
    #print()
  #taille_motie=int(taille/2)
    #TEST 0  00   000
   # if not os.path.exists(cheminTest):
    #    os.mkdir(cheminTest)
     #   for i in range(0,taille_motie):
      #      shutil.copy((pathDataSet+"/"+file+"/"+listImage[i]),cheminTest)

    #APPRENTISSAGE
    #if not os.path.exists(cheminTrain):
     #   os.mkdir(cheminTrain)
      #  for j in range(taille_motie,(taille)):
       #     shutil.copy((pathDataSet + "/" + file + "/"+ listImage[j]), cheminTrain)"""



