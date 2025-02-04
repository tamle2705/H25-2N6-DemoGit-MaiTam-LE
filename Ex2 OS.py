import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{'_'*60}")
print(f"Q1: Imprimez le répertoire courant : {os.getcwd()}")


# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2: {os.environ.get('USERPROFILE')}")
print(f"Q2{'_'*60}")



# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
os.chdir("C:\\Users\\9055224\\Documents")
repertoire_courant = os.getcwd()
print(f"Q3: {repertoire_courant}")
print(f"Q3{'_'*60}")


# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4: {os.listdir()}")
print(f"Q4{'_'*60}")



# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
dossier_existe = os.path.isdir(f"{repertoire_courant}\\OS-ExercQ5")
if dossier_existe == False :
    os.mkdir("OS-ExercQ5")
print(f"Q5: {os.listdir()}")
print(f"Q5{'_'*60}")



# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
dossier_existe2 = os.path.isdir(f"{repertoire_courant}\\OS-ExercQ6")
if dossier_existe2 == False :
    os.makedirs("OS-ExercQ6\\Subdir1")
print(f"Q6: {os.listdir()}")
print(f"Q6{'_'*60}")



#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
if dossier_existe2 == False :
    os.rename("C:\\Users\\9055224\\Documents\\OS-ExercQ6\\Subdir1", "C:\\Users\\9055224\\Documents\\OS-ExercQ6\\Sous_repertoire")
print(f"Q7: {os.listdir("C:\\Users\\9055224\\Documents\\OS-ExercQ6")}")
print(f"Q7{'_'*60}")



# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
#fichiers_repertoire = os.listdir("C:\\Users\\9055224\\Documents\\OS-ExercQ6")
#os.chdir("C:\\Users\\9055224\\Documents\\OS-ExercQ6")
fichiers_repertoire = os.listdir("C:\\Users\\9055224\\Documents\\OS-ExercQ6")
##fichiers_repertoire = "C:\\Users\\9055224\\Documents\\OS-ExercQ6"
#for fichier in fichiers_repertoire :
    #nouvelle_location = os.path.join(fichiers_repertoire, fichier)
   # os.remove("C:\\Users\\9055224\\Documents\\OS-ExercQ6\\"-{fichier})

#os.rmdir()
#print(f"Q8: {os.listdir("C:\\Users\\9055224\\Documents\\OS-ExercQ6")}")
print(f"Q8{'_'*60}")





