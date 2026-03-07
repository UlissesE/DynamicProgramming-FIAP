alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_caixa_alta = alfabeto.upper()

def cifragem(letra, k):
    indice = alfabeto.index(letra)
    indice += k
    while indice > len(alfabeto) - 1:
        indice -= len(alfabeto)
    return alfabeto[indice]

def caesarCipher(s, k):
    novaString = ""
    for letra in s:
        if letra in alfabeto:
            novaString += cifragem(letra, k)
        elif letra in alfabeto_caixa_alta:
            letra = letra.lower()
            letraCifrada = cifragem(letra, k)
            letra = letraCifrada.upper()
            novaString += letra
        else:
            novaString += letra
    return novaString