from bs4 import BeautifulSoup

folder_source = "C:/Users/Satoshi/Desktop/Extraction_Recettes/Salée/"
url = "Bouchées à la courgette.html"
url_complet = folder_source + url
print(url_complet)
with open(url_complet, 'r',encoding='utf-8') as file_html:
    html_soup = BeautifulSoup(file_html, 'html.parser')

liens = html_soup.find_all('li', class_="wprm-recipe-ingredient")
liste_ingredients = []

for lien in liens:
    try:
      quantite = lien.find('span', class_="wprm-recipe-ingredient-amount").string
    except AttributeError:
        quantite = ""
    try:
      aliments = lien.find('span', class_="wprm-recipe-ingredient-name").string
    except AttributeError:
        aliments = ""
    # print(aliments)
    try:
      unite = lien.find('span', class_= "wprm-recipe-ingredient-unit").string
    except AttributeError:
        unite = ""

    liste_ingredients.append(quantite +" "+ unite + " " + aliments)
    print (liste_ingredients)