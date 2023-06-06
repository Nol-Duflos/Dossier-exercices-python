savings = input()

savings = float(input())

balance = float(savings) * 1.05


message = "savings in one year: " + str(balance)

print(message)


def taille(arbre_binaire):
    if arbre_binaire.est_vide():
        return 0
    else:
        return 1 + taille(arbre_binaire.sag) + taille(arbre_binaire.sad)