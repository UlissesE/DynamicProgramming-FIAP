# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
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
# As questoes teoricas desta lista tem uma explicacao guardada
# (embaralhada) no arquivo explicacao_robber.py, que vem junto com
# este. Quando travar numa questao, descomente a linha
# `# explicar('nome')` logo abaixo dela e rode o arquivo: a explicacao
# aparece.
def explicar(questao):
    try:
        from explicacao_robber import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_robber.py' nao foi encontrado.")
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
EXPLICACAO

Voce eh um ladrao e tem uma rua inteira pela frente. Cada casa da rua
tem uma quantia de dinheiro guardada:

    rua = [2, 7, 9, 3, 1]
    #       0  1  2  3  4     <- os indices sao os "enderecos" das casas

A casa 0 tem 2 reais, a casa 1 tem 7, a casa 2 tem 9, e assim por
diante.

Voce quer levar o MAXIMO possivel. O problema eh o alarme: casas
VIZINHAS tem o sistema de seguranca conectado. Se voce assaltar duas
casas vizinhas na mesma noite, a policia eh chamada.

Ou seja: voce escolhe um conjunto de casas para assaltar, e nesse
conjunto nao pode haver duas casas de indices consecutivos.

    assaltar as casas 0 e 2  ->  pode (0 e 2 nao sao vizinhas)
    assaltar as casas 0 e 1  ->  ALARME (sao vizinhas)
    assaltar as casas 1 e 4  ->  pode

Para rua = [2, 7, 9, 3, 1], a melhor jogada eh assaltar as casas 0, 2
e 4, levando 2 + 9 + 1 = 12 reais.

Repare que a ORDEM em que voce assalta nao importa - o que importa eh
QUAIS casas entram no plano. E repare tambem que pegar a casa mais
cheia nem sempre eh o certo: aqui a casa 2 (com 9) entrou, mas a casa
1 (com 7) teve que ficar de fora justamente porque eh vizinha dela.

Nesta lista voce vai resolver esse problema tres vezes: primeiro com
recursao (que sai quase igual a formula, mas fica lenta), depois com
memoizacao (que salva a recursao), e por fim com uma tabela.
'''


# ===== FASE 1 - Entender o problema =====

'''
EXERCICIO

Uma rua de 4 casas:

    rua = [6, 2, 2, 6]
    #       0  1  2  3

Quatro planos de assalto foram propostos. Qual eh o MELHOR plano? Lembre-se de
NAO disparar o alarme?

    a) assaltar as casas 0 e 1
    b) assaltar as casas 0 e 3
    c) assaltar as casas 1 e 2
    d) assaltar as casas 0 e 2
'''
melhor_plano = 'b'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('melhor_plano')

assert verifica(melhor_plano, '85b4a657591f79df9d564ff1ecdfabdfd7b89d4637dbec5568e34715', nome_questao='melhor_plano'), 'melhor_plano incorreta'
print('Exercicio melhor_plano: OK')


'''
EXERCICIO

Calculo a mao. Outra rua de 4 casas:

    rua = [5, 1, 1, 5]
    #       0  1  2  3

Olhe casa por casa e teste os planos possiveis (lembre: nao pode pegar
duas vizinhas). Quanto o ladrao consegue levar, no maximo?
'''
roubo_5115 = 10

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('roubo_5115')

assert verifica(roubo_5115, 'bba793672c4fd2178461183df5151ad495976e237a2122e213232eee', nome_questao='roubo_5115'), 'roubo_5115 incorreta'
print('Exercicio roubo_5115: OK')


'''
EXERCICIO

Calculo a mao. Agora uma rua de 5 casas:

    rua = [3, 5, 4, 1, 6]
    #       0  1  2  3  4

Quanto o ladrao consegue levar, no maximo?

Repare que nao funciona sair pegando as casas mais ricas (a estrategia 'greedy')
Ok, você pega a casa com 6 reais, mas depois pega a com 5 e acaba saindo perdendo
'''
roubo_35416 = 13

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('roubo_35416')

assert verifica(roubo_35416, '0450f2528e3c2abdf02f216e4a1c6610792e705e2ea08fb5163a5144', nome_questao='roubo_35416'), 'roubo_35416 incorreta'
print('Exercicio roubo_35416: OK')


# ===== FASE 2 - A recorrencia =====

'''
EXPLICACAO

