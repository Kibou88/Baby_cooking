#Fonction pour ajouter les différents choix de l'utilisateur dans l'adresse url
def url_including_choice(page_recettes, format_choice):
  page_recettes = page_recettes+"?"
  count = 0
  if len(format_choice) <= 2: # Si il n'y a qu'1 choix
    match format_choice:
      case "0":  # Age entre 9 et 12 mois
        page_recettes = page_recettes + "wp_recettes%5BrefinementList%5D%5Bage%5D%5B0%5D=9%20%C3%A0%2012%20mois"
      case "1":  # Age de 12 mois et +
        page_recettes = page_recettes + "wp_recettes%5BrefinementList%5D%5Bage%5D%5B1%5D=12%20mois%20et%20%2B"
      case "10":  # Repas sucrée
        page_recettes = page_recettes + "wp_recettes%5BrefinementList%5D%5Bmoment%5D%5B0%5D=Sucr%C3%A9"
      case "11":  # Repas salée
        page_recettes = page_recettes + "wp_recettes%5BrefinementList%5D%5Bmoment%5D%5B0%5D=Sal%C3%A9"
      case "20":  # Repas famille
        page_recettes = page_recettes +"wp_recettes%5BrefinementList%5D%5Btype%5D%5B0%5D=Parents-b%C3%A9b%C3%A9"
        print("Page famille choisie")
      case _:  # Si aucun choix n'est sélectionné
        print(f"Le choix {format_choice} n'est pas valide")
  elif len(format_choice) > 2: # Si il y a plusieurs choix
    for i in format_choice:
        if count != 0 and count < len(format_choice):
          page_recettes = page_recettes +"&"
        match i:
          case "0": #Age entre 9 et 12 mois
            page_recettes = page_recettes+"wp_recettes%5BrefinementList%5D%5Bage%5D%5B0%5D=9%20%C3%A0%2012%20mois"
            count += 1
          case "1": #Age de 12 mois et +
            page_recettes = page_recettes+"wp_recettes%5BrefinementList%5D%5Bage%5D%5B1%5D=12%20mois%20et%20%2B"
            count += 1
          case "10": #Repas sucrée
            page_recettes = page_recettes+"wp_recettes%5BrefinementList%5D%5Bmoment%5D%5B0%5D=Sucr%C3%A9"
            count += 1
          case "11": #Repas salée
            page_recettes = page_recettes+"wp_recettes%5BrefinementList%5D%5Bmoment%5D%5B0%5D=Sal%C3%A9"
            count += 1
          case _: #Si aucun choix n'est sélectionné
            print(f"Le choix {i} n'est pas valide en multi choix")
  return page_recettes

#Fonction pour parser la page en fonction des choix utilisateurs
def parser_page(page):
  from bs4 import BeautifulSoup
  page_source = page.page_source
  soup = BeautifulSoup(page_source, 'html.parser')
  return soup

#Fonction pour récupérer toutes les balises <li> avec la classe: "ais-Hits-item"
def recup_balises_li(page_soup):
  balises_li = page_soup.find_all('li', class_="ais-Hits-item")
  return balises_li

#Fonction pour récupérer dans les liens et les noms
def recup_liens_noms(balises_li,liste_nom, liste_lien):
  for balise in balises_li:
    name = balise.find('p').string
    link = balise.find('a')

    if not "Batch" in name:
      liste_nom.append(name)
      liste_lien.append(link.get('href'))
  return liste_nom, liste_lien

#Fonction pour récupérer les balises <div> sur une recette
def recup_balises_div(page_recette_soup):
  balises_div = page_recette_soup.find_all('div', class_="wprm-recipe-template-recette-individuelle-overlay-container")
  return balises_div

#Fonction pour récupérer le lien de la page print
def lien_print(balises_div):
  link_print=[]
  for div in balises_div:
    link = div.find('a')
    link_print.append(link.get('href'))
  print("liste: ",  link_print)
  return link_print