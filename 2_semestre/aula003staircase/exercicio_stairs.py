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
# Varias questoes teoricas tem uma explicacao guardada (embaralhada)
# no arquivo explicacao_stairs.py, que vem junto com este. Quando
# travar numa questao, descomente a linha `# explicar('nome')` logo
# abaixo dela e rode o arquivo: a explicacao aparece.
def explicar(questao):
    try:
        from explicacao_stairs import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_stairs.py' nao foi encontrado.")
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

Voce esta no pe de uma escada com n degraus e quer chegar ao topo.
A cada passo, voce pode subir um numero de degraus que esteja na
lista `passos` (inteiros positivos, todos diferentes).

Por exemplo, se 'passos' for [1,2] significa que você pode
subir um degrau, ou pular um degrau e subir dois direto.

Se passos for [3], você tem que pular de 3 em 3

De quantas MANEIRAS diferentes da pra subir a escada?

Duas maneiras sao diferentes quando a sequencia de passos eh
diferente - a ORDEM importa: subir 1 degrau e depois 2 eh diferente
de subir 2 degraus e depois 1 (voce pisa em degraus diferentes no
caminho).

Exemplo: n=4, passos=[1, 2]. Existem 5 maneiras:

    1 1 1 1 # uma usando nenhum passo duplo
    1 1 2   # tres usando um passo duplo
    1 2 1
    2 1 1
    2 2     # uma usando 2 passos duplos

Nesta lista voce vai resolver esse problema tres vezes: 
primeiro com uma tabela inspirada na recorrencia, que eh bem rapida
depois com recursao, que sai mais parecida com a recorrencia mas fica lenta
depois com memorizacao (que salva a recursao - em breve te explico)
'''


# ===== FASE 1 - Enumerar a mao =====

'''
EXERCICIO

n=3 degraus, passos=[1, 2].
Liste no papel TODAS as maneiras de subir (lembre que a ordem importa).

Quantas sao? Responda abaixo
'''
maneiras_n3 = 3

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('maneiras_n3')

assert verifica(maneiras_n3, 'c75d7ca27bf4aea720a9ba1c88c6b7e84e268166d36e574e27670e8a', nome_questao='maneiras_n3'), 'maneiras_n3 incorreta'
print('Exercicio maneiras_n3: OK')


'''
EXERCICIO

n=5 degraus, passos=[1, 2].

Liste no papel todas as maneiras. Da mais trabalho - e esse eh o
ponto: enumerar na mao para de escalar rapido.

Dica pra nao se perder: agrupe pela quantidade de passos de 2
(nenhum, um, dois).

Quantas sao?
'''
maneiras_n5 = 8

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('maneiras_n5')

assert verifica(maneiras_n5, '480a36529f741fbf193da929d83e5b926c6d46a352c19e996a8a8054', nome_questao='maneiras_n5'), 'maneiras_n5 incorreta'
print('Exercicio maneiras_n5: OK')


'''
EXERCICIO

Agora com outros passos: n=4 degraus, passos=[1, 3].

Quantas maneiras?
'''
maneiras_n4_13 = 3

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('maneiras_n4_13')

assert verifica(maneiras_n4_13, 'df88428e9dceac97cb70d0122294be5ff011eadc7bd094c6b88f99a5', nome_questao='maneiras_n4_13'), 'maneiras_n4_13 incorreta'
print('Exercicio maneiras_n4_13: OK')


# ===== FASE 2 - A recorrencia =====

'''
EXPLICACAO

Como contar SEM enumerar tudo? Olhe para o ULTIMO passo.

Toda maneira de subir n degraus termina num ultimo passo p (algum
valor da lista passos). Se o ultimo passo foi p, o que veio antes
foi uma maneira de subir n - p degraus. 

Se a minha lista de passos é [1,2,5]

entao 
conta(n) = conta(n-1) + conta(n-2) + conta(n-5)

ou seja, para eu subir n degraus, posso 
    subir n-1, e arrematar com uma subida normal
    subir n-2 degraus e arrematar subindo 2 de uma vez
    subir n-5 degraus, e arrematar dando meu pulão de 5 degraus

Se a lista de passos fosse [p1,p2,p3...], teriamos

    conta(n) = conta(n - p1) + conta(n - p2) + ...

tomando o cuidado de soh usar passos que caibam (isto eh, p <= n).
Se eu tenho a possibilidade de p=7 (dar um pulo de 7 degraus)
mas o tamanho da escada eh n=5, esse p nao serve, nao temos
p <= n, nao vou usar na conta

