# Fonction pour ajouter les éléments dans un fichier csv
def add_elements_csv(file_csv, file, liste_ingredients):
    import csv
    with open(file_csv, 'a', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([file, liste_ingredients])

# Fonction pour créer un fichier csv
def create_csv(folder):
    import csv
    en_tete = ['Recettes', 'Ingrédients']
    file_csv = folder + '.csv'
    with open(file_csv, 'w', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(en_tete)
    return file_csv

# Fonction pour mettre les csv dans le dossier
def main_folder():
    import os

    os.chdir("C:/Users/Satoshi/Desktop/Extraction_Recettes/")