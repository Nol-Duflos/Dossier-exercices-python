def chiffrer_caesar(message:str, cle) -> dict:

    resultat = {}
    for lettre in message:
        if resultat.get(lettre) is not None:
            resultat[lettre] += 1
        else:
            resultat[lettre] = 1
    return resultat

def trouver_max_dico(dico:dict) -> str:

    return max(dico, key=lambda key:dico[key])
