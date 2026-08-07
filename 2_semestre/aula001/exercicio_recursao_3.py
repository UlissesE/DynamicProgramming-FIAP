
# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
import hashlib
def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, list):
        valores = [sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    respostas = [hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo for valor in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper

import sys


# === Helper de vogais (pode ignorar) ===
# `eh_vogal(letra)` voce vai usar dentro da sua funcao tira_vogais, na
# Fase 2 (e numa variavel de aquecimento). Retorna True se a letra eh
# uma vogal minuscula.

def eh_vogal(letra):
    return letra in 'aeiou'
# fim do helper


'''
EXPLICACAO

Quarta lista de RECURSAO. Tema: VARIACOES sobre listas e strings.

O padrao continua o mesmo de sempre:

    def funcao(entrada):
        if caso_base(entrada):
            return resposta_imediata
        else:
            resposta_menor = funcao(entrada_menor)
            return combina(entrada, resposta_menor)

- CASO RECURSIVO / TERCEIRIZACAO: chama a propria funcao com uma
  entrada MENOR e combina o resultado com o pedaco que voce tirou.
- CASO BASE: a entrada e pequena o suficiente pra responder na hora,
  sem precisar chamar a funcao de novo.

Quase todas as funcoes daqui sao do tipo "primeiro + resto" que voce
ja conhece. O que MUDA de uma pra outra eh o jeito de COMBINAR o
primeiro com o resto terceirizado:

    - tira_vogais:   MANTEM ou DESCARTA o primeiro, conforme uma condicao
    - eh_ordenada:   combina com `and` — compara o primeiro com o vizinho
    - intercala:     NOVIDADE — encolhe DUAS listas ao mesmo tempo
    - inverte_lista: joga o primeiro pro FIM

'''


# ===== FASE 1 - inverte_lista(lista) =====

'''
EXPLICACAO

`inverte_lista(lista)` retorna uma NOVA lista com os elementos na
ordem inversa. Eh o paralelo, para listas, do `inverte` de string da
Lista 1.

    inverte_lista([1, 2, 3])
        = inverte_lista([2, 3]) + [1]
        (escondi os passos terceirizados aqui)
        = [3,2] + [1]
        = [3,2,1]

A ideia: pega o primeiro elemento, inverte o RESTO (terceirize!), e
junta o primeiro no FIM.

Caso base: `[]` (lista vazia) — e tambem lista de 1 elemento — ja
estao "invertidas" (sao iguais a si mesmas).
Terceirizacao: inverte_lista(lista) = inverte_lista(lista[1:]) + [lista[0]]


'''

lista_para_inverter = [10, 20, 30, 40]

'''
EXERCICIO - variaveis ilustrando o passo recursivo

Vamos ilustrar o passo recursivo com VARIAVEIS, antes de escrever a
funcao. Considere a `lista_para_inverter` = [10, 20, 30, 40] acima.

1) Qual o PRIMEIRO elemento?
   Use uma EXPRESSAO Python: `lista_para_inverter[0]`.
'''
primeiro_elemento = lista_para_inverter[0]

'''
2) Quais sao os DEMAIS elementos (a partir do indice 1)?
   Use `lista_para_inverter[1:]`.
'''
demais_elementos = lista_para_inverter[1:]

'''
3) Agora terceirize: inverta A MAO os DEMAIS elementos (ou seja,
   inverta a lista [20, 30, 40]).
'''
demais_invertidos = [40,30,20]

'''
4) Pra montar a lista toda invertida, junte: os `demais_invertidos`
   PRIMEIRO, e depois o `primeiro_elemento` no fim.

   Use uma EXPRESSAO Python: `demais_invertidos + [primeiro_elemento]`.
   (repare nos colchetes: pra concatenar, o primeiro_elemento precisa
   virar uma lista de um elemento so)
'''
lista_invertida = demais_invertidos + [lista_para_inverter[0]]

assert verifica(primeiro_elemento, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'primeiro_elemento incorreta'
assert verifica(demais_elementos, '4347885d167edadb32ddf1ecb92c798b6ee7026b6e102be1b57e2622'), 'demais_elementos incorreta'
assert verifica(demais_invertidos, '4347885d167edadb32ddf1ecb92c798b6ee7026b6e102be1b57e2622'), 'demais_invertidos incorreta'
assert verifica(lista_invertida, '2cc616ae608702a6c459d706a0c56cc721b1fde96ef83c5a9713229f'), 'lista_invertida incorreta'
print('Exercicio inverte_lista terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `inverte_lista(lista)`. Ela retorna uma
NOVA lista com os elementos na ordem inversa.

DICA: pra comecar, faca funcionar pra `[]` (caso base — a lista vazia
invertida eh ela mesma). Depois implemente a recursao — exatamente o
que voce fez nas variaveis acima:

    inverte_lista(lista) = inverte_lista(lista[1:]) + [lista[0]]

    >>> inverte_lista([])
    []
    >>> inverte_lista([5])
    [5]
    >>> inverte_lista([1, 2, 3])
    [3, 2, 1]
'''
def inverte_lista(lista):
    if len(lista) <= 1:
        return lista

    primeiro_item = [lista[0]]
    resto = inverte_lista(lista[1:])
    
    return resto + primeiro_item

# Bloco 1: casos base.
assert inverte_lista([]) == [], 'inverte_lista([]) deveria ser [] (caso base)'
assert inverte_lista([5]) == [5], 'inverte_lista([5]) deveria ser [5] (caso base)'
print('Exercicio inverte_lista casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert inverte_lista([1, 2]) == [2, 1], 'inverte_lista([1, 2]) deveria ser [2, 1]'
assert inverte_lista([1, 2, 3]) == [3, 2, 1], 'inverte_lista([1, 2, 3]) deveria ser [3, 2, 1]'
assert inverte_lista([1, 1, 2]) == [2, 1, 1], 'inverte_lista com elemento repetido'
assert inverte_lista(['a', 'b', 'c']) == ['c', 'b', 'a'], 'inverte_lista tambem serve pra listas de strings'

sys.setrecursionlimit(50)
try:
    inverte_lista(list(range(100)))
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao inverte_lista e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio inverte_lista caso recursivo: OK')


# ===== FASE 2 - tira_vogais(palavra) =====

'''
EXPLICACAO

`tira_vogais(palavra)` retorna a palavra sem as vogais (a, e, i, o, u).

    tira_vogais('banana') = 'bnn'
    tira_vogais('aeiou')  = ''
    tira_vogais('xyz')    = 'xyz'

Aqui a recursao "filtra": a cada passo, voce decide se o primeiro
caractere ENTRA ou NAO entra no resultado.

    - se o primeiro caractere eh vogal: DESCARTA ele, retorna so o
      resto terceirizado.
    - se NAO eh vogal: MANTEM ele na frente do resto terceirizado.

Caso base: `''` (string vazia) retorna `''`.
Terceirizacao:
    - se eh_vogal(palavra[0]):  tira_vogais(palavra[1:])
    - senao:                    palavra[0] + tira_vogais(palavra[1:])

Pra ajudar, ja definimos `eh_vogal(letra)` no topo do arquivo
(retorna True se a letra eh vogal).
'''

palavra_para_tirar_vogais = 'banana'

'''
EXERCICIO - variaveis ilustrando o passo recursivo

Considere `palavra_para_tirar_vogais` = 'banana'.

1) Qual a PRIMEIRA letra?
   Pode começar colocando o valor, mas depois use uma EXPRESSAO Python
'''
primeira_letra_tv = 'b'

'''
2) A primeira letra eh vogal? (True/False)
   Pode começar colocando o valor, mas depois use uma EXPRESSAO Python

'''
eh_vogal_a_primeira = eh_vogal(primeira_letra_tv)

'''
3) Quais sao as DEMAIS letras (a partir do indice 1)?
   Use `palavra_para_tirar_vogais[1:]`.
'''
demais_letras_tv = palavra_para_tirar_vogais[1:]

'''
4) Agora terceirize: tire A MAO as vogais das DEMAIS letras (ou seja,
   o resultado de tira_vogais('anana')).
