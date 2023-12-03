# Fonction pour récupérer les dossiers "Famille", "Sucrée" et "Salée"
def list_folders():
    import os
    folder_source = "C:/Users/Satoshi/Desktop/Extraction_Recettes/"
    get_folders = os.listdir(folder_source)
    print("Noms des dossiers: ", get_folders)
    return get_folders, folder_source

# Fonction pour récupérer les recettes dans chaque dossier
def list_files(folder, folder_source):
    import os
    file_in_folder = folder_source + folder  # Permet de mettre le lien vers un dossier (Famille, sucrée ou salée)
    get_files = os.listdir(file_in_folder)
    print(f"Dans le répertoire {folder}, il y a {len(get_files)} recettes")
    return get_files, file_in_folder

# Fonction pour enregistrer dans une variable l'emplacement d'un fichier recette HTML
def address_file(file_in_folder, file):
    file_html = file_in_folder+"/"+file
    return file_html

# Fonction pour ouvrir un fichier recette HTML
def open_parse_file_HTML(file_html):
    from bs4 import BeautifulSoup
    with open(file_html,'r', encoding='UTF-8') as file_html:
        html_soup = BeautifulSoup(file_html, 'html.parser')
    return html_soup

# Fonction pour récupérer les balises <li>
def save_balises_li(html_soup):
    from bs4 import BeautifulSoup
    list_li = html_soup.find_all('li', class_="wprm-recipe-ingredient")
    return list_li

# Fonction pour récupérer les ingrédients
def recup_ingredients(lien):
      try:
          quantite = lien.find('span', class_="wprm-recipe-ingredient-amount").string
      except AttributeError:
          quantite = ""
      try:
          aliments = lien.find('span', class_="wprm-recipe-ingredient-name").string
      except AttributeError:
          aliments = ""
      try:
          unite = lien.find('span', class_="wprm-recipe-ingredient-unit").string
      except AttributeError:
          unite = ""
      return quantite, aliments, unite