Confira com n=4, passos=[1, 2] (as 5 maneiras la de cima):

    terminam com passo de 1 (antes dele, subiu-se 3 degraus):
        1 1 1 [1]     1 2 [1]     2 1 [1]      -> conta(3) = 3
    terminam com passo de 2 (antes dele, subiu-se 2 degraus):
        1 1 [2]       2 [2]                    -> conta(2) = 2

    conta(4) = conta(3) + conta(2) = 3 + 2 = 5   (confere!)

E quando a escada acaba (n = 0)? Existe UMA maneira de subir zero
degraus: nao dar passo nenhum (a "maneira vazia"). Por isso
conta(0) = 1 - esse eh o caso-base da recursao.


'''

'''
EXERCICIO

Calculo a mao. passos=[1, 2]. Voce ja sabe que conta(4) = 5 (acima)
e conta(5) = 8 (voce enumerou na Fase 1).

Use a recorrencia para calcular conta(6, [1, 2]).
'''
conta6_a_mao = 13

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('conta6_a_mao')

assert verifica(conta6_a_mao, '87f1dead2cc2e37a594b5f992bb384954237f4346ef6a39219079990', nome_questao='conta6_a_mao'), 'conta6_a_mao incorreta'
print('Exercicio conta6_a_mao: OK')


'''
EXERCICIO

Calculo a mao, agora com passos=[1, 3] - repare que as parcelas
mudam junto com os passos.

Suponha que alguém já fez pra você:
conta(1, [1,3]) = 1,
conta(2, [1,3]) = 1,
conta(3, [1,3]) = 2,
conta(4, [1,3]) = 3 e
conta(5, [1,3]) = 4.

Use a recorrencia para calcular conta(6, [1, 3]).
'''

conta6_13_a_mao = 6

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('conta6_13_a_mao')

assert verifica(conta6_13_a_mao, '2133e4380d570ff774621dec4ee4742458973177cd8c9ad8051f67aa', nome_questao='conta6_13_a_mao'), 'conta6_13_a_mao incorreta'
print('Exercicio conta6_13_a_mao: OK')


# ===== FASE 3 - Tabela bottom-up =====

'''
EXPLICACAO

Já vimos em outras aulas recursoes que recomputam um bocado de valores.

Veremos isso de novo em breve.

Mas primeiro, vamos fazer uma solucao extremamente rapida.

A ideia da TABELA eh: computar cada valor UMA vez, 
do menor para o maior, guardando numa lista.

A regra de preenchimento eh a MESMA recorrencia da Fase 2, 


    tabela[0] = 1                       (caso-base)
    tabela[v] = tabela[v - p1] + tabela[v - p2]...   (para cada passo p com p <= v)

Preenchendo passo a passo para passos=[1, 2], ate o indice 5:

    tabela[0] = 1                                 -> tabela completa: [1]
    (estou usando 1 para 0 degraus. Isso faz sentido, mas por enquanto soh aceita.
    Te explico na fase 4)
    tabela[1] = tabela[0]             = 1         -> tabela completa: [1, 1]
    (porque o ultimo passo foi de tamanho 1. Com 2 já estaria fora da escada)
    tabela[2] = tabela[1] + tabela[0] = 2         -> tabela completa: [1, 1, 2]
    (pois o ultimo passo pode ser de tamanho 1 ou 2)
    tabela[3] = tabela[2] + tabela[1] = 3         -> tabela completa: [1, 1, 2, 3]
    tabela[4] = tabela[3] + tabela[2] = 5         -> tabela completa: [1, 1, 2, 3, 5]
    tabela[5] = tabela[4] + tabela[3] = 8         -> tabela completa: [1, 1, 2, 3, 5, 8]

Por que tabela[3] = tabela[2] + tabela[1]? Olhe as listas de
possibilidades. As maneiras de subir 2 degraus sao "1 1" e "2"
(por isso tabela[2] = 2); a maneira de subir 1 degrau eh "1"
(tabela[1] = 1). Toda maneira de subir 3 degraus eh uma dessas,
arrematada com mais um passo:

    quem subiu 2, arremata com um passo de 1:
        1 1 [1]     2 [1]           <- as tabela[2] = 2 maneiras
    quem subiu 1, arremata com um passo de 2:
        1 [2]                       <- a  tabela[1] = 1 maneira

Sao 2 + 1 = 3 maneiras, sem sobrar nem repetir: "1 1 1", "2 1" e
"1 2" - exatamente as 3 que voce enumerou na Fase 1 para n=3.
'''

'''
EXERCICIO

