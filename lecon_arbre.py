# class arbre_binaire:
#     |--> constructeur
#     |--> ajouter un enfant
#     |--> verifier si on est une feuille
#     |--> Trouver la profondeur de l'arbre 
#     |--> parcours_profondeur 
#     |--> parcours_largeur 

#Faire un arbre et trouver sa profondeur maximale et sa largeur maximale

class arbre_binaire:
    def __init__(self,racine = None, sag = None, sad = None):
        self.racine = racine
        self.sag = sag
        self.sad = sad
    def est_vide(self):
        if self.racine is None:
            return True
        else:
            return False
        

class Noeud:
    def __init__(self, valeur, gauche =  None, droite = None) -> None:
        self.valeur = valeur
        self.valeur = gauche
        self.valeur = droite


def taille(arbre_binaire):
    if arbre_binaire.est_vide():
        return 0
    else:
        return 1 + taille(arbre_binaire.sag) + taille(arbre_binaire.sad)
    


def taille(a):
    if a is None:
        return 0
    else:
        taille_gauche = taille(a.gauche)
        taille_droite = taille(a.droite)

        return 1 + taille_gauche + taille_droite

print(Noeud)

a = arbre_binaire()
a.racine = 1
a.sag = arbre_binaire(2)
a.sad = arbre_binaire(3)
a.sag.sag = arbre_binaire(4)
a.sad.sad = arbre_binaire()