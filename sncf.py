# #galvanised square steele
# import csv
# data_marchandises=[]
# all_marchandises=[]
# with open("Données marchandises.csv",mode='r',newline='') as csvmarchandises:
#     marchandises=csv.DictReader(csvmarchandises)
#     for row in marchandises:
#         print(row)
#         data_marchandises.append(dict(row))
#     print(data_marchandises)
#     # for i in range(len(data_marchandises)):
#     #     all_marchandises.append(data_marchandises[i][data_marchandises[i].values()])


import pandas as pd

def excel_to_dict(filename, sheet_name=0):
    # Lire le fichier Excel
    df = pd.read_excel(filename, sheet_name=sheet_name)

    # Initialiser le dictionnaire de résultat
    result_dict = {}

    # Parcourir les lignes du DataFrame et remplir le dictionnaire
    for index, row in df.iterrows():
        # Assurer que les colonnes existent dans le DataFrame
            nom = row['nom']
            dimensions = [row['longueur'], row['largeur'], row['hauteur']]
            result_dict[nom] = dimensions
    return result_dict

# Utilisation
filename = 'Données marchandises.xlsx'
marchandises_dict = excel_to_dict(filename)
print(marchandises_dict)
