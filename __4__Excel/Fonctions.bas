Attribute VB_Name = "Fonctions"
Function CompterEspaces(chaine As String) As Integer
    Dim i As Integer
    Dim compteur As Integer
    
    ' Initialisation du compteur � z�ro
    compteur = 0
    
    ' Parcours de la cha�ne caract�re par caract�re
    For i = 1 To Len(chaine)
        ' V�rification si le caract�re actuel est un espace
        If Mid(chaine, i, 1) = " " Then
            ' Incr�mentation du compteur si c'est un espace
            compteur = compteur + 1
        End If
    Next i
    
    ' Retourne le nombre total d'espaces compt�s
    CompterEspaces = compteur
End Function
Function derniere_ligne(name As String) As Integer
    'Fonction pour trouver la derni�re ligne d'un onglet
    Dim Lig As Integer
    Lig = 1 'premi�re ligne � v�rifier
    Do While Not IsEmpty(Worksheets(name).Cells(Lig, 1).Value)
        Lig = Lig + 1
    Loop
    derniere_ligne = Lig ' Assigner la valeur � la fonction
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
    last_ligne = derniere_ligne(sheetName) ' attribuer la valeur retourn�e par la fonction � last_ligne
    For l = 2 To last_ligne ' Boucle � travers les lignes pour r�cup�rer les ingr�dients
        liste_total_ingredients = Worksheets(sheetName).Cells(l, 2).Value

        'D�limiteurs suppl�mentaires � remplacer
        delimiteurs = Array("'", "[", "]")
        delimiteursInutiles = Array("c. � soupe", "c. � caf�", "sel", "poivre", "huile dolive", "de s�same", "olive")
        delimiteursQuantite = Array("", "mg ", "cg ", "g ", "kg ", "mL ", "cL ", "L ", "� ")

        'Remplacer les d�limiteurs suppl�mentaires par le d�limiteur principal rien
        For i = LBound(delimiteurs) To UBound(delimiteurs)
            liste_total_ingredients = Replace(liste_total_ingredients, delimiteurs(i), "")
            liste_total_ingredients = Replace(liste_total_ingredients, "  ", " ")
        Next i

        'S�parer la cha�ne de caract�res � chaque ','
        tri_ingredients = Split(liste_total_ingredients, ",")
        
        For x = LBound(tri_ingredients) To UBound(tri_ingredients)
            tri_ingredients(x) = Trim(tri_ingredients(x)) 'Supprimer les espaces en d�but et fin
             nbEspaces = CompterEspaces(tri_ingredients(x))
            Debug.Print "Nom:" & tri_ingredients(x)
                       
            ' Trouver la position du caract�re dans le texte complet
           positionCaractere = InStr(tri_ingredients(x), " ")
           ingredients = Right(tri_ingredients(x), Len(tri_ingredients(x)) - positionCaractere) ' Commence la chaine de caract�re apr�s le 1er espace
            
            For n = LBound(delimiteursInutiles) To UBound(delimiteursInutiles)
                If InStr(ingredients, delimiteursInutiles(n)) > 0 Then
                    ingredients = ""
                End If
            Next n

            For d = LBound(delimiteursQuantite) To UBound(delimiteursQuantite)
                ingredients = Replace(ingredients, delimiteursQuantite(d), "")
            Next d
                
            Worksheets("Liste_ingr�dients").Cells(m, 1).Value = ingredients
            m = m + 1
        Next x
    Next l
    On Error Resume Next ' Pour g�rer les �ventuelles erreurs
    Worksheets("liste_ingr�dients").Range("A:A").RemoveDuplicates Columns:=1, Header:=xlNo
    On Error GoTo 0 ' R�activer la gestion normale des erreurs
End Sub


