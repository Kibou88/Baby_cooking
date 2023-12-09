Attribute VB_Name = "Fonctions"
Function CompterEspaces(chaine As String) As Integer
    Dim i As Integer
    Dim compteur As Integer
    
    ' Initialisation du compteur à zéro
    compteur = 0
    
    ' Parcours de la chaîne caractère par caractère
    For i = 1 To Len(chaine)
        ' Vérification si le caractère actuel est un espace
        If Mid(chaine, i, 1) = " " Then
            ' Incrémentation du compteur si c'est un espace
            compteur = compteur + 1
        End If
    Next i
    
    ' Retourne le nombre total d'espaces comptés
    CompterEspaces = compteur
End Function
Function derniere_ligne(name As String) As Integer
    'Fonction pour trouver la dernière ligne d'un onglet
    Dim Lig As Integer
    Lig = 1 'première ligne à vérifier
    Do While Not IsEmpty(Worksheets(name).Cells(Lig, 1).Value)
        Lig = Lig + 1
    Loop
    derniere_ligne = Lig ' Assigner la valeur à la fonction
    ' Debug.Print Lig 'On affiche la valeur de Lig
End Function
Sub ProcessIngredientsFromSheet(sheetName As String)
    Dim liste_total_ingredients As String
    Dim delimiteurs As Variant
    Dim delimiteursInutiles As Variant
    Dim delimiteursQuantite As Variant
    Dim tri_ingredients() As String
    Dim ingredients As String
    Dim m As Integer
    Dim last_ligne As Integer

    m = 2
    last_ligne = derniere_ligne(sheetName) ' attribuer la valeur retournée par la fonction à last_ligne
    For l = 2 To last_ligne ' Boucle à travers les lignes pour récupérer les ingrédients
        liste_total_ingredients = Worksheets(sheetName).Cells(l, 2).Value

        'Délimiteurs supplémentaires à remplacer
        delimiteurs = Array("'", "[", "]")
        delimiteursInutiles = Array("c. à soupe", "c. à café", "sel", "poivre", "huile dolive", "de sésame", "olive")
        delimiteursQuantite = Array("", "mg ", "cg ", "g ", "kg ", "mL ", "cL ", "L ", "à ")

        'Remplacer les délimiteurs supplémentaires par le délimiteur principal rien
        For i = LBound(delimiteurs) To UBound(delimiteurs)
            liste_total_ingredients = Replace(liste_total_ingredients, delimiteurs(i), "")
            liste_total_ingredients = Replace(liste_total_ingredients, "  ", " ")
        Next i

        'Séparer la chaîne de caractères à chaque ','
        tri_ingredients = Split(liste_total_ingredients, ",")
        
        For x = LBound(tri_ingredients) To UBound(tri_ingredients)
            tri_ingredients(x) = Trim(tri_ingredients(x)) 'Supprimer les espaces en début et fin
             nbEspaces = CompterEspaces(tri_ingredients(x))
            Debug.Print "Nom:" & tri_ingredients(x)
                       
            ' Trouver la position du caractère dans le texte complet
           positionCaractere = InStr(tri_ingredients(x), " ")
           ingredients = Right(tri_ingredients(x), Len(tri_ingredients(x)) - positionCaractere) ' Commence la chaine de caractère après le 1er espace
            
            For n = LBound(delimiteursInutiles) To UBound(delimiteursInutiles)
                If InStr(ingredients, delimiteursInutiles(n)) > 0 Then
                    ingredients = ""
                End If
            Next n

            For d = LBound(delimiteursQuantite) To UBound(delimiteursQuantite)
                ingredients = Replace(ingredients, delimiteursQuantite(d), "")
            Next d
                
            Worksheets("Liste_ingrédients").Cells(m, 1).Value = ingredients
            m = m + 1
        Next x
    Next l
    On Error Resume Next ' Pour gérer les éventuelles erreurs
    Worksheets("liste_ingrédients").Range("A:A").RemoveDuplicates Columns:=1, Header:=xlNo
    On Error GoTo 0 ' Réactiver la gestion normale des erreurs
End Sub


