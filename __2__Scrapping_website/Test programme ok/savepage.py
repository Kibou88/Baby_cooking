import requests
from bs4 import BeautifulSoup

# Les informations de connexion
login_payload = {
    'username': "audrey.laporte@laposte.net",
    'password': 'Chocolate55!'
}

# URL du formulaire de connexion
login_url = 'https://www.cuisinez-pour-bebe.fr/se-connecter/'

# URL de la page à enregistrer après la connexion
page_url = 'https://www.cuisinez-pour-bebe.fr/pumpkin-biscuits/'

# Créez une session pour gérer la persistance de la connexion
with requests.Session() as session:
    # Connectez-vous en envoyant une requête POST avec les informations d'authentification
    login_response = session.post(login_url, data=login_payload)

        # Maintenant que vous êtes connecté, vous pouvez récupérer la page protégée
    protected_page = session.get(page_url)

        # Utilisez Beautiful Soup pour analyser et enregistrer la page
    soup = BeautifulSoup(protected_page.text, 'html.parser')

        # Enregistrez la page dans un fichier
    with open('page_protegee.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