passos=[1, 2]. A tabela preenchida ate o indice 5 eh

    tabela = [1, 1, 2, 3, 5, 8]
    #         0  1  2  3  4  5

Continue MAIS UMA casa (ate o indice 6).

Responda com a lista INTEIRA, do indice 0 ao 6 (7 numeros).
'''
tabela_12_ate6 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tabela_12_ate6')

assert verifica(tabela_12_ate6, 'bb0328c5a5fa38decaeea590f407caf5b0c0848044f8c82e2e7c3a05', ordem_importa=True, nome_questao='tabela_12_ate6'), 'tabela_12_ate6 incorreta'
print('Exercicio tabela_12_ate6: OK')

'''
EXERCICIO

E mais uma casa (ate o indice 7). passos=[1, 2].

Lista inteira de novo (8 numeros).
'''
tabela_12_ate7 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tabela_12_ate7')

assert verifica(tabela_12_ate7, 'fad3e45f859df8176777df089ee1faa0fc6aea4e8e55cbc4a44d25b1', ordem_importa=True, nome_questao='tabela_12_ate7'), 'tabela_12_ate7 incorreta'
print('Exercicio tabela_12_ate7: OK')


'''
EXERCICIO

Agora com TRES parcelas: passos=[1, 2, 3].

Preencha a mao a tabela do indice 0 ate o 6. Comece por
tabela[0] = 1; em cada casa v, some as casas 
adequadas

Responda com a lista inteira (7 numeros).
'''
tabela_123_ate6 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tabela_123_ate6')

assert verifica(tabela_123_ate6, '6f74a18aacfd7c74690eda66bf79301bbb0b94368c3e50e690be5d04', ordem_importa=True, nome_questao='tabela_123_ate6'), 'tabela_123_ate6 incorreta'
print('Exercicio tabela_123_ate6: OK')


'''
EXERCICIO

Tabela para passos=[2, 3], preenchida ate o indice 7:

    tabela = [1, 0, 1, 1, 1, 2, 2, 3]
    #         0  1  2  3  4  5  6  7

(Repare no tabela[1] = 0: com passos de 2 e 3 nao ha maneira nenhuma
de subir 1 degrau.)

Qual expressao Python calcula o valor da PROXIMA casa (tabela[8])?

    a) tabela[2] + tabela[3]
    b) tabela[8 - 2] + tabela[8 - 3]
    c) tabela[-1] + tabela[-2]
    d) 2 + 3
'''
expressao_proxima = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('expressao_proxima')

assert verifica(expressao_proxima, '4b7f055142271485067dc30edf800e5bd938fd0db060a3cd15703a0a', nome_questao='expressao_proxima'), 'expressao_proxima incorreta'
print('Exercicio expressao_proxima: OK')


'''
EXERCICIO

Faca conta_maneiras_tabela(n, passos): monta a lista tabela do
indice 0 ate o n (como voce fez a mao nos exercicios acima) e
retorna tabela[n]. SEM recursao: 
- um laco de v = 1 ate n, para calcular a posicao v da tabela.
- dentro dele, um laco pelos passos para consultar a tabela nas posicoes relevantes

    >>> conta_maneiras_tabela(4, [1, 2])
    5
    >>> conta_maneiras_tabela(5, [1, 2, 3])
    13
'''
def conta_maneiras_tabela(n, passos):
    pass

assert conta_maneiras_tabela(0, [1, 2]) == 1, f'conta_maneiras_tabela(0, [1,2]): esperado 1, obteve {conta_maneiras_tabela(0, [1, 2])}'
assert conta_maneiras_tabela(1, [1]) == 1, f'conta_maneiras_tabela(1, [1]): esperado 1, obteve {conta_maneiras_tabela(1, [1])}'
assert conta_maneiras_tabela(3, [1, 2]) == 3, f'conta_maneiras_tabela(3, [1,2]): esperado 3, obteve {conta_maneiras_tabela(3, [1, 2])}'
assert conta_maneiras_tabela(4, [1, 2]) == 5, f'conta_maneiras_tabela(4, [1,2]): esperado 5, obteve {conta_maneiras_tabela(4, [1, 2])}'
assert conta_maneiras_tabela(5, [1, 2]) == 8, f'conta_maneiras_tabela(5, [1,2]): esperado 8, obteve {conta_maneiras_tabela(5, [1, 2])}'
assert conta_maneiras_tabela(4, [1, 2, 3]) == 7, f'conta_maneiras_tabela(4, [1,2,3]): esperado 7, obteve {conta_maneiras_tabela(4, [1, 2, 3])}'
assert conta_maneiras_tabela(4, [1, 3]) == 3, f'conta_maneiras_tabela(4, [1,3]): esperado 3, obteve {conta_maneiras_tabela(4, [1, 3])}'
assert conta_maneiras_tabela(3, [2]) == 0, f'conta_maneiras_tabela(3, [2]): esperado 0, obteve {conta_maneiras_tabela(3, [2])}'
assert conta_maneiras_tabela(14, [7]) == 1, f'conta_maneiras_tabela(14, [7]): esperado 1, obteve {conta_maneiras_tabela(14, [7])}'
assert conta_maneiras_tabela(28, [1, 2]) == 514229, f'conta_maneiras_tabela(28, [1,2]): esperado 514229, obteve {conta_maneiras_tabela(28, [1, 2])}'

print('  teste com n = 1000 - a recursao ingenua que veremos breve NUNCA terminaria; a tabela termina num piscar')
assert verifica(conta_maneiras_tabela(1000, [1, 2]), '006bd2701dc25987995b23da295ca8041692c68ca4180c12e0330713', nome_questao='n1000'), 'conta_maneiras_tabela(1000, [1,2]) incorreta'
print('Exercicio conta_maneiras_tabela: OK')


# ===== FASE 4 - A recursao =====

'''
EXPLICACAO

