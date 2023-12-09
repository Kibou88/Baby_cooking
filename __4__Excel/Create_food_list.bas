Attribute VB_Name = "Create_food_list"
Sub create_list()
    ProcessIngredientsFromSheet "Famille"
    ProcessIngredientsFromSheet "Sucrée" ' Remplacez "Feuille2" par le nom de votre deuxième feuille
    ProcessIngredientsFromSheet "Famille" ' Remplacez "Feuille3" par le nom de votre troisième feuille
End Sub



