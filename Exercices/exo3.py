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