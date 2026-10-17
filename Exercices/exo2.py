ventes = [
    {"client": "Entreprise A", "montant": 1200, "paye": True},
    {"client": "Entreprise B", "montant": 850, "paye": False},
    {"client": "Entreprise C", "montant": 2100, "paye": True},
    {"client": "Entreprise D", "montant": 450, "paye": False}
]

ventes_test = [
    {"client": "Entreprise A", "montant": 1200, "paye": True},
    {"client": "", "montant": 850, "paye": False},
    {"client": "Entreprise C", "montant": -200, "paye": True},
    {"client": "Entreprise D", "montant": "inconnu", "paye": False},
    {"client": "Entreprise E", "paye": True},
    {"client": "   ", "montant": 500, "paye": "oui"},
    {"client": "Entreprise G", "montant": True, "paye": False}
]

# 0. Prise en compte des erreurs potentielles dans les données de ventes (exemple : montant négatif, client manquant, etc.)
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
            isinstance(vente["montant"], bool) or
            not isinstance(vente["montant"], (int, float))
        ):
            erreurs.append(f"Vente {numero} : montant non numérique")

        elif vente["montant"] < 0:
            erreurs.append(f"Vente {numero} : montant négatif")

        # Vérifier le statut de paiement
        if "paye" not in vente:
            erreurs.append(f"Vente {numero} : statut de paiement manquant")
        elif not isinstance(vente["paye"], bool):
            erreurs.append(f"Vente {numero} : statut de paiement non valide")
    return erreurs


# 1. Calculer le montant total des ventes
def calculer_ca(ventes):
    """
    Calcule le chiffre d'affaires total à partir d'une liste de ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Chiffre d'affaires total.
    """
    return sum(vente["montant"] for vente in ventes)



# 2. Identifier les factures impayées
def factures_impayees(ventes):
    """
    Identifie les factures impayées à partir d'une liste de ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Liste des factures impayées.
    """
    return [vente for vente in ventes if not vente["paye"]]




# 3. Affiche un rapport contenant : le chiffre d'affaires total, le montant encaissé, le montant restant à encaisser, le nombre de factures impayées et le nom client ayant la facture la plus élevée
def rapport_ventes(ventes):
    """
    Génère un rapport des ventes.

    Args:
        ventes: Liste de dictionnaires représentant les ventes.

    Returns:
        Dictionnaire contenant le rapport des ventes.
    """
    
    erreurs = verifier_donnees(ventes)
    if erreurs:
        raise ValueError("\n".join(erreurs))
    
    
    ca_total = calculer_ca(ventes)
    montant_encaisse = sum(vente["montant"] for vente in ventes if vente["paye"])
    montant_restant = ca_total - montant_encaisse
    factures_impayees_list = factures_impayees(ventes)
    nombre_factures_impayees = len(factures_impayees_list)
    facture_plus_elevee = max(ventes, key=lambda x: x["montant"]) if ventes else None
    client_facture_plus_elevee = facture_plus_elevee["client"] if facture_plus_elevee else None

    return {
        "chiffre_affaires_total": ca_total,
        "montant_encaisse": montant_encaisse,
        "montant_restant": montant_restant,
        "nombre_factures_impayees": nombre_factures_impayees,
        "client_facture_plus_elevee": client_facture_plus_elevee
    }


if __name__ == "__main__":
    # Calculer et afficher le chiffre d'affaires total, les factures impayées et le rapport des ventes
    print("Chiffre d'affaires total :", calculer_ca(ventes))
    print("Factures impayées :", factures_impayees(ventes))
    print("Rapport des ventes :", rapport_ventes(ventes))

    for erreur in verifier_donnees(ventes_test):
       print(erreur)