Enumerar todos os planos a mao funciona com 4 ou 5 casas e mas acaba
ficando lento demais. Precisamos de uma formula.

O truque eh olhar para a PRIMEIRA casa da rua e perceber que so
existem duas decisoes possiveis sobre ela: ou voce assalta essa casa,
ou voce pula essa casa. Nao ha terceira opcao.

Vamos chamar de rouba(casa) a maior quantia que da pra levar
considerando a rua A PARTIR daquela casa (ou seja, esquecendo tudo que
ficou para tras). A resposta do problema todo eh rouba(0).

Entao, para

    rua = [3, 5, 4, 1, 6]
    #       0  1  2  3  4

temos

    rouba(0) = max( rouba(1),  3 + rouba(2) )

ou seja: para atacar a rua a partir da casa 0, eu posso

    PULAR a casa 0 - nao levo nada dela, e por causa disso o melhor 
    que consigo eh o melhor da rua a partir da casa 1, que eh rouba(1);

    ASSALTAR a casa 0 - levo os 3 reais dela, a casa 1 fica proibida
    (eh vizinha), e o melhor que consigo dai em diante eh o melhor da
    rua a partir da casa 2, que eh rouba(2).

Como quero o maximo, fico com o maior dos dois. Em geral, para uma
casa qualquer:

    rouba(casa) = max( rouba(casa + 1),  rua[casa] + rouba(casa + 2) )

O `casa + 2` eh o alarme aparecendo na formula: assaltar a casa da vez
me obriga a saltar por cima da casa seguinte.

E quando a rua acaba? Se casa ja passou da ultima casa (casa >= len(rua)),
nao ha nada para roubar:

    rouba(casa) = 0    quando casa >= len(rua)

Esse eh o caso-base.
'''

'''
EXERCICIO

Calculo a mao, usando a recorrencia.

    rua = [3, 5, 4, 1, 6]
    #       0  1  2  3  4

Alguem ja calculou para voce:

    rouba(1) = 11
    rouba(2) = 10
    rouba(3) = 6
    rouba(4) = 6
    rouba(5) = 0

Aplique a recorrencia e calcule rouba(0).
'''
rouba_a_mao_1 = 13

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('rouba_a_mao_1')

assert verifica(rouba_a_mao_1, '5f0a5bb7ef556340ea5214ac0b2c91be4d8a48228184dc74a8b0c327', nome_questao='rouba_a_mao_1'), 'rouba_a_mao_1 incorreta'
print('Exercicio rouba_a_mao_1: OK')


'''
EXERCICIO

Calculo a mao de novo, com outra rua:

    rua = [1, 9, 1, 1]
    #       0  1  2  3

Alguem ja calculou para voce:

    rouba(1) = 10
    rouba(2) = 1
    rouba(3) = 1
    rouba(4) = 0

Aplique a recorrencia e calcule rouba(0).
'''
rouba_a_mao_2 = 10

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('rouba_a_mao_2')

assert verifica(rouba_a_mao_2, '14fb004729858bc5308d3557fa60a895b9a06547bbd31d70ebbeb350', nome_questao='rouba_a_mao_2'), 'rouba_a_mao_2 incorreta'
print('Exercicio rouba_a_mao_2: OK')


'''
EXERCICIO

    rua = [1, 9, 1, 1]
    #       0  1  2  3

Essa rua tem 4 casas, de indice 0 a 3. Quanto vale rouba(7)?
'''
rouba_base = 0

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('rouba_base')

assert verifica(rouba_base, '64557d31170dd9f296471468cec881fc479c577ffed3a1a8f76f01ac', nome_questao='rouba_base'), 'rouba_base incorreta'
print('Exercicio rouba_base: OK')


# ===== FASE 3 - A recursao =====

'''
EXPLICACAO

A recorrencia da Fase 2 vira uma funcao recursiva quase linha a
linha. As tres linhas da formula:

    rouba(casa) = 0                                        se casa >= len(rua)
    rouba(casa) = max( rouba(casa+1),  rua[casa] + rouba(casa+2) )  caso contrario

viram, em Python, um `if` do caso-base e um `return` com o `max`.

A funcao recebe `rua` (a rua inteira, que nunca muda) e `casa` (de qual
casa em diante estamos olhando, que eh o que muda a cada chamada).
'''

'''
EXERCICIO