Agora que jah fizemos a tabela, vamos experimentar a recursao
Primeiramente ela vai ficar lenta, mas depois vamos fazer ela
ficar tao boa quanto a tabela
'''

'''
EXERCICIO

Faca uma funcao conta_maneiras(n, passos) RECURSIVA que retorna de
quantas maneiras da pra subir uma escada de n degraus dando passos
da lista passos.

Dicas: 
* Use conta(0) = 1 como caso base. Se voce pensar 
em conta(5,[1,3]) como 'quantas listas existem com os numeros 1 e 3
que somam 5', é justo dizer conta(0,[1,3]) = 1, porque
só existe uma lista, a lista vazia.

* Cuidado tambem com passos que NAO CABEM: se restam n degraus e o
passo p eh maior que n, a parcela dele nao entra na soma - senao
voce chamaria conta de um numero negativo. Ex: conta(2, [1, 3]) tem
so a parcela do passo 1 (o passo 3 nao cabe em 2 degraus), entao
conta(2) = conta(1).

    >>> conta_maneiras(4, [1, 2])
    5
    >>> conta_maneiras(4, [1, 3])
    3
'''
def conta_maneiras(n, passos):
    pass

print('  iniciando testes de conta_maneiras')
print('  (Se travar aqui, sua recursao nao esta chegando no caso-base - rode no pythontutor para ver o que esta acontecendo.)')
assert conta_maneiras(0, [1, 2]) == 1, f'conta_maneiras(0, [1,2]): esperado 1 (a maneira vazia), obteve {conta_maneiras(0, [1, 2])}'
assert conta_maneiras(1, [1]) == 1, f'conta_maneiras(1, [1]): esperado 1, obteve {conta_maneiras(1, [1])}'
assert conta_maneiras(3, [1, 2]) == 3, f'conta_maneiras(3, [1,2]): esperado 3, obteve {conta_maneiras(3, [1, 2])}'
assert conta_maneiras(4, [1, 2]) == 5, f'conta_maneiras(4, [1,2]): esperado 5, obteve {conta_maneiras(4, [1, 2])}'
assert conta_maneiras(5, [1, 2]) == 8, f'conta_maneiras(5, [1,2]): esperado 8, obteve {conta_maneiras(5, [1, 2])}'
assert conta_maneiras(4, [1, 2, 3]) == 7, f'conta_maneiras(4, [1,2,3]): esperado 7, obteve {conta_maneiras(4, [1, 2, 3])}'
assert conta_maneiras(4, [1, 3]) == 3, f'conta_maneiras(4, [1,3]): esperado 3, obteve {conta_maneiras(4, [1, 3])}'
assert conta_maneiras(3, [2]) == 0, f'conta_maneiras(3, [2]): esperado 0 (so com passos de 2 nao da pra somar 3), obteve {conta_maneiras(3, [2])}'
assert conta_maneiras(14, [7]) == 1, f'conta_maneiras(14, [7]): esperado 1 (uma unica maneira: 7 e 7), obteve {conta_maneiras(14, [7])}'
print('Exercicio conta_maneiras: OK')


'''
EXERCICIO

Agora voce tem as duas solucoes na mao - vale parar e comparar o que
cada uma guarda.

