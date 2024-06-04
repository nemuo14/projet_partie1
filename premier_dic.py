import time
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
        dic[key].append(dic[key][1]/dic[key][0]) #a division *23
    return dic

def tri_ratio(dic):
    dic_trie = dict(sorted(dic.items(), key=lambda item: item[1][2], reverse=True)) #sorting dic
    return dic_trie

def rangement_ratio(dic):
    massmax = 0.6
    totalmass = 0
    totalutilite = 0
    sacados = []
    for key in dic: #*23
        print(key)
        if totalmass + dic[key][0] <= massmax: #23 add
            totalmass += dic[key][0] #<23 add
            totalutilite += dic[key][1] #<23 add
            sacados.append(key)

    print('Objets à prendre:', sacados)
    print('Total masse:', totalmass)
    print('Total utilité:', totalutilite)

def dico_nbr_entiers(dic):
    for items in dic.items():
        items[1][0]=round(items[1][0]*100)
        items[1][1]=round(items[1][1]*100)
        print('voici les items', items)
    print(dic)
    return dic

def tobin(n):
    return bin(n)[2:]

def select_bin_objects(dic,nbin):
    liste = []
    for i in range(len(nbin)):
        if nbin[i]=='1':
            liste.append(list(dic)[i])
    return liste

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

def bruteforce(dic,massmax):
    liste_finale = []
    n = len(dic)
    for i in range(2**n):
        liste_objets = select_bin_objects(dic,tobin(i).zfill(n))
        if calcul_masse(liste_objets,dic) <= massmax+0.0001:# 0.6 + marge d'erreur des floats
            liste_objets.append(calcul_utilite(liste_objets,dic))#on rajoute le total de l'utilité à la fin de la liste
            liste_finale.append(liste_objets)
    return liste_finale

def recherche_locale(dic,massmax):
    massmissing=massmax
    liste_all = []
    liste_retenue = []
    for k,v in dic.items():
        liste_obj=[k,v]
        liste_all.append(liste_obj)
    #print(liste_all)
    #print('\n')
    while liste_all!=[]:
        liste_pop=[]
        for i in range(len(liste_all)):
            if liste_all[i][1][0]>=massmissing+0.0001:
                liste_pop.append(i)
        #print(liste_pop)
        for index in range(len(liste_pop)):
            liste_all.pop(liste_pop[index]-index)
            #print(liste_all)
        break

    for i in range(40):
        choix = randint(0,1)
        print(choix)
        #si c'est 0 on enlève un élément
        #si c'est 1 on rajoute un élément

        liste_tmp = liste_retenue.copy()

        if choix==0:
            liste_tmp.pop(randint(0,len(liste_tmp)-1))
        if choix==1:
            liste_tmp.append(liste_all[randint(0,len(liste_all)-1)])
        
        if calcul_masse(liste_tmp,dic) <= massmax + 0.0001:
            if calcul_utilite(liste_tmp,dic) > calcul_utilite(liste_retenue,dic):
                liste_retenue = liste_tmp.copy()
                print('--------------\nnouvelle liste retenue')
                print(liste_retenue)
                print("score :",calcul_utilite(liste_retenue,dic))

        
    print("-----------------\nliste finale :",liste_retenue)
    print("score final :",calcul_utilite(liste_retenue,dic))


"""
        liste_solution_initiale = [liste_all[0]]

        while calcul_utilite(liste_solution_initiale,dic)<calcul_utilite(liste_all,dic):
            pass
"""


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

    recherche_locale(dic,0.6)

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
