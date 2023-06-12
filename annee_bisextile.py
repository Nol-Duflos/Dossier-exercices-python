def calcul_annee(annee_choisie):
    if annee_choisie % 100 == 0 and annee_choisie % 400 == 0:
        print("L'année est bisextile :D")
    
    else:
        print("L'année n'est pas bisextile")

calcul_annee(annee_choisie = int(input("Entrez une année : ")))