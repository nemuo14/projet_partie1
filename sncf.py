#galvanised square steele
import csv
data_marchandises={}
all_marchandises=[]
with open("Données marchandises.csv",mode='r',newline='') as csvmarchandises:
    marchandises=csv.reader(csvmarchandises,delimiter=';')
    for elements in marchandises:
        data_marchandises.append(

        print(row)

        #data_marchandises.append(dict(row))
    print(data_marchandises)
    # for i in range(len(data_marchandises)):
    #     all_marchandises.append(data_marchandises[i][data_marchandises[i].values()])
