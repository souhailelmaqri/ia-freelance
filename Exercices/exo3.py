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

        # Vérifier la date du paiement
        if "date" not in vente:
            erreurs.append(f"Vente {numero} : date manquante")
        elif not isinstance(vente["date"], str):
            erreurs.append(f"Vente {numero} : date non valide")
    return erreurs


# Convertir les valeurs de montant en types appropriés lorsque c'est possible (str -> float), sinon affiche une erreur et ne traite pas la ligne
# Utiliser la fonction raise pour l'exception et la fonction enumerate pour afficher le numéro de la ligne
def convertir_montants(ventes):
    """
    Convertit les valeurs de montant en types appropriés (str -> float) lorsque c'est possible.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Nouvelle liste de dictionnaires avec les montants convertis.
    """
    nouvelles_ventes = []
    for numero, vente in enumerate(ventes, start=1):
        try:
            vente["montant"] = float(vente["montant"])
            nouvelles_ventes.append(vente)
        except ValueError:
            print(f"Erreur : Montant non convertible en float pour la vente {numero}. Ligne ignorée.")
    return nouvelles_ventes

# Calculer les statistiques de ventes
def calculer_statistiques(ventes):
    """
    Calcule les statistiques de ventes à partir d'une liste de ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Dictionnaire contenant les statistiques de ventes.
    """
    total_montant = sum(vente["montant"] for vente in ventes)
    statistiques = {
        "total_ventes": len(ventes),
        "total_montant": total_montant,
        "moyenne_montant": total_montant / len(ventes) if ventes else 0,
        "max_montant": max(vente["montant"] for vente in ventes) if ventes else 0,
        "client_max_montant": max(ventes, key=lambda x: x["montant"])["client"] if ventes else None,
    }
    return statistiques

# Générer un fichier TXT contenant le rapport des ventes

chemin_fichier_rapport = "C:\\Users\\souhe\\Desktop\\Projet_Freelance\\Git_projects\\git_practice_2\\ia-freelance\\Rapports\\rapport.txt"

def generer_rapport(ventes, chemin_fichier):
    """
    Génère un fichier TXT contenant le rapport des ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.
        chemin_fichier: Chemin vers le fichier TXT à générer.
    """
    statistiques = calculer_statistiques(ventes)
    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        fichier.write("Rapport des ventes\n")
        fichier.write("==================\n")
        fichier.write(f"Nombre total de ventes : {statistiques['total_ventes']}\n")
        fichier.write(f"Montant total des ventes : {statistiques['total_montant']:.2f}\n")
        fichier.write(f"Montant moyen des ventes : {statistiques['moyenne_montant']:.2f}\n")
        fichier.write(f"Montant maximum des ventes : {statistiques['max_montant']:.2f}\n")
        fichier.write(f"Client avec la vente la plus élevée : {statistiques['client_max_montant']}\n")


