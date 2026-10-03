import random
from datetime import datetime
from zone_frequence import zone_frequence
import csv


def generer_mesure():
    frequence = random.uniform(25, 42)
    couleur = zone_frequence(frequence)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, frequence, couleur


def enregistrer_mesure(timestamp, frequence, couleur):
    with open("production_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, f"{frequence:.2f}", couleur])


timestamp, frequence, couleur = generer_mesure()
enregistrer_mesure(timestamp, frequence, couleur)


def generer_rapport():
    frequences = []
    rouge_count = 0
    with open("production_log.csv", "r") as file:
        reader = csv.reader(file)
        for ligne in reader:
            frequences.append(float(ligne[1]))
            if ligne[2] == "ROUGE":
                rouge_count += 1

    print(f"Nombre de mesures rouges: {rouge_count}")
    print(f"Nombre total de mesures: {len(frequences)}")
    print(f"Fréquence moyenne: {sum(frequences) / len(frequences):.2f}")
    print(f"Valeur minimale: {min(frequences):.2f}")
    print(f"Valeur maximale: {max(frequences):.2f}")


generer_rapport()
