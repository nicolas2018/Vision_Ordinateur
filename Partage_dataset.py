import os.path
from os import listdir
import shutil
pathDataSet ="./dataset"
pathDataTest = "./test"
pathDataTrain ="./train"

#PARTAGE DU DATASET
listDossier = listdir(pathDataSet)
for file in  listDossier:
    listImage = os.listdir(pathDataSet+"/"+file)
    cheminTest=pathDataTest+"/"+file
    cheminTrain = pathDataTrain + "/" + file
    taille=len(listImage)
    print(taille)
    taille_motie=int(taille/2)
    #TEST 0  00   000
    if not os.path.exists(cheminTest):
        os.mkdir(cheminTest)
        for i in range(15):
            shutil.copy((pathDataSet+"/"+file+"/"+listImage[i]),cheminTest)

    #APPRENTISSAGE
    if not os.path.exists(cheminTrain):
        os.mkdir(cheminTrain)
        for j in range(16,31):
            shutil.copy((pathDataSet + "/" + file + "/"+ listImage[j]), cheminTrain)



