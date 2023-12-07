from cx_Freeze import setup, Executable
base = None
# Remplacer "main.py" par le nom du script qui lance votre programme
executables = [Executable("main.py", base=base)]
# Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna", "tqdm", "time", "os", "random", "bs4", "selenium.webdriver.common.keys",
            "selenium.webdriver.common.by","selenium"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
# Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Scrapping_website",
    options = options,
    version = "1.0",
    description = "Ce programme a pour but de se connecter automatiquement au site 'Cuisinez bébé', et de récupérer"
                  "les recettes par rapports aux choix de l'utilisateur",
    executables = executables
)