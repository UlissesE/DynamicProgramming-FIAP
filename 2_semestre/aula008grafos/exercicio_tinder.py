# Exercicio - grafos, exemplo 1: um tinder (grafo DIRIGIDO).

'''
ENUNCIADO

Faca o miolo de um TINDER.

Cada pessoa cadastrada pode CURTIR outras pessoas. Curtir eh de mao
unica: a ana curtir o breno nao diz nada sobre o breno ter curtido a ana.

Por um menu, o usuario pode:

  1) CADASTRAR uma pessoa nova - ela entra sem ter curtido ninguem;
  2) CURTIR: uma pessoa curte outra;
  3) abrir o PERFIL de alguem, que mostra tres coisas:
       - os MATCHES: quem ela curtiu E a curtiu de volta;
       - os PRETENDENTES: quem a curtiu e ainda nao foi correspondido;
       - os SIMILARES: quem os matches dela curtiram;
  4) SAIR.

Regras:

  - so da pra curtir quem esta cadastrado;
  - curtir duas vezes a mesma pessoa nao vira duas curtidas;
  - ninguem curte a si mesmo.

O menu ja esta pronto la embaixo. O que falta sao as seis funcoes.
'''

'''
EXPLICACAO

O app inteiro cabe num dicionario. A chave eh a pessoa, o valor eh a
LISTA de quem ela curtiu:

    curtidas = {'ana': ['breno'], 'breno': []}

Le-se: a ana curtiu o breno; o breno nao curtiu ninguem (ainda).

Este eh um grafo DIRIGIDO. A curtida da ana no breno esta escrita UMA vez
so, na lista da ana - e eh por isso que o breno nem fica sabendo. Num
grafo NAO dirigido (uma amizade, um trilho de metro) a mesma ligacao
apareceria escrita dos DOIS lados.

Duas consequencias que valem pra toda esta lista:

  1. quem entra no app vira uma chave com lista VAZIA. Ele existe no
     grafo mesmo sem nenhuma seta saindo dele.
  2. as setas que SAEM de alguem estao todas juntas (a lista dele); as
     que CHEGAM nele estao espalhadas pelas listas dos outros.

Na linguagem de grafos, a gente chamaria as pessoas de VERTICES e as
curtidas de ARESTAS. Se A curte B, diriamos que A é adjacente a B
(adjacente é algo como 'proximo', entao faz sentido usar essa palavra)
Dai este dicionario é uma LISTA DE ADJACENCIA, porque
cada chave vem acompanhada da lista de quem eh adjacente a ela.

Aqui a gente vai continuar falando de pessoa e de curtida, que eh mais
facil de pensar. Mas o vocabulario tecnico vai aparecer de vez em quando,
pra ele nao ser novidade no dia em que voce encontrar num livro ou num
site de exercicios.
'''


curtidas_exemplo = {
    'ana':    ['breno', 'duda'],
    'breno':  ['ana', 'elza'],
    'caio':   ['ana', 'duda'],
    'duda':   ['ana', 'flavio'],
    'elza':   ['flavio'],
    'flavio': [],
}

breakpoint_aqui = 42

# PARE
# Experimente acessar esse dicionario, via pythontutor ou via o REPL do
# vscode (ponha um breakpoint na linha `breakpoint_aqui = 42` acima, rode
# com 'debug python file', use o debug console)
# digite coisas como print(curtidas_exemplo), print(curtidas_exemplo['ana'])
# Depois tente usar o dicionario pra revelar valores como ['ana', 'elza'],
# 'flavio', [] e depois True (a ana curtiu o breno?)
# Se nao conseguir, me chame


