# galvanised square steel

# marchandise : [nom, longueur, largeur, hauteur]

# dimensions : [longueur, largeur, hauteur]
dimensions_wagon = [11.583, 2.294, 2.569]

import csv
import tkinter as tk
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=1600, height=750)#création du canvas
canvas.pack()
root.state('zoomed')#plein écran fenêtré


def dessiner_quoi(canvas, x, y, longueur, largeur, couleur="brown", texte=""):
    # dessine un rectangle avec texte (centrée) et couleur
    canvas.create_rectangle(x, y, x + largeur, y + longueur, outline="black", fill=couleur)
    canvas.create_text(x + largeur / 2, y + longueur / 2, text=texte, fill="white")


def read_data_from_csv():
    # renvoie une liste de marchandises avec les données du csv
    data_marchandises = []

    with open("Données marchandises.csv", mode='r', newline='') as csvmarchandises:
        marchandises = csv.reader(csvmarchandises, delimiter=';')
        for row in marchandises:

            if row[0] == 'Numéro ':  # skip la première ligne
                continue
            row.pop(0)  # on enlève le numéro
            row[0] = row[0].replace(' ', '')  # on enlève les espaces
            row[1] = float(row[1].replace(',', '.'))  # on remplace les virgules par des points
            row[2] = float(row[2].replace(',', '.'))
            row[3] = float(row[3].replace(',', '.'))

            data_marchandises.append(row)
    return data_marchandises







"""
      _               _               _ _ 
   __| | ___  ___ ___(_)_ __       __| / |
  / _` |/ _ \/ __/ __| | '_ \     / _` | |
 | (_| |  __/\__ \__ \ | | | |   | (_| | |
  \__,_|\___||___/___/_|_| |_|    \__,_|_|

"""

sm = [24,8] # multiplicateur de taille

wagon_coords = [10,10]
etagere_coords = [0,0]

def dessine_train(train):
    dessine_wagons(train,wagon_coords)

    canvas.create_text(1200, 500, text="nombre de wagons : " + str(len(train)), fill="black")
    root.mainloop()

def dessine_wagons(train,wagon_coords):
    if dimension == 3:
        dessine_train_d3(train)
    for wagon in train:
        wrap_coords(wagon_coords)
        dessiner_quoi(canvas, wagon_coords[0], wagon_coords[1],dimensions_wagon[0]*sm[1], dimensions_wagon[1]*sm[0], "brown")
        
        if dimension == 1:
            marchandise_coords = wagon_coords.copy()
            dessine_marchandises(wagon,marchandise_coords)

        elif dimension == 2:
            etagere_coords = wagon_coords.copy()
            dessine_etageres(wagon,etagere_coords)

        wagon_coords[0] += 100

def dessine_etageres(etageres,etagere_coords):
    for etagere in etageres:
        dessiner_quoi(canvas, etagere_coords[0], etagere_coords[1], dimensions_wagon[0]*sm[1], etagere[0][2]*size_multiplier, "blue")
        
        marchandise_coords = etagere_coords.copy()
        dessine_marchandises(etagere, marchandise_coords)

        etagere_coords[0] += etagere[0][2]*sm[0]

def dessine_marchandises(marchandises,marchandise_coords):
    for marchandise in marchandises:
        dessiner_quoi(canvas, marchandise_coords[0], marchandise_coords[1], marchandise[1]*sm[1], marchandise[2]*sm[0], "green",marchandise[0][:3])
        marchandise_coords[1] += marchandise[1]*sm[1]

def wrap_coords(coords):
    if coords[0] > 1400:
        coords[0] = 10
        coords[1] += 150

"""
      _               _               _ _____
   __| | ___  ___ ___(_)_ __       __| |___ /
  / _` |/ _ \/ __/ __| | '_ \     / _` | |_ \
 | (_| |  __/\__ \__ \ | | | |   | (_| |___) |
  \__,_|\___||___/___/_|_| |_|    \__,_|____/

"""
sm = [24,8] # multiplicateur de taille
# [x, y, extra x]
etagere_coords = [0,0,0]

