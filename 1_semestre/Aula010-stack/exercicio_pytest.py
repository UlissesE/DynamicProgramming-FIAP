
# === Boilerplate (pode ignorar) ===
# Esse código só serve para os testes. Você não precisa ler ele. Pode ignorar
# mas não delete
import hashlib
def verifica(valor, codigo):
    assert hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo, f'Valor errado: voce colocou {valor}'

try:
    import gabarito_NAO_MANDAR as _gab
    _GAB = {k: v for k, v in vars(_gab).items() if not k.startswith('_')}
except ImportError:
    _GAB = {}

def _aplica(nome):
    if nome in _GAB:
        globals()[nome] = _GAB[nome]
# fim do boilerplate


'''
EXPLICACAO

Uma pilha é uma estrutura de dados onde o último elemento inserido
é o primeiro a sair (LIFO - Last In, First Out).
Pense numa pilha de pratos: você sempre coloca e tira pratos pelo topo.

Em Python, podemos usar uma lista como pilha:
    - Para empilhar (push): usamos lista.append(x)
    - Para desempilhar (pop): usamos lista.pop()
    - Para ver o topo: usamos lista[-1]

Por exemplo:
    > pilha = []
    > pilha.append(10)   # pilha = [10]
    > pilha.append(20)   # pilha = [10, 20]
    > pilha.append(30)   # pilha = [10, 20, 30]
    > pilha[-1]          # 30 (o topo)
    > pilha.pop()        # remove e retorna 30, pilha = [10, 20]
    > pilha[-1]          # 20 (novo topo)
'''

# ===== FASE 1 - Entendendo a pilha =====

'''
EXERCICIO

Considere uma pilha que começa vazia. Fazemos as seguintes operacoes:
    append(5), append(10), append(3)

1) Qual o valor no topo da pilha?
'''
topo_1 = 3

'''
2) Agora, fazemos pop(). Qual o novo topo?
'''
topo_2 = 10

'''
3) Fazemos append(7). Qual o topo agora?
'''
topo_3 = 7

'''
4) Fazemos pop(), pop(). Qual o topo agora?
'''
topo_4 = 5

_aplica('topo_1'); _aplica('topo_2'); _aplica('topo_3'); _aplica('topo_4') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

