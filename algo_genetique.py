#Les algorythmes génétiques

# 1) Créer botre population de base
# 2) On fait évoluer notre population
# 3) on selectionne les meilleurs
# 4) on les croises (les enfants) et on reviens à l'étape 2 de manière itérative

#Beaucoup plus efficaces sur les très gros calculs
# On créer une classe avec une methode pour créer des chemins au hasard
# On créer une méthode pour selectionner les meilleurs
# On créer une methode pour faire les mutations

#On vas commencer notre programme par deux imports de bibliothèques logicielles pour générer des nombres aléatoires;
from random import random
from string import ascii_letters

#On déclare ensuite une fonction en ligne
choix = lambda x: x[int(random() * len(x))]


#On déclare ensuite notre chaîne de caractères que le script devra deviner en un minimum de générations
CHANCE_TO_MUTATE = 0.1
GRADED_RETAIN_NONGRATED = 0.2
CHANCE_RETAIN_NONGRATED = 0.05
#CHANCE_TO_MUTATE est un pourcentage qui determine la probabilité qu'un individu mute

#On déclare ensuite la taille de la populations et le nombre de génération maximum
POPULATION_COUNT = 100
GENERATION_COUNT_MAX = 100000

def algo_genetique():
