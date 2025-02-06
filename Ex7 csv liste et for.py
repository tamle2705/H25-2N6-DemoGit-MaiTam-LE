import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Regardez le contenu du fichier "Ex7 Lan Party.csv"
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                 Lan Party;Top 1;Top 2; Top 3
#          Top 1, Top 2 et Top 3 sont les jeux les plus populaires dans chaque Lan Party
#          
#          Vous aimez jouer à Valorant
#          Imprimez la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops
# 
#          Aucune instruction détaillée n'est donnée plus bas

ficher_a_lire = os.path.join("csvs", "Ex7 Lan Party.csv")

#repertoire = os.getcwd()
with open(ficher_a_lire, "r", encoding ="utf-8") as fichierlu :
    lecteur_csv = csv.reader(fichierlu,delimiter=";")
    next(lecteur_csv)
    jeu_prefere = "Valorant"
    for ligne_fichier in lecteur_csv :
        if (jeu_prefere in ligne_fichier[1]) or (jeu_prefere in ligne_fichier[2]) or (jeu_prefere in ligne_fichier[3]) :
            print(f"la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops : {ligne_fichier[0]}")

