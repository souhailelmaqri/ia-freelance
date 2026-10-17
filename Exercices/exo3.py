import csv

chemin_fichier = "C:\\Users\\souhe\\Desktop\\Projet_Freelance\\Git_projects\\git_practice_2\\ia-freelance\\Donnees\\ventes.csv"

# Lecture du fichier CSV Donnees/ventes.csv avec DictReader

def lire_ventes(chemin_fichier):
    """
    Lit les ventes à partir d'un fichier CSV et retourne une liste de dictionnaires.

    Args:
        chemin_fichier: Chemin vers le fichier CSV.

    Returns:
        Liste de dictionnaires représentant les ventes.
    """
    ventes = []
    with open(chemin_fichier, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            ventes.append(ligne)
    return ventes


ventes = lire_ventes(chemin_fichier)
for vente in ventes:
    print(vente)


# Convertir les valeurs de montant en types appropriés
def convertir_montants(ventes):
    """
    Convertit les valeurs de montant en types appropriés (float).

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Liste de dictionnaires avec les montants convertis.
    """
    for vente in ventes:
        try:
            vente["montant"] = float(vente["montant"])
        except ValueError:
            print("Impossible de convertir le montant.")  # Message d'erreur si la conversion échoue
    return ventes


# Calculer les statistiques de ventes
def calculer_statistiques(ventes):
    """
    Calcule les statistiques de ventes à partir d'une liste de ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Dictionnaire contenant les statistiques de ventes.
    """
    statistiques = {
        "total_ventes": len(ventes),
        "total_montant": sum(vente["montant"] for vente in ventes),
        "moyenne_montant": sum(vente["montant"] for vente in ventes) / len(ventes) if ventes else 0,
        "max_montant": max(vente["montant"] for vente in ventes) if ventes else 0,
        "client_max_montant": max(ventes, key=lambda x: x["montant"])["client"] if ventes else None,
    }
    return statistiques


