import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By # Importation du module By pour les éléments du navigateur
from selenium.webdriver.common.keys import Keys # Importation du module By pour les éléments du navigateur
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import BaseWebDriver

# Configuration pour le mode headless (invisble)
firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument('--headless')  # Active le mode headless


url = "https://www.cuisinez-pour-bebe.fr/se-connecter/"
mail = "audrey.laporte@laposte.net"
motDePasse = "Chocolate55!"
page = webdriver.Firefox(options=firefox_option) #Création de l'objet page pour le navigateur Firefox
#Ajouter options=firefox_option entre les () pour faire une connexion invisible
page.get(url)

caseMail= page.find_element(By.ID,"iump_login_username") #Recherche de l'élément login par ID
caseMail.send_keys(mail) #Envoi la valeur contenu dans mail dans la case "login"
caseMdp = page.find_element(By.ID, "iump_login_password") #Recherche de l'élément mot de passe par ID
caseMdp.send_keys(motDePasse) #Envoi la valeur contenu dans mail dans la case "login"
time.sleep(2)
buttonLogin= page.find_element(By.NAME, "Submit") #Recherche de l'élément "Connexion" avec son nom
buttonLogin.click() #Clique sur l'élément qu'on a sélectionné

# Récupérez l'adresse URL de la page après la connexion réussie
url_apres_connexion = page.current_url

# Affichez l'URL ou faites-en ce que vous voulez
print("Adresse URL après connexion :", url_apres_connexion)

new_url = "https://www.cuisinez-pour-bebe.fr/pumpkin-biscuits/"
page.get(new_url)
page_source = page.page_source
with open("essai.html", 'w', encoding='utf-8') as file:
    file.write(page_source)

