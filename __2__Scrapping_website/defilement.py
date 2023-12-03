#Fonction pour faire défiler la page en bas et faire apparaître toutes les recettes
def defilement_auto_bas(page, nombre_defilement_bas):
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from tqdm import tqdm
    import time
    print("\033[0;33m")
    with tqdm(total=nombre_defilement_bas, desc="Défilement bas de la page en cours") as pbar:
        for nbre in range(nombre_defilement_bas):  # Boucle pour faire descendre la page en bas
    # Pour faire défiler en utilisant la touche Page Down :
          page.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
          pbar.update(1)
          time.sleep(0.25)

# Fonction pour afficher le message atteinte bas de page
def bas_page():
    print("\033[0;32mBas de page atteint")