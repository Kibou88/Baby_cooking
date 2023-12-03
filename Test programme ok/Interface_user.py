def messages():
  print("\033[0;36mBienvenue sur le programme pour extraire les recettes bébés"
        )  #Message en cyan
  print("\033[1;33mVoici les différents choix:")  #Message en jaune
  print("\033[0;35mAge:\t\t\t\t\t\033[0;32mRepas:"
        )  #Message violet pour Age et vert pour Repas
  print("\033[0;35m0: 9 mois à 12 mois\t\t\033[0;32m10: Sucrée"
        )  #Message violet pour Age et vert pour Repas
  print("\033[0;35m1: 12 mois et +\t\t\t\033[0;32m11: Salée"
        )  #Message violet pour Age et vert pour Repas
  print("\t\t\t\t\t\t\t\033[0;32m20: Famille"
        )  #Message vert pour Repas
  print("\n")  #Saut de ligne
  print("\033[0;31mPOUR CHOISIR, UTILISER LE '-' ENTRE CHAQUE CHOIX.\nMETTRE SOUS LA FORME '0-1-10'.")  #Message en rouge pour l'instruction


#Function to permit the user to choose
def choices():
  user_choice = input(
      "\033[0;34mQuel est votre choix: ")  #Demande à l'utilisateur de choisir
  return user_choice


#Function to format the user's choice(s) i.e:'0-1-11' to the list i.e:[0,1,11]
def formatting(user_choice):
  if user_choice == "20":
      format_choice = "20"
  else:
    user_choice = user_choice.split("-")  # Sépare les choix en 3 parties
    format_choice = user_choice
  print("\033[0;34mVous avez choisi: ", format_choice)
  return format_choice


#Function to validate by the user his choice(s)
def confirm(valid):
  valid = input(
      "\033[0;33mVoulez vous confirmer votre choix? O pour 'Oui' et N pour 'Non': "
  )
  print("\n")
  return valid


valid = "O"
while (
    valid.lower != "n"
):  #Boucle pour permettre à l'utilisateur de changer ses choix, si il le veut
  messages()
  user_choice = choices()
  format_choice = formatting(user_choice)
  valid = confirm(valid)
