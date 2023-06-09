
def nombre_entier(nombreUtilisateur):
    if nombreUtilisateur % 1 == 0:
        print("Le nombre est pair ! :D")

    else:
        print("Le nombre est impair :)")

nombre_entier(nombreUtilisateur = int(input("Entrez un nombre entier : ")))