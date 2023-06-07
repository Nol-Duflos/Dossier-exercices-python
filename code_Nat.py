from math import *
from itertools import permutations


dico = {
    0:(0,0),
    1:(300.8, 202.54),
    2:(5432.6, 676.865),
    3:(65.9, 49.643),
}


"""
Renvoi un tableau contenant toutes les possibilités d'une chaine 
   
Args : 
    dictionnaire : un tableau de chiffres ou de lettres
    nbr : le nombre de chiffres à afficher dans chacuns des résultats

Ex :
    tableau_initial = [1, 2, 3]
    resultat_fonction = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
"""
def calcul_possibilite(dictionnaire, nbr):
    tableau_possibilite = []
    temp = permutations(dictionnaire, nbr)
    for i in list(temp):
        if (i[1] != 0):
            tableau_possibilite.append(i)
            # print(tableau_possibilite)
    return tableau_possibilite


print(calcul_possibilite(dico, 4))