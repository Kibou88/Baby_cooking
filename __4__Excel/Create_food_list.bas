Attribute VB_Name = "Create_food_list"
Sub create_list()
    ProcessIngredientsFromSheet "Famille"
    ProcessIngredientsFromSheet "Sucr�e" ' Remplacez "Feuille2" par le nom de votre deuxi�me feuille
    ProcessIngredientsFromSheet "Famille" ' Remplacez "Feuille3" par le nom de votre troisi�me feuille
End Sub