'''
EXERCICIO

Faca uma funcao cadastra(curtidas, pessoa) que poe a pessoa no app.

Ela entra sem ter curtido ninguem - ou seja, vira uma chave com lista
vazia. Cadastrar de novo quem ja esta no app nao pode apagar o que a
pessoa ja curtiu.

A funcao NAO devolve nada: o dicionario eh mutavel, entao ela modifica o
proprio `curtidas` que recebeu.

    >>> c = {'ana': []}
    >>> cadastra(c, 'breno')
    >>> c
    {'ana': [], 'breno': []}
'''
def cadastra(curtidas, pessoa):
    if pessoa not in curtidas:
        curtidas[pessoa] = []

'''
EXERCICIO

Faca uma funcao curte(curtidas, quem, alvo) que registra que `quem`
curtiu `alvo`. Tambem modifica o dicionario e nao devolve nada.

Cuidado com as duas armadilhas:

  - a seta eh de mao unica: NAO escreva nada na lista do `alvo`;
  - curtir duas vezes a mesma pessoa nao pode virar duas curtidas.

    >>> c = {'ana': [], 'breno': []}
    >>> curte(c, 'ana', 'breno')
    >>> c
    {'ana': ['breno'], 'breno': []}
'''
def curte(curtidas, quem, alvo):
    if alvo not in curtidas[quem]:
        curtidas[quem].append(alvo)
    


curtidas_t = {}
cadastra(curtidas_t, 'ana')
cadastra(curtidas_t, 'breno')
assert curtidas_t == {'ana': [], 'breno': []}, f'depois de cadastrar ana e breno, curtidas deveria ser {{"ana": [], "breno": []}}, mas ficou {curtidas_t}'
curte(curtidas_t, 'ana', 'breno')
cadastra(curtidas_t, 'ana')
assert curtidas_t == {'ana': ['breno'], 'breno': []}, f'cadastrar de novo nao pode apagar as curtidas da ana; ficou {curtidas_t}'
curte(curtidas_t, 'ana', 'breno')
assert curtidas_t['ana'] == ['breno'], f'curtir duas vezes nao vira duas curtidas: curtidas["ana"] deveria ser ["breno"], ficou {curtidas_t["ana"]}'
assert curtidas_t['breno'] == [], f'a curtida da ana NAO aparece na lista do breno (a seta eh de mao unica), mas ficou {curtidas_t["breno"]}'
print('Exercicio 1 (cadastra e curte): OK')


'''
EXERCICIO

Faca uma funcao eh_match(curtidas, a, b) que devolve True se `a` e `b` se
curtiram - ou seja, se a seta existe nos DOIS sentidos.

    >>> eh_match({'ana': ['breno'], 'breno': ['ana']}, 'ana', 'breno')
    True
    >>> eh_match({'ana': ['breno'], 'breno': []}, 'ana', 'breno')
    False
'''
def eh_match(curtidas, a, b):
    if b in curtidas[a] and a in curtidas[b]:
        return True
    return False


assert eh_match(curtidas_exemplo, 'ana', 'breno') == True, 'a ana curtiu o breno e o breno curtiu a ana: eh match'
assert eh_match(curtidas_exemplo, 'breno', 'ana') == True, 'match nao tem ordem: se vale pra ana e o breno, vale pro breno e a ana'
assert eh_match(curtidas_exemplo, 'caio', 'ana') == False, 'o caio curtiu a ana, mas ela nao curtiu ele - falta a seta de volta'
assert eh_match(curtidas_exemplo, 'elza', 'flavio') == False, 'a elza curtiu o flavio, mas ele nao curtiu ninguem'
print('Exercicio 2 (eh_match): OK')


'''
EXERCICIO

Faca uma funcao matches(curtidas, pessoa) que devolve a lista de quem
deu match com ela.

Dica: todo match eh alguem que ela ja curtiu - entao basta percorrer a
lista dela e usar a funcao anterior. Devolva na ordem em que os nomes
aparecem na lista da pessoa.

    >>> matches(curtidas_exemplo, 'ana')
    ['breno', 'duda']
'''
def matches(curtidas, pessoa):
    m = []

    for alvo in curtidas[pessoa]:
        if eh_match(curtidas, pessoa, alvo):
            m.append(alvo)
    return m



