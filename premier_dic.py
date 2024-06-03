nom = ["Pompe", "Démonte-pneus", "Gourde", "Chambre à air", "Clé de 15", "Multi-tool", "Pince multiprise", "Couteau suisse", "Compresses", "Désinfectant", "Veste de pluie", "Pantalon de pluie", "Crème solaire", "Carte IGN", "Batterie Portable", "Téléphone mobile", "Lampes", "Arrache Manivelle", "Bouchon valve chromé bleu", "Maillon rapide", "Barre de céréales", "Fruits", "Rustines"]
masse = [0.2, 0.1, 1, 0.2, 0.3, 0.2, 0.4, 0.2, 0.1, 0.2, 0.4, 0.4, 0.4, 0.1, 0.5, 0.4, 0.3, 0.4, 0.01, 0.05, 0.4, 0.6, 0.05]
utilite = [1.5, 1.5, 2, 0.5, 1, 1.7, 0.8, 1.5, 0.4, 0.6, 1, 0.75, 1.75, 0.2, 0.4, 2, 1.8, 0, 0.1, 1.4, 0.8, 1.3, 1.5]

dicc = {
    'Pompe': [0.2, 1.5],
    'Démonte-pneus': [0.1, 1.5],
    'Gourde': [1, 2],
    'Chambre à air': [0.2, 0.5],
    'Clé de 15': [0.3, 1],
    'Multi-tool': [0.2, 1.7],
    'Pince multiprise': [0.4, 0.8],
    'Couteau suisse': [0.2, 1.5],
    'Compresses': [0.1, 0.4],
    'Désinfectant': [0.2, 0.6],
    'Veste de pluie': [0.4, 1],
    'Pantalon de pluie': [0.4, 0.75],
    'Crème solaire': [0.4, 1.75],
    'Carte IGN': [0.1, 0.2],
    'Batterie Portable': [0.5, 0.4],
    'Téléphone mobile': [0.4, 2],
    'Lampes': [0.3, 1.8],
    'Arrache Manivelle': [0.4, 0],
    'Bouchon valve chromé bleu': [0.01, 0.1],
    'Maillon rapide': [0.05, 1.4],
    'Barre de céréales': [0.4, 0.8],
    'Fruits': [0.6, 1.3],
    'Rustines': [0.05, 1.5]
}

dic = {}
for i in range(len(nom)):
    dic[nom[i]] = [masse[i], utilite[i]]

print(dic)