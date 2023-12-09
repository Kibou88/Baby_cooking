Attribute VB_Name = "MAJ_ouverture_excel"
Private Sub Workbook_Open()
    Dim ws As Worksheet
    Dim lastRow As Long

    ' Sp�cifie la feuille sur laquelle tu veux travailler
    Set ws = ThisWorkbook.Sheets("NomDeTaFeuille") ' Remplace "NomDeTaFeuille" par le nom de ta feuille

    ' V�rifie si on est � la fin du mois
    If Day(Now) = Day(DateAdd("d", 1, DateSerial(Year(Now), Month(Now) + 1, 1))) Then
        ' Trouve la derni�re ligne avec des donn�es dans la colonne A
        lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row

        ' Copie les valeurs de la colonne A � partir de la ligne 1 vers la colonne B
        ws.Range("A1:A" & lastRow).Copy Destination:=ws.Range("B1")
    End If
End Sub


