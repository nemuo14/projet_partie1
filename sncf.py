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

        
        #data_marchandises.append(

        data_marchandises.append(row)

        #data_marchandises.append(dict(row))
    print(data_marchandises)
    # for i in range(len(data_marchandises)):
    #     all_marchandises.append(data_marchandises[i][data_marchandises[i].values()])