Considere a tabela da Fase 3, construida com passos=[1, 2] e preenchida
ate o indice 20:

    tabela = [1, 1, 2, 3, 5, 8, 13, ...]
    #         0  1  2  3  4  5   6

A celula tabela[9] tem exatamente o mesmo valor de qual chamada?

    a) conta_maneiras(9, [1, 2])
    b) conta_maneiras(2, [1, 9])
    c) conta_maneiras(10, [1, 2])
    d) nenhuma das demais
'''
qual_celula = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('qual_celula')

assert verifica(qual_celula, 'ac09b9ad631d43b08624b765be582bf47ff604e94c0c516c4547560f', nome_questao='qual_celula'), 'qual_celula incorreta'
print('Exercicio qual_celula: OK')


# ===== FASE 5 - Ver a perda de tempo com recalculos =====

'''
EXPLICACAO

Sua conta_maneiras esta CORRETA - mas desperdica muito trabalho.

Vamos entender quantas vezes cada valor foi calculado,
desenhando as chamadas que acontecem em conta(4, [1, 2]) 

    conta(4)
      conta(3)            
      conta(2)

conta(4) chamou conta(3) e conta(2) - usamos a indentacao pra mostrar quem chamou quem
Se a gente for pensar nesse conta(3) e conta(2), eles terão suas chamadas...          

    conta(4)
      conta(3)            <- 4 - 1
        conta(2)          <- 3 - 1
        conta(1)          <- 3 - 2
      conta(2)            <- 4 - 2
        conta(1)
        conta(0)

Expandindo a coisa toda, teriamos
        
    conta(4)
      conta(3)            <- 4 - 1
        conta(2)          <- 3 - 1
          conta(1)
            conta(0)
          conta(0)
        conta(1)          <- 3 - 2
          conta(0)
      conta(2)            <- 4 - 2
        conta(1)
          conta(0)
        conta(0)


Repare: conta(2) eh computado 2 VEZES - uma dentro de conta(3),
outra chamada direto por conta(4). A segunda vez refaz do zero um
trabalho que ja tinha sido feito.
'''

'''
EXERCICIO

Desenhe (ou rascunhe no papel) a arvore de chamadas de
conta(5, [1, 2]).

Quantas vezes conta(2) eh computado?
'''
vezes_conta2_em_conta5 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('vezes_conta2_em_conta5')

assert verifica(vezes_conta2_em_conta5, '2c32a8e3a2ad380ca93647601221c4b3bbedf6c9d991d44df47b9790', nome_questao='vezes_conta2_em_conta5'), 'vezes_conta2_em_conta5 incorreta'
print('Exercicio vezes_conta2_em_conta5: OK')


'''
EXERCICIO

Agora SEM desenhar a arvore inteira. conta(6) chama conta(5) e
conta(4). Entao:

    vezes que conta(2) aparece dentro de conta(6)
        = vezes dentro de conta(5) + vezes dentro de conta(4)

Voce ja tem os dois numeros: o de conta(4) esta na explicacao da
arvore, o de conta(5) voce acabou de calcular.

Quantas vezes conta(2) eh computado dentro de conta(6, [1, 2])?
'''
vezes_conta2_em_conta6 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('vezes_conta2_em_conta6')

assert verifica(vezes_conta2_em_conta6, 'c60717289a8646f363bf7f2b0dac4c76f7e9366bf03acaf3165f3f73', nome_questao='vezes_conta2_em_conta6'), 'vezes_conta2_em_conta6 incorreta'
print('Exercicio vezes_conta2_em_conta6: OK')

'''
EXPLICACAO

As repeticoes de conta(2) dentro de conta(6) (5 vezes) ja sao mais
que o dobro das de conta(4) (2 vezes). Se a gente deixar isso
correr um pouco mais, provavelmente teremos numeros inviaveis
de operacoes!
'''

'''
EXPLICACAO

Fizemos algumas contas na mão pra entender o recalculo.

Agora, vamos medir o tamanho desse recalculo que estamos fazendo?

A tecnica: passar um dicionario
`medidor` para a funcao e, toda vez que ela computa um valor n,
somar 1 em medidor[n]:

    medidor[n] = medidor.get(n, 0)                              + 1
                 # devolve 0 se n nao for uma chave ainda
                 # devolve o valor se n ja for uma chave

'''

'''
EXERCICIO

Faca conta_maneiras_medida(n, passos, medidor): igual a sua
conta_maneiras, mas medindo quantas vezes cada valor eh computado.

