import cv2
import numpy as np
import matplotlib.pyplot as plt
import os.path
from os import listdir
import pickle
from scipy.spatial import distance
from sklearn.metrics import confusion_matrix

pathDataSet ="./dataset"
pathDataTest = "./test"
pathDataTrain ="./train"
pathDescripteur="./descripteur"
pathConfusion="./matrix_confusion"
listDossiers = listdir(pathDataTest)

#Affichage de l'image  avec matplotlib
def show_rgb_img(img):
    return plt.imshow(cv2.cvtColor(img, cv2.CV_32S))

#Transformation de l'image en niveau de gris et affichage avec matplotlib
def a_gris(color_img):
    gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    return gray

# Generation des point d'intérêt et des descripteurs
def gen_sift_pi(gray_img):
    sift = cv2.xfeatures2d.SIFT_create()
    kp, desc = sift.detectAndCompute(gray_img, None)
    return kp, desc

#Affichage des points d'intérêts
def show_sift_features(gray_img, color_img, kp):
    return plt.imshow(cv2.drawKeypoints(gray_img, kp, color_img.copy()))

#Creation du fichier pour stockage des descripteurs pickle
def pickle_fch_descripteur(fichier,descripteur):   
    pkl=pickle.Pickler(fichier)
    pkl.dump(descripteur)
    
#Récupération du descripteur Unpickle
def unpickle_fch_descripteur(fichier):   
    Unpkl=pickle.Unpickler(fichier)
    fic=(Unpkl.load())
    return fic
   
#Génération des points d'intérets et des descripteurs    
def grt_descripteur(chemin_image):
    image_rgb = cv2.imread(chemin_image)
    image_gris = a_gris(image_rgb)
    
    # génération des point d'intérêts et des descripteur avec SIFT 
    image_pi, image_descip = gen_sift_pi(image_gris)
    #show_sift_features(image_gris, image_rgb, image_pi)
    return image_descip

#Génération des points d'intérets et des descripteurs    
def grt_descr_image_only(chemin_image):
    image_rgb = cv2.imread(chemin_image)
    image_gris = a_gris(image_rgb)
    
    # génération des point d'intérêts et des descripteur avec SIFT 
    image_pi, image_descip = gen_sift_pi(image_gris)
    #show_sift_features(image_gris, image_rgb, image_pi)
    return image_pi,image_descip
  
    
#Apprentissage avec une image( Lecture de l'image et transformation a niveau de gris)
def crt_descripteur():
    print("==============================================================================")
    print("                      GENERATION DES DESCRIPTEURS                              ")
    print("                                            ")
    listDossier = listdir(pathDataTrain)
    
    for file in  listDossier:
        listImage = os.listdir(pathDataTrain+"/"+file)
        cheminDescripteur = pathDescripteur + "/" + file
        chemin_Image = (pathDataTrain+"/"+file)
        if not os.path.exists(cheminDescripteur):
            os.mkdir(cheminDescripteur)
        listDescripteur=[]
        #creation du fichier du descripteur
        f = open((cheminDescripteur+"/"+file+".txt"),'wb')
        for image in listImage:
            descripteur = grt_descripteur((chemin_Image+"/"+image))
            listDescripteur.append(descripteur)
        pickle_fch_descripteur(f,listDescripteur)
        f.close   
            
#Fonction pour le test
def test_image(image,ratio=0.75):
    descripteur = grt_descripteur(image)
    listDossier = listdir(pathDescripteur)
    categorie=""
    nb_max_image_corr=0
    for dossier in listDossier:
        nb_image_corr=0
        f = open((pathDescripteur+"/"+dossier+"/"+dossier+".txt"),"rb")
        listeDescripteur = unpickle_fch_descripteur(f)
        for descripteur_img in listeDescripteur:
           nb_correspondance=[]
           if (descripteur_img is not None):
               bf = cv2.BFMatcher()
               matches = bf.knnMatch(descripteur,descripteur_img,k=2)
               if(len(matches[0])>1 ):
                   for m,n in matches:
                       if ((m.distance / n.distance)<0.4):
                           nb_correspondance.append([m])
               if ((len(nb_correspondance)/len(descripteur))>0.5):
                  nb_image_corr+=1
        if nb_image_corr>nb_max_image_corr:
            categorie=dossier
            nb_max_image_corr=nb_image_corr
    return categorie

pourcentage=[]
realite=[]
prediction=[]
label=[]
#Test du data set de test et calcul du taux de réussite
def test_dataset(ratio=0.75):
    print("==============================================================================")
    print("TEST DU DATASET VEUILLEZ PATIENTER")
    print("                                            ")
    for test in  listDossiers:
        image_bien_classe=0
        label.append(test)
        listImage = os.listdir(pathDataTest+"/"+test)
        print(test)
        for image in listImage:
            lien=(("./test/"+test+"/"+image))
            categorie = test_image(lien,ratio)
            realite.append(test)
            prediction.append(categorie)
            #print(image, "   prediction ===  ", categorie)
            if  categorie == test:
                image_bien_classe+=1
        p = test + "  " , ((image_bien_classe*100)/len(listImage))
        pourcentage.append(p)
        print(test)
        print("Taux de réussite: ", ((image_bien_classe*100)/len(listImage)),"%")
        print("===============================================================")
        print("                                                                 ")
    fiche = open((pathConfusion+"/pourcentage.txt"),'wb')
    pickle_fch_descripteur(fiche,pourcentage)
    fiche.close
    m_confusion = confusion_matrix(realite, prediction,label)
    fic = open((pathConfusion+"/realite.txt"),'wb')
    pickle_fch_descripteur(fic,realite)
    fic.close 

    fich = open((pathConfusion+"/prediction.txt"),'wb')
    pickle_fch_descripteur(fich,prediction)
    fich.close 
    
    fi = open((pathConfusion+"/matrice.txt"),'wb')
    pickle_fch_descripteur(fi,m_confusion)
    fi.close 

    fc = open((pathConfusion+"/label.txt"),'wb')
    pickle_fch_descripteur(fc,label)
    fc.close  

def affichage_PI_image(lien, lien1):
    k,d=grt_descr_image_only(lien)
    k1,d1=grt_descr_image_only(lien1)
     
    image_rgb = cv2.imread(lien)
    image_gris = a_gris(image_rgb)
    image_rgb1 = cv2.imread(lien1)
    image_gris1 = a_gris(image_rgb1)
    
    N_MATCHES = 100
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    
    matches = bf.match(d, d1)

# Sort the matches in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)


    match_img = cv2.drawMatches(
    image_gris, k,
    image_gris1, k,
    matches[:N_MATCHES], image_gris.copy(), flags=0)

    plt.figure(figsize=(14,5))
    
    plt.imshow(match_img);
   
#affichage_PI_image(("/home/nicolas/Bureau/i.png"),     "/home/nicolas/PycharmProjects/Sift_TP2/dataset/obj1/obj1__0.png")