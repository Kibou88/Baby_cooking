#Créer les dossiers par rapport à la liste
def create_folder(name_folder):
  import os
  import shutil


  #Boucle pour créer des dossiers
  if not os.path.exists(name_folder):
    os.mkdir(name_folder)
    print(f"Dossier {name_folder} créé avec succès.")
  else:
    print(f"Le dossier existe déjà")
"""      
  #Boucle pour supprimer des dossiers    
  for nom_dossier in nom_liste:
    if os.path.exists(nom_dossier):
      shutil.rmtree(nom_dossier)
      print(f"Dossier {nom_dossier} supprimé avec succès.")
    else:
      print(f"Le dossier n'existe pas déjà")"""

import os
liste = ("Alpha", "Bravo", "Charlie")
folder = input("Quel est le nom du sous-dossier")
#Code pour choisir le dossier de destination
repertory = ''.join(["C:/Users/Satoshi/Desktop/Code/Extraction recette/" + folder])
os.chdir(repertory)
for name in liste:
    create_folder(name)