from selenium import webdriver # Importation du module Selenium
from selenium.webdriver.common.by import By # Importation du module By pour les éléments du navigateur
import time
from tqdm import tqdm


# Configuration pour le mode headless (invisble)
firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument('--headless')  # Active le mode headless

url = "https://www.cuisinez-pour-bebe.fr/se-connecter/"
mail = "audrey.laporte@laposte.net"
motDePasse = "Chocolate56!"
page = webdriver.Firefox(options=firefox_option) #Création de l'objet page pour le navigateur Firefox
#Ajouter options=firefox_option entre les () pour faire une connexion invisible
page.get(url)
# Utilisation de TQDM pour suivre la progression
with tqdm(total=6,desc="Connexion en cours") as pbar:
    caseMail= page.find_element(By.ID,"iump_login_username") #Recherche de l'élément login par ID
    time.sleep(0.5)
    pbar.update(1)
    caseMail.send_keys(mail) #Envoi la valeur contenu dans mail dans la case "login"
    time.sleep(0.5)
    pbar.update(1)
    caseMdp = page.find_element(By.ID, "iump_login_password") #Recherche de l'élément mot de passe par ID
    time.sleep(0.5)
    pbar.update(1)
    caseMdp.send_keys(motDePasse) #Envoi la valeur contenu dans mail dans la case "login"
    time.sleep(0.5)
    pbar.update(1)
    buttonLogin= page.find_element(By.NAME, "Submit") #Recherche de l'élément "Connexion" avec son nom
    time.sleep(0.5)
    pbar.update(1)
    buttonLogin.click() #Clique sur l'élément qu'on a sélectionné
    time.sleep(0.5)
    pbar.update(1)

# Récupérez l'adresse URL de la page après la connexion réussie

url_apres_connexion = page.current_url

# Affichez l'URL ou faites-en ce que vous voulez
print("Adresse URL après connexion :", url_apres_connexion)

if not "login_fail" in url_apres_connexion:
  print("Connexion réussie")
else:
    print("Connexion échoué")
    print("Erreur nom d'utilisateur et/ou mot de passe")
    quit()