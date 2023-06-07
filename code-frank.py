from math import *
from itertools import permutations

# On part du dico
# ça nous donne le nombre de points
# déterminer la liste des distances à calculer

# on va créer une liste qui contient les distances
# à partir de la liste des trajets, pour chaque trajet, on va faire la somme des distances
# cela va nous donner une nouvelle liste et on choisira la plus petite valeur

# Dictionnaire de Nat
dico = {
    0:(0,0),
    1:(300.8, 202.54),
    2:(5432.6, 676.865),
    3:(65.9, 49.643),
}

# print(dico)
point_to_calc = sum(dico)
print(point_to_calc)



x1 = int(input("Entrez un nombre entier : ")) 
y1= int(input("Entrez un nombre entier : ")) 

x2 = int(input("Entrez un nombre entier : ")) 
y2 = int(input("Entrez un nombre entier : ")) 

distance = ((x1 - x2)**2 +(y1 - y2)**2)**0.5

# Output le resultat : 
print("the distance betwenn X ans Y is : " + str(distance))



# Create distances list to calculate
def list_distances(nombre_points:int) ->list:
    """Create distances list to calculate

    Args:
        nombre_points (int): Store the number of points

    Returns:
        list: List of distances
    """
    
    list_distances = [] # Store the list of distances to calculate
    cpt = 2
    tmp = ()
    tmp_inverse = ()
    
    for i in range(1,nombre_points + 1):
        for cpt in range(1,nombre_points):
            if i != cpt: # remove values when the two points are identical
                tmp = (i, cpt)
                tmp_inverse = (cpt,i) # Store the reverse list
                                      # so as not to calculate the same distance twice  
                if not list_distances.count(tmp_inverse):
                    
                    list_distances.append(tmp)
                    print(list_distances)
  
list_distances(4) # For testing


def distance_calc():
    list_distances = []
    for i in range(1, )