Faca uma funcao rouba(rua, casa) RECURSIVA que devolve a maior quantia
que da pra levar considerando a rua a partir daquela casa.

Dicas:

* O caso-base eh a rua ter acabado: se casa >= len(rua), devolva 0.

* Nas chamadas recursivas, repasse a MESMA rua - o que muda eh so a
  casa. Uma chamada anda para `casa + 1` (pulei a casa da vez) e a outra
  anda para `casa + 2` (assaltei a casa da vez, entao a casa seguinte
  esta proibida).

* Nao precisa se preocupar com `casa + 2` passar do fim da lista: quem
  cuida disso eh o caso-base: para qualquer casa grande o bastante a
  gente ja definiu a resposta como 0.

    >>> rouba([1, 2, 3, 1], 0)
    4
    >>> rouba([2, 7, 9, 3, 1], 0)
    12
'''
def rouba(rua, casa):
    if casa >= len(rua): return 0
    
    case = rua[casa] + rouba(rua, casa+2)

    case1 = rouba(rua, casa+1)

    return max(case, case1)
    


print('  iniciando testes de rouba')
print('  (Se travar aqui, sua recursao nao esta chegando no caso-base - rode no pythontutor para ver o que esta acontecendo.)')
assert rouba([], 0) == 0, f'rouba([], 0): esperado 0 (rua vazia), obteve {rouba([], 0)}'
assert rouba([7], 0) == 7, f'rouba([7], 0): esperado 7 (uma casa so, pode assaltar), obteve {rouba([7], 0)}'
assert rouba([4, 9], 0) == 9, f'rouba([4, 9], 0): esperado 9 (as duas sao vizinhas, so da pra pegar a maior), obteve {rouba([4, 9], 0)}'
assert rouba([2, 7, 9, 3, 1], 3) == 3, f'rouba([2, 7, 9, 3, 1], 3): esperado 3 (a rua a partir da casa 3 eh so [3, 1]), obteve {rouba([2, 7, 9, 3, 1], 3)}'
assert rouba([2, 7, 9, 3, 1], 9) == 0, f'rouba([2, 7, 9, 3, 1], 9): esperado 0 (casa ja passou do fim da rua), obteve {rouba([2, 7, 9, 3, 1], 9)}'
assert rouba([1, 2, 3, 1], 0) == 4, f'rouba([1, 2, 3, 1], 0): esperado 4 (Exemplo 1 do enunciado), obteve {rouba([1, 2, 3, 1], 0)}'
assert rouba([2, 7, 9, 3, 1], 0) == 12, f'rouba([2, 7, 9, 3, 1], 0): esperado 12 (Exemplo 2 do enunciado), obteve {rouba([2, 7, 9, 3, 1], 0)}'
assert rouba([5, 1, 1, 5], 0) == 10, f'rouba([5, 1, 1, 5], 0): esperado 10 (voce calculou isso a mao na Fase 1), obteve {rouba([5, 1, 1, 5], 0)}'
assert rouba([3, 5, 4, 1, 6], 0) == 13, f'rouba([3, 5, 4, 1, 6], 0): esperado 13 (voce calculou isso a mao na Fase 1), obteve {rouba([3, 5, 4, 1, 6], 0)}'
assert rouba([1, 9, 1, 1], 0) == 10, f'rouba([1, 9, 1, 1], 0): esperado 10 (voce calculou isso a mao na Fase 2), obteve {rouba([1, 9, 1, 1], 0)}'
assert rouba([6, 2, 2, 6], 0) == 12, f'rouba([6, 2, 2, 6], 0): esperado 12, obteve {rouba([6, 2, 2, 6], 0)}'
print('Exercicio rouba: OK')


# ===== FASE 4 - Ver o trabalho repetido =====

'''
EXERCICIO

Sua rouba esta CORRETA. Agora vamos olhar COMO ela trabalha.

Faca o seguinte, nesta ordem:

1. Suba ate a sua funcao rouba e acrescente, como PRIMEIRA linha do
   corpo dela, este print:

       print('rouba chamada com casa =', casa)

2. Descomente a linha abaixo e rode o arquivo:

       # print(rouba([3, 5, 4, 1, 6, 2], 0))

3. Olhe a saida. Sao so 6 casas na rua - role a saida e repare em
   quais casas aparecem. (Vao aparecer tambem a casa 6 e a casa 7, que
   ja passaram do fim da rua: sao as chamadas que caem no caso-base.)