assert matches(curtidas_exemplo, 'ana') == ['breno', 'duda'], f'a ana tem dois matches, na ordem da lista dela; voce devolveu {matches(curtidas_exemplo, "ana")}'
assert matches(curtidas_exemplo, 'caio') == [], f'o caio curtiu duas pessoas e nao foi correspondido por nenhuma; voce devolveu {matches(curtidas_exemplo, "caio")}'
assert matches(curtidas_exemplo, 'flavio') == [], f'o flavio nao curtiu ninguem, entao nao tem match; voce devolveu {matches(curtidas_exemplo, "flavio")}'
print('Exercicio 3 (matches): OK')


'''
EXERCICIO

Faca uma funcao pretendentes(curtidas, pessoa) que devolve quem curtiu
essa pessoa e ainda NAO foi correspondido.

Repare que aqui voce precisa das setas que CHEGAM nela - e elas nao estao
guardadas em lugar nenhum. Nao tem jeito: varra o dicionario inteiro
procurando quem tem o nome dela na lista. Devolva na ordem em que as
pessoas aparecem no dicionario.

Em grafos, quantas arestas SAEM de um vertice eh o GRAU DE SAIDA dele, e
quantas CHEGAM eh o GRAU DE ENTRADA. O grau de saida é rapido de calcular
(eh o tamanho da lista da pessoa),
e o de entrada exige varrer o grafo inteiro. Essa assimetria existe so em
grafos como o tinder: A pode dar like em B, sem B dar de volta. 
grafos DIRIGIDOS. Num grafo não dirigido, grau de entrada e de saída é a mesma coisa

    >>> pretendentes(curtidas_exemplo, 'ana')
    ['caio']
'''
def pretendentes(curtidas, pessoa):
    
    p = []
    for usuario in curtidas:
        for likes in curtidas[usuario]:
            if pessoa in likes:
                p.append(usuario)
    return p


assert pretendentes(curtidas_exemplo, 'ana') == ['caio'], f'o breno e a duda ja sao match da ana, entao sobra o caio; voce devolveu {pretendentes(curtidas_exemplo, "ana")}'
assert pretendentes(curtidas_exemplo, 'flavio') == ['duda', 'elza'], f'as duas curtiram o flavio e ele nao curtiu de volta; voce devolveu {pretendentes(curtidas_exemplo, "flavio")}'
assert pretendentes(curtidas_exemplo, 'caio') == [], f'ninguem curtiu o caio; voce devolveu {pretendentes(curtidas_exemplo, "caio")}'
assert pretendentes(curtidas_exemplo, 'breno') == [], f'a ana curtiu o breno, mas eles ja sao match - match nao eh pretendente; voce devolveu {pretendentes(curtidas_exemplo, "breno")}'
print('Exercicio 4 (pretendentes): OK')


'''
EXERCICIO

Faca uma funcao similares(curtidas, pessoa) que devolve as pessoas que os
MATCHES dela curtiram - tirando ela mesma, tirando quem ela ja curtiu, e
sem repetir ninguem.

O nome vem da ideia: se um match seu curtiu voce E curtiu o fulano, voces
dois agradam a mesma pessoa - tem algo em comum. Por isso SIMILAR.

Eh o passo a mais no grafo: em vez de olhar so os vizinhos da pessoa,
olhe os vizinhos dos vizinhos.

VIZINHO eh outra palavra de grafo, e ela quer dizer exatamente quem esta
na sua lista. Entao o que voce procura aqui sao os vertices a DISTANCIA 2
de voce: nao os que voce alcanca com uma aresta, e sim os que voce alcanca
com duas.

    >>> similares(curtidas_exemplo, 'ana')
    ['elza', 'flavio']

Lembrando das regras adicionais: tirando ela mesma, tirando quem ela ja curtiu, e
sem repetir ninguem.
'''
def similares(curtidas, pessoa):
    pass


