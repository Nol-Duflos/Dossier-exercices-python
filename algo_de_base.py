hauteur = int(input("Entre le nombre de lignes : "))

# symbol = '*'
# for i in range(0 , hauteur):
#     print(symbol)
#     symbol = symbol + '*'

# for j in range(hauteur, 0, -1):
#     for i in range(j , 0, -1):
#         print('*', end= '_')
#     print(' ')

nombre_espace = hauteur - 1
nombre_etoile = 1

for i in range(0, hauteur):
    print(nombre_espace * " " + nombre_etoile * "*")
    nombre_espace -= 1
    nombre_etoile += 2