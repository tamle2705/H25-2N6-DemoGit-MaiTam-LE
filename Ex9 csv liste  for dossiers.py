import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv


 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Vous voulez créer un dossier par Lan Party
#         Et pour chaque Lan Party, créez des sous-dossier pour chaque jeu
#                   (On y mettra éventuellement la liste des participants du Lan qui veulent jouer à ce jeu)
#         ATTENTION: Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères

#         Si besoin, des instructions détaillées sont données plus bas





















# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Créez un dossier pour le nom du Lan Party
#      Déplacez vous dans ce dossier
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
#      Créez un dossier pour le jeu avec le nouveau nom de jeu
#      Revenez au dossier parent

fichier_a_lire = os.path.join('csvs','Ex7 Lan Party.csv')


liste_jeux = []
with open(fichier_a_lire, "r", encoding="utf-8") as fichier_lu : # Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
    lecteur_csv = csv.reader(fichier_lu, delimiter=";") # utilisez csv.reader pour lire le fichier avec le bon delimiter
    next(lecteur_csv) # Sautez la première ligne de l'entête
    for ligne_fichier in lecteur_csv : # Faites une boucle pour passer à travers chacune des lignes 
        repertoire_courant = os.getcwd()
        dossier_existe = os.path.isdir(f"{repertoire_courant}\\Lan Party") # Créez un dossier pour le nom du Lan Party
        if dossier_existe == False :
            os.mkdir("Lan Party")
        os.chdir("Lan Party") # Déplacez vous dans ce dossier
        jeux_3 = ligne_fichier[1:4] # slicing pour garder uniquement les 3 jeux
        for chaque_jeu in jeux_3 : # Faites une boucle pour passer à travers chacun des jeux
            nom_modifie = chaque_jeu.replace(":", "_") # Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
            nouveau_nom = nom_modifie[:20]
            
            sous_dossier_existe = os.path.isdir(f"{nouveau_nom}")
            if sous_dossier_existe == False :   
                os.mkdir(nouveau_nom) # Créez un dossier pour le jeu avec le nouveau nom de jeu
                liste_jeux.append(nouveau_nom)
            print(f"Q2: {liste_jeux}")
            print(f"Q2: {os.getcwd()}")
        
        os.chdir(repertoire_courant) # Revenez au dossier parent

            