'''
demais_sem_vogais = 'nn'

'''
5) Junte: como a primeira letra ('b') NAO eh vogal, ela ENTRA na
   frente. O resultado eh o `primeira_letra_tv` mais o
   `demais_sem_vogais`.

   Use uma EXPRESSAO Python: `primeira_letra_tv + demais_sem_vogais`.
'''
palavra_sem_vogais = primeira_letra_tv + demais_sem_vogais

assert verifica(primeira_letra_tv, 'c681e18b81edaf2b66dd22376734dba5992e362bc3f91ab225854c17'), 'primeira_letra_tv incorreta'
assert verifica(eh_vogal_a_primeira, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'eh_vogal_a_primeira incorreta'
assert verifica(demais_letras_tv, 'dc04b379e66b8de4b5fe0ee4434825b54509166525143208d3a1e544'), 'demais_letras_tv incorreta'
assert verifica(demais_sem_vogais, '0ad0279bde7d38bf138a522396196d86e375f668f360d8b5525edc54'), 'demais_sem_vogais incorreta'
assert verifica(palavra_sem_vogais, 'b4d0ef625dedb74d87e5a73261b27d725bf9080ed5ef8190e3127365'), 'palavra_sem_vogais incorreta'
print('Exercicio tira_vogais terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `tira_vogais(palavra)`.

DICA: caso base — string vazia retorna `''`. Terceirizacao — olhe
`palavra[0]`:
    - se eh_vogal(palavra[0]): retorna `tira_vogais(palavra[1:])`
      (descarta o primeiro)
    - senao: retorna `palavra[0] + tira_vogais(palavra[1:])`
      (mantem o primeiro)

    >>> tira_vogais('')
    ''
    >>> tira_vogais('banana')
    'bnn'
    >>> tira_vogais('aeiou')
    ''
'''
def tira_vogais(palavra):
    if palavra == '':
        return palavra

    letra = palavra[0]
    resto = palavra[1:]
    limpo = tira_vogais(resto)

    if eh_vogal(letra):
        return limpo

    return palavra[0] + limpo