verifica(topo_1, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474')
verifica(topo_2, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c')
verifica(topo_3, '56929c1607626a1edbdaafb9c7f10c247e54fcbb20f1e3260f783011')
verifica(topo_4, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17')
print('Exercicio topo: OK')


'''
EXERCICIO

Faca uma funcao empilha(pilha, x) que adiciona x no topo da pilha.
A funcao nao precisa retornar nada, basta modificar a lista.

Dica: em Python, para adicionar um elemento no fim de uma lista, usamos
o metodo .append(x). Por exemplo:

    >>> lista = [1, 2, 3]
    >>> lista.append(99)
    >>> lista
    [1, 2, 3, 99]
    >>> lista.append(100)
    >>> lista
    [1, 2, 3, 99, 100]

Como queremos que a sua funcao se comporte:

    >>> p = [10, 20]
    >>> empilha(p, 30)
    >>> p
    [10, 20, 30]
'''
def empilha(pilha, x):
    pilha.append(x)
    
_aplica('empilha') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

p = []
empilha(p, 10)
assert p == [10], f'Apos empilha([], 10), esperado [10], obteve {p}'
empilha(p, 20)
assert p == [10, 20], f'Apos empilha([10], 20), esperado [10, 20], obteve {p}'
empilha(p, 5)
assert p == [10, 20, 5], f'Apos empilha([10,20], 5), esperado [10, 20, 5], obteve {p}'
print('Exercicio empilha: OK')


'''
EXERCICIO

Faca uma funcao desempilha(pilha) que remove e retorna o elemento do topo.

Dica: em Python, o metodo .pop() de uma lista remove o ultimo elemento
E ja retorna esse elemento. Por exemplo:

    >>> lista = [10, 20, 30]
    >>> x = lista.pop()
    >>> x
    30
    >>> lista
    [10, 20]
    >>> y = lista.pop()
    >>> y
    20
    >>> lista
    [10]

Como queremos que a sua funcao se comporte:

    >>> p = [10, 20, 30]
    >>> desempilha(p)
    30
    >>> p
    [10, 20]
'''
def desempilha(pilha):
    return pilha.pop()
_aplica('desempilha') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

p = [10, 20, 30]
assert desempilha(p) == 30, 'desempilha([10,20,30]) deveria retornar 30'
assert p == [10, 20], f'Apos desempilha, pilha deveria ser [10, 20], obteve {p}'
assert desempilha(p) == 20, 'desempilha([10,20]) deveria retornar 20'
assert p == [10], f'Apos desempilha, pilha deveria ser [10], obteve {p}'
print('Exercicio desempilha: OK')


'''
EXERCICIO

Faca uma funcao topo(pilha) que retorna o elemento do topo sem remover.

Dica: em Python, podemos acessar o ultimo elemento de uma lista usando
o indice -1 (negativo). Isso NAO remove o elemento, so le. Por exemplo:

    >>> lista = [10, 20, 30]
    >>> lista[-1]
    30
    >>> lista
    [10, 20, 30]
    >>> lista[-2]
    20

Como queremos que a sua funcao se comporte:

    >>> p = [10, 20, 30]
    >>> topo(p)
    30
    >>> p
    [10, 20, 30]
'''
def topo(pilha):
    return pilha[-1]
_aplica('topo') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

p = [10, 20, 30]
assert topo(p) == 30, 'topo([10,20,30]) deveria retornar 30'
assert p == [10, 20, 30], 'topo nao deveria modificar a pilha'
assert topo([42]) == 42, 'topo([42]) deveria retornar 42'
print('Exercicio topo: OK')


# ===== FASE 2 - Interpretando as operacoes =====

'''
EXPLICACAO

Agora vamos aprender a interpretar operacoes em formato de string.

No nosso problema, cada operacao e uma string:
    "1 x"  -> empilha o numero x
    "2"    -> desempilha (remove o topo)
    "3"    -> consulta o maior valor da pilha

Para extrair o tipo da operacao, podemos usar split:
    > op = "1 42"
    > partes = op.split(" ")
    > partes
    ['1', '42']
    > partes[0]
    '1'
    > int(partes[1])
    42

    > op = "2"
    > partes = op.split(" ")
    > partes
    ['2']
    > partes[0]
    '2'
'''

'''
EXERCICIO

Faca uma funcao tipo_da_operacao(operacao) que recebe uma string
e retorna o tipo como inteiro (1, 2 ou 3).

    >>> tipo_da_operacao("1 42")
    1
    >>> tipo_da_operacao("2")
    2
    >>> tipo_da_operacao("3")
    3
'''
def tipo_da_operacao(operacao):
    op = operacao.split(" ")
    return int(op[0])
_aplica('tipo_da_operacao') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# primeiro: o valor esta certo (aceitando int ou string)
assert tipo_da_operacao("1 42") == 1 or tipo_da_operacao("1 42") == "1", f'tipo_da_operacao("1 42") deveria ser 1, voce retornou {tipo_da_operacao("1 42")!r}'
assert tipo_da_operacao("1 999") == 1 or tipo_da_operacao("1 999") == "1", f'tipo_da_operacao("1 999") deveria ser 1, voce retornou {tipo_da_operacao("1 999")!r}'
assert tipo_da_operacao("2") == 2 or tipo_da_operacao("2") == "2", f'tipo_da_operacao("2") deveria ser 2, voce retornou {tipo_da_operacao("2")!r}'
assert tipo_da_operacao("3") == 3 or tipo_da_operacao("3") == "3", f'tipo_da_operacao("3") deveria ser 3, voce retornou {tipo_da_operacao("3")!r}'
# depois: precisa ser inteiro, nao string
assert isinstance(tipo_da_operacao("1 42"), int), f'tipo_da_operacao deveria retornar um inteiro, mas voce retornou uma string ({tipo_da_operacao("1 42")!r}). Use int(...) para converter.'
print('Exercicio tipo_da_operacao: OK')


'''
EXERCICIO

Faca uma funcao valor_a_empilhar(operacao) que recebe uma string
do tipo 1 (por exemplo "1 42") e retorna o valor como inteiro.

    >>> valor_a_empilhar("1 42")
    42
    >>> valor_a_empilhar("1 100")
    100
'''
def valor_a_empilhar(operacao):
    op = operacao.split(" ")
    return int(op[1])
    
_aplica('valor_a_empilhar') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# primeiro: o valor esta certo (aceitando int ou string)
assert valor_a_empilhar("1 42") == 42 or valor_a_empilhar("1 42") == "42", f'valor_a_empilhar("1 42") deveria ser 42, voce retornou {valor_a_empilhar("1 42")!r}'
assert valor_a_empilhar("1 100") == 100 or valor_a_empilhar("1 100") == "100", f'valor_a_empilhar("1 100") deveria ser 100, voce retornou {valor_a_empilhar("1 100")!r}'
assert valor_a_empilhar("1 999999") == 999999 or valor_a_empilhar("1 999999") == "999999", f'valor_a_empilhar("1 999999") deveria ser 999999, voce retornou {valor_a_empilhar("1 999999")!r}'
# depois: precisa ser inteiro, nao string
assert isinstance(valor_a_empilhar("1 42"), int), f'valor_a_empilhar deveria retornar um inteiro, mas voce retornou uma string ({valor_a_empilhar("1 42")!r}). Use int(...) para converter.'
print('Exercicio valor_a_empilhar: OK')


# ===== FASE 3 - Juntando pilha + operacoes =====

'''
EXERCICIO

Faca uma funcao executa_operacao(pilha, operacao) que recebe uma pilha
e uma string de operacao, e executa a operacao na pilha.

Se a operacao for do tipo 1, empilha o valor.
Se a operacao for do tipo 2, desempilha.
Se a operacao for do tipo 3, retorna o maior valor da pilha (sem remover nada).
Para os tipos 1 e 2, nao precisa retornar nada.

Dica: para achar o maior valor de uma lista, use a funcao max()

    >>> p = [10, 20]
    >>> executa_operacao(p, "1 30")
    >>> p
    [10, 20, 30]
    >>> executa_operacao(p, "3")
    30
    >>> executa_operacao(p, "2")
    >>> p
    [10, 20]
'''
def executa_operacao(pilha, operacao):
    
    op_tipo = tipo_da_operacao(operacao)

    match op_tipo:
        case 1:
            empilha(pilha, valor_a_empilhar(operacao))
        case 2:
            desempilha(pilha)
        case 3:
            return max(pilha)
        case _:
            pass

_aplica('executa_operacao') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

p = []
executa_operacao(p, "1 10")
assert p == [10], f'Apos push 10, esperado [10], obteve {p}'
executa_operacao(p, "1 20")
assert p == [10, 20], f'Apos push 20, esperado [10, 20], obteve {p}'
assert executa_operacao(p, "3") == 20, 'max de [10, 20] deveria ser 20'
assert p == [10, 20], 'operacao 3 nao deveria modificar a pilha'
executa_operacao(p, "2")
assert p == [10], f'Apos pop, esperado [10], obteve {p}'
p2 = [5, 100, 3]
assert executa_operacao(p2, "3") == 100, 'max de [5, 100, 3] deveria ser 100'
print('Exercicio executa_operacao: OK')


'''
EXERCICIO

Agora vamos juntar tudo!

Faca uma funcao processa_operacoes(operacoes) que recebe uma lista de
strings de operacoes e retorna uma lista com os resultados de todas
as consultas do tipo 3.

    >>> processa_operacoes(["1 10", "1 20", "3", "2", "3"])
    [20, 10]

Porque?
    "1 10"  -> empilha 10. Pilha: [10]
    "1 20"  -> empilha 20. Pilha: [10, 20]
    "3"     -> maior = 20
    "2"     -> desempilha. Pilha: [10]
    "3"     -> maior = 10
'''
def processa_operacoes(operacoes):
    pilha = []
    maximos = []
    for operacao in operacoes:
        res = executa_operacao(pilha, operacao)
        
        if res != None:
            maximos.append(res)

    return maximos

    
    

_aplica('processa_operacoes') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

assert processa_operacoes(["1 10", "1 20", "3", "2", "3"]) == [20, 10]
assert processa_operacoes(["1 5", "1 3", "1 8", "3", "2", "3"]) == [8, 5]
assert processa_operacoes(["1 100", "3", "1 200", "3", "2", "3"]) == [100, 200, 100]
print('Exercicio processa_operacoes: OK')


# ===== FASE 4 - Otimizando com pilha auxiliar =====

'''
EXPLICACAO

A solucao acima funciona, mas tem um problema de eficiencia.

Cada vez que fazemos uma consulta do tipo 3, chamamos max(pilha), que
precisa percorrer TODA a pilha para achar o maior. Se a pilha tem n
elementos, isso custa O(n).

Se tivermos muitas consultas do tipo 3, isso pode ficar lento.

Ideia: e se mantivessemos uma pilha auxiliar que guarda o maior valor
em cada nivel?

Exemplo:
    empilha 10  -> pilha: [10],         maximos: [10]
    empilha 5   -> pilha: [10, 5],      maximos: [10, 10]
    empilha 15  -> pilha: [10, 5, 15],  maximos: [10, 10, 15]
    max?        -> maximos[-1] = 15     (resposta instantanea!)
    pop         -> pilha: [10, 5],      maximos: [10, 10]
    max?        -> maximos[-1] = 10     (resposta instantanea!)

Perceba: na pilha de maximos, cada posicao guarda o maior valor
entre todos os elementos da pilha principal do comeco ate aquela posicao.

Quando empilhamos x, o novo maximo e max(x, maximos[-1]).
Quando desempilhamos, basta desempilhar de ambas as pilhas.
'''

'''
EXERCICIO

Considere a seguinte sequencia de operacoes. Preencha como ficam as
pilhas apos cada operacao.

    empilha 3   -> pilha: [3],          maximos: [3]
    empilha 7   -> pilha: [3, 7],       maximos: [3, 7]
    empilha 2   -> pilha: [3, 7, 2],    maximos: [3, 7, ?]

1) Qual o valor de ? na pilha de maximos?
'''
max_apos_empilha_2 = 7

'''
    Continuando...
    empilha 8   -> pilha: [3, 7, 2, 8], maximos: [3, 7, 7, ?]

2) Qual o valor de ?
'''
max_apos_empilha_8 = 8

'''
    pop         -> pilha: [3, 7, 2],    maximos: [3, 7, ?]

3) Qual o valor de ?
'''
max_apos_pop = 7

_aplica('max_apos_empilha_2'); _aplica('max_apos_empilha_8'); _aplica('max_apos_pop') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
verifica(max_apos_empilha_2, '56929c1607626a1edbdaafb9c7f10c247e54fcbb20f1e3260f783011')
verifica(max_apos_empilha_8, '525ab75c928c6fac98a0f62e4da5316b7247ccd704c967ef9142925c')
verifica(max_apos_pop, '56929c1607626a1edbdaafb9c7f10c247e54fcbb20f1e3260f783011')
print('Exercicio pilha de maximos: OK')


'''
EXERCICIO

Faca uma funcao empilha_com_max(pilha, maximos, x) que:
    - empilha x na pilha
    - empilha o novo maximo na pilha de maximos

Dica: o novo maximo e o maior entre x e o maximo atual (maximos[-1]).
Cuidado: se maximos estiver vazia, o novo maximo e simplesmente x.

    >>> p = [10]
    >>> m = [10]
    >>> empilha_com_max(p, m, 5)
    >>> p
    [10, 5]
    >>> m
    [10, 10]
    >>> empilha_com_max(p, m, 20)
    >>> p
    [10, 5, 20]
    >>> m
    [10, 10, 20]
'''
def empilha_com_max(pilha, maximos, x):
    pilha.append(x)

    if maximos == []:
        maximos.append(x)

    if x > maximos[-1]:
        maximos.append(x)

_aplica('empilha_com_max') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

p, m = [], []
empilha_com_max(p, m, 10)
assert p == [10] and m == [10], f'Apos empilha_com_max([], [], 10): p={p}, m={m}'
empilha_com_max(p, m, 5)
assert p == [10, 5] and m == [10, 10], f'Apos empilha 5: p={p}, m={m}'
empilha_com_max(p, m, 20)
assert p == [10, 5, 20] and m == [10, 10, 20], f'Apos empilha 20: p={p}, m={m}'
empilha_com_max(p, m, 15)
assert p == [10, 5, 20, 15] and m == [10, 10, 20, 20], f'Apos empilha 15: p={p}, m={m}'
print('Exercicio empilha_com_max: OK')


'''
EXERCICIO

Faca uma funcao desempilha_com_max(pilha, maximos) que:
    - desempilha da pilha
    - desempilha da pilha de maximos
    - retorna o valor desempilhado da pilha

    >>> p = [10, 5, 20]
    >>> m = [10, 10, 20]
    >>> desempilha_com_max(p, m)
    20
    >>> p
    [10, 5]
    >>> m
    [10, 10]
'''
def desempilha_com_max(pilha, maximos):
    maximos.pop()
    return pilha.pop()


_aplica('desempilha_com_max') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

p, m = [10, 5, 20], [10, 10, 20]
assert desempilha_com_max(p, m) == 20, 'desempilha_com_max deveria retornar 20'
assert p == [10, 5] and m == [10, 10], f'Apos desempilha: p={p}, m={m}'
assert desempilha_com_max(p, m) == 5, 'desempilha_com_max deveria retornar 5'
assert p == [10] and m == [10], f'Apos desempilha: p={p}, m={m}'
print('Exercicio desempilha_com_max: OK')


'''
EXERCICIO

Agora, junte tudo para fazer a solucao eficiente!

Faca uma funcao getMax(operacoes) que recebe uma lista de strings
de operacoes e retorna uma lista com os resultados de todas as
consultas do tipo 3.

Use a tecnica da pilha auxiliar de maximos para que cada operacao
custe O(1).

    >>> getMax(["1 10", "1 15", "1 13", "3", "3", "2", "3", "2", "3"])
    [15, 15, 15, 10]
'''
def getMax(operacoes):
    pass
_aplica('getMax') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

assert getMax(["1 10", "1 15", "1 13", "3", "3", "2", "3", "2", "3"]) == [15, 15, 15, 10]
assert getMax(["1 5", "1 3", "1 8", "3", "2", "3", "2", "3"]) == [8, 5, 5]
assert getMax(["1 1", "1 2", "1 3", "1 4", "3", "2", "2", "2", "3"]) == [4, 1]
assert getMax(["1 100", "3", "1 50", "3", "1 200", "3", "2", "3", "2", "3"]) == [100, 100, 200, 100, 100]
print('Exercicio getMax: OK')

print('\n=== PARABENS! Todos os exercicios completos! ===')