A linha da medicao ja esta escrita - voce nao precisa pensar nela.
Escreva o resto da funcao no lugar das linhas de dica: aquela chamada
com n_que_voce_quiser esta la so pra lembrar que o MESMO medidor tem
que ser repassado nas chamadas recursivas. Ela nao roda como esta -
troque pelas suas chamadas de verdade.

    >>> med = {}
    >>> conta_maneiras_medida(4, [1, 2], med)
    5
    >>> med[2]
    2
'''
def conta_maneiras_medida(n, passos, medidor):
    medidor[n] = medidor.get(n, 0) + 1
    # escreva o resto da sua funcao aqui
    conta_maneiras_medida(n_que_voce_quiser, passos_que_voce_quiser, medidor) #nao esqueca de passar o medidor nas 
    #suas chamadas recursivas
    pass


med = {}
resultado = conta_maneiras_medida(12, [1, 2], med)
assert resultado == 233, f'conta_maneiras_medida(12, [1,2], ...): esperado 233, obteve {resultado}'
assert med.get(2) == 89, f'apos rodar n=12, medidor[2]: esperado 89 computacoes, obteve {med.get(2)}'
assert med.get(10) == 2, f'apos rodar n=12, medidor[10]: esperado 2 computacoes, obteve {med.get(10)}'
print('Exercicio conta_maneiras_medida: OK')

print('  medindo a recomputacao com n=28...')
print('  (dependendo da maquina, da pra SENTIR a demora - e cada degrau a mais quase dobra o tempo)')
med28 = {}
conta_maneiras_medida(28, [1, 2], med28)

'''
EXERCICIO

O codigo logo acima ja rodou conta_maneiras_medida(28, [1, 2], med28).

Quantas vezes o valor 2 foi computado? Responda com a EXPRESSAO
Python que consulta isso no dicionario
'''
medidor2_n28 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('medidor2_n28')

assert medidor2_n28 != 'coloque o valor aqui', 'preencha a variavel'
assert verifica(medidor2_n28, 'dba2ca3cec56733ee852ac3583719746cae5609497b41d6c1962e24c', nome_questao='medidor2_n28'), 'medidor2_n28 incorreta'
print('Exercicio medidor2_n28: OK')


breakpoint_aqui = 42

# PARE
# Voce acabou de olhar UMA chave do med28. Vale olhar o dicionario
# inteiro: ele tem, para cada valor, quantas vezes a sua recursao
# computou aquele valor.
# Ponha um breakpoint na linha `breakpoint_aqui = 42` acima, rode com
# 'debug python file' e use o debug console:
# digite print(med28) pra ver tudo de uma vez, e depois compare as duas
# pontas da escada: print(med28[28]), print(med28[27]), print(med28[26])
# contra print(med28[2]), print(med28[1]), print(med28[0]).
# Duas perguntas pra levar: por que os degraus do TOPO foram computados
# tao poucas vezes, e os de baixo tantas? E olhe o med28[0] - ele eh o
# mesmo 514229 que a sua tabela da Fase 3 devolveu, e nao eh
# coincidencia. Por que contar quantas vezes a recursao chegou no
# degrau 0 daria justamente o numero de maneiras de subir a escada?
# (Aqui o pythontutor nao ajuda - sao mais de um milhao de chamadas.)
# Se nao conseguir, me chame

'''
EXPLICACAO

Quase DUZENTAS MIL computacoes so do valor 2 - numa escada de apenas
28 degraus. E piora rapido: com passos=[1, 2], o numero de chamadas
cresce como o proprio fibonacci, entao cada degrau a mais multiplica
o tempo por ~1,62.

Contas aproximadas, sempre com passos=[1, 2], partindo dos ~0,3s
que o n=28 levou aqui:

    n=40    ~1,5 minuto          (da pra ir buscar um cafe)
    n=50    ~3 horas             (deixa rodando e va dormir)
    n=60    ~17 dias
    n=76    ~90 anos             (sua vida inteira)
    n=83    ~3 mil anos          (terminaria la pelo ano 5000)
    n=100   ~10 milhoes de anos  (30x a idade da especie humana)
    n=115   ~14 bilhoes de anos  (a idade do universo)

Tudo isso para uma escada de MENOS de 120 degraus - menos que um
predio de 8 andares. A tabela que voce ja escreveu nao tem esse
problema: la cada valor eh computado UMA vez so. A proxima fase
consegue o mesmo SEM abrir mao da recursao.
'''


# ===== FASE 6 - Memoizacao =====

'''
EXPLICACAO

A tabela resolve, mas exigiu nao usar a recursao, e tivemos
que ter mais cuidado com o caminho do codigo. 
A MEMOIZACAO consegue o mesmo efeito mantendo a recursao:
antes de computar, a funcao CONSULTA um dicionario `memo`; se o
valor ja foi computado alguma vez, devolve o guardado; senao,
computa, GUARDA no memo e devolve.

