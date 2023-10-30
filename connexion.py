#Fonction pour se connecter automatiquement au site
def connexion_auto():
  from selenium import webdriver  # Importation du module Selenium
  from selenium.webdriver.common.by import By  # Importation du module By pour les éléments du navigateur
  from tqdm import tqdm # Importation du module pour la barre de chargement
  import time # Importation du module pour utiliser un délai


  # Spécifiez le User-Agent que vous souhaitez utiliser
  user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
  # Configuration pour le mode headless (invisble)
  firefox_option = webdriver.FirefoxOptions()
  firefox_option.add_argument('--headless')  # Active le mode headless
  firefox_option.add_argument(f"user-agent={user_agent}")

  url = "https://www.cuisinez-pour-bebe.fr/se-connecter/"
  mail = "audrey.laporte@laposte.net"
  motDePasse = "Chocolate55!"
  page = webdriver.Firefox(options=firefox_option)  #Création de l'objet page pour le navigateur Firefox
  #Ajouter options=firefox_option entre les () pour faire une connexion invisible
  page.get(url)
  # Inscription login + password et valide pour se connecter
  with tqdm(total=6, desc="Connexion en cours") as pbar:
      caseMail = page.find_element(By.ID, "iump_login_username")  # Recherche de l'élément login par ID
      time.sleep(0.25)
      pbar.update(1)
      caseMail.send_keys(mail)  # Envoi la valeur contenu dans mail dans la case "login"
      time.sleep(0.25)
      pbar.update(1)
      caseMdp = page.find_element(By.ID, "iump_login_password")  # Recherche de l'élément mot de passe par ID
      time.sleep(0.25)
      pbar.update(1)
      caseMdp.send_keys(motDePasse)  # Envoi la valeur contenu dans mail dans la case "login"
      time.sleep(0.25)
      pbar.update(1)
      buttonLogin = page.find_element(By.NAME, "Submit")  # Recherche de l'élément "Connexion" avec son nom
      time.sleep(0.25)
      pbar.update(1)
      buttonLogin.click()  # Clique sur l'élément qu'on a sélectionné
      pbar.update(1)

  url_connexion = page.current_url
  if not "login_fail" in url_connexion:
      print("\033[0;32mConnexion réussie")
      new_url = "https://www.cuisinez-pour-bebe.fr/recette-bebe/"
      page.get(new_url)
      return new_url, page
  else:
      # print("\n")
      print("\033[0;31mConnexion échoué")
      print("\033[0;31mErreur nom d'utilisateur et/ou mot de passe")
      quit()


