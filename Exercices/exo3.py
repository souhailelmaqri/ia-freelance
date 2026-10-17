import csv



chemin_fichier_import = "C:\\Users\\souhe\\Desktop\\Projet_Freelance\\Git_projects\\git_practice_2\\ia-freelance\\Donnees\\ventes.csv"

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


ventes = lire_ventes(chemin_fichier_import)
for vente in ventes:
    print(vente)

# Vérifier les ventes, collecter les erreurs et si une ligne contient une erreur : arreter le programme et afficher les erreurs
def verifier_donnees(ventes):
    erreurs = []

    for numero, vente in enumerate(ventes, start=1):

        # Vérifier le client
        if "client" not in vente:
            erreurs.append(f"Vente {numero} : client manquant")
        elif not isinstance(vente["client"], str):
            erreurs.append(f"Vente {numero} : client non valide")
        elif not vente["client"].strip():
            erreurs.append(f"Vente {numero} : client vide")

        # Vérifier le montant
        if "montant" not in vente:
            erreurs.append(f"Vente {numero} : montant manquant")

        elif (
            not isinstance(vente["montant"], (str, int, float))
        ):
            erreurs.append(f"Vente {numero} : montant non numérique")

        elif vente["montant"] < 0:
            erreurs.append(f"Vente {numero} : montant négatif")

        # Vérifier le statut de paiement
        if "date" not in vente:
            erreurs.append(f"Vente {numero} : date manquante")
        elif not isinstance(vente["date"], str):
            erreurs.append(f"Vente {numero} : date non valide")
    return erreurs


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

# Générer un fichier contenant le rapport des ventes

chemin_fichier_rapport = "C:\\Users\\souhe\\Desktop\\Projet_Freelance\\Git_projects\\git_practice_2\\ia-freelance\\Rapports\\rapport.txt"

def generer_rapport_ventes(ventes, statistiques, chemin_fichier):
    """
    Génère un fichier contenant le rapport des ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.
        statistiques: Dictionnaire contenant les statistiques de ventes.
        chemin_fichier: Chemin vers le fichier de rapport.
    """
    with open(chemin_fichier, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Total ventes", "Total montant", "Moyenne montant", "Max montant", "Client max montant"])
        writer.writerow([
            statistiques["total_ventes"],
            statistiques["total_montant"],
            statistiques["moyenne_montant"],
            statistiques["max_montant"],
            statistiques["client_max_montant"]
        ])




