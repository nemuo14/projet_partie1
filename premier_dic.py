# nom : [masse, utilite, ratio]
dic = {
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

# calcul ratio masse/utilite
for key in dic:
    dic[key].append(dic[key][1]/dic[key][0])

# tri par ratio
dic = dict(sorted(dic.items(), key=lambda item: item[1][2], reverse=True))

massmax = 0.6
totalmass = 0
sacados = {}
while totalmass < massmax:
    for key in dic:
        if totalmass + dic[key][0] <= massmax:
            sacados[key] = dic[key]
            totalmass += dic[key][0]
            break

for key in sacados:
    print(key, sacados[key])
print('Total masse:', totalmass)