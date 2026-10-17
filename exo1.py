factures = [120, 450, 89, 1200, 340, 780, 55, 230];

# 1. Calculer le montant total des factures
total = sum(factures);
print("Montant total des factures :", total);
# 2. Calculer le montant moyen
moyenne = total / len(factures);
print("Montant moyen des factures :", moyenne);
# 3. Identifier la facture la plus élevée
max_facture = max(factures);
print("Facture la plus élevée :", max_facture);

# 4. Compter les factures supérieures à 300 €
count = len([f for f in factures if f > 300]);
print("Nombre de factures supérieures à 300 € :", count);

# 5. Appliquer une réduction de 10 % aux factures
#    supérieures à 500 €
reduced_factures = [f * 0.9 if f > 500 else f for f in factures];
print("Factures réduites :", reduced_factures);
