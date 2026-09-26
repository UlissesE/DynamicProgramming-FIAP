# === Helper de verificacao (pode ignorar) ===
# So os DESAFIOS do fim do arquivo usam esta funcao. Ela compara o seu valor
# com a resposta correta (que fica escondida em formato de hash). Voce nao
# precisa entender ela - se voce errou, ela imprime "Valor errado: voce
# colocou X" e o assert logo abaixo dispara.
import hashlib
def verifica(valor, codigo, ordem_importa=False, nome_questao=''):
    if isinstance(valor, tuple):
        valor = list(valor)
    if isinstance(valor, dict):
        valor = sorted(valor.items())
    valores = [valor]
    if isinstance(valor, list):
        valores = [valor if ordem_importa else sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    def _hash(v):
        s = f'{nome_questao}:{v}' if nome_questao else str(v)
        return hashlib.sha224(s.encode('utf-8')).hexdigest()
    respostas = [_hash(v) == codigo for v in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper


# === Helper de dicas (pode ignorar o codigo) ===
# Toda questao teorica dos desafios tem uma explicacao guardada (embaralhada)
# no arquivo explicacao_padaria.py, que vem junto com este. Quando travar numa
# questao, descomente a linha `# explicar('nome')` logo abaixo dela e rode o
# arquivo: a explicacao aparece.
def explicar(questao):
    try:
        from explicacao_padaria import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_padaria.py' nao foi encontrado.")
        print("Esse arquivo vem JUNTO com este exercicio - peca ao")
        print("professor.")
        return
    import codecs
    if questao not in EXPLICACOES:
        print(f"Nao tenho explicacao para '{questao}'.")
        print(f"Questoes disponiveis: {sorted(EXPLICACOES.keys())}")
        return
    print(codecs.decode(EXPLICACOES[questao], 'rot_13'))
    input("aperte enter para continuar")
# fim do helper de dicas


'''
ENUNCIADO

Voce eh dono de uma padaria. Na despensa ha uma quantidade limitada de dois
ingredientes: FARINHA e ACUCAR, medidos em xicaras.

Voce conhece algumas RECEITAS. Cada receita gasta um tanto de farinha e um
tanto de acucar, e da um LUCRO quando o bolo eh vendido:

    pudim:          1 xicara de farinha, 2 de acucar   ->  lucro 4
    broa:           2 xicaras de farinha, 1 de acucar  ->  lucro 5
    bolo de festa:  3 xicaras de farinha, 3 de acucar  ->  lucro 6

Da pra assar QUANTOS BOLOS DE CADA RECEITA QUISER - nao ha limite de quantas
vezes uma receita eh usada. O que acaba eh o ingrediente.

O programa tem este menu:

    1. Ver as receitas
    2. Assar um bolo
    3. Comprar ingredientes
    4. Sair

Regras:

- Uma receita so cabe se houver farinha suficiente E acucar suficiente. As
  duas coisas sao necessarias: sobrar farinha nao compensa faltar acucar.
- Quando nenhuma receita cabe, a lista das que cabem aparece vazia, e o
  maior lucro possivel eh 0.
- Assar um bolo que nao cabe nao acontece: o programa avisa e nao mexe na
  despensa.
- Nome de receita que a padaria nao conhece tambem so rende um aviso.

O menu ja esta pronto la embaixo. O que falta sao as 4 funcoes.

Depois do menu ha dois DESAFIOS opcionais, desligados por padrao.
'''

'''
EXPLICACAO

Cada receita eh um DICIONARIO com quatro campos:

    {'nome': 'pudim', 'farinha': 1, 'acucar': 2, 'lucro': 4}

e as receitas da padaria sao uma LISTA desses dicionarios. Entao ha dois
passos pra chegar num numero: primeiro escolher a receita na lista, depois
escolher o campo dentro dela.

receitas = [
    {'nome': 'pudim',         'farinha': 1, 'acucar': 2, 'lucro': 4},
    {'nome': 'broa',          'farinha': 2, 'acucar': 1, 'lucro': 5},
    {'nome': 'bolo de festa', 'farinha': 3, 'acucar': 3, 'lucro': 6},
]


    >>> receitas[1]
    {'nome': 'broa', 'farinha': 2, 'acucar': 1, 'lucro': 5}
    >>> receitas[1]['lucro']
    5
    >>> receitas[1]['nome']
    'broa'

Pra percorrer as receitas, o `for` corre a LISTA:

    for receita in receitas:
        print(receita['nome'])

e imprime todos os nomes, pois `receita` eh, a cada volta, um dos dicionarios.
'''


receitas = [
    {'nome': 'pudim',         'farinha': 1, 'acucar': 2, 'lucro': 4},
    {'nome': 'broa',          'farinha': 2, 'acucar': 1, 'lucro': 5},
    {'nome': 'bolo de festa', 'farinha': 3, 'acucar': 3, 'lucro': 6},
]

# a despensa do comeco do dia
farinha_inicial = 6
acucar_inicial = 6


breakpoint_aqui = 42

# PARE
# Antes de seguir, vale ver essa lista de dicionarios por dentro.
# Ponha um breakpoint na linha `breakpoint_aqui = 42` acima, rode com
# 'debug python file' e use o debug console:
# digite print(receitas) pra ver tudo de uma vez, e depois compare
# print(receitas[0]) com print(receitas[0]['farinha']) e
# print(receitas[0]['lucro']).
# Digite tambem print(receitas[0].keys()) pra ver os nomes dos campos.
# Depois tente revelar, usando a lista, os valores 3 (o acucar do bolo de
# festa), 5 (o lucro da broa) e 'pudim' (o nome da primeira receita).
# E entao, no olho, sem rodar nada: com 2 xicaras de farinha e 2 de acucar
# na despensa, quais das tres receitas dariam pra assar? E com 1 e 1?
# Se nao conseguir, me chame


'''
EXERCICIO 1

Faca cabe(receita, farinha, acucar), que devolve True se dah pra assar essa
receita com a farinha e o acucar que temos na despensa, e False se nao da.

Sao DUAS condicoes, e as duas precisam valer: tem que ter farinha suficiente
E acucar suficiente. Sobrar farinha nao compensa faltar acucar.

Cuidado com dois numeros que se parecem: `receita['farinha']` eh quanto a
receita GASTA, e `farinha` eh quanto a despensa TEM.

    >>> cabe({'nome': 'pudim', 'farinha': 1, 'acucar': 2, 'lucro': 4}, 6, 6)
    True
    >>> cabe({'nome': 'bolo de festa', 'farinha': 3, 'acucar': 3, 'lucro': 6}, 2, 5)
    False
'''
def cabe(receita, farinha, acucar):
    if receita['farinha'] <= farinha and receita['acucar'] <= acucar: return True
    return False

receitas = [
    {'nome': 'pudim',         'farinha': 1, 'acucar': 2, 'lucro': 4},
    {'nome': 'broa',          'farinha': 2, 'acucar': 1, 'lucro': 5},
    {'nome': 'bolo de festa', 'farinha': 3, 'acucar': 3, 'lucro': 6},
]


pudim = receitas[0]
broa = receitas[1]
festa = receitas[2]

print('  iniciando os testes de cabe')
assert cabe(pudim, 6, 6) == True, f'cabe(pudim, 6, 6): esperado True, voce devolveu {cabe(pudim, 6, 6)}'
assert cabe(pudim, 1, 2) == True, f'cabe(pudim, 1, 2): a despensa da exatamente pra um pudim, esperado True, voce devolveu {cabe(pudim, 1, 2)}'
assert cabe(pudim, 1, 1) == False, f'cabe(pudim, 1, 1): falta acucar, esperado False, voce devolveu {cabe(pudim, 1, 1)}'
assert cabe(pudim, 0, 2) == False, f'cabe(pudim, 0, 2): falta farinha, esperado False, voce devolveu {cabe(pudim, 0, 2)}'
assert cabe(pudim, 2, 1) == False, f'cabe(pudim, 2, 1): sobra farinha mas falta acucar - as DUAS condicoes precisam valer. Esperado False, voce devolveu {cabe(pudim, 2, 1)}'
assert cabe(festa, 6, 2) == False, f'cabe(festa, 6, 2): sobra farinha mas falta acucar, esperado False, voce devolveu {cabe(festa, 6, 2)}'
assert cabe(festa, 3, 3) == True, f'cabe(festa, 3, 3): a despensa da exatamente pra um bolo de festa, esperado True, voce devolveu {cabe(festa, 3, 3)}'
assert cabe(broa, 0, 0) == False, f'cabe(broa, 0, 0): despensa vazia, esperado False, voce devolveu {cabe(broa, 0, 0)}'
print('Exercicio 1 (cabe): OK')


'''
EXERCICIO 2

Faca receitas_que_cabem(receitas, farinha, acucar), que devolve a lista dos
NOMES das receitas que cabem nessa despensa - na mesma ordem em que elas
aparecem na lista de receitas.

Se nenhuma couber, devolva a lista vazia.

    >>> receitas_que_cabem(receitas, 2, 2)
    ['pudim', 'broa']
    >>> receitas_que_cabem(receitas, 1, 1)
    []
'''
def receitas_que_cabem(receitas, farinha, acucar):
    res = []
    for receita in receitas:
        if cabe(receita, farinha, acucar):
            res.append(receita['nome'])
    return res


print('  iniciando os testes de receitas_que_cabem')
assert receitas_que_cabem(receitas, 6, 6) == ['pudim', 'broa', 'bolo de festa'], f'receitas_que_cabem(receitas, 6, 6): esperado as tres, voce devolveu {receitas_que_cabem(receitas, 6, 6)}'
assert receitas_que_cabem(receitas, 3, 3) == ['pudim', 'broa', 'bolo de festa'], f'receitas_que_cabem(receitas, 3, 3): o bolo de festa cabe exatamente, voce devolveu {receitas_que_cabem(receitas, 3, 3)}'
assert receitas_que_cabem(receitas, 2, 2) == ['pudim', 'broa'], f'receitas_que_cabem(receitas, 2, 2): o bolo de festa ja nao cabe, voce devolveu {receitas_que_cabem(receitas, 2, 2)}'
assert receitas_que_cabem(receitas, 1, 2) == ['pudim'], f'receitas_que_cabem(receitas, 1, 2): so o pudim, voce devolveu {receitas_que_cabem(receitas, 1, 2)}'
assert receitas_que_cabem(receitas, 2, 1) == ['broa'], f'receitas_que_cabem(receitas, 2, 1): so a broa - repare que eh o contrario do caso anterior, voce devolveu {receitas_que_cabem(receitas, 2, 1)}'
assert receitas_que_cabem(receitas, 1, 1) == [], f'receitas_que_cabem(receitas, 1, 1): nao cabe nada, esperado [], voce devolveu {receitas_que_cabem(receitas, 1, 1)}'
assert receitas_que_cabem([], 6, 6) == [], f'receitas_que_cabem([], 6, 6): padaria sem receita nenhuma, esperado [], voce devolveu {receitas_que_cabem([], 6, 6)}'
print('Exercicio 2 (receitas_que_cabem): OK')


'''
EXPLICACAO

Agora a pergunta da aula: dada a despensa, qual o MAIOR LUCRO TOTAL possivel?

O chute obvio eh assar sempre a receita de maior lucro que couber. Com 6 e 6
isso da dois bolos de festa: gasta os 6 e os 6, lucro 12. Mas dois pudins e
duas broas gastam esses mesmos 6 e 6 e lucram 8 + 10 = 18.

O caso pequeno que explica o problema eh a despensa (3, 3):

    o bolo de festa cabe INTEIRINHO ali e lucra 6;
    um pudim (1, 2) mais uma broa (2, 1) gastam os mesmos 3 e 3 e lucram 9.

Ou seja: escolher pelo maior lucro nao serve, e escolher pelo maior lucro
por xicara tambem nao (a gente vai testar essas regras simples e ver que nao
funciona nos desafios opcionais depois do menu). 

O que resolve eh resolver passo a passo. Resolver as despensas obvias, 
depois usar essas solucoes pra saber a resposta de despensas maiores.
guardar a resposta de TODAS as despensas menores e montar a resposta da
maior em cima delas.

Essa eh a TABELA:

    tabela[f][a] = o maior lucro possivel com NO MAXIMO f xicaras de
                   farinha e a xicaras de acucar

"No maximo", e nao "exatamente" - sobrar ingrediente eh permitido. E
tabela[0][0] eh 0 porque nao assar nada lucra zero; nao eh "impossivel".

Com as receitas da padaria, e a despensa indo ate 6 de cada, a tabela fica
assim (linha = farinha, coluna = acucar):

            a=0  a=1  a=2  a=3  a=4  a=5  a=6
      f=0     0    0    0    0    0    0    0
      f=1     0    0    4    4    4    4    4
      f=2     0    5    5    5    8    8    8
      f=3     0    5    5    9    9    9   12
      f=4     0    5   10   10   10   13   13
      f=5     0    5   10   10   14   14   14
      f=6     0    5   10   15   15   15   18

Repare no 9 da posicao [3][3] - eh o pudim mais a broa ganhando do bolo de
festa - e no 18 do canto, que eh a resposta do 6x6

Como se descobre o numero de UMA posicao? Escolhendo o ULTIMO bolo assado. 
Teste todas as que cabem: cada uma
rende o lucro dela mais o MAXIMO LUCRO USANDO O QUE SOBRA. Na posicao [3][3]:

    pudim (1, 2, lucro 4):  4 + tabela[3-1][3-2] = 4 + tabela[2][1] = 4 + 5 = 9
    broa  (2, 1, lucro 5):  5 + tabela[3-2][3-1] = 5 + tabela[1][2] = 5 + 4 = 9
    festa (3, 3, lucro 6):  6 + tabela[3-3][3-3] = 6 + tabela[0][0] = 6 + 0 = 6

A maior eh 9. E se NENHUMA receita couber, o maior lucro eh 0 - nao se assa
nada.
'''

'''
EXPLICACAO

A matriz de zeros vem pronta - montar matriz nao eh o assunto de hoje:

def matriz_de_zeros(linhas, colunas):
    tabela = []
    for i in range(linhas):
        tabela.append([0] * colunas)
    return tabela

    >>> matriz_de_zeros(2, 3)
    [[0, 0, 0], [0, 0, 0]]
'''


def matriz_de_zeros(linhas, colunas):
    # nao mexa nessa funcao. Ela ja esta pronta
    # so estou te lembrando como ela eh pra voce poder usar

    tabela = []
    for i in range(linhas):
        tabela.append([0] * colunas)
    return tabela


'''
EXERCICIO 3

Faca calcula_posicao_da_tabela(tabela, receitas, f, a), que recebe uma
tabela com as posicoes MENORES ja preenchidas e devolve o numero que vai na
posicao tabela[f][a]. Ela DEVOLVE esse numero - quem escreve na tabela eh a
proxima funcao.

Para cada receita que CABE em (f, a), a parcela dela eh o lucro dela mais a
posicao que sobra depois de gastar os ingredientes dela. Devolva a MAIOR
parcela - e 0 quando nenhuma receita couber.

Lmebre da checagem do `cabe`: alem de pular a receita que nao serve, eh ela
que impede a conta de gerar um indice negativo.

Os dados do exemplo, pra voce conferir sem rolar pra cima:

    tabela = [[0, 0, 0, 0],
              [0, 0, 4, 4],
              [0, 5, 5, 5],
              [0, 0, 0, 0]]

            a=0  a=1  a=2  a=3
      f=0     0    0    0    0
      f=1     0    0    4    4
      f=2     0    5    5    5
      f=3     0    0    0    0

Com f=3 e a=3 as tres receitas cabem, as parcelas sao 9, 9 e 6, e a resposta
eh 9.

    >>> tab = [[0, 0, 0, 0], [0, 0, 4, 4], [0, 5, 5, 5], [0, 0, 0, 0]]
    >>> calcula_posicao_da_tabela(tab, receitas, 3, 3)
    9
'''

def calcula_posicao_da_tabela(tabela, receitas, f, a):

    maior_lucro = 0
    for receita in receitas:
        farinha_receita = receita['farinha']
        acucar_receita = receita['acucar']

        if cabe(receita, f, a):
        
            lucro_atual = receita['lucro'] + tabela[f - farinha_receita][a - acucar_receita]

            if lucro_atual > maior_lucro:
                maior_lucro = lucro_atual
                
    return maior_lucro
    



# tabela de teste: as linhas 0, 1 e 2 ja preenchidas, o resto ainda em zero
tab = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 4, 4, 4, 4],
    [0, 5, 5, 5, 8, 8, 8],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
receitas = [
    {'nome': 'pudim',         'farinha': 1, 'acucar': 2, 'lucro': 4},
    {'nome': 'broa',          'farinha': 2, 'acucar': 1, 'lucro': 5},
    {'nome': 'bolo de festa', 'farinha': 3, 'acucar': 3, 'lucro': 6},
]
so_um_biscoito = [{'nome': 'biscoito', 'farinha': 1, 'acucar': 1, 'lucro': 100}]

# tabela coerente com so_um_biscoito: cada biscoito gasta (1, 1) e lucra 100,
# entao tabela[f][a] = 100 * min(f, a)
tab_biscoito = [
    [0,   0,   0],
    [0, 100, 100],
    [0, 0, 0],
]

print('  iniciando os testes de calcula_posicao_da_tabela')
assert calcula_posicao_da_tabela(tab, receitas, 0, 0) == 0, f'posicao (0,0): despensa vazia, esperado 0, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 0, 0)}'
assert calcula_posicao_da_tabela(tab, receitas, 1, 1) == 0, f'posicao (1,1): nenhuma receita cabe, esperado 0, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 1, 1)}'
assert calcula_posicao_da_tabela(tab, receitas, 3, 0) == 0, f'posicao (3,0): sem acucar nada cabe, esperado 0, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 3, 0)}'
assert calcula_posicao_da_tabela(tab, receitas, 3, 1) == 5, f'posicao (3,1): so a broa cabe, esperado 5, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 3, 1)}'
assert calcula_posicao_da_tabela(tab, receitas, 2, 4) == 8, f'posicao (2,4): esperado 8, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 2, 4)}'
assert calcula_posicao_da_tabela(tab, receitas, 3, 3) == 9, f'posicao (3,3): as tres cabem e o bolo de festa PERDE, esperado 9, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 3, 3)}'
assert calcula_posicao_da_tabela(tab, receitas, 3, 6) == 12, f'posicao (3,6): esperado 12, voce devolveu {calcula_posicao_da_tabela(tab, receitas, 3, 6)}'
assert calcula_posicao_da_tabela(tab_biscoito, so_um_biscoito, 2, 2) == 200, f'posicao (2,2) na tabela do biscoito: cabem DOIS biscoitos, esperado 200, voce devolveu {calcula_posicao_da_tabela(tab_biscoito, so_um_biscoito, 2, 2)}'
assert calcula_posicao_da_tabela(tab_biscoito, so_um_biscoito, 1, 2) == 100, f'posicao (1,2) na tabela do biscoito: sobra acucar mas so da um biscoito, esperado 100, voce devolveu {calcula_posicao_da_tabela(tab_biscoito, so_um_biscoito, 1, 2)}'
assert calcula_posicao_da_tabela(tab, [], 6, 6) == 0, f'posicao (6,6) sem receita nenhuma: esperado 0, voce devolveu {calcula_posicao_da_tabela(tab, [], 6, 6)}'
print('Exercicio 3 (calcula_posicao_da_tabela): OK')


'''
EXPLICACAO

Falta montar a tabela inteira, posicao a posicao. Duas coisas delicadas aqui.

A primeira eh o TAMANHO. A linha 0 e a coluna 0 tambem sao posicoes: com 6
xicaras de farinha os indices vao de 0 a 6, que sao SETE linhas. Entao a
matriz eh matriz_de_zeros(farinha + 1, acucar + 1), e os lacos vao ate
range(farinha + 1).

A segunda eh a ORDEM. Vale a pena começar pelas posicoes menores:
Toda receita gasta farinha toda receita gasta acucar. Entao a tabela cheia
de zeros já tem uma linha e uma coluna corretas de graça

0000000
0
0
0
0

E se a gente for preenchendo as posicoes, uma a uma, com f (de farinha)
crescendo e depois de completar uma linha crescer o a de acucar,
a gente sempre consulta só as posicoes que já descobrimos, nunca
usamos um zero 'falso' que só esta na matriz por causa da inicializacaoo.

Se voce percorresse de tras pra frente, ela leria zeros e devolveria numeros
errados, sem estourar erro nenhum. Eh o pior tipo de bug: o programa roda e
fala besteira em vez de dar erro.

A resposta final fica na ULTIMA posicao preenchida, a da despensa cheia.
'''

'''
EXERCICIO 4

Faca maior_lucro(farinha_na_despensa, acucar_na_despensa, receitas), que
devolve o maior lucro possivel com essa despensa: monta a matriz do tamanho
certo com matriz_de_zeros, percorre as posicoes na ordem (f crescendo por
fora, a crescendo por dentro), preenche cada uma chamando a
calcula_posicao_da_tabela, e no fim devolve a posicao da despensa cheia.

Os parametros chamam farinha_na_despensa e acucar_na_despensa porque 
voce provavelmente vai definir outras variaveis relacionadas com acucar
e farinha dentro da funcao

    >>> maior_lucro(6, 6, receitas)
    18
    >>> maior_lucro(3, 3, receitas)
    9
'''
def maior_lucro(farinha_na_despensa, acucar_na_despensa, receitas):
    pass


receitas2 = [
    {'nome': 'sonho',     'farinha': 2, 'acucar': 3, 'lucro': 7},
    {'nome': 'rosquinha', 'farinha': 4, 'acucar': 1, 'lucro': 6},
    {'nome': 'biscoito',  'farinha': 1, 'acucar': 1, 'lucro': 2},
]

print('  iniciando os testes de maior_lucro')
assert maior_lucro(0, 0, receitas) == 0, f'maior_lucro(0, 0): despensa vazia, esperado 0, voce devolveu {maior_lucro(0, 0, receitas)}'
assert maior_lucro(1, 1, receitas) == 0, f'maior_lucro(1, 1): nenhuma receita cabe, esperado 0, voce devolveu {maior_lucro(1, 1, receitas)}'
assert maior_lucro(1, 2, receitas) == 4, f'maior_lucro(1, 2): da exatamente um pudim, esperado 4, voce devolveu {maior_lucro(1, 2, receitas)}'
assert maior_lucro(2, 1, receitas) == 5, f'maior_lucro(2, 1): da exatamente uma broa, esperado 5, voce devolveu {maior_lucro(2, 1, receitas)}'
assert maior_lucro(3, 3, receitas) == 9, f'maior_lucro(3, 3): esperado 9 (pudim + broa, e nao o bolo de festa), voce devolveu {maior_lucro(3, 3, receitas)}'
assert maior_lucro(6, 6, receitas) == 18, f'maior_lucro(6, 6): esperado 18, voce devolveu {maior_lucro(6, 6, receitas)}'
assert maior_lucro(3, 6, receitas) == 12, f'maior_lucro(3, 6): tres pudins, esperado 12, voce devolveu {maior_lucro(3, 6, receitas)}'
assert maior_lucro(6, 3, receitas) == 15, f'maior_lucro(6, 3): tres broas, esperado 15 - e repare que nao eh o mesmo numero do caso anterior: trocar farinha com acucar muda a resposta. Voce devolveu {maior_lucro(6, 3, receitas)}'
assert maior_lucro(5, 5, receitas2) == 11, f'maior_lucro(5, 5, receitas2): esperado 11, voce devolveu {maior_lucro(5, 5, receitas2)}'
assert maior_lucro(9, 7, receitas2) == 20, f'maior_lucro(9, 7, receitas2): esperado 20, voce devolveu {maior_lucro(9, 7, receitas2)}'
assert maior_lucro(9, 6, so_um_biscoito) == 600, f'maior_lucro(9, 6, so_um_biscoito): seis biscoitos - acaba o acucar antes da farinha. Esperado 600, voce devolveu {maior_lucro(9, 6, so_um_biscoito)}'
assert maior_lucro(6, 6, []) == 0, f'maior_lucro(6, 6, []): padaria sem receita nenhuma, esperado 0, voce devolveu {maior_lucro(6, 6, [])}'
print('Exercicio 4 (maior_lucro): OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== O MENU (ja esta pronto - nao precisa mexer) =====

def main():
    farinha = farinha_inicial
    acucar = acucar_inicial

    while True:
        # tudo que eh derivado eh recalculado aqui dentro, a cada volta -
        # assim assar e comprar mudam os numeros na tela
        cabem = receitas_que_cabem(receitas, farinha, acucar)
        lucro = maior_lucro(farinha, acucar, receitas)

        print()
        print('=== PADARIA ===')
        print(f'despensa: {farinha} de farinha, {acucar} de acucar')
        print(f'cabem agora: {cabem}')
        print(f'maior lucro possivel daqui pra frente: {lucro}')
        print('1. Ver as receitas')
        print('2. Assar um bolo')
        print('3. Comprar ingredientes')
        print('4. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            for receita in receitas:
                print(f"  {receita['nome']}: {receita['farinha']} farinha, "
                      f"{receita['acucar']} acucar, lucro {receita['lucro']}")

        elif opcao == '2':
            nome = input('  qual receita? ')
            escolhida = None
            for receita in receitas:
                if receita['nome'] == nome:
                    escolhida = receita
            if escolhida is None:
                print('  nao conheco essa receita')
            elif not cabe(escolhida, farinha, acucar):
                print('  falta ingrediente pra essa - nao assei')
            else:
                farinha = farinha - escolhida['farinha']
                acucar = acucar - escolhida['acucar']
                print(f"  assado! lucro {escolhida['lucro']}")

        elif opcao == '3':
            farinha = farinha + int(input('  quantas xicaras de farinha? '))
            acucar = acucar + int(input('  quantas xicaras de acucar? '))

        elif opcao == '4':
            break

        else:
            print('Opcao invalida')


# Pra rodar a padaria, descomente:
# main()


# ===================================================================
# ===== DESAFIOS (opcionais) - daqui pra frente nada eh obrigatorio
# ===================================================================

'''
EXPLICACAO

Os exercicios da aula acabaram. O que vem agora sao dois desafios que puxam
o mesmo assunto pra outros dois lados:

    DESAFIO 1 - por que os jeitos SIMPLES de escolher nao funcionam
    DESAFIO 2 - como fazer a tabela dizer QUAIS bolos assar

Os asserts dos dois ficam DESLIGADOS por padrao. Para ligar (e ver "OK"
conforme acerta), mude a flag `desafio` abaixo de False para True. Se nao
quiser fazer, deixe False e o arquivo continua terminando no PARABENS.
'''


desafio = False    # ligue os desafios mudando para True


# ===== DESAFIO 1 - estrategias simples que nao funcionam =====

'''
EXPLICACAO

Ao longo da aula voce leu que escolher "no chute" nao serve. Acreditar nisso
eh facil; SENTIR eh outra coisa - e pra sentir voce precisa fazer as contas
do chute com a propria mao e ver o numero ficar menor.

Entao aqui vai uma despensa NOVA, com as mesmas tres receitas:

    DESPENSA: 10 xicaras de farinha, 8 de acucar

    pudim:          1 farinha, 2 acucar   ->  lucro 4
    broa:           2 farinha, 1 acucar   ->  lucro 5
    bolo de festa:  3 farinha, 3 acucar   ->  lucro 6

E duas estrategias simples, das que qualquer um tentaria primeiro:

    ESTRATEGIA A - asse sempre a receita de MAIOR LUCRO que couber.
    ESTRATEGIA B - asse sempre a receita de maior LUCRO POR XICARA GASTA
                   (o lucro dividido pelo total de xicaras que ela gasta,
                   considerando iguais as xicara de farinha e as de acucar).

As duas funcionam do mesmo jeito: escolha, asse, desconte da despensa,
repita - ate nao caber mais nada. Depois some os lucros.

Faca as contas no papel. Sao quatro ou cinco fornadas em cada uma.
'''

'''
EXERCICIO

ESTRATEGIA A, na despensa de 10 farinha e 8 acucar.

Asse sempre a receita de MAIOR LUCRO que couber, desconte, repita. Quanto a
padaria lucra no total?
'''
lucro_greedy_lucro = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('lucro_greedy_lucro')

'''
EXERCICIO

Antes da estrategia B, a medida que ela usa - aplicada a UMA receita.

O bolo de festa gasta 3 xicaras de farinha e 3 de acucar, e lucra 6. Quanto
eh o lucro POR XICARA GASTA dele?

Faca a conta na mao (eh uma divisao so) - a ideia aqui eh voce ver de onde
sai o numero, nao mandar o Python calcular.
'''
por_xicara_do_bolo_de_festa = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_xicara_do_bolo_de_festa')

'''
EXERCICIO

ESTRATEGIA B, na mesma despensa de 10 farinha e 8 acucar.

Calcule o lucro por xicara das TRES receitas, veja qual eh a maior, e asse
sempre essa enquanto couber - descontando e repetindo, como antes. Quanto a
padaria lucra no total?
'''
lucro_greedy_por_xicara = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('lucro_greedy_por_xicara')

'''
EXERCICIO

E qual eh o lucro de verdade, o maior possivel nessa despensa?

Esse voce nao precisa calcular a mao - voce escreveu a funcao que responde
isso. Responda com a EXPRESSAO Python que devolve o numero.
'''
melhor_lucro_de_verdade = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('melhor_lucro_de_verdade')

'''
EXERCICIO

Multipla escolha. Compare os tres numeros que voce acabou de achar.

Por que a ESTRATEGIA B - que parece a mais esperta das duas, porque olha o
custo e nao so o lucro - mesmo assim fica abaixo do maximo?

    a) porque a receita que ela escolhe nao eh a de maior lucro
    b) porque ela pode usar tudo de um ingrediente e deixar sobrando bastante
       do outro
    c) porque ela assa os bolos numa ordem errada - assando na ordem
       inversa o total mudaria
    d) porque a conta de lucro por xicara deveria dividir so pela farinha
'''
por_que_o_greedy_por_xicara_erra = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_que_o_greedy_por_xicara_erra')

'''
EXERCICIO

Multipla escolha. E o que a TABELA faz que nenhuma das duas estrategias faz?

    a) ela testa todas as combinacoes possiveis de bolos, uma por uma, ate
       achar a melhor
    b) ela sempre escolhe a receita de maior lucro por xicara, so que com
       mais cuidado
    c) ela ordena as receitas da melhor pra pior antes de comecar
    d) ela guarda a resposta de TODA despensa menor, entao a escolha de cada
       bolo ja leva em conta o melhor que da pra fazer com o que sobra
'''
o_que_a_tabela_faz_de_diferente = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_a_tabela_faz_de_diferente')


if desafio:
    assert verifica(lucro_greedy_lucro, 'b51b7c62a8f4d550cce261862c5af0e2e125f04db01403661f684a7c', nome_questao='lucro_greedy_lucro'), 'lucro_greedy_lucro incorreta'
    assert verifica(por_xicara_do_bolo_de_festa, 'ad197aec44044395bd7e99ad7f9ba9016894a925c6b023806edabb3c', nome_questao='por_xicara_do_bolo_de_festa'), 'por_xicara_do_bolo_de_festa incorreta'
    assert verifica(lucro_greedy_por_xicara, 'd45b2a065e3c00cde26f55ea08d6243885e20a09095cbe2237a404ec', nome_questao='lucro_greedy_por_xicara'), 'lucro_greedy_por_xicara incorreta'
    assert verifica(melhor_lucro_de_verdade, 'ecd281dc02333f44bbf28f3241c8b8d7db9066e6b0abd47733a6e9bf', nome_questao='melhor_lucro_de_verdade'), 'melhor_lucro_de_verdade incorreta'
    assert verifica(por_que_o_greedy_por_xicara_erra, 'fd016d68a375f91fb5b2bcdc147c79dc2a1f3eb6705c64577a50ff4b', nome_questao='por_que_o_greedy_por_xicara_erra'), 'por_que_o_greedy_por_xicara_erra incorreta'
    assert verifica(o_que_a_tabela_faz_de_diferente, '8c92d97c808c8b07ff7d57fe5884c13db2ba6be135a7b7adc4ca4310', nome_questao='o_que_a_tabela_faz_de_diferente'), 'o_que_a_tabela_faz_de_diferente incorreta'
    print('Desafio 1: OK')


# ===== DESAFIO 2 - recompor o plano (quais bolos assar) =====

'''
EXPLICACAO

A tabela responde QUANTO: 18 reais, 28 reais. Mas quem esta na padaria as
cinco da manha precisa da outra resposta - QUAIS bolos assar.

O reflexo aqui eh guardar, enquanto preenche, uma segunda matriz com a lista
de bolos de cada posicao. Funciona. Mas nao precisa: a informacao ja esta na
tabela de numeros, e da pra recuperar ela PERGUNTANDO QUEM FECHA A CONTA.

Veja. Esta eh a tabela da despensa (3, 3):

            a=0  a=1  a=2  a=3
      f=0     0    0    0    0
      f=1     0    0    4    4
      f=2     0    5    5    5
      f=3     0    5    5    9

Na posicao (3, 3) esta o 9. Que receita produziu esse 9? Teste as tres:

    pudim (1, 2, lucro 4):  4 + tabela[3-1][3-2] = 4 + tabela[2][1] = 4 + 5 = 9   <- bate
    broa  (2, 1, lucro 5):  5 + tabela[3-2][3-1] = 5 + tabela[1][2] = 5 + 4 = 9   <- bate
    festa (3, 3, lucro 6):  6 + tabela[3-3][3-3] = 6 + tabela[0][0] = 6 + 0 = 6

O pudim bate. Entao um pudim faz parte do plano - e, tirado o pudim, sobra a
despensa (2, 1). Porque nao a broa? Na verdade, podia ser também. A questao é
que *da pra atingir o lucro maximo com o pudim*, nao que essa é a 
*unica maneira de atingir o lucro maximo*

Escolhendo o pudim, podemos repetir: a broa bate (5 + tabela[0][0] = 5), entao vai
uma broa. Sobra (0, 0), onde nada cabe, e acabou.

    plano: pudim, broa   -> 4 + 5 = 9, que eh o numero que estava na tabela.

No final das contas, a nossa tabela continha os dois caminhos
Pudim depois broa e broa depois pudim

Agora, vamos tentar fazer essa 'engenharia reversa'. 
Sao tres funcoes, e a primeira voce ja escreveu quase inteira.
'''

'''
EXERCICIO

Multipla escolha. Com a tabela ja preenchida na mao, como se descobre qual
receita foi usada na posicao (f, a)?

    a) eh sempre a receita de maior lucro que cabe em (f, a)
    b) eh a primeira receita da lista que cabe em (f, a)
    c) eh a receita em que receita['lucro'] mais a posicao que sobra da
       exatamente o numero que esta em tabela[f][a]
    d) nao da pra descobrir depois: eh obrigatorio guardar a escolha numa
       segunda matriz enquanto preenche a primeira
'''
como_se_descobre_a_escolha = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('como_se_descobre_a_escolha')

'''
EXERCICIO

Faca monta_tabela(farinha_na_despensa, acucar_na_despensa, receitas), que
devolve a TABELA INTEIRA preenchida, em vez de so o numero do canto.

Eh a sua maior_lucro com a ultima linha trocada: em vez de devolver
tabela[farinha_na_despensa][acucar_na_despensa], devolve a tabela.

Ela existe pra tabela ser montada UMA vez e depois consultada a vontade -
sem isso, cada pergunta sobre o plano remontaria tudo do zero.

    >>> monta_tabela(2, 2, receitas)
    [[0, 0, 0], [0, 0, 4], [0, 5, 5]]
'''
def monta_tabela(farinha_na_despensa, acucar_na_despensa, receitas):
    pass


'''
EXERCICIO

Faca qual_receita_usar(tabela, receitas, f, a), que devolve o NOME da receita
que produziu o numero que esta em tabela[f][a] - ou None, se nenhuma
produziu (ou seja, se nada cabe ali).

Eh a irma da calcula_posicao_da_tabela: mesmo laco, mesma guarda, mesma
conta. A diferenca eh que, em vez de guardar o maior numero, ela devolve o
nome da receita cuja conta da EXATAMENTE tabela[f][a]. Em caso de empate,
devolve a primeira que bater.

    >>> tab33 = [[0, 0, 0, 0], [0, 0, 4, 4], [0, 5, 5, 5], [0, 5, 5, 9]]
    >>> qual_receita_usar(tab33, receitas, 3, 3)
    'pudim'
    >>> qual_receita_usar(tab33, receitas, 1, 1)
    None
'''
def qual_receita_usar(tabela, receitas, f, a):
    pass


'''
EXERCICIO

Faca plano_do_dia(farinha_na_despensa, acucar_na_despensa, receitas), que
devolve a LISTA DOS NOMES dos bolos a assar.

Monte a tabela UMA vez com monta_tabela. Depois comece na despensa cheia e
va andando: pergunte a qual_receita_usar quem esta ali; se ela devolver um
nome, guarde o nome e desconte os ingredientes DAQUELA receita; se devolver
None, acabou.

A ordem da lista eh a ordem em que voce assou. A conferencia ignora a ordem
(ela compara as duas listas ordenadas), entao nao se preocupe se a sua sair
numa ordem diferente da do exemplo - o que tem que bater eh QUAIS bolos e
QUANTOS de cada.

    >>> plano_do_dia(3, 3, receitas)
    ['pudim', 'broa']
    >>> plano_do_dia(1, 1, receitas)
    []
'''
def plano_do_dia(farinha_na_despensa, acucar_na_despensa, receitas):
    pass


if desafio:
    assert verifica(como_se_descobre_a_escolha, 'a2805c3f3f4b546b5610f2e6dcae9592357d96f48286b099b6a6d141', nome_questao='como_se_descobre_a_escolha'), 'como_se_descobre_a_escolha incorreta'

    print('  iniciando os testes de monta_tabela')
    assert monta_tabela(0, 0, receitas) == [[0]], f'monta_tabela(0, 0): uma despensa vazia ainda eh uma posicao, esperado [[0]], voce devolveu {monta_tabela(0, 0, receitas)}'
    assert monta_tabela(2, 2, receitas) == [[0, 0, 0], [0, 0, 4], [0, 5, 5]], f'monta_tabela(2, 2): voce devolveu {monta_tabela(2, 2, receitas)}'
    assert monta_tabela(3, 3, receitas) == [[0, 0, 0, 0], [0, 0, 4, 4], [0, 5, 5, 5], [0, 5, 5, 9]], f'monta_tabela(3, 3): voce devolveu {monta_tabela(3, 3, receitas)}'
    assert monta_tabela(2, 3, receitas) == [[0, 0, 0, 0], [0, 0, 4, 4], [0, 5, 5, 5]], f'monta_tabela(2, 3): sao 3 linhas de 4 colunas - se voce devolveu 4 linhas de 3, trocou farinha com acucar. Voce devolveu {monta_tabela(2, 3, receitas)}'
    assert monta_tabela(3, 2, receitas) == [[0, 0, 0], [0, 0, 4], [0, 5, 5], [0, 5, 5]], f'monta_tabela(3, 2): sao 4 linhas de 3 colunas. Voce devolveu {monta_tabela(3, 2, receitas)}'
    assert monta_tabela(2, 2, []) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]], f'monta_tabela(2, 2, []): sem receita nenhuma a tabela fica toda zero, voce devolveu {monta_tabela(2, 2, [])}'
    print('Desafio 2, monta_tabela: OK')

    print('  iniciando os testes de qual_receita_usar')
    tabela_6x6 = monta_tabela(6, 6, receitas)
    assert qual_receita_usar(tabela_6x6, receitas, 0, 0) is None, f'qual_receita_usar em (0, 0): nada cabe, esperado None, voce devolveu {qual_receita_usar(tabela_6x6, receitas, 0, 0)}'
    assert qual_receita_usar(tabela_6x6, receitas, 1, 1) is None, f'qual_receita_usar em (1, 1): nada cabe, esperado None, voce devolveu {qual_receita_usar(tabela_6x6, receitas, 1, 1)}'
    assert qual_receita_usar(tabela_6x6, receitas, 1, 2) == 'pudim', f"qual_receita_usar em (1, 2): esperado 'pudim', voce devolveu {qual_receita_usar(tabela_6x6, receitas, 1, 2)}"
    assert qual_receita_usar(tabela_6x6, receitas, 2, 1) == 'broa', f"qual_receita_usar em (2, 1): esperado 'broa', voce devolveu {qual_receita_usar(tabela_6x6, receitas, 2, 1)}"
    assert qual_receita_usar(tabela_6x6, receitas, 4, 4) == 'broa', f"qual_receita_usar em (4, 4): esperado 'broa', voce devolveu {qual_receita_usar(tabela_6x6, receitas, 4, 4)}"
    assert qual_receita_usar(tabela_6x6, receitas, 6, 3) == 'broa', f"qual_receita_usar em (6, 3): esperado 'broa', voce devolveu {qual_receita_usar(tabela_6x6, receitas, 6, 3)}"
    assert qual_receita_usar(tabela_6x6, receitas, 3, 6) == 'pudim', f"qual_receita_usar em (3, 6): esperado 'pudim' - repare que eh o contrario do caso anterior. Voce devolveu {qual_receita_usar(tabela_6x6, receitas, 3, 6)}"
    assert qual_receita_usar(tabela_6x6, receitas, 6, 6) == 'pudim', f"qual_receita_usar em (6, 6): pudim e broa empatam, e a primeira a bater eh o pudim. Voce devolveu {qual_receita_usar(tabela_6x6, receitas, 6, 6)}"
    print('Desafio 2, qual_receita_usar: OK')

    print('  iniciando os testes de plano_do_dia')
    assert sorted(plano_do_dia(0, 0, receitas)) == [], f'plano_do_dia(0, 0): despensa vazia, esperado [], voce devolveu {plano_do_dia(0, 0, receitas)}'
    assert sorted(plano_do_dia(1, 1, receitas)) == [], f'plano_do_dia(1, 1): nada cabe, esperado [], voce devolveu {plano_do_dia(1, 1, receitas)}'
    assert sorted(plano_do_dia(1, 2, receitas)) == sorted(['pudim']), f'plano_do_dia(1, 2): esperado um pudim, voce devolveu {plano_do_dia(1, 2, receitas)}'
    assert sorted(plano_do_dia(3, 3, receitas)) == sorted(['pudim', 'broa']), f'plano_do_dia(3, 3): esperado um pudim e uma broa, voce devolveu {plano_do_dia(3, 3, receitas)}'
    assert sorted(plano_do_dia(4, 4, receitas)) == sorted(['broa', 'broa']), f'plano_do_dia(4, 4): esperado duas broas, voce devolveu {plano_do_dia(4, 4, receitas)}'
    assert sorted(plano_do_dia(6, 3, receitas)) == sorted(['broa', 'broa', 'broa']), f'plano_do_dia(6, 3): esperado tres broas, voce devolveu {plano_do_dia(6, 3, receitas)}'
    assert sorted(plano_do_dia(3, 6, receitas)) == sorted(['pudim', 'pudim', 'pudim']), f'plano_do_dia(3, 6): esperado tres pudins - repare que eh o contrario do caso anterior. Voce devolveu {plano_do_dia(3, 6, receitas)}'
    assert sorted(plano_do_dia(6, 6, receitas)) == sorted(['pudim', 'pudim', 'broa', 'broa']), f'plano_do_dia(6, 6): esperado dois pudins e duas broas - os 18 da aula. Voce devolveu {plano_do_dia(6, 6, receitas)}'
    assert sorted(plano_do_dia(10, 8, receitas)) == sorted(['pudim', 'pudim', 'broa', 'broa', 'broa', 'broa']), f'plano_do_dia(10, 8): dois pudins e quatro broas - eh a sacola que da os 28 do Desafio 1, gastando a despensa exata. Voce devolveu {plano_do_dia(10, 8, receitas)}'
    assert sorted(plano_do_dia(6, 6, [])) == [], f'plano_do_dia(6, 6, []): sem receita nenhuma nao ha plano, esperado [], voce devolveu {plano_do_dia(6, 6, [])}'
    print('Desafio 2, plano_do_dia: OK')

    print('\n=== DESAFIOS COMPLETOS! ===')


'''
EXPLICACAO

Ultima coisa, e essa nao tem assert nenhum.

O `plano_do_dia` devolve a resposta que a padaria de verdade quer, e ela nao
esta aparecendo em lugar nenhum - o menu la de cima mostra QUANTO da pra
lucrar, mas nao diz O QUE assar.

Ponha ela la. Acrescente uma opcao ao menu - algo como "4. Plano do dia" -
que chame plano_do_dia(farinha, acucar, receitas) e imprima a lista. Lembre
de renumerar o "Sair".

Se quiser caprichar: em vez de imprimir ['pudim', 'pudim', 'broa', 'broa'],
imprima "2 pudins, 2 broas". Da pra contar percorrendo a lista e somando num
dicionario - o mesmo tipo de dicionario que as receitas ja sao.
'''
