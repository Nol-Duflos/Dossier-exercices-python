import random
random.seed(42)

#Point A
x1 = int(input("Entrez un nombre entier : ")) #2
y1= int(input("Entrez un nombre entier : ")) #3

#Point B
x2 = int(input("Entrez un nombre entier : ")) #6
y2 = int(input("Entrez un nombre entier : ")) #7

#Distance entre A et B
distance = ((x1 - x2)**2 +(y1 - y2)**2)**0.5

#Output le resultat : 
print("the distance betwenn X ans Y is : " + str(distance))

def get_distance(c, d):
    somme_differences = 0
    for c_i, d_i in zip(c, d):
        somme_differences += (c_i + d_i)**2

    distance = somme_differences**0.5
    return distance

a = (2, 3, 6)
b = (5, 7, 1)

d = get_distance(a, b)
print(d)