assert similares(curtidas_exemplo, 'ana') == ['elza', 'flavio'], f'a elza veio pelo breno e o flavio veio pela duda; voce devolveu {similares(curtidas_exemplo, "ana")}'
assert similares(curtidas_exemplo, 'caio') == [], f'o caio nao tem match, entao nao tem por onde achar um similar; voce devolveu {similares(curtidas_exemplo, "caio")}'
assert similares(curtidas_exemplo, 'duda') == ['breno'], f'o unico match da duda eh a ana, que curtiu o breno (e a propria duda, que nao conta); voce devolveu {similares(curtidas_exemplo, "duda")}'
print('Exercicio 5 (similares): OK')

print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== O menu =====
#
# Ja esta pronto - eh o seu app rodando em cima das funcoes que voce
# escreveu. Pra usar, descomente a ultima linha do arquivo.

def main():
    curtidas = curtidas_exemplo    # o app comeca com o pessoal do exemplo

    while True:
        print()
        print('=== TINDER ===')
        print(f'cadastrados: {sorted(curtidas.keys())}')
        print('1. Cadastrar uma pessoa')
        print('2. Curtir alguem')
        print('3. Ver o perfil de alguem')
        print('4. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            pessoa = input('  nome: ')
            cadastra(curtidas, pessoa)
            print(f'  {pessoa} entrou no app, sem ter curtido ninguem ainda')

        elif opcao == '2':
            quem = input('  quem curte: ')
            alvo = input('  curte quem: ')
            if quem not in curtidas.keys() or alvo not in curtidas.keys():
                print('  so da pra curtir entre pessoas cadastradas - veja a opcao 1')
            elif quem == alvo:
                print('  ninguem curte a si mesmo')
            else:
                curte(curtidas, quem, alvo)
                if eh_match(curtidas, quem, alvo):
                    print(f'  MATCH! {quem} e {alvo} se curtiram')
                else:
                    print(f'  curtida enviada. {alvo} nem fica sabendo')

        elif opcao == '3':
            pessoa = input('  de quem: ')
            if pessoa not in curtidas.keys():
                print(f'  {pessoa} nao esta cadastrada')
            else:
                print(f'  matches:      {matches(curtidas, pessoa)}')
                print(f'  te curtiram:  {pretendentes(curtidas, pessoa)}')
                print(f'  similares:    {similares(curtidas, pessoa)}')

        elif opcao == '4':
            break

        else:
            print('Opcao invalida')


# Pra rodar o app, descomente:
# main()


# ===== Depois desta aula: os mesmos exercicios num juiz online =====
#
# As seis funcoes que voce escreveu resolvem uma familia inteira de
# problemas do LeetCode: os que perguntam sobre GRAU num grafo dirigido -
# quem nao tem seta saindo, quem nao tem seta chegando, quantas chegam.
# Nenhum deles precisa percorrer o grafo. Falta uma peca so.
#
# A PECA QUE FALTA
#
# O juiz nao te entrega o dicionario pronto. Ele te entrega a LISTA DE
# ARESTAS, tipo [['ana', 'breno'], ['breno', 'elza']]. Virar dicionario eh
# um for em cima do que voce ja escreveu:
#
#     def monta_grafo(arestas):
#         curtidas = {}
#         for quem, alvo in arestas:
#             cadastra(curtidas, quem)
#             cadastra(curtidas, alvo)
#             curte(curtidas, quem, alvo)
#         return curtidas
#
# Os DOIS cadastra() sao obrigatorios. Sem o segundo, quem so aparece como
# ALVO nunca vira chave do dicionario - e ai desaparece do grafo. Eh a
# regra do flavio ("existe mesmo sem nenhuma seta saindo dele"), agora
# aplicada na hora de ler a entrada.
#
# Quando o problema NUMERA as pessoas (de 0 a n-1, ou de 1 a n), tem um
# passo antes do laco: cadastre todas elas primeiro, porque quem nao
# aparece em aresta nenhuma tambem conta.
#
#     for pessoa in range(n):        # ou range(1, n + 1)
#         cadastra(curtidas, pessoa)
#
# OS PROBLEMAS, do mais parecido com esta aula pro menos
#
#   LC 1436 - Destination City (facil)
#       As pessoas sao CIDADES com nome, e a seta eh "tem estrada pra".
#       A resposta eh a cidade sem estrada saindo dela - ou seja, o
#       flavio. Depois do monta_grafo, o problema inteiro eh achar a chave
#       cuja lista esta vazia. Comece por este.
#
#   LC 2924 - Find Champion II (facil)
#       n times, e a seta eh "eh mais forte que". O campeao eh quem
#       NINGUEM aponta - o contrario do flavio. Eh o pretendentes(): quem
#       tem a lista de pretendentes vazia. Se sobrar mais de um, nao ha
#       campeao.
#
#   LC 997 - Find the Town Judge (facil)
#       Aqui precisa das DUAS direcoes ao mesmo tempo: o juiz nao confia
#       em ninguem (a lista dele esta vazia) E todos os outros confiam
#       nele (ele tem n-1 pretendentes). Eh o matches() e o pretendentes()
#       trabalhando juntos. O n aqui vai ate 1000, e chamar pretendentes()
#       uma vez por pessoa passa folgado.
#
#   LC 1557 - Minimum Number of Vertices to Reach All Nodes (medio)
#       Devolva TODOS os vertices que ninguem aponta - eh o mesmo
#       pretendentes() do 2924, sem o "so um". A IDEIA eh a de hoje; o
#       TAMANHO nao eh. Nos tres problemas de cima o n vai ate 100 ou
#       1000; aqui vai ate 100 MIL, e eh so isso que muda.
#
#       E eh o bastante pra reprovar. O pretendentes() varre o dicionario
#       INTEIRO a cada chamada; chamar ele uma vez por vertice sao 100 mil
#       varreduras de 100 mil - da uns 15 minutos, e o juiz te da alguns
#       segundos. Nao ha nada de errado com a sua funcao: ela responde uma
#       pergunta por vez, e voce esta fazendo n perguntas.
#
#       O conserto nao troca a ideia, troca quantas vezes voce varre: UMA
#       varredura so, contando num dicionario quantas setas chegam em cada
#       pessoa; depois, quem ficou com zero eh a resposta. Nos mesmos 100
#       mil, isso roda em 0,05 segundo.
#
#       Esse dicionario de contagem tem nome - GRAU DE ENTRADA - e eh o
#       assunto da aula da grade de materias. Vale saber que ele existe: eh
#       o pulo que separa "escrevi certo" de "passou no juiz", e ele
#       reaparece em todo problema de grafo dirigido grande.
#
#   LC 2374 - Node With Highest Edge Score (medio)
#       Cada pessoa curte exatamente UMA outra, e a nota de alguem eh a
#       SOMA dos numeros de quem a curtiu. Duas diferencas: a entrada nao
#       eh lista de pares (edges[i] ja eh direto quem o i curtiu, entao o
#       monta_grafo muda um pouco), e nao basta contar - tem que somar num
#       dicionario. O n tambem vai ate 100 mil, entao vale o mesmo aviso do
#       1557: uma varredura so.
#
#
# COMO SUBMETER
#
# O LeetCode pede um METODO dentro de uma class Solution, e as funcoes
# daqui sao soltas. Cole as suas funcoes ACIMA da classe e chame elas de
# dentro do metodo - o nome do metodo eh o que o juiz mandar:
#
# Se o juiz fornecer
#
#     class Solution:
#         def destCity(self, paths):
#
# Voce escreve algo como
#
#     class Solution:
#         def destCity(self, paths):
#             curtidas = monta_grafo(paths)
#             for cidade in curtidas.keys():
#                 if curtidas[cidade] == []:
#                     return cidade
#
# Pode ignorar o self, o que o juiz fornecer vai vir dentro das outras variaveis
