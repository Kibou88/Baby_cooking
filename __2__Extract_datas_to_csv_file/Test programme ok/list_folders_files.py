import os

folder_source = "C:/Users/Satoshi/Desktop/Extraction_recettes/"

get_folders = os.listdir(folder_source)
print("Noms des dossiers: ", get_folders)

for folder in get_folders:
    file_in_folder = folder_source + folder # Permet de mettre le lien vers un dossier (Famille, sucrée ou salée)
    get_files = os.listdir(file_in_folder)
    print(f"Dans le répertoire {folder}, il y a {len(get_files)} recettes")