Esse dict eh a mesma tabela da Fase 3 - so que preenchida sob demanda, na
ordem em que a recursao precisa, em vez de 0, 1, 2, ..., n.
'''

'''
EXERCICIO

Faca conta_maneiras_memo(n, passos, memo, medidor): a sua
conta_maneiras_medida com memoizacao. Ordem dentro do corpo:

1. se n esta no memo, retorne memo[n] - SEM mexer no medidor
   (consultar o cache nao eh computar);
2. registre no medidor que n vai ser computado (como na Fase 5);
3. compute o total (caso-base e parcelas, repassando o MESMO memo e
   o MESMO medidor nas chamadas recursivas);
4. guarde o total em memo[n] e retorne.

    >>> memo = {}
    >>> med = {}
    >>> conta_maneiras_memo(4, [1, 2], memo, med)
    5
    >>> med[2]
    1

Dica: nao comece do zero - copie a sua conta_maneiras_medida (da
Fase 5, ela ja registra no medidor) e acrescente as duas pontas do
cache: a consulta ao memo logo no comeco (passo 1) e a guardada em
memo[n] antes de cada return (passo 4). Atencao ao caso-base: o
return do n = 0 tambem eh um return.
'''
def conta_maneiras_memo(n, passos, memo, medidor):
    pass

memo28 = {}
med_memo28 = {}
resultado = conta_maneiras_memo(28, [1, 2], memo28, med_memo28)
assert resultado == 514229, f'conta_maneiras_memo(28, [1,2], ...): esperado 514229, obteve {resultado}'
assert max(med_memo28.values()) == 1, f'com memoizacao, cada valor deve ser computado no maximo UMA vez - o seu maximo foi {max(med_memo28.values())}. Confira se voce consulta o memo ANTES de computar (e se repassa o MESMO memo nas chamadas recursivas)'
assert conta_maneiras_memo(5, [1, 2, 3], {}, {}) == 13, f'conta_maneiras_memo(5, [1,2,3], ...): esperado 13, obteve {conta_maneiras_memo(5, [1, 2, 3], {}, {})}'
assert conta_maneiras_memo(0, [1, 2], {}, {}) == 1, f'conta_maneiras_memo(0, [1,2], ...): esperado 1, obteve {conta_maneiras_memo(0, [1, 2], {}, {})}'
assert conta_maneiras_memo(3, [2], {}, {}) == 0, f'conta_maneiras_memo(3, [2], ...): esperado 0, obteve {conta_maneiras_memo(3, [2], {}, {})}'
assert conta_maneiras_memo(30, [1, 3], {}, {}) == conta_maneiras_tabela(30, [1, 3]), 'conta_maneiras_memo(30, [1,3]) deveria dar o mesmo que conta_maneiras_tabela(30, [1,3])'
print('Exercicio conta_maneiras_memo: OK')


'''
EXPLICACAO

Compare com a Fase 5: rodar n=28 na recursao ingenua computou o
valor 2 quase DUZENTAS MIL vezes. Com memoizacao, UMA vez
(medidor[2] == 1) - e a resposta eh a mesma. Esse eh o truque
inteiro da programacao dinamica: nao computar nada duas vezes.
'''


# ===== DESAFIO (opcional) =====

'''
EXPLICACAO

Os exercicios abaixo sao opcionais. Os asserts deles ficam
DESLIGADOS por padrao: para ligar (e ver "OK" conforme acerta), mude
a flag `desafio` abaixo de False para True. Se nao quiser fazer,
deixe False.

Curiosidade antes de comecar: para passos=[1, 2], a sequencia que a
tabela gera (1, 1, 2, 3, 5, 8, 13, ...) eh a sequencia de FIBONACCI.
Se voce ja tinha visto fibonacci-com-memoizacao em algum lugar,
acabou de descobrir onde ele mora: numa escada.
'''


desafio = False    # ligue o desafio mudando para True


'''
EXERCICIO (DESAFIO D1a)

E se a ordem NAO importasse? Isto eh: "1 1 2", "1 2 1" e "2 1 1"
contam como UMA maneira so - o que importa eh usar dois passos de 1
e um passo de 2, nao a ordem deles -- por exemplo, se, em vez de passos,
fossem moedas de 1 e 2, e você quisesse pagar 4 reais a alguem.

