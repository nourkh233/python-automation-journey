# Simulateur de zones de frequence - Andon LEONI
# # Reproduit en Python la logique du systeme Andon du poste PGTF L481 (stage LEONI)
# # Seuils bases sur le cahier des charges reel : 39/35/32 Hz
def zone_frequence(frequence):
    if frequence >= 39:
        return "BLEU"
    elif frequence >= 35 and frequence < 39:
        return "VERT"
    elif frequence < 35 and frequence >= 32:
        return "ORANGE"
    else:
        return "ROUGE"


if __name__ == "__main__":

    try:
        frequence = float(input("Entrez une frequence entre 0 et 50 : "))

        if frequence < 0 or frequence > 50:
            raise ValueError("frequence hors limites")

        print(f"la couleur afficher est {zone_frequence(frequence)}")

    except ValueError:
        print("Erreur : entrez un nombre compris entre 0 et 50.")
