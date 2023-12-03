from tqdm import tqdm
import time


def my_task(item):
  # Simulez une tâche quelconque
  time.sleep(0.1)
  if item % 2 == 0:
    return True
  else:
    return False


# Liste d'éléments sur lesquels itérer
items = range(1, 100)

# Initialisation des compteurs
success_count = 0
failure_count = 0

# Utilisation de TQDM pour suivre la progression
with tqdm(total=len(items),desc="Analyse en cours",
    unit="secondes") as pbar:
  for item in items:
    result = my_task(item)
    if result:
      success_count += 1
      pbar.update(1)  # Met à jour la barre de progression si ça réussit
    else:
      failure_count += 1
      pbar.update(1)  # Met à jour la barre de progression si ça réussit


print("Toutes les tâches sont terminées.")
print(f"Nombre de tâches réussies : {success_count}")
print(f"Nombre de tâches échouées : {failure_count}")
