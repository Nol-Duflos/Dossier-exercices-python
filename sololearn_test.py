# glucose_level = int(input("Glucose Level : "))

# if glucose_level <= 70:
#     print("Low glucose level")

# elif glucose_level >= 140:
#     print("High glucose level")

# else:
#     print("Normal range")


# heart_rate = 180
# if heart_rate < 40:
#     print("Low heart rate")
# elif heart_rate >= 180:
#     print("Hight heart rate")
# else:
#     print("Normal range")

# seats = 100
# while seats > 0:
#     print("Sell tickets")
#     seats = seats - 1

# temperature = 40

# if temperature < 35:
#     print("Hypothermia")

# elif temperature > 39:
#     print("Fever")
# else:
#     print("Normal temperature")

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# listSum = sum(myList)
# print(f"Sum of list -> {listSum}")

# text = input("Entrez votre text : ")
# print(text[2])

# str = "Yay! I lernaed about lists"
# print(str[0] + str[8])

# nums = [5, 8, 2]
# nums[1] = 42

# print(nums)

# nums=[10, 9, 8, 7, 6, 5]
# nums[0] = nums[1]-5
# if 4 in nums:
#     print(nums[3])
# else:
#     print(nums[4])

# nums = [4, 7, 3, 1]
# for x in nums:
#     print(x*2)

# str = "testing for loops"
# count = 0

# for x in str:
#     if x == 't':
#         count += 1

# print(count)

# text = "some text"
# for x in text:
#     if x == 'e':
#         break
#     print(x)

# list = [2, 3, 4, 5, 6, 7]
# for x in list:
#     if(x%2==1 and x>4):
#         print(x)
#         break

# list = [11, 2, 7, 31, -5, 12, 13, -3]
# for x in list:
#     print(x)
#     if x <= 0:
#         break

# i = 1
# while (i <= 10):
#     print(i)
#     i = i + 1

# maListe = ["Javascript", "PHP", "Python" ]

# n = len(maListe)
# for i in range(0 , n):
#     print(maListe[i])
#     #Parcours les éléments de ma liste un par un

# maListe = ["Javascript", "PHP", "Python" ]
# maListe.append("Django") #append() ajoute un élément à la fin de la liste

# print(maListe)

# maListe = ["Javascript", "PHP", "Python" ]
# maListe.insert(1, "PyGame") #insert() ajoute un élément à un endroit préci de la liste

# print(maListe)

# maListe = ["Javascript", "PHP", "Python", "C++", "C#", "Pygame" ]
# maListe.remove("PHP")

# print(maListe)

# maListe.pop(1)
# print(maListe)

# maListe = ["Javascript", "PHP", "Python", "C++", "C#", "Pygame" ]
# # # del maListe[2]
# # # del maListe #Supprime entierement ma liste
# maListe.reverse()
# # maListe.clear() #Génère une liste vide
# print(maListe)


# dictAges = {"Samir": 21 , "Najat" : 19 , "Elisa" : 20 , "Ahmed" : 18 , "Robert" : 21}
# dictAges["Najat"] = 20
# dictAges["Alma"] = 19
# dictAges.pop("Robert")
# for valeur in dictAges.values(): #n'affiche que les valerus
#     print(valeur)
# for clefs in dictAges.keys():
#     print(clefs)

# print(dictAges)



# def produit(y, x):
#     return x*y

# print(produit(7, 8))

# import math
# print(math.fabs(-5))

# name = input("Ecrivez votre nom : ")
# print("Bienvenue " + name + " !")

# a = int(input("Entrez un nombre : "))
# b = int(input("Entrez un second nombre : "))
# c = a + b
# d = [a, b]

# print("la somme de a et b est : " + str(c))
# print("le nombre le plus haut est ", max(d))


# e = 1
# for i in range(100):
#     print("Hello", e)
#     e = e +1


# def nombre_entier(nombreUtilisateur):
#     if nombreUtilisateur % 2 == 0:
#         print("Le nombre est pair ! :D")

#     else:
#         print("Le nombre est impair :)")

# nombre_entier(nombreUtilisateur = int(input("Entrez un nombre entier : ")))

# nombre_entier = None
# try:
#     nombre_entier = int(input("Entrez un nombre :  "))
# except ValueError:
#     print("\x1b[31m\x1b[46mJe t'avais dit d'entrer un nombre petit malin >:(\x1b[37m\x1b[0m")

# if nombre_entier != None :
#     if (nombre_entier % 2) == 0:
#         print( str(nombre_entier)+" est pair")
#     else :
#         print( str(nombre_entier)+" est impair")

# x = int(input("Entrez un premier nombre : "))
# y = int(input("Entrez un second nombre : "))
# z = int(input("Entrez un troisième nombre : "))

# d = [x, y, z ]
# print("Le nombre le plus haut est", max(d))

# n = int(input("Entrez un nombre entier : "))

# somme = 0
# for i in range(1, n + 1):
#     somme = somme + i
# print("La somme 1 + 2 +3 + ... +", n, " = : ", somme)

# def getFactors(n):
    # factors = []

    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         factors.append(i)

    # return factors

# n = int(input("Entrez un nombre entier : "))
# print(getFactors(256))


# def get_liste(L, n):
#     somme = []

#     for i in L:
#         somme.append(n * i)

#     return somme

# # L = [3, 9, 5, 18 ]
# # n = 6
# # print(get_liste(L, n)) 

# def nombre_entier(nombreUtilisateur):
#     if nombreUtilisateur % 1 == 0:
#         print("Le nombre est pair ! :D")

#     else:
#         print("Le nombre est impair :)")

# nombre_entier(nombreUtilisateur = int(input("Entrez un nombre entier : ")))

# list = [2, 3, 4, 5, 6, 7]

# for x in list:
#     if(x%2==1 and x>4):
#         print(x)
#         break

# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# sum = 0

# for num in x:
#     sum += num
# print(sum)

# nums = [1, 2, 3, 4]
# res = 0

# for x in nums:
#     if x %2 == 0:
#         continue
#     else:
#         res += x

# print(res)


# numbers = [1, 2, 3]
# total = 0

# for n in numbers:
#     total = total + n

# print(total)

# numbers = list(range(3, 8))
# print(numbers)

# print(range(20) == range(0,20))

# numbers = list(range(5, 20, 2))
# print(numbers)

# nums = list(range(3, 15, 3))
# print(nums[2]) #On print le deuxième output dans la liste donnée en partant de 0

# for i in range(0, 20, 2):
#     print(i)

# a = int(input())
# b = int(input())
# annees = list(range(a, b))
# print(annees)

# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[7:5:-1])

# res = input("Enter a string of words : ")
# liste = list(res[::-1])
# print(liste[0])

# nums = [1, 2, 3, 4, 5, 6]
# res= nums[::-1]
# print(res[2])

# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
# print(sqs[4:7])

# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

# for i in range(10):
#     if not i % 2 == 0:
#         print(i+1)

# x = input()
# print(x[0:3])

# x = [6, 4, 2, 9]
# x = x[::-1]
# print(x[0]+x[2])

N = int(input())
print(sum(range(1,N+1)))
print(sum(range(1, N+1)))