Depois responda a questao abaixo.
'''

# print(rouba([3, 5, 4, 1, 6, 2], 0))

'''
EXERCICIO

Olhe a saida do print.

Entre as casas abaixo, qual apareceu MAIS vezes?

    a) a casa 0
    b) a casa 2
    c) a casa 5
    d) todas apareceram o mesmo numero de vezes
'''
casa_mais_repetida = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('casa_mais_repetida')

assert verifica(casa_mais_repetida, '1194b8647503a70ad41e1beaad3b9ced59270cf3868de24a7c44c2cd', nome_questao='casa_mais_repetida'), 'casa_mais_repetida incorreta'
print('Exercicio casa_mais_repetida: OK')

'''
EXPLICACAO

Toda vez que a sua rouba recebe uma casa que ela ja recebeu antes, ela
refaz do zero uma conta que ela ja tinha feito - e o resultado eh
exatamente o mesmo, porque rua nao mudou e casa nao mudou. Eh trabalho
jogado fora.

E repare ONDE o desperdicio se concentra. A casa 0 apareceu uma vez
so; a casa 5, la no fim da rua, apareceu varias. Faz sentido: a casa 0
eh alcancada por um caminho so - a chamada que voce mesmo fez. Ja o
fim da rua eh alcancado por muitos caminhos diferentes (pulando,
assaltando, pulando de novo...), e cada caminho refaz a conta inteira.

Com 6 casas isso ainda termina rapido. Com uma rua de verdade, nao
termina nunca.

Nas proximas fases voce vai matar essa repeticao de dois jeitos
diferentes: primeiro guardando cada resultado num dicionario
(memoizacao), depois trocando a recursao por uma tabela.

Antes de seguir: APAGUE o print de dentro da sua rouba e comente de
novo a linha `print(rouba([3, 5, 4, 1, 6, 2], 0))` acima - senao as
proximas fases vao rodar cheias de ruido.
'''


# ===== FASE 5 - Memoizacao =====

'''
EXPLICACAO

MEMOIZAR eh guardar o que ja foi computado para nao computar de novo.

A funcao ganha um parametro a mais, `memo`, que eh um dicionario. A
chave eh a casa; o valor eh o que rouba(rua, casa) devolveu daquela vez.
O corpo da funcao ganha duas pontas:

    NO COMECO: se casa ja esta no memo, devolva memo[casa] na hora, sem
    computar nada.

    NO FIM: antes de devolver o resultado, guarde ele em memo[casa].

Assim, cada casa eh computada no maximo UMA vez. Da segunda
chamada em diante, a resposta ja esta guardada.

O mesmo `memo` tem que ser repassado nas chamadas recursivas - eh um
dicionario so, compartilhado por toda a recursao. (Dicionario eh
MUTAVEL: quando voce passa ele por parametro, as chamadas de dentro
mexem no mesmo dicionario que esta aqui fora, entao o que uma guarda
a outra enxerga.)
'''

'''
EXPLICACAO

Antes de escrever, vamos montar a funcao por partes.

Voce NAO precisa escrever recursao aqui - a recursao ja esta pronta,
eh a sua rouba da Fase 3. Memoizar eh acrescentar duas pontas a ela,
sem mexer no meio. O esqueleto, com os buracos marcados:

    def rouba_memo(rua, casa, memo):
        ###  (A)  ###
        if casa >= len(rua):
            return 0
        pula    = rouba_memo(rua, casa + 1, ###  (B)  ###)
        assalta = rua[casa] + rouba_memo(rua, casa + 2, ###  (B)  ###)
        ###  (C)  ###

As tres questoes abaixo sao uma para cada buraco.
'''

'''
EXERCICIO

Q1 - consulta_do_memo (buraco A)

    def rouba_memo(rua, casa, memo):
  -->   ###  (A)  ###
        if casa >= len(rua):
            return 0
        pula    = rouba_memo(rua, casa + 1, ###  (B)  ###)
        assalta = rua[casa] + rouba_memo(rua, casa + 2, ###  (B)  ###)
        ###  (C)  ###

O buraco (A) eh a ponta de cima: devolver na hora o que ja foi
computado. O que entra ali?

    a) memo[casa] = 0
    b) if memo[casa]: return memo[casa]
    c) if casa in memo.keys(): return memo[casa]
    d) if casa in memo.keys(): return casa
