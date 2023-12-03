from list_folders_files import *
from functions_csv import *
from tqdm import tqdm

#----------Récupération des dossiers et recettes dans chaque dossier---------
get_folders, folder_source = list_folders()
main_folder()
for folder in get_folders:
    get_files, file_in_folder = list_files(folder, folder_source) # Test ok
    file_csv = create_csv(folder)
    with tqdm(total=len(get_files), desc=f"Fichier {folder} en cours") as pbar:
        for file in get_files:
            file_html = address_file(file_in_folder, file) # Fonction pour récupérer le chemin d'accès du fichier HTML complet
            try:
                html_soup = open_parse_file_HTML(file_html) # Fonction pour ouvrir et parser le fichier HTML
            except FileNotFoundError:
                continue
            list_li = save_balises_li(html_soup) # Fonction pour récupérer les balises <li>
            liste_ingredients = []
            for lien in list_li:
                quantite, aliments, unite = recup_ingredients(lien) # Fonction pour extraire la liste des ingrédients
                liste_ingredients.append(quantite + " " + unite + " " + aliments)

            #-------Test ok------------
            add_elements_csv(file_csv, file, liste_ingredients)
            pbar.update(1)







