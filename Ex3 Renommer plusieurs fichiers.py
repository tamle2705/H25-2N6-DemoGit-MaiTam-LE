# importez os
import os

# # allez dans le dossier Ex3 Videos
info_repertoire = "C:\\Users\9055224\\OneDrive - Cégep Édouard-Montpetit\H2025\\420-2N6-EM - Programmation 2\\OneDrive_2025-01-30\\R03 Exercices Depart\\Ex3 Videos"
repertoire = os.listdir(info_repertoire)

# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

for fichier in repertoire : # boucle for, passez à travers chacun des dossiers de os.listdir()
    nom_fichier, extension = os.path.splitext(fichier) # utilisez os.path.splitext pour obtenir le filename et l'extension
    if "_" in nom_fichier :
        titre, cours, info_cours = nom_fichier.split("_") # utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
        titre = titre.strip() # utilisez strip pour enlever les espaces pour le titre
        info_cours = info_cours.strip() # utilisez strip pour enlever les espaces pour le numéro
        carac_spec, no_cours = info_cours.split("#") # séparer le caractère spécial et numéro
        no_cours = no_cours.zfill(2) # remplir le numéro de sorte que 1 deviendra 01
        nouveau_nom = titre + cours + no_cours + extension
        os.rename(os.path.join(info_repertoire, fichier), os.path.join(info_repertoire, nouveau_nom))
        print(titre)
        print(cours)
        print(no_cours)