# Bloco 1: casos base.
assert tira_vogais('') == '', "tira_vogais('') deveria ser '' (caso base)"
assert tira_vogais('a') == '', "tira_vogais('a') deveria ser '' (so uma vogal)"
assert tira_vogais('b') == 'b', "tira_vogais('b') deveria ser 'b' (so uma consoante)"
print('Exercicio tira_vogais casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert tira_vogais('banana') == 'bnn', "tira_vogais('banana') deveria ser 'bnn'"
assert tira_vogais('aeiou') == '', "tira_vogais('aeiou') deveria ser '' (filtra tudo)"
assert tira_vogais('xyz') == 'xyz', "tira_vogais('xyz') deveria ser 'xyz' (nao filtra nada)"
assert tira_vogais('abacaxi') == 'bcx', "tira_vogais('abacaxi') deveria ser 'bcx'"

sys.setrecursionlimit(50)
try:
    tira_vogais('z' * 100)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao tira_vogais e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio tira_vogais caso recursivo: OK')


# ===== FASE 3 - eh_ordenada(lista) =====

'''
EXPLICACAO

`eh_ordenada(lista)` retorna True se a lista esta em ordem crescente
(mais precisamente: nao-decrescente — elementos iguais lado a lado
estao OK).

    eh_ordenada([1, 2, 3])    = True
    eh_ordenada([1, 1, 2])    = True    (iguais lado a lado valem)
    eh_ordenada([3, 1, 2])    = False
    eh_ordenada([])           = True    (caso base)
    eh_ordenada([5])          = True    (caso base)

A ideia recursiva: a lista esta ordenada se DUAS coisas valem ao
mesmo tempo:
    - o primeiro elemento eh <= o segundo  (o primeiro par esta OK)
    - o RESTO (a partir do segundo) tambem esta ordenado (terceirize!)

Combina-se as duas com `and`.

Caso base: lista com 0 OU 1 elemento eh sempre ordenada (True). Repare
que aqui o caso base pega DOIS tamanhos — e isso eh necessario: pra
fazer a comparacao `lista[0] <= lista[1]` voce precisa de PELO MENOS 2
elementos. Com 1 elemento (ou nenhum) nao ha par a comparar, entao a
resposta eh True direto.

Terceirizacao: eh_ordenada(lista) = lista[0] <= lista[1] and eh_ordenada(lista[1:])
'''

lista_para_ordenada = [3, 7, 5, 10]

'''
EXERCICIO - variaveis ilustrando o passo recursivo

Considere `lista_para_ordenada` = [3, 7, 5, 10]. (Repare: ela NAO esta
ordenada — o 5 vem depois do 7.)

1) Qual o PRIMEIRO elemento? (use `lista_para_ordenada[0]`)
'''
primeiro_ord = lista_para_ordenada[0]

'''
2) Qual o SEGUNDO elemento? (use `lista_para_ordenada[1]`)
'''
segundo_ord = lista_para_ordenada[1]

'''
3) O primeiro eh menor ou igual ao segundo? (True/False)
   Use uma EXPRESSAO Python: `primeiro_ord <= segundo_ord`.
'''
primeiro_menor_igual_segundo = primeiro_ord <= segundo_ord

'''
4) Qual o RESTO (a partir do indice 1)? (use `lista_para_ordenada[1:]`)
   Repare: o resto AINDA inclui o segundo elemento.
'''
demais_ord = lista_para_ordenada[1:]

'''
5) Terceirize: o RESTO [7, 5, 10] esta ordenado? Decida A MAO (True
   ou False). Dica: olhe o 7 e o 5...
'''
demais_estao_ordenados = False

'''
6) Junte: a lista inteira esta ordenada se o primeiro par esta OK E o
   resto tambem esta ordenado.

   Use uma EXPRESSAO Python:
       primeiro_menor_igual_segundo and demais_estao_ordenados

   (repare como um unico `False` la no resto derruba o resultado todo,
   mesmo o primeiro par estando OK)
'''
lista_esta_ordenada = primeiro_menor_igual_segundo and demais_estao_ordenados

assert verifica(primeiro_ord, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'primeiro_ord incorreta'
assert verifica(segundo_ord, '56929c1607626a1edbdaafb9c7f10c247e54fcbb20f1e3260f783011'), 'segundo_ord incorreta'
assert verifica(primeiro_menor_igual_segundo, 'b45899583510159617e22fca2b6f561a09289be12ccb30f6df8d4a11'), 'primeiro_menor_igual_segundo incorreta'
assert verifica(demais_ord, '3586bc5a03789738abc5f59ec7fa54e3e90f5e5b8bd1a815dd81cd8a'), 'demais_ord incorreta'
assert verifica(demais_estao_ordenados, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'demais_estao_ordenados incorreta'
assert verifica(lista_esta_ordenada, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'lista_esta_ordenada incorreta'
print('Exercicio eh_ordenada terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `eh_ordenada(lista)`.

DICA: caso base — lista com 0 ou 1 elemento retorna True (use
`len(lista) <= 1`). Terceirizacao — retorna
`lista[0] <= lista[1] and eh_ordenada(lista[1:])`.

    >>> eh_ordenada([])
    True
    >>> eh_ordenada([5])
    True
    >>> eh_ordenada([1, 2, 3])
    True
    >>> eh_ordenada([3, 1, 2])
    False
'''
def eh_ordenada(lista):
    if len(lista) <= 1: return True
    primeiro = lista[0]
    segundo = lista[1]

    if segundo < primeiro: return False

    resposta = eh_ordenada(lista[1:])
    return resposta

# Bloco 1: casos base.
assert eh_ordenada([]) == True, 'eh_ordenada([]) deveria ser True (caso base)'
assert eh_ordenada([5]) == True, 'eh_ordenada([5]) deveria ser True (caso base)'
print('Exercicio eh_ordenada casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert eh_ordenada([1, 2, 3]) == True, '[1, 2, 3] esta ordenada'
assert eh_ordenada([1, 1, 1]) == True, '[1, 1, 1] esta ordenada (iguais valem, eh <=)'
assert eh_ordenada([1, 2, 2, 3]) == True, '[1, 2, 2, 3] esta ordenada'
assert eh_ordenada([1, 3, 2]) == False, '[1, 3, 2] NAO esta ordenada'
assert eh_ordenada([3, 2, 1]) == False, '[3, 2, 1] NAO esta ordenada'
assert eh_ordenada([1, 2, 3, 2]) == False, '[1, 2, 3, 2] quase passa — falha so no ultimo par'

sys.setrecursionlimit(50)
try:
    eh_ordenada(list(range(100)))
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao eh_ordenada e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio eh_ordenada caso recursivo: OK')


# ===== FASE 4 - intercala(lista_a, lista_b) =====

'''
EXPLICACAO  - NOVIDADE: RECURSAO SOBRE DUAS ENTRADAS

`intercala(lista_a, lista_b)` retorna uma lista que alterna os
elementos das duas, comecando pela lista_a.

    intercala([1, 2, 3], [4, 5, 6]) = [1, 4, 2, 5, 3, 6]

NOVIDADE: ate agora a recursao encolhia UMA entrada. Aqui temos DUAS
listas, e a cada passo tiramos o primeiro de CADA UMA e terceirizamos
os DOIS restos juntos:

    intercala([1, 2, 3], [4, 5, 6])
        = [1, 4] + intercala([2, 3], [5, 6])
        = [1, 4] + [2, 5] + intercala([3], [6])
        = [1, 4] + [2, 5] + [3, 6] + intercala([], [])
        = [1, 4, 2, 5, 3, 6]

Caso base: se uma das listas estiver vazia, nao ha mais o que
alternar — retorna a OUTRA lista inteira.
    intercala([], lista_b) = lista_b
    intercala(lista_a, []) = lista_a
(isso tambem resolve, de brinde, listas de tamanhos diferentes — quando
a menor acaba, o resto da maior eh anexado direto.)

Terceirizacao:
    intercala(a, b) = [a[0], b[0]] + intercala(a[1:], b[1:])
'''

lista_a_para_intercalar = [1, 2, 3]
lista_b_para_intercalar = [10, 20, 30]

'''
EXERCICIO - variaveis ilustrando o passo recursivo

Considere `lista_a_para_intercalar` = [1, 2, 3] e
`lista_b_para_intercalar` = [10, 20, 30].

1) Qual o PRIMEIRO elemento de a? (use `lista_a_para_intercalar[0]`)
'''
primeiro_de_a = 'coloque o valor aqui'

'''
2) Qual o PRIMEIRO elemento de b? (use `lista_b_para_intercalar[0]`)
'''
primeiro_de_b = 'coloque o valor aqui'

'''
3) Qual o RESTO de a (a partir do indice 1)? (use `lista_a_para_intercalar[1:]`)
'''
resto_de_a = 'coloque o valor aqui'

'''
4) Qual o RESTO de b (a partir do indice 1)? (use `lista_b_para_intercalar[1:]`)
'''
resto_de_b = 'coloque o valor aqui'

'''
5) Terceirize: intercale A MAO os dois RESTOS, ou seja, o resultado de
   intercala([2, 3], [20, 30]).
