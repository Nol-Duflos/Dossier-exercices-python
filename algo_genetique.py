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
EXPECTED_STR = "Something something."

#On déclare ensuite notre chaîne de caractères que le script devra deviner en un minimum de générations
CHANCE_TO_MUTATE = 0.1
GRADED_RETAIN_PERCENT = 0.2
CHANCE_RETAIN_NONGRATED = 0.05
#CHANCE_TO_MUTATE est un pourcentage qui determine la probabilité qu'un individu mute

#On déclare ensuite la taille de la populations et le nombre de génération maximum
POPULATION_COUNT = 100
GENERATION_COUNT_MAX = 100000

#On déclare ensuite un certain nombre de constantes pour le reste du script.

#Le nombre d’individus « hauts gradés » à retenir (GRADED_INDIVIDUAL_RETAIN_COUNT)
GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_COUNT * GRADED_RETAIN_PERCENT)
#La taille de la chaîne de caractères à deviner (LENGTH_OF_EXPECTED_STR).
LENGTH_OF_EXPECTED_STR = len(EXPECTED_STR)
#La moitié de la taille de la chaîne de caractères à deviner (MIDDLE_LENGTH_OF_EXPECTED_STR).
MIDDLE_LENGTH_OF_EXPECTED_STR = LENGTH_OF_EXPECTED_STR // 2
#La liste des caractères autorisés (ALLOWED_CHARMAP).
ALLOWED_CHARMAP = ascii_letters + ' !\'.'
#Et pour finir, la valeur maximum du score qu’un individu peut obtenir (MAXIMUM_FITNESS).
MAXIMUM_FITNESS = LENGTH_OF_EXPECTED_STR


def algo_genetique():
    