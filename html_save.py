# Fonction permettant d'enregistrer les pages dans un dossier spécifique
def directory(format_choice):
    import os

    match format_choice:
            case "10": # L'utilisateur a choisi le sucrée
                folder = "Sucrée/"
            case "11":  # L'utilisateur a choisi le salée
                folder = "Salée/"
            case "20": # L'utilisateur a choisi la famille
                folder = "Famille/"
            # Code pour choisir le dossier de destination
    repertory = ''.join(["C:/Users/Satoshi/Desktop/Extraction_recette/"+folder])
    os.chdir(repertory)
    return repertory

# Fonction pour enregistrer la page HTML
def save_page(page, output_file):
  page_source = page.page_source
  with open(output_file, 'w', encoding='utf-8') as file:
      file.write(page_source)

# Fonction pour mettre un temps de repos entre 2 apges
def delay():
    import random
    attente = random.uniform(1,5)
    return attente