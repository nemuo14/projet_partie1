import time
import random as rd
# nom : [masse, utilite, ratio]
from random import randint

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

def calcul_ratio(dic):
    for key in dic:
        dic[key].append( (dic[key][1]) / (dic[key][0]) ) #a division *23
    return dic

def tri_ratio(dic):
    dic_trie = dict(sorted(dic.items(), key=lambda item: item[1][2], reverse=True)) #sorting dic
    return dic_trie

def tobin(n):
    return bin(n)[2:]

def select_bin_objects(dic,nbin):
    liste = []
    for i in range(len(nbin)):
        if nbin[i]=='1':
            liste.append(list(dic)[i])
    return liste


# calculs à partir de noms d'objets

def calcul_masse(liste_objets,dic):
    masse=0
    for obj in liste_objets:
        masse+=dic[obj][0]
    return masse

def calcul_utilite(liste_objets,dic):
    utilite=0
    for obj in liste_objets:
        utilite+=dic[obj][1]
    return utilite


"""
        _                      _        _
   __ _| | __ _  ___  ___     | |_ _ __(_)___
  / _` | |/ _` |/ _ \/ __|    | __| '__| / __|
 | (_| | | (_| | (_) \__ \    | |_| |  | \__ \
  \__,_|_|\__, |\___/|___/     \__|_|  |_|___/
          |___/

"""

# approché glouton
def rangement_ratio(dic):
    massmax = 0.6
    totalmass = 0
    totalutilite = 0
    sacados = []
    for key in dic: #*23
        #print(key)
        if totalmass + dic[key][0] <= massmax: #23 add
            totalmass += dic[key][0] #<23 add
            totalutilite += dic[key][1] #<23 add
            sacados.append(key)
    return sacados

# exact
def bruteforce(dic,massmax):
    liste_finale = []
    n = len(dic)
    for i in range(2**n):
        liste_objets = select_bin_objects(dic,tobin(i).zfill(n))
        if calcul_masse(liste_objets,dic) <= massmax+0.0001:# 0.6 + marge d'erreur des floats
            liste_objets.append(calcul_utilite(liste_objets,dic))#on rajoute le total de l'utilité à la fin de la liste
            liste_finale.append(liste_objets)
    return liste_finale

# appoché recherche locale
def recherche_locale(dic,massmax):
    massmissing=massmax
    liste_all = []
    liste_retenue = []
    for k,v in dic.items():
        liste_all.append(k)

    liste_retenue=['Lampes']#rangement_ratio(dic_trie)

    pourcentage_pop = 40

    #print('\n\nliste initiale:',liste_retenue)
    #print("score initial :",calcul_utilite(liste_retenue,dic))
    # print("\ntous les objets :",liste_all)

    for i in range(1000000):
        #si c'est 0 on enlève un élément
        #si c'est 1 on rajoute un élément

        liste_tmp = liste_retenue.copy()

        #pop ou append
        if randint(0,100) < pourcentage_pop and len(liste_tmp) > 0:
            liste_tmp.pop(randint(0,len(liste_tmp)-1))
        else:
            index_all = randint(0,len(liste_all)-1)
            elt = liste_all[index_all]
            if elt not in liste_tmp:
                liste_tmp.append(liste_all[index_all])

        #
        #print(liste_tmp)
        if calcul_masse(liste_tmp,dic) <= massmax + 0.0001:
            #print("\nnouvelle liste :",liste_tmp)
            #print("liste retenue :",liste_retenue)
            utilite_tmp = calcul_utilite(liste_tmp,dic)
            utilite_retenue = calcul_utilite(liste_retenue,dic)
            #print(utilite_tmp," > ",utilite_retenue," ?")
            if utilite_tmp > utilite_retenue:
                liste_retenue = liste_tmp.copy()
                #print('--------------\nnouvelle liste retenue:',liste_retenue)
                #print("score :",calcul_utilite(liste_retenue,dic))

        
    print("\n-----------------\n\nliste finale :",liste_retenue)
    print("score final :",calcul_utilite(liste_retenue,dic))



"""
                  _
  _ __ ___   __ _(_)_ __
 | '_ ` _ \ / _` | | '_ \
 | | | | | | (_| | | | | |
 |_| |_| |_|\__,_|_|_| |_|

"""


if __name__ == "__main__":
    dic = calcul_ratio(dic)
    dic_trie = tri_ratio(dic)

    sac = rangement_ratio(dic_trie)
    print('voici le sac',sac)
    print(calcul_utilite(sac,dic))
    print(calcul_masse(sac,dic))

    temps1 = time.time()
    recherche_locale(dic,0.6)
    temps_tot1 = time.time() - temps1
    print(format(temps_tot1,".25f"))
    # dic_tronc = dict(list(dic_trie.items())[:18])
    #
    #
    # temps1=time.time()
    #
    # #print(max(bruteforce(dic,4),key=lambda x:x[-1]))
    #
    # temps_tot1 = time.time()-temps1
    # print(format(temps_tot1,".25f"))
    #
    #
    # temps2=time.time()
    #
    # print(max(bruteforce(dic_tronc,5),key=lambda x:x[-1]))
    #
    # temps_tot2 = time.time()-temps2
    # print(format(temps_tot2,".25f"))

    # temps1=time.time()
    # print(rangement_ratio(dic))
    #
    # temps_tot1 = time.time()-temps1
    # print(format(temps_tot1,".25f"))

# bruteforce nul :     0.6 =>  7.60 en 51.25s 
#                      2   => 15.05 en 55.28s
#                      3   => 17.85 en 58.59s
#                      4   => 19.95 en 63.48s
#                      5   => 22.00 en 65.83s
#
# bruteforce tronqué : 0.6 =>  7.60 en 1.15s
#                      2   => 15.05 en 2.03s
#                      3   => 17.75 en 2.13s
#                      4   => 19.85 en 2.39s
#                      5   => 21.85 en 2.48s
#
