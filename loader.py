import sys
import time

def simulate_download_loader(duration):
    print("Chiffrement en cours : [", end='', flush=True)

    # Nombre total d'itérations pour le chargement
    total_iterations = 50
    iteration = 0

    # Calcul du temps écoulé à chaque itération
    interval = duration / total_iterations

    while iteration <= total_iterations:
        sys.stdout.write('#')
        sys.stdout.flush()
        time.sleep(interval)
        iteration += 1

    print("] Chiffrement terminé")