size_multiplier_y = 8
size_multiplier = 24

def dessine_marchandisesd3(etagere,etagere_coords):
    march_y = 0
    for marchandise in etagere:
        dessiner_quoi(canvas, etagere_coords[0]+5, etagere_coords[1] + march_y,
                      marchandise[1] * size_multiplier_y, marchandise[2] * size_multiplier,
                      "green",marchandise[0][:3])
        march_y += marchandise[1] * size_multiplier_y
    etagere_coords[0] += etagere[0][2] * size_multiplier

def dessine_etageresd3(etage,etage_coords):
    for etagere in etage:

        dessiner_quoi(canvas, etage_coords[0] + 5, etage_coords[1] + 35,
                        dimensions_wagon[0] * sm[1], etagere[0][2] * size_multiplier, "blue")
        
        etagere_coords[1] = etage_coords[1] + 35
        dessine_marchandisesd3(etagere, etagere_coords)
    

def dessine_train_d3(train):
    window_width = 1400
    

    wagon_coords = [10, 10]
    etage_coords = [10, 40]

    wagon_header_y = 10
    etage_header_y = 40

    largetagere = 0

    # train : [ w[ e[ m[nom, long, largeur, hauteur] ] ] ] wagon_coords[0]+dimensions_wagon[0]

    for i in range(len(train)):
        wagon = train[i]
        dessiner_quoi(canvas, wagon_coords[0], wagon_coords[1], 25,
                      dimensions_wagon[1] * len(wagon) * size_multiplier + 5 * (len(wagon) + 1), "purple",
                      "wagon " + str(i + 1))
        dessiner_quoi(canvas, wagon_coords[0], wagon_coords[1] + 30, dimensions_wagon[0] * size_multiplier_y + 40,
                      dimensions_wagon[1] * size_multiplier * len(wagon) + 5 * (len(wagon) + 1), "brown")

        for j in range(len(wagon)):
            etage = wagon[j]
            dessiner_quoi(canvas, etage_coords[0] + 5, etage_coords[1] + 5, 25, dimensions_wagon[1] * size_multiplier,
                          "violet", "etage " + str(j + 1))
            dessiner_quoi(canvas, etage_coords[0] + 5, etage_coords[1] + 35, dimensions_wagon[0] * size_multiplier_y,
                          dimensions_wagon[1] * size_multiplier, "pink")

            etagere_coords[0] = etage_coords[0]

            for etagere in etage:
                dessiner_quoi(canvas, etagere_coords[0] + 5, etage_coords[1] + 35,
                              dimensions_wagon[0] * sm[1], etagere[0][2] * size_multiplier, "blue")
                
                etagere_coords[1] = etage_coords[1] + 35
                dessine_marchandisesd3(etagere, etagere_coords)

            
            etage_coords[0] += dimensions_wagon[1] * size_multiplier + 5

        wagon_coords[0] += dimensions_wagon[1] * size_multiplier * len(wagon) + dimensions_wagon[
            1] * size_multiplier + 5 * (len(wagon) + 1)
        etage_coords[0] = wagon_coords[0]

        if wagon_coords[0] > window_width:
            etage_coords[0] = 10
            wagon_coords[0] = 10
            wagon_coords[1] += 200
            etage_coords[1] += 200
            # wagon_header_y += 200

    canvas.create_text(1200, 500, text="nombre de wagons : " + str(len(train)), fill="black")

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
    # wagon : [[nom, longueur, largeur, hauteur], ...]
    # retourne la longueur disponible dans le wagon (en d1)
    return dimensions_wagon[0] - sum([marchandise[1] for marchandise in wagon])


