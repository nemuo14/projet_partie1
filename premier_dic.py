import time
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

def calcul_ratio(dic):
    for key in dic:
        dic[key].append(dic[key][1]/dic[key][0]) #a division *23
    return dic

def tri_ratio(dic):
    # elements = list(dic.items()).reverse()
    # print(elements)

    # def get_second_value(item):
    #     return item[1][2]

    # elements.sort(key=get_second_value)

    # dic_trie = {k: v for k, v in elements}
    dic_trie = dict(sorted(dic.items(), key=lambda item: item[1][2], reverse=True)) #sorting dic
    return dic_trie

#

#while totalmass < massmax:
# for i in range(100):
#     rangement_ratio(dic_trie)

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

def rangement_dynamique(dic):
    T=[[0]*]
    for c in range(round(0.6*100)):
        T[0].append(c)
    for i in range(23):
        for c in range(round(0.6 * 100)):
            if c>=








if __name__ == "__main__":

    temps=time.time()

    #for i in range(100):
    dic = calcul_ratio(dic)
    dic_trie = tri_ratio(dic)
    rangement_ratio(dic_trie)

    temps_tot = time.time()-temps
    print(format(temps_tot,".25f"))
    dico_nbr_entiers(dic)
    #bonjour