'''
consulta_do_memo = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('consulta_do_memo')

assert verifica(consulta_do_memo, '0ca1224333edeaf45c3ee063e21bd5c307621735ded42637c88eb554', nome_questao='consulta_do_memo'), 'consulta_do_memo incorreta'
print('Exercicio consulta_do_memo: OK')


'''
EXERCICIO

Q2 - memo_nas_chamadas (buraco B)

    def rouba_memo(rua, casa, memo):
        if casa in memo.keys():
            return memo[casa]
        if casa >= len(rua):
            return 0
  -->   pula    = rouba_memo(rua, casa + 1, ###  (B)  ###)
  -->   assalta = rua[casa] + rouba_memo(rua, casa + 2, ###  (B)  ###)
        ###  (C)  ###

O que vai no lugar de (B), nas DUAS chamadas recursivas?

    a) memo
    b) {}
    c) nada - chamar so com dois argumentos: rouba_memo(rua, casa + 1)
    d) memo[casa]
'''
memo_nas_chamadas = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('memo_nas_chamadas')

assert verifica(memo_nas_chamadas, '64c87ebb4c99fedf67c61e25f56f706a2889741eb94f33971928c002', nome_questao='memo_nas_chamadas'), 'memo_nas_chamadas incorreta'
print('Exercicio memo_nas_chamadas: OK')


'''
EXERCICIO

Q3 - guarda_no_memo (buraco C)

    def rouba_memo(rua, casa, memo):
        if casa in memo.keys():
            return memo[casa]
        if casa >= len(rua):
            return 0
        pula    = rouba_memo(rua, casa + 1, memo)
        assalta = rua[casa] + rouba_memo(rua, casa + 2, memo)
  -->   ###  (C)  ###

O buraco (C) eh a ponta de baixo, e eh a ultima coisa que a funcao
faz. O que entra ali?

    a) return max(pula, assalta)
    b) memo[casa] = max(pula, assalta)
    c) memo[max(pula, assalta)] = casa
       return casa
    d) memo[casa] = max(pula, assalta)
       return memo[casa]
'''
guarda_no_memo = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('guarda_no_memo')

assert verifica(guarda_no_memo, '607bd00525ded614ea4b6e26620cd68592b3c0d241102bc19b21eb88', nome_questao='guarda_no_memo'), 'guarda_no_memo incorreta'
print('Exercicio guarda_no_memo: OK')


'''
EXERCICIO

Faca rouba_memo(rua, casa, memo): a sua rouba com memoizacao.

Monte a funcao com as tres respostas que voce acabou de dar, nos tres
buracos do esqueleto.

Dica: nao comece do zero - copie a sua rouba e acrescente as duas
pontas.

    >>> rouba_memo([1, 2, 3, 1], 0, {})
    4

Vale olhar o memo POR DENTRO depois da chamada. Passe um dicionario
seu e imprima ele no fim:

    >>> memo = {}
    >>> rouba_memo([1, 2, 3, 1], 0, memo)
    4
    >>> print(memo)
    {3: 1, 2: 3, 1: 3, 0: 4}

Cada entrada eh uma casa e a resposta DAQUELA CASA EM DIANTE - o
mesmo numero que a sua rouba da Fase 3 devolveria para aquela casa:

    memo[3] eh 1  ->  da casa 3 em diante so existe a casa 3, com 1
    memo[2] eh 3  ->  da casa 2 em diante, o melhor eh assaltar a casa
                      2 (3 reais) e parar
    memo[1] eh 3  ->  da casa 1 em diante, tanto faz assaltar as casas
                      1 e 3 (2 + 1) ou so a casa 2 (3) - da 3 dos dois
                      jeitos
    memo[0] eh 4  ->  a rua inteira: casas 0 e 2, 1 + 3 = 4