def chercher_index_place_min(liste_place_dispo):
    # liste_place_dispo : [[index_wagon, place_dispo], ...]
    # retourne l'index du wagon avec le moins de place dispo dans la liste
    # on parcourt toute la liste, si on trouve un meilleur minimum, on le garde et on note son index
    place_min = 1000000
    index_place_min = 0
    for i in range(len(liste_place_dispo)):
        if liste_place_dispo[i][1] < place_min:
            place_min = liste_place_dispo[i][1]
            index_place_min = liste_place_dispo[i][0]
    return index_place_min


def charger_train_d1(data_marchandises, train):
    # data_marchandises (la liste de toutes les marchandises à rentrer): [[nom, longueur, largeur, hauteur], ...]
    # train (la liste des wagons): [[marchandise1, marchandise2, ...], ...]
    # retourne le train avec tous les wagons remplis avec toutes les marchandises
    # on parcourt toutes les marchandises,
    while len(data_marchandises) > 0:
        liste_place_dispo = []
        for i in range(len(train)):
            wagon = train[i]
            if longeur_dispo_wagon(wagon) >= data_marchandises[0][1]:
                liste_place_dispo.append([i, longeur_dispo_wagon(wagon)])

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


def is_trop_long(etagere, marchandise):
    return marchandise[1] > longeur_dispo_etagere(etagere)


def longeur_dispo_etagere(etagere):
    if len(etagere) == 0:
        return dimensions_wagon[0]
    return dimensions_wagon[0] - somme_longueur_etagere(etagere)


def somme_longueur_etagere(etagere):
    if len(etagere) == 0:
        return 0
    return sum([marchandise[1] for marchandise in etagere])


def is_trop_large(etagere, marchandise):
    return largeur_etagere(etagere) < marchandise[2]


def largeur_etagere(etagere):
    return etagere[0][2]


def largeur_utilisee_wagon(wagon):
    return sum([etagere[0][2] for etagere in wagon if etagere])


def charger_train_d2(data_marchandises, train):
    while len(data_marchandises) > 0:
        marchandise = data_marchandises.pop(0)

        placed = False

        for i in range(len(train)):  # parcourir tous les wagons
            wagon = train[i]

            for j in range(len(wagon)):  # parcourir toutes les étagères
                etagere = wagon[j]

                if (not is_trop_long(etagere, marchandise)) and (not is_trop_large(etagere, marchandise)) and (
                not placed):  # si la marchandise rentre dans l'étagère
                    etagere.append(marchandise)  # on la met dans l'étagère
                    placed = True

            # ici on a parcouru toutes les étagères du wagon et on n'a pas trouvé de place pour la marchandise
            if not placed:  # si on n'a pas trouvé de place pour la marchandise dans une des étagères existantes, on va créer une nouvelle étagère
                if largeur_utilisee_wagon(wagon) + marchandise[2] <= dimensions_wagon[
                    1]:  # on vérifie si on peut créer une nouvelle étagère
                    wagon.append([marchandise])
                    placed = True

        # ici on a parcouru tous les wagons et on n'a pas trouvé de place pour une étagère pour la marchandise
        if not placed:
            train.append([[marchandise]])  # on crée un nouveau wagon et on met la marchandise dedans
            placed = True

    return train


"""
                           _ _                                  _ _____
  _ __ ___ _ __ ___  _ __ | (_)___ ___  __ _  __ _  ___      __| |___ /
 | '__/ _ \ '_ ` _ \| '_ \| | / __/ __|/ _` |/ _` |/ _ \    / _` | |_ \
 | | |  __/ | | | | | |_) | | \__ \__ \ (_| | (_| |  __/   | (_| |___) |
 |_|  \___|_| |_| |_| .__/|_|_|___/___/\__,_|\__, |\___|    \__,_|____/

"""


# nouveau formalisme : train : [] de wagons : [] d'étages : [] d'étagères : [] de marchandises : [nom, long, larg, haut]

def is_trop_long(etagere, marchandise):
    return marchandise[1] > longeur_dispo_etagere(etagere)


def longeur_dispo_etagere(etagere):
    if len(etagere) == 0:
        return dimensions_wagon[0]
    return dimensions_wagon[0] - somme_longueur_etagere(etagere)


