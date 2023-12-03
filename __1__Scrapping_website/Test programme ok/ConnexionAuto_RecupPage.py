from selenium import webdriver # Importation du module Selenium
import time # Importation du module time pour la fonction sleep
from selenium.webdriver.common.by import By # Importation du module By pour les éléments du navigateur
from selenium.webdriver.common.keys import Keys
import urllib

# Configuration pour le mode headless (invisble)
firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument('--headless')  # Active le mode headless

url = "https://www.cuisinez-pour-bebe.fr/se-connecter/"
mail = "audrey.laporte@laposte.net"
motDePasse = "Chocolate55!"
page = webdriver.Firefox() #Création de l'objet page pour le navigateur Firefox
#Ajouter options=firefox_option entre les () pour faire une connexion invisible
page.get(url)

caseMail= page.find_element(By.ID,"iump_login_username") #Recherche de l'élément login par ID
caseMail.send_keys(mail) #Envoi la valeur contenu dans mail dans la case "login"
caseMdp = page.find_element(By.ID, "iump_login_password") #Recherche de l'élément mot de passe par ID
caseMdp.send_keys(motDePasse) #Envoi la valeur contenu dans mail dans la case "login"

buttonLogin= page.find_element(By.NAME, "Submit") #Recherche de l'élément "Connexion" avec son nom
buttonLogin.click() #Clique sur l'élément qu'on a sélectionné

# Récupérez l'adresse URL de la page après la connexion réussie
url_apres_connexion = page.current_url
new_url = "https://www.cuisinez-pour-bebe.fr/recette-bebe/?wp_recettes%5BrefinementList%5D%5Bage%5D%5B0%5D=9%20%C3%A0%2012%20mois&wp_recettes%5BrefinementList%5D%5Bage%5D%5B1%5D=12%20mois%20et%20%2B&wp_recettes%5BrefinementList%5D%5Bmoment%5D%5B0%5D=Sucr%C3%A9"
page.get(new_url)
time.sleep(2)
#urllib permet d'enregistrer la page comme elle apparaît
urllib.request.urlretrieve(new_url, "Recettes/Pumpkin.html") #2nd argument: mettre le lien du dossier où enregistrer le fichier
#A activer pour suivre le cheminement auto
for i in range(15):
  page.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
  page.implicitly_wait(5)
  time.sleep(3)
