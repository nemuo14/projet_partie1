#galvanised square steel
#nom longueur largeur hauteur
import csv
data_marchandises=[]
#all_marchandises=[]
with open("Données marchandises.csv",mode='r',newline='') as csvmarchandises:
    marchandises=csv.reader(csvmarchandises,delimiter=';')
    for row in marchandises:
    
        if row[0] == 'Numéro ':#skip la première ligne
            continue

        row.pop(0)#on enlève le numéro

        row[0] = row[0].replace(' ','')#on enlève les espaces
        
        row[1] = float(row[1].replace(',','.'))#on remplace les virgules par des points
        row[2] = float(row[2].replace(',','.'))
        row[3] = float(row[3].replace(',','.'))

        data_marchandises.append(row)

    print(data_marchandises)

#longeur largeur hauteur
dimensions_wagon = [11.583,2.294,2.569]

train = [[]]

def longeur_dispo_wagon(wagon):
    return dimensions_wagon[0] - sum([marchandise[1] for marchandise in wagon])

while len(data_marchandises) > 0:
    #on parcourt tout le train par wagons.
    #on calcule la place disponible dans chaque wagon et on stocke le résultat dans une liste.
    #on met dans cette liste uniquement les wagons qui ont la place suffisante pour la marchandise.
    #on met ensuite la marchandise dans le wagon qui a le moins de place disponible (min de la liste).
    #si aucun wagon n'a la place suffisante, on rajoute un wagon et on met la marchandise dedans.
    
    liste_place_dispo = []
    for wagon in train:
        print(wagon)
        print(longeur_dispo_wagon(wagon))
    pass
    