def somme_longueur_etagere(etagere):
    if len(etagere) == 0:
        return 0
    return sum([marchandise[1] for marchandise in etagere])


def is_trop_large(etagere, marchandise):
    return largeur_etagere(etagere) < marchandise[2]


def largeur_etagere(etagere):
    return etagere[0][2]


def largeur_utilisee_etage(etage):
    return sum([etagere[0][2] for etagere in etage if etagere])


def is_trop_haut(etagere, marchandise):
    return hauteur_etagere(etagere) < marchandise[3]


def hauteur_etagere(etagere):
    return etagere[0][3]


def hauteur_utilisee_wagon(wagon):
    # récupérer la somme des hauteurs des étages.
    # hauteur d'un étage = hauteur du premier objet de l'étagère
    return sum([etage[0][0][3] for etage in wagon if etage])


def charger_train_d3(data_marchandises, train):
    while len(data_marchandises) > 0:
        marchandise = data_marchandises.pop(0)

        placed = False

        for i in range(len(train)):  # parcourir tous les wagons
            wagon = train[i]

            for j in range(len(wagon)):  # parcourir tous les étages
                etage = wagon[j]

                for k in range(len(etage)):  # parcourir toutes les étagères
                    etagere = etage[k]

                    if (not is_trop_long(etagere, marchandise)) and (not is_trop_large(etagere, marchandise)) and (
                    not is_trop_haut(etagere, marchandise)) and (not placed):  # si la marchandise rentre dans l'étagère
                        etagere.append(marchandise)  # on la met dans l'étagère
                        placed = True

                # ici on a parcouru toutes les étagères de l'étage et on n'a pas trouvé de place pour la marchandise
                if not placed:  # si on n'a pas trouvé de place pour la marchandise dans une des étagères existantes, on va créer une nouvelle étagère
                    if largeur_utilisee_etage(etage) + marchandise[2] <= dimensions_wagon[
                        1]:  # on vérifie si on peut créer une nouvelle étagère
                        etage.append([marchandise])
                        placed = True

            # ici on a parcouru tous les étages et on n'a pas trouvé de place pour une étagère pour la marchandise
            if not placed:  # on va créer un nouvel étage
                if hauteur_utilisee_wagon(wagon) + marchandise[3] <= dimensions_wagon[
                    2]:  # on vérifie si on peut créer un nouvel étage
                    wagon.append([[marchandise]])
                    placed = True

        if not placed:
            train.append([[[marchandise]]])  # on crée un nouveau wagon et on met la marchandise dedans
            placed = True

    return train


"""
  _        _             _          _ _     _
 | |_ _ __(_)___      __| | ___    | (_)___| |_ ___
 | __| '__| / __|    / _` |/ _ \   | | / __| __/ _ \
 | |_| |  | \__ \   | (_| |  __/   | | \__ \ ||  __/
  \__|_|  |_|___/    \__,_|\___|   |_|_|___/\__\___|

"""


def tri_d1(data_marchandises): #par longueur
    return sorted(data_marchandises, key=lambda x: x[1], reverse=True)


def tri_d2_largeur(data_marchandises): #par largeur
    return sorted(data_marchandises, key=lambda x: x[2], reverse=True)


def tri_d2(data_marchandises): #par surface
    for i in range(len(data_marchandises)):
        data_marchandises[i].append(data_marchandises[i][1] * data_marchandises[i][2])
    return sorted(data_marchandises, key=lambda x: x[4], reverse=True)

def tri_d2_largeur_longeur(data_marchandises):
    return sorted(data_marchandises, key=lambda x: (x[2],x[1]), reverse=True)




def tri_d3(data_marchandises): #par volume
    for i in range(len(data_marchandises)):
        data_marchandises[i].append(data_marchandises[i][1] * data_marchandises[i][2] * data_marchandises[i][3])
    return sorted(data_marchandises, key=lambda x: x[5],
                  reverse=True)  # attention à combien on utilise de bananes dans la vallée ohoh de dana lalilala