n=4, passos=[1, 2]: quantas maneiras SEM contar a ordem? (Liste no
papel.)
'''
sem_ordem_n4 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('sem_ordem_n4')

'''
EXERCICIO (DESAFIO D1b)

n=6, passos=[1, 2]: quantas maneiras SEM contar a ordem?
'''
sem_ordem_n6 = 'coloque o valor aqui'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('sem_ordem_n6')

'''
EXPLICACAO

A tabela desta lista NAO resolve essa variante: ela conta "1 1 2",
"1 2 1" e "2 1 1" separadamente. Contar SEM ordem eh o problema do
TROCO (de quantas formas se paga um valor com moedas de certas
denominacoes) - e exige uma mudanca estrutural na tabela. Fica de
provocacao: o que precisaria mudar? Esse eh o assunto de uma proxima
lista.
'''

if desafio:
    assert verifica(sem_ordem_n4, '57c8958407a6e88705ab0db27357db898248d7bb68f61413ca1a7fc6', nome_questao='sem_ordem_n4'), 'sem_ordem_n4 incorreta'
    assert verifica(sem_ordem_n6, '96fa9a96549844f8fd0a47a72b1e3b586544121c5dfdcbb6857cf5cc', nome_questao='sem_ordem_n6'), 'sem_ordem_n6 incorreta'
    print('Desafio D1: OK')


'''
EXERCICIO (DESAFIO D2a)

Para calcular uma casa nova, o laco consulta so umas poucas casas
recentes - o comeco da tabela nunca mais eh usado. Entao da pra
responder o mesmo que conta_maneiras_tabela guardando SO as ultimas
casas (numa lista pequena), em vez da tabela inteira.

Antes de mais nada: QUANTAS casas a gente tem que guardar?

Considere passos_d2 = [2, 5, 3] (ja definida em codigo logo abaixo).
Com esses passos, a casa nova soma as casas 2, 5 e 3 posicoes atras.
A casa mais antiga ainda consultada esta quantas posicoes atras?
Esse eh o tamanho minimo da janela a guardar.

Qual expressao Python da esse tamanho?

    a) len(passos_d2)
    b) passos_d2[-1]
    c) max(passos_d2)
    d) sum(passos_d2)
'''
passos_d2 = [2, 5, 3]

tamanho = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tamanho')

'''
EXERCICIO (DESAFIO D2b)

Agora faca conta_maneiras_pouca_memoria(n, passos): responde o mesmo
que conta_maneiras_tabela, mas guarda so a janela de casas que voce
calculou acima (para a lista `passos` que a funcao recebeu), em vez
da tabela inteira.

    >>> conta_maneiras_pouca_memoria(4, [1, 2])
    5
'''
def conta_maneiras_pouca_memoria(n, passos):
    pass

if desafio:
    assert verifica(tamanho, '2ee72be73af0b94315d2a75fa658dc8cf7b9ecbcaaea1ef7e238a37f', nome_questao='tamanho'), 'tamanho incorreta'
    assert conta_maneiras_pouca_memoria(0, [1, 2]) == 1, f'conta_maneiras_pouca_memoria(0, [1,2]): esperado 1, obteve {conta_maneiras_pouca_memoria(0, [1, 2])}'
    assert conta_maneiras_pouca_memoria(4, [1, 2]) == 5, f'conta_maneiras_pouca_memoria(4, [1,2]): esperado 5, obteve {conta_maneiras_pouca_memoria(4, [1, 2])}'
    assert conta_maneiras_pouca_memoria(5, [1, 2, 3]) == 13, f'conta_maneiras_pouca_memoria(5, [1,2,3]): esperado 13, obteve {conta_maneiras_pouca_memoria(5, [1, 2, 3])}'
    assert conta_maneiras_pouca_memoria(3, [2]) == 0, f'conta_maneiras_pouca_memoria(3, [2]): esperado 0, obteve {conta_maneiras_pouca_memoria(3, [2])}'
    assert conta_maneiras_pouca_memoria(14, [7]) == 1, f'conta_maneiras_pouca_memoria(14, [7]): esperado 1, obteve {conta_maneiras_pouca_memoria(14, [7])}'
    assert conta_maneiras_pouca_memoria(28, [1, 2]) == 514229, f'conta_maneiras_pouca_memoria(28, [1,2]): esperado 514229, obteve {conta_maneiras_pouca_memoria(28, [1, 2])}'
    assert conta_maneiras_pouca_memoria(1000, [1, 2]) == conta_maneiras_tabela(1000, [1, 2]), 'conta_maneiras_pouca_memoria(1000, [1,2]) deveria dar o mesmo que a tabela'
    print('Desafio D2: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')
