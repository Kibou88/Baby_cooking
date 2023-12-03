#Extraction recette
#main.py
#But:
#Extraire toutes les recettes sucrees
#du site "cuisinez-bebe"

#Importation des modules et fonctions
from interface import *
from connexion import *
from html_function import *
from defilement import *
from html_save import *
from tqdm import tqdm
import time

#-----------Interface utilisateur---------------
valid = "n"
while valid == 'n':  #Boucle pour permettre à l'utilisateur de changer ses choix
  message()  #Affiche l'interface
  user_choice = choices()  #Permet à l'utilisateur de faire un choix
  format_choice = formatting(user_choice)
  valid = confirm()
#------------Test ok----------------------

#-----------Connexion automatique---------------
page_recettes, page = connexion_auto()  #Fait la connexion automatiquement + renvoie l'url de la page "Recette bébé"
#-----------Test ok----------------------

#-----------Affichage de la page "Recette" en fonction des choix utilisateurs---------------
page_recettes_choisies = "" #Variable pour stocker l'url de la page recette
# print("Valeur de format choice: ", format_choice)
page_recettes_choisies = url_including_choice(page_recettes, format_choice)  #Ajoute les choix utilisateurs dans l'url
page.get(page_recettes_choisies)
#-----------Test ok----------------------

#----------Récupération du lien et du titre de chaque recette-------------
balises_li = []  #Initialisation de la liste pour récupérer les balises <li>
liste_nom = []  #Initialisation de la liste pour récupérer les titres
liste_lien = []  #Initialisation de la liste pour récupérer les liens
nombre_defilement_bas = 200


defilement_auto_bas(page,nombre_defilement_bas) #Fonction pour faire défiler la page + barre de chargement
bas_page() #Fonction pour faire afficher le message "Bas de page atteint"
print("\033[0;33m") #Changement en orange
with tqdm(range(3),desc="Récupération des noms des recettes") as pbar:
  page_soup = parser_page(page)
  pbar.update(1)
  balises_li = recup_balises_li(page_soup)
  pbar.update(1)
  liste_nom, liste_lien = recup_liens_noms(balises_li,liste_nom, liste_lien)
  pbar.update(1)
total_nom = len(liste_nom)
print("\033[0;32mNombres de noms de recette récupérés: ", total_nom)
#-----------Test ok----------------------

#------------Enregistrer la page d'une recette-----------
print("\033[0;33m") #Changement en orange
count = 0
with tqdm(total=total_nom, desc="Extraction html en cours") as pbar:
  for i in range(total_nom): #Changer "range(2)" par "len(liste_nom)"
    page.get(liste_lien[i])
    output_file = liste_nom[i] + '.html'
    repertory = directory(format_choice)
    output_file = repertory + output_file
    save_page(page, output_file)
    pbar.update(1)
    count += 1
    time.sleep(delay())

print("\033[0;32mNombres de recettes extraites: ", count)
#-----------------------------------------------------------
quit()