'''
restos_intercalados = 'coloque o valor aqui'

'''
6) Junte: o resultado eh o primeiro de a, o primeiro de b, e depois os
   restos ja intercalados.

   Use uma EXPRESSAO Python:
       [primeiro_de_a, primeiro_de_b] + restos_intercalados
'''
intercalada_total = 'coloque o valor aqui'

assert verifica(primeiro_de_a, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'primeiro_de_a incorreta'
assert verifica(primeiro_de_b, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'primeiro_de_b incorreta'
assert verifica(resto_de_a, '6e203ed3f5165334817e0c19f82f510152817eafabbb2405a4df890f'), 'resto_de_a incorreta'
assert verifica(resto_de_b, '282fb42ba4a0549c78022332f02995c83c3ac81b70492db54682638d'), 'resto_de_b incorreta'
assert verifica(restos_intercalados, 'e4bc5133fcf82a47b77f84bea5e25b0d844295920ef0474d32818ebc'), 'restos_intercalados incorreta'
assert verifica(intercalada_total, 'fe8f240e71e599bddfb49d2b11eaae012e03dbb637cca5e40e454147'), 'intercalada_total incorreta'
print('Exercicio intercala terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `intercala(lista_a, lista_b)`.

DICA: caso base — se `lista_a == []`, retorna `lista_b`; se
`lista_b == []`, retorna `lista_a`. Terceirizacao — retorna
`[lista_a[0], lista_b[0]] + intercala(lista_a[1:], lista_b[1:])`.

    >>> intercala([], [])
    []
    >>> intercala([1, 2, 3], [4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    >>> intercala([1], [7, 8, 9])
    [1, 7, 8, 9]
'''
def intercala(lista_a, lista_b):
    pass

# Bloco 1: casos base.
assert intercala([], []) == [], 'intercala([], []) deveria ser [] (caso base)'
assert intercala([], [1, 2]) == [1, 2], 'intercala([], [1, 2]) deveria ser [1, 2] (caso base)'
assert intercala([1, 2], []) == [1, 2], 'intercala([1, 2], []) deveria ser [1, 2] (caso base)'
print('Exercicio intercala casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert intercala([1], [2]) == [1, 2], 'intercala([1], [2]) deveria ser [1, 2]'
assert intercala([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6], 'intercala de listas do mesmo tamanho'
assert intercala([1, 2, 3], [9]) == [1, 9, 2, 3], 'tamanhos diferentes: lista_b acaba primeiro'
assert intercala([1], [7, 8, 9]) == [1, 7, 8, 9], 'tamanhos diferentes: lista_a acaba primeiro'

sys.setrecursionlimit(50)
try:
    intercala(list(range(100)), list(range(100)))
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao intercala e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio intercala caso recursivo: OK')


print('\n=== PARABENS! Lista 4 completa! ===')
