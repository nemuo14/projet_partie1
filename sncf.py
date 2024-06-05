# galvanised square steel
# nom longueur largeur hauteur
import csv

import tkinter as tk

root = tk.Tk()
root.title("Dessin de plusieurs rectangles")

# Création du canvas
canvas = tk.Canvas(root, width=1600, height=600)
canvas.pack()
root.state('zoomed')

def dessiner_quoi(canvas, x, y, longueur, largeur, couleur="brown", texte=""):
    canvas.create_rectangle(x, y, x + largeur, y + longueur, outline="black", fill=couleur)
    canvas.create_text(x + largeur/2, y + longueur / 2, text=texte, fill="white")


def read_data_from_csv():

    data_marchandises = []
    
    with open("Données marchandises.csv", mode='r', newline='') as csvmarchandises:
        marchandises = csv.reader(csvmarchandises, delimiter=';')
        for row in marchandises:

            if row[0] == 'Numéro ': # skip la première ligne
                continue
            row.pop(0) # on enlève le numéro
            row[0] = row[0].replace(' ', '') # on enlève les espaces
            row[1] = float(row[1].replace(',', '.')) # on remplace les virgules par des points
            row[2] = float(row[2].replace(',', '.'))
            row[3] = float(row[3].replace(',', '.'))

            data_marchandises.append(row)
    return data_marchandises




"""
      _               _
   __| | ___  ___ ___(_)_ __
  / _` |/ _ \/ __/ __| | '_ \
 | (_| |  __/\__ \__ \ | | | |
  \__,_|\___||___/___/_|_| |_|

"""

def dessine_train_d1(train):
    window_width = 1400

    size_multiplier = 12
    small_margin = 3
    wagon_width = 100

    wagon_coords = [10,10]
    march_coords = [10,10]

    for i in range(len(train)):
        wagon = train[i]
        dessiner_quoi(canvas, wagon_coords[0], wagon_coords[1], dimensions_wagon[0]*size_multiplier, wagon_width, "brown")
        for j in range(len(train[i])):
            marchandise = train[i][j]
            dessiner_quoi(canvas, march_coords[0], march_coords[1], marchandise[1]*size_multiplier, wagon_width, "green", marchandise[0])
            march_coords[1] += marchandise[1]*size_multiplier

        march_coords[0] += 110
        march_coords[1] = wagon_coords[1]
        wagon_coords[0] += 110

        if wagon_coords[0] > window_width:
            wagon_coords[0] = 10
            wagon_coords[1] += 150
            march_coords[0] = 10
            march_coords[1] += 150
    
    canvas.create_text(1200,500, text="nombre de wagons : "+str(len(train)), fill="black")

    root.mainloop()



"""
                           _ _                                  _ _
  _ __ ___ _ __ ___  _ __ | (_)___ ___  __ _  __ _  ___      __| / |
 | '__/ _ \ '_ ` _ \| '_ \| | / __/ __|/ _` |/ _` |/ _ \    / _` | |
 | | |  __/ | | | | | |_) | | \__ \__ \ (_| | (_| |  __/   | (_| | |
 |_|  \___|_| |_| |_| .__/|_|_|___/___/\__,_|\__, |\___|    \__,_|_|
                    |_|                      |___/

"""

def longeur_dispo_wagon(wagon):
    #wagon : [[nom, longueur, largeur, hauteur], ...]
    #retourne la longueur disponible dans le wagon (en d1)
    return dimensions_wagon[0] - sum([marchandise[1] for marchandise in wagon])

def chercher_index_place_min(liste_place_dispo):
    #liste_place_dispo : [[index_wagon, place_dispo], ...]
    #retourne l'index du wagon avec le moins de place dispo dans la liste
    #on parcourt toute la liste, si on trouve un meilleur minimum, on le garde et on note son index
    place_min = 1000000
    index_place_min = 0
    for i in range(len(liste_place_dispo)):
        if liste_place_dispo[i][1] < place_min:
            place_min = liste_place_dispo[i][1]
            index_place_min = liste_place_dispo[i][0]
    return index_place_min

def charger_train_d1(data_marchandises, train):
    #data_marchandises (la liste de toutes les marchandises à rentrer): [[nom, longueur, largeur, hauteur], ...]
    #train (la liste des wagons): [[marchandise1, marchandise2, ...], ...]
    #retourne le train avec tous les wagons remplis avec toutes les marchandises
    #on parcourt toutes les marchandises, 
    while len(data_marchandises) > 0:
        liste_place_dispo = []
        for i in range(len(train)):
            wagon = train[i]
            if longeur_dispo_wagon(wagon) >= data_marchandises[0][1]:
                liste_place_dispo.append([i,longeur_dispo_wagon(wagon)])

        index_place_min = chercher_index_place_min(liste_place_dispo)
        
        if len(liste_place_dispo) == 0:
            train.append([data_marchandises.pop(0)])
        else:
            train[index_place_min].append(data_marchandises.pop(0))
    return train


"""
                           _ _                                  _ ____
  _ __ ___ _ __ ___  _ __ | (_)___ ___  __ _  __ _  ___      __| |___ \
 | '__/ _ \ '_ ` _ \| '_ \| | / __/ __|/ _` |/ _` |/ _ \    / _` | __) |
 | | |  __/ | | | | | |_) | | \__ \__ \ (_| | (_| |  __/   | (_| |/ __/
 |_|  \___|_| |_| |_| .__/|_|_|___/___/\__,_|\__, |\___|    \__,_|_____|
                    |_|                      |___/

"""
def surface_dispo_etagere(etagere):
    largeur_etagere=etagere[0][2]


def charger_train_d2(data_marchandises, train):
    while len(data_marchandises) > 0:
        #on pose le premier objet, ce qui crée une étagère
        #on regarde si le deuxieme rentre dans cette étagère, sinon il crée une nouvelle étagère
        #et si plus de place dans le wagon, il en crée un nouveau






"""
  _        _             _          _ _     _
 | |_ _ __(_)___      __| | ___    | (_)___| |_ ___
 | __| '__| / __|    / _` |/ _ \   | | / __| __/ _ \
 | |_| |  | \__ \   | (_| |  __/   | | \__ \ ||  __/
  \__|_|  |_|___/    \__,_|\___|   |_|_|___/\__\___|

"""
def tri_d1(data_marchandises):
    return sorted(data_marchandises, key=lambda x: x[1], reverse=True)


def tri_d2(data_marchandises):
    for i in range(len(data_marchandises)):
        data_marchandises[i].append(data_marchandises[i][1] * data_marchandises[i][2])
    return sorted(data_marchandises, key=lambda x: x[4], reverse=True)


def tri_d3(data_marchandises):
    for i in range(len(data_marchandises)):
        data_marchandises[i].append(data_marchandises[i][1] * data_marchandises[i][2] * data_marchandises[i][3])
    return sorted(data_marchandises, key=lambda x: x[5], reverse=True)#attention à combien on utilise de bananes dans la vallée ohoh de dana lalilala






dimensions_wagon = [11.583, 2.294, 2.569]


"""
data_marchandises_offline_d1 = tri_d1(data_marchandises)
data_marchandises_offline_d2 = tri_d2(data_marchandises)
data_marchandises_offline_d3 = tri_d3(data_marchandises)
"""


if __name__ == "__main__":
    data_marchandises = read_data_from_csv()
    train_patrie = [[]]
    train_patrie = charger_train_d1(data_marchandises, train_patrie)
    dessine_train_d1(train_patrie)
