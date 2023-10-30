#Fonction pour afficher l'interface utilisateur
def message():
  print("\033[0;36mBienvenue sur le programme pour extraire les recettes bébés") #Message en cyan
  print("\033[1;33mVoici les différents choix:") #Message en jaune
  print("\033[0;35mAge:\t\t\t\t\033[0;32mRepas:") #Message violet pour Age et vert pour Repas
  print("\033[0;35m0: 9 mois à 12 mois\t\t\033[0;32m10: Sucrée") #Message violet pour Age et vert pour Repas
  print("\033[0;35m1: 12 mois et +\t\t\t\033[0;32m11: Salée") #Message violet pour Age et vert pour Repas
  print("\t\t\t\t\033[0;32m20: Famille")  #Message vert pour Repas
  print("\n") #Saut de ligne
  print("\033[0;31mPOUR CHOISIR, UTILISER LE '-' ENTRE CHAQUE CHOIX.\nMETTRE SOUS LA FORME '0-1-10'.") #Message en rouge pour l'instruction
  print("\033[0;31mCHOISIR SOIT SUCREE, SOIT SALEE. PAS LES 2!!.") #Message en rouge pour l'instruction
  print("\033[0;31mLE CHOIX FAMILLE DOIT ETRE UNIQUE!!.") #Message en rouge pour l'instruction

#Fonction pour permettre à l'utilisateur de faire ses choix
def choices():
  user_choice = input("\033[0;34mQuel est votre choix: ") #Demande à l'utilisateur de choisir
  return user_choice

#Fonction pour séparer les choix utilisateurs i.e:'0-1-11' en une liste i.e:[0,1,11]
def formatting(user_choice):
  if user_choice == "20":
      format_choice = "20"
  else:
    user_choice = user_choice.split("-")  # Sépare les choix en 3 parties
    format_choice = user_choice.sort()
  print("\033[0;34mVous avez choisi: ", format_choice)
  return format_choice

#Fonction pour demander à l'utilisateur de confirmer ses choix
def confirm():
  valid = input("\033[0;33mVoulez vous confirmer votre choix? O pour 'Oui' et N pour 'Non': ")
  print("\n")
  return valid