Duas coisas para reparar. A primeira eh que memo[0] eh a resposta do
problema todo. A segunda eh a ORDEM em que as chaves entraram: 3, 2,
1, 0 - de tras para a frente. A recursao so consegue guardar a
resposta de uma casa depois de ja ter as respostas das casas
seguintes.
'''


def rouba_memo(rua, casa, memo):
    pass

assert rouba_memo([], 0, {}) == 0, f'rouba_memo([], 0, {{}}): esperado 0, obteve {rouba_memo([], 0, {})}'
assert rouba_memo([7], 0, {}) == 7, f'rouba_memo([7], 0, {{}}): esperado 7, obteve {rouba_memo([7], 0, {})}'
assert rouba_memo([4, 9], 0, {}) == 9, f'rouba_memo([4, 9], 0, {{}}): esperado 9, obteve {rouba_memo([4, 9], 0, {})}'
assert rouba_memo([1, 2, 3, 1], 0, {}) == 4, f'rouba_memo([1, 2, 3, 1], 0, {{}}): esperado 4, obteve {rouba_memo([1, 2, 3, 1], 0, {})}'
assert rouba_memo([2, 7, 9, 3, 1], 0, {}) == 12, f'rouba_memo([2, 7, 9, 3, 1], 0, {{}}): esperado 12, obteve {rouba_memo([2, 7, 9, 3, 1], 0, {})}'
assert rouba_memo([3, 5, 4, 1, 6], 0, {}) == 13, f'rouba_memo([3, 5, 4, 1, 6], 0, {{}}): esperado 13, obteve {rouba_memo([3, 5, 4, 1, 6], 0, {})}'
assert rouba_memo([2, 7, 9, 3, 1], 3, {}) == 3, f'rouba_memo([2, 7, 9, 3, 1], 3, {{}}): esperado 3, obteve {rouba_memo([2, 7, 9, 3, 1], 3, {})}'

# o memo tem mesmo que ser preenchido - depois da chamada, ele nao pode
# estar vazio
memo_conferido = {}
rouba_memo([2, 7, 9, 3, 1], 0, memo_conferido)
assert len(memo_conferido) > 0, 'depois de rouba_memo(..., memo), o memo deveria ter resultados guardados - confira se voce faz memo[casa] = ... antes de devolver'

# uma rua de 90 casas: a rouba da Fase 3 nao terminaria nunca aqui
rua_grande = []
for k in range(90):
    rua_grande.append((k * 37) % 100)

print('  iniciando teste da rua de 90 casas')
print('  (Se travar aqui, o seu memo nao esta sendo consultado no comeco, ou voce nao esta repassando o MESMO memo nas chamadas recursivas.)')
assert rouba_memo(rua_grande, 0, {}) == 2700, f'rouba_memo(rua_grande, 0, {{}}): esperado 2700, obteve {rouba_memo(rua_grande, 0, {})}'
print('Exercicio rouba_memo: OK')


# ===== FASE 6 - DP com lista: a tabela a mao =====

'''
EXPLICACAO

A memoizacao guarda os resultados num dicionario, preenchido sob
demanda, na ordem em que a recursao pede. Da pra chegar no mesmo
lugar sem recursao nenhuma: guardando os resultados numa LISTA,
preenchida numa ordem escolhida por nos.

A lista se chama `tabela`, e a celula `tabela[casa]` guarda exatamente o
que rouba(rua, casa) devolvia: a maior quantia da rua a partir da casa
casa.

Em que ordem preencher? Olhe a recorrencia:

    tabela[casa] = max( tabela[casa + 1],  rua[casa] + tabela[casa + 2] )

Para preencher a celula de uma casa eu preciso das celulas `casa + 1` e
`casa + 2`, que estao a DIREITA dela. Entao a tabela se preenche DE TRAS PARA A
FRENTE: da ultima casa ate a casa 0.

E o caso-base? Ele vira duas celulas a mais no fim da tabela, valendo
0 - sao as posicoes "a rua ja acabou". Quando voce for computar a posicao
maxima da rua (casa) vai pegar casa+1 e casa+2, e eh interessante deixar
registrado que esses dois valores sao 0.

Por isso a tabela tem len(rua) + 2 celulas, e nao len(rua) celulas.

Veja com rua = [1, 2, 3, 1] (o Exemplo 1 do enunciado). A tabela tem
4 + 2 = 6 celulas, todas comecando em 0:

    tabela = [0, 0, 0, 0, 0, 0]
    #         0  1  2  3  4  5

As celulas 4 e 5 sao o caso-base e ficam 0 para sempre. Agora
preenchemos de tras para a frente:

    casa = 3:  max( tabela[4],  rua[3] + tabela[5] ) = max(0, 1 + 0) = 1
    casa = 2:  max( tabela[3],  rua[2] + tabela[4] ) = max(1, 3 + 0) = 3
    casa = 1:  max( tabela[2],  rua[1] + tabela[3] ) = max(3, 2 + 1) = 3
    * ou nao uso a casa 1, e tenho acesso a dois (valor tabela[2])
    * ou uso a 1, e so tenho acesso a 3 (rua[1] + tabela[3])
    casa = 0:  max( tabela[1],  rua[0] + tabela[2] ) = max(3, 1 + 3) = 4

    tabela = [4, 3, 3, 1, 0, 0]

