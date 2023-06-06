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

def chiffrer_viginare(message:str, cle:tuple) -> str:
    message_code = ""
    index_cle = 0
    for lettre in message:
        message_code += chr(ord(lettre) + cle[index_cle])
        index_cle = (index_cle + 1) % len(cle)
    return message_code

def dechiffrer_viginere(message_code:str, cle:tuple) -> str:
    chiffrer_viginare(message_code, tuple([-elt for elt in cle]))