def tri_d3_hauteur(data_marchandises): #par hauteur
    return sorted(data_marchandises, key=lambda x: x[3], reverse=True)

"""
                  _
  _ __ ___   __ _(_)_ __
 | '_ ` _ \ / _` | | '_ \
 | | | | | | (_| | | | | |
 |_| |_| |_|\__,_|_|_| |_|

"""

if __name__ == "__main__":
    dimension = 3

    data_marchandises = read_data_from_csv()
    
    if dimension == 1:
        train = charger_train_d1(data_marchandises, [])
        print(train)
    
    elif dimension == 2:
        train = charger_train_d2(data_marchandises, [])
        print(train)
    
    elif dimension == 3:
        train = charger_train_d3(data_marchandises, [])
        print(train)
    
    dessine_train(train)

    """
    data_marchandises_offline_d1 = tri_d1(data_marchandises)
    data_marchandises_offline_d2_largeur = tri_d2_largeur(data_marchandises)
    data_marchandises_offline_d2 = tri_d2(data_marchandises)
    data_marchandises_offline_d2_largeur_longueur=tri_d2_largeur_longeur(data_marchandises)
    data_marchandises_offline_d3 = tri_d3(data_marchandises)
    data_marchandises_offline_d3_hauteur= tri_d3_hauteur(data_marchandises)
############################################################################################
    train_patrie = [[]]
    vide=[[]]
    temps1 = time.time()
    for i in range(10000000): #pour estimer le temps
        train_patrie = charger_train_d3(data_marchandises_offline_d3_hauteur, vide)
    temps_tot1 = time.time() - temps1
    print(format(temps_tot1,".25f"))


    nb_wagons = 0
    nb_etages = 0
    nb_etageres = 0
    nb_marchandises = 0

    for wagon in train_patrie:
        nb_wagons += 1
        for etage in wagon:
            nb_etages += 1
            for etagere in etage:
                nb_etageres += 1
                for marchandise in etagere:
                    nb_marchandises += 1
    print(train_patrie)
    print("nombre de wagons : " + str(nb_wagons))
    print("nombre d'étages : " + str(nb_etages))
    print("nombre d'étagères : " + str(nb_etageres))
    print("nombre de marchandises : " + str(nb_marchandises))

    print("nombre moyen d'étages par wagon : " + str(nb_etages / nb_wagons))

    # print(train_patrie)
    dessine_train_d3(train_patrie)
#######################################################################
    # train_patrie = [[]]
    # vide=[[]]
    # temps1 = time.time()
    # for i in range(10000000): #pour estimer le temps
    #     train_patrie = charger_train_d1(data_marchandises_offline_d1, vide)
    # temps_tot1 = time.time() - temps1
    # print(format(temps_tot1,".25f"))
    #
    # nb_wagons = 0
    # nb_etages = 0
    # nb_etageres = 0
    # nb_marchandises = 0
    # for wagon in train_patrie:
    #     nb_wagons += 1
    #     for marchandise in wagon:
    #         nb_marchandises += 1
    # print(nb_wagons)
    # print(nb_marchandises)
    # dessine_train_d1(train_patrie)
###############################################################
    # train_patrie = [[]]
    # vide=[[]]
    # temps1 = time.time()
    # for i in range(1000000): #pour estimer le temps
    #     train_patrie = charger_train_d2(data_marchandises, vide)
    # temps_tot1 = time.time() - temps1
    # print(format(temps_tot1,".25f"))
    #
    # nb_wagons = 0
    # nb_etages = 0
    # nb_etageres = 0
    # nb_marchandises = 0
    # for wagon in train_patrie:
    #     nb_wagons += 1
    #     for etagere in wagon:
    #         nb_etageres+=1
    #         for marchandise in etagere:
    #             nb_marchandises += 1
    # print(nb_wagons)
    # print(nb_etageres)
    # print(nb_marchandises)
    # dessine_train_d2(train_patrie)


    """