E a resposta do problema eh tabela[0] = 4 - o mesmo 4 do enunciado.
'''

'''
EXERCICIO

Preencha a mao a tabela do Exemplo 2 do enunciado:

    rua = [2, 7, 9, 3, 1]
    #       0  1  2  3  4

A tabela tem 5 + 2 = 7 celulas. As duas ultimas sao o caso-base e
valem 0. Preencha de tras para a frente, como no exemplo acima, e
escreva a tabela INTEIRA (as 7 celulas, na ordem, do indice 0 ao 6).

Confira sozinho: a celula 0 tem que dar 12, que eh a resposta do
Exemplo 2.
'''
tabela_2793 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tabela_2793')

assert verifica(tabela_2793, '1bfc89c91dafddf12d73d3604a58c0a86f836cb046e3c322ef6e4cb0', ordem_importa=True, nome_questao='tabela_2793'), 'tabela_2793 incorreta'
print('Exercicio tabela_2793: OK')


# ===== FASE 7 - Ponte: montar a tabela em Python =====

'''
EXPLICACAO

Voce ja preencheu a tabela a mao. Falta traduzir isso para Python.

Em portugues, a funcao inteira sao quatro linhas:

    crie a tabela, cheia de zeros
    para cada casa, da ULTIMA para a primeira:
        tabela[casa] = o melhor entre pular e assaltar aquela casa
    devolva a resposta da rua inteira

Uma questao para cada linha. A cada questao, as linhas que voce JA
respondeu aparecem em Python; a linha em foco (marcada com -->) e as
que ainda vem continuam em portugues.
'''

'''
EXERCICIO

Q1 - tamanho_da_tabela

  -->  crie a tabela, cheia de zeros
       para cada casa, da ULTIMA para a primeira:
           tabela[casa] = o melhor entre pular e assaltar aquela casa
       devolva a resposta da rua inteira

A rua tem len(rua) casas. De que tamanho tem que ser a tabela?

    a) tabela = [0] * len(rua)
    b) tabela = [0] * (len(rua) + 1)
    c) tabela = [0] * (len(rua) + 2)
    d) tabela = []
'''
tamanho_da_tabela = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tamanho_da_tabela')

assert verifica(tamanho_da_tabela, 'e4fa6c08f2786f74f89b117a5dbd8dbd45eb50b1e4073f3a9e9d6b49', nome_questao='tamanho_da_tabela'), 'tamanho_da_tabela incorreta'
print('Exercicio tamanho_da_tabela: OK')


'''
EXERCICIO

Q2 - laco_da_tabela

       tabela = [0] * (len(rua) + 2)
  -->  para cada casa, da ULTIMA para a primeira:
           tabela[casa] = o melhor entre pular e assaltar aquela casa
       devolva a resposta da rua inteira

A tabela se preenche DE TRAS PARA A FRENTE: da ultima casa da rua
(indice len(rua) - 1) ate a casa 0, inclusive. Qual laco faz isso?

    a) for casa in range(len(rua)):
    b) for casa in range(len(rua) - 1, -1, -1):
    c) for casa in range(len(rua) - 1, 0, -1):
    d) for casa in range(len(rua), 0, -1):
'''
laco_da_tabela = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('laco_da_tabela')

assert verifica(laco_da_tabela, 'ba5896b4d27346549b7487c7eee2b74625f279cc41d788e2991f70dc', nome_questao='laco_da_tabela'), 'laco_da_tabela incorreta'
print('Exercicio laco_da_tabela: OK')


'''
EXERCICIO

Q3 - dentro_do_laco

       tabela = [0] * (len(rua) + 2)
       for casa in range(len(rua) - 1, -1, -1):
  -->      tabela[casa] = o melhor entre pular e assaltar aquela casa
       devolva a resposta da rua inteira

Eh a mesma recorrencia da Fase 2, agora lendo da tabela em vez de
chamar a funcao. Qual linha vai dentro do laco?

    a) tabela[casa] = max(tabela[casa + 1], rua[casa] + tabela[casa + 2])
    b) tabela[casa] = max(tabela[casa - 1], rua[casa] + tabela[casa - 2])
    c) tabela[casa] = rua[casa] + tabela[casa + 2]
    d) tabela[casa] = max(rua[casa], tabela[casa + 1])
'''
dentro_do_laco = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('dentro_do_laco')

assert verifica(dentro_do_laco, 'c8a099b7bf062c77490616a31be494cf4d1e0860fc51a4c1e6cccb8a', nome_questao='dentro_do_laco'), 'dentro_do_laco incorreta'
print('Exercicio dentro_do_laco: OK')


'''
EXERCICIO

Q4 - o_que_devolver

       tabela = [0] * (len(rua) + 2)
       for casa in range(len(rua) - 1, -1, -1):
           tabela[casa] = max(tabela[casa + 1], rua[casa] + tabela[casa + 2])
  -->  devolva a resposta da rua inteira

A tabela esta preenchida. Onde esta a resposta do problema?

    a) return tabela
    b) return tabela[len(rua) - 1]
    c) return tabela[-1]
    d) return tabela[0]
'''
o_que_devolver = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_devolver')

assert verifica(o_que_devolver, '7d7ed8577e01566c0657c67637b3ae68e7d6b2ccabe607a24c6f5513', nome_questao='o_que_devolver'), 'o_que_devolver incorreta'
print('Exercicio o_que_devolver: OK')


'''
EXERCICIO

Faca rouba_tabela(rua), que resolve o problema com a tabela, sem
recursao nenhuma.

Monte a funcao com as quatro respostas que voce acabou de dar.

Repare que ela NAO tem parametro casa: a tabela guarda a resposta de
todas as casas de uma vez, e quem chama so quer a resposta do problema
todo.

    >>> rouba_tabela([1, 2, 3, 1])
    4
    >>> rouba_tabela([2, 7, 9, 3, 1])
    12
'''
def rouba_tabela(rua):
    pass

assert rouba_tabela([]) == 0, f'rouba_tabela([]): esperado 0 (rua vazia), obteve {rouba_tabela([])}'
assert rouba_tabela([7]) == 7, f'rouba_tabela([7]): esperado 7, obteve {rouba_tabela([7])}'
assert rouba_tabela([4, 9]) == 9, f'rouba_tabela([4, 9]): esperado 9, obteve {rouba_tabela([4, 9])}'
assert rouba_tabela([1, 2, 3, 1]) == 4, f'rouba_tabela([1, 2, 3, 1]): esperado 4 (Exemplo 1 do enunciado), obteve {rouba_tabela([1, 2, 3, 1])}'
assert rouba_tabela([2, 7, 9, 3, 1]) == 12, f'rouba_tabela([2, 7, 9, 3, 1]): esperado 12 (Exemplo 2 do enunciado), obteve {rouba_tabela([2, 7, 9, 3, 1])}'
assert rouba_tabela([5, 1, 1, 5]) == 10, f'rouba_tabela([5, 1, 1, 5]): esperado 10, obteve {rouba_tabela([5, 1, 1, 5])}'
assert rouba_tabela([3, 5, 4, 1, 6]) == 13, f'rouba_tabela([3, 5, 4, 1, 6]): esperado 13, obteve {rouba_tabela([3, 5, 4, 1, 6])}'
assert rouba_tabela([1, 9, 1, 1]) == 10, f'rouba_tabela([1, 9, 1, 1]): esperado 10, obteve {rouba_tabela([1, 9, 1, 1])}'
assert rouba_tabela([3, 5, 4, 1, 6, 2]) == 13, f'rouba_tabela([3, 5, 4, 1, 6, 2]): esperado 13, obteve {rouba_tabela([3, 5, 4, 1, 6, 2])}'
assert rouba_tabela(rua_grande) == 2700, f'rouba_tabela(rua_grande): esperado 2700, obteve {rouba_tabela(rua_grande)}'

# as tres solucoes tem que concordar
assert rouba_tabela([2, 7, 9, 3, 1]) == rouba([2, 7, 9, 3, 1], 0), 'rouba_tabela e rouba deveriam dar a mesma resposta'
assert rouba_tabela(rua_grande) == rouba_memo(rua_grande, 0, {}), 'rouba_tabela e rouba_memo deveriam dar a mesma resposta'
print('Exercicio rouba_tabela: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')
