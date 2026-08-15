
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


'''
EXPLICACAO

Terceira lista de RECURSAO. Tema: funcoes NUMERICAS — entrada e
saida sao numeros, nao listas. O padrao do caso base + terceirizacao
continua igual, so muda a "forma" de encolher a entrada.

Voce vai conhecer tambem uma novidade importante: a primeira funcao
com RECURSAO MULTIPLA (mais de uma chamada a si mesma por passo).
'''


# ===== FASE 1 - potencia(base, expoente) =====

'''
EXPLICACAO

`potencia(base, n)` retorna base elevado a n. Vamos limitar a
expoentes inteiros >= 0.

    potencia(2, 5)  = 2*2*2*2*2 = 32
    potencia(2, 0)  = 1
    potencia(10, 3) = 1000

Caso base:    potencia(base, 0) = 1
Terceirizacao: potencia(base, n) = base * potencia(base, n - 1)

Repare a estrutura tipo "fatorial": a cada passo, encolhe o expoente
em 1, multiplica pela base.
'''

pot_2_de_0 = 1   # caso base, ja preenchido

'''
EXERCICIO - terceirizacao em cadeia

Use o `pot_2_de_0` em uma EXPRESSAO Python pra calcular `pot_2_de_1`,
e assim por diante.

    pot_2_de_1 = pot_2_de_0 * 2
    pot_2_de_2 = pot_2_de_1 * 2
    pot_2_de_3 = pot_2_de_2 * 2

Cada variavel reusa a anterior — exatamente o que `potencia(2, n)`
vai fazer.
'''
pot_2_de_1 = 2
pot_2_de_2 = 4
pot_2_de_3 = 8

'''
EXERCICIO

Imagine que voce ja sabe que `pot_2_de_9 = 512`. Use uma EXPRESSAO
pra calcular `pot_2_de_10`.
'''
pot_2_de_9 = 512
pot_2_de_10 = 1024

assert verifica(pot_2_de_1, '58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9'), 'pot_2_de_1 incorreta'
assert verifica(pot_2_de_2, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'pot_2_de_2 incorreta'
assert verifica(pot_2_de_3, '525ab75c928c6fac98a0f62e4da5316b7247ccd704c967ef9142925c'), 'pot_2_de_3 incorreta'
assert verifica(pot_2_de_10, '28f7ea4d1696b0ee0e7fd54668161ff658c4a50714053421c5baa609'), 'pot_2_de_10 incorreta'
print('Exercicio potencia terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `potencia(base, expoente)`. Voce pode
assumir que `expoente` eh um inteiro >= 0.

DICA: caso base — expoente == 0 retorna 1. Terceirizacao — retorna
`base * potencia(base, expoente - 1)`.

    >>> potencia(2, 0)
    1
    >>> potencia(2, 5)
    32
    >>> potencia(10, 3)
    1000
'''
def potencia(base, expoente):
    if expoente == 1: return base
    if expoente == 0: return 1
    pot = potencia(base, expoente-1)
    return pot*base

# Bloco 1: caso base.
assert potencia(2, 0) == 1, 'potencia(2, 0) (caso base)'
assert potencia(10, 0) == 1, 'potencia(10, 0) (caso base — qualquer base elevada a 0 eh 1)'
assert potencia(7, 0) == 1, 'potencia(7, 0) (caso base)'
print('Exercicio potencia caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert potencia(2, 1) == 2
assert potencia(2, 5) == 32
assert potencia(2, 10) == 1024
assert potencia(3, 4) == 81
assert potencia(10, 3) == 1000
assert potencia(5, 2) == 25

sys.setrecursionlimit(50)
try:
    potencia(2, 100)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao potencia e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio potencia caso recursivo: OK')


# ===== FASE 2 - fibonacci(n) =====

'''
EXPLICACAO  - NOVIDADE: RECURSAO MULTIPLA

A sequencia de FIBONACCI comeca com 0 e 1; cada termo seguinte eh a
soma dos DOIS anteriores:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
          ^
          eh 1 porque os dois anteriores eram 0 e 1

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
             ^
             eh 2 porque os dois anteriores eram 1 e 1

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
                              ^
                              eh 21 porque os dois anteriores eram 13 e 8, 21=8+13


    A funcao que voce vai escrever, `fibonacci(n)` 
    retorna o n-esimo termo 

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(5) = 5     
    fibonacci(8) = 21

    (repare que, como em listas, o primeiro valor esta na "posicao" 0.
    Essa escolha eh arbitraria, mas precisa ser respeitada)

Caso base: fibonacci(0) = 0  e  fibonacci(1) = 1
Terceirizacao: fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

NOVIDADE: agora a recursao TERCEIRIZA DUAS VEZES por passo — pra
calcular fibonacci(5), precisamos de fibonacci(4) E fibonacci(3).
Cada um desses por sua vez precisa de DOIS predecessores. Isso e
chamado de RECURSAO MULTIPLA (ou "recursao em arvore").

Tambem aparece: agora temos DOIS casos base, nao um. Isso e
necessario porque a terceirizacao consulta n-1 E n-2 — se so
houvesse fibonacci(0) como caso base, alguem ia tentar chamar
fibonnacci(1), e o fibonacci(1) ia acabar tentando chamar o fibonacci(-1)

Isso daria um problema -- provavelmente um 'loop infinito'
'''

fib_0 = 0   # caso base, ja preenchido
fib_1 = 1   # caso base, ja preenchido

'''
EXERCICIO - terceirizacao em cadeia (com DOIS predecessores)

Use os dois caso base pra calcular o resto, sempre somando os DOIS
anteriores.

    fib_2 = fib_0 + fib_1
    fib_3 = fib_1 + fib_2
    fib_4 = fib_2 + fib_3
    ...

Use EXPRESSOES Python — cada variavel reusa as anteriores. Repare
que aqui voce precisa CARREGAR a memoria dos dois ultimos a cada
passo. A funcao recursiva fara o mesmo, terceirizando duas vezes.
'''
fib_2 = fib_0 + fib_1
fib_3 = fib_1 + fib_2
fib_4 = fib_2 + fib_3
fib_5 = fib_3 + fib_4
fib_6 = fib_4 + fib_5

assert verifica(fib_2, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'fib_2 incorreta'
assert verifica(fib_3, '58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9'), 'fib_3 incorreta'
assert verifica(fib_4, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'fib_4 incorreta'
assert verifica(fib_5, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'fib_5 incorreta'
assert verifica(fib_6, '525ab75c928c6fac98a0f62e4da5316b7247ccd704c967ef9142925c'), 'fib_6 incorreta'
print('Exercicio fibonacci terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `fibonacci(n)`. Voce pode assumir que
`n` eh um inteiro >= 0.

DICA: voce precisa de DOIS casos base — n == 0 retorna 0, n == 1
retorna 1. Terceirizacao — retorna `fibonacci(n-1) + fibonacci(n-2)`.

ATENCAO: como a funcao se chama DUAS vezes por passo, a versao
que estamos construindo fica BEM lenta pra n grande (n = 35 ja demora
varios segundos, n = 40 leva minutos). Os testes abaixo so chamam
ate n = 25.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
'''

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    a = fibonacci(n-1) + fibonacci(n-2)
    return a

# respostas = {0:0, 1:1}

# def fibonacci(n):
#     if n in respostas.keys():
#         return respostas[n]

#     f_a = fibonacci(n-1)
#     f_b = fibonacci(n-2)
#     respostas[n] = f_a + f_b

#     return f_a + f_b

# Bloco 1: casos base.
assert fibonacci(0) == 0, 'fibonacci(0) (caso base)'
assert fibonacci(1) == 1, 'fibonacci(1) (caso base)'
print('Exercicio fibonacci casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(10) == 55
assert fibonacci(15) == 610
assert fibonacci(20) == 6765

# Teste de recursividade. 
sys.setrecursionlimit(30)
try:
    fibonacci(40)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao fibonacci e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio fibonacci caso recursivo: OK')


# ===== FASE 3 - soma_digitos(n) =====

'''
EXPLICACAO

`soma_digitos(n)` soma todos os digitos de n.

    soma_digitos(7)    = 7
    soma_digitos(123)  = 1 + 2 + 3 = 6
    soma_digitos(9999) = 9+9+9+9 = 9*4 = 36

Caso base: n < 10 (so um digito) retorna o proprio n.
Terceirizacao: Precisamos separar o menor digito do resto
Por exemplo, para 123, precisamos separar em 12 e 3

OPERADORES Python que voce vai usar:
    n % 10    # o RESTO da divisao por 10 — eh o ULTIMO digito
    n // 10   # divisao INTEIRA por 10 — corta o ultimo digito

    >>> 123 % 10
    3
    >>> 123 // 10
    12

'''

numero_para_soma_digitos = 123

'''
EXERCICIO

Considere `numero_para_soma_digitos` = 123.

1) Qual o ULTIMO digito? (use uma EXPRESSAO: `numero_para_soma_digitos % 10`)
'''
ultimo_digito = numero_para_soma_digitos % 10

'''
2) Qual o NUMERO SEM O ULTIMO digito? (use `numero_para_soma_digitos // 10`)
'''
numero_sem_ultimo = numero_para_soma_digitos // 10

'''
3) Qual a `soma_digitos` do numero sem o ultimo digito (12)?
   (calcule a mao: 1 + 2 -- estamos imaginando que terceirizamos esse problema)
'''
soma_digitos_dos_demais = 3

'''
4) Junte: a soma total dos digitos eh o ultimo digito mais a soma
   dos demais. Use uma EXPRESSAO:

       ultimo_digito + soma_digitos_dos_demais
'''
soma_digitos_total = ultimo_digito + soma_digitos_dos_demais

assert verifica(ultimo_digito, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'ultimo_digito incorreta'
assert verifica(numero_sem_ultimo, '3c794f0c67bd561ce841fc6a5999bf0df298a0f0ae3487efda9d0ef4'), 'numero_sem_ultimo incorreta'
assert verifica(soma_digitos_dos_demais, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'soma_digitos_dos_demais incorreta'
assert verifica(soma_digitos_total, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'soma_digitos_total incorreta'
print('Exercicio soma_digitos terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `soma_digitos(n)`. Voce pode assumir
que n eh um inteiro >= 0.

DICA: caso base — se n < 10, retorna n. Terceirizacao — retorna
`(n % 10) + soma_digitos(n // 10)`.

    >>> soma_digitos(7)
    7
    >>> soma_digitos(123)
    6
    >>> soma_digitos(9999)
    36
'''
def soma_digitos(n):
    if n < 10: return n
    a = (n % 10) + soma_digitos(n // 10)
    return a

# Bloco 1: caso base.
assert soma_digitos(0) == 0, 'soma_digitos(0) (caso base)'
assert soma_digitos(5) == 5, 'soma_digitos(5) (caso base — so um digito)'
assert soma_digitos(9) == 9, 'soma_digitos(9) (caso base)'
print('Exercicio soma_digitos caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert soma_digitos(10) == 1
assert soma_digitos(123) == 6
assert soma_digitos(456) == 15
assert soma_digitos(1000) == 1
assert soma_digitos(9999) == 36
assert soma_digitos(11111) == 5

sys.setrecursionlimit(50)
try:
    soma_digitos(10 ** 100)   # 101 digitos — bem mais que 50 de recursao
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao soma_digitos e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio soma_digitos caso recursivo: OK')


# ===== FASE 4 - mdc(a, b): construcao em 3 partes =====

'''
EXPLICACAO

O MDC (Maximo Divisor Comum) entre dois numeros eh o maior numero
que divide ambos sem deixar resto.

    mdc(12, 18) = 6      (6 divide 12 e 18; nenhum numero maior divide ambos)
    mdc(48, 36) = 12
    mdc(17, 5)  = 1      (numeros coprimos)

Vamos construir essa funcao em TRES partes, do simples ao rapido:

    Parte 1: `mdc_lento(a, b)` — ITERATIVO (sem recursao), com um for.
             Forca bruta: testa todos os divisores possiveis.

    Parte 2: `mdc_subtracao(a, b)` — RECURSIVO usando subtracao.
             Aproveita uma identidade matematica bonita.

    Parte 3: `mdc(a, b)` — RECURSIVO usando o operador `%`. Eh o
             algoritmo classico de Euclides, MUITO rapido.
'''


# ----- PARTE 1: mdc_lento (iterativo, com for) -----

'''
EXPLICACAO

Forca bruta: pra achar o maior divisor comum, basta testar TODOS os
candidatos de 1 ate min(a, b) e pegar o maior que divide os dois.

Como testar se i divide a sem deixar resto?
    a % i == 0   <- o resto da divisao eh zero, entao i divide a.

(`%` voce ja conhece da Fase 3.)

Algoritmo:
    melhor = 1
    pra cada i de 1 ate min(a, b):     #para cada possivel divisor
        se a % i == 0 E b % i == 0:    #se ele divide o a com resto zero (a%i == 0) 
                                        e a mesma coisa com o b
            melhor = i                 #salve ele
    retorna melhor

Nesse algoritmo a faixa dos possiveis divisores vai de 1 ate min(a,b)
Ou seja, se a < b, de 1 ate a. O que faz sentido. Se a < b, entao com
certeza numeros maiores que a nao servem!

Como `i` vai crescendo, sempre que achamos um divisor comum,
sobrescrevemos `melhor`. No fim, `melhor` tem o MAIOR.
'''

'''
EXERCICIO

Implemente `mdc_lento(a, b)` SEM recursao, usando um for.

DICA: comece com `melhor = 1`. Pra
cada i, teste se `a % i == 0` e `b % i == 0`; se sim, faca
`melhor = i`. No fim, retorne melhor.

    >>> mdc_lento(12, 18)
    6
    >>> mdc_lento(17, 5)
    1
'''
def mdc_lento(a, b):
    menor = a if a < b else b
    div = 1
    
    for i in range(2, menor+1):
        if a % i == 0 and b % i == 0:
            div = i

    return div

assert mdc_lento(12, 18) == 6, 'mdc_lento(12, 18) = 6'
assert mdc_lento(48, 36) == 12, 'mdc_lento(48, 36) = 12'
assert mdc_lento(17, 5) == 1, 'mdc_lento(17, 5) = 1 (coprimos)'
assert mdc_lento(100, 75) == 25, 'mdc_lento(100, 75) = 25'
assert mdc_lento(1, 1) == 1
assert mdc_lento(7, 14) == 7, 'um divide o outro'
print('Exercicio mdc_lento (iterativo): OK')

'''
OBSERVACAO

`mdc_lento` funciona, mas eh LENTO: pra entrada grande (digamos
mdc_lento(1000000, 999999)), o for roda quase um milhao de vezes.
Por isso o nome — "lento". Da pra fazer MUITO melhor com recursao.
'''


# ----- PARTE 2: mdc_subtracao (recursivo com subtracao) -----

'''
EXPLICACAO - a identidade matematica

Tem uma observacao SIMPLES que muda tudo:

    Se um numero d divide a E divide b, entao d tambem divide
    a diferenca (a - b).

Por que? Imagine d = 6, a = 18, b = 12.
    a / d = 18 / 6 = 3   (sao 3 grupinhos de 6 em 18)
    b / d = 12 / 6 = 2   (sao 2 grupinhos de 6 em 12)
    a - b = 6            (sobrou 1 grupinho de 6)
    (a - b) / d = 1      (que tambem eh divisivel por 6!)

A consequencia eh poderosa: qualquer divisor comum de a e b tambem
eh divisor comum de (a - b) e b. E vice-versa.

Em particular, o MAIOR divisor comum eh o mesmo dos dois pares:

    mdc(a, b) = mdc(a - b, b)     quando a > b
    mdc(a, b) = mdc(a, b - a)     quando b > a
    mdc(a, a) = a                  (CASO BASE — divide ele mesmo)

Olhando mdc(18, 12) passo a passo:
    mdc(18, 12)              # a > b: subtrai b de a
        = mdc(6, 12)         # b > a: subtrai a de b
        = mdc(6, 6)          # a == b: CASO BASE
        = 6

    De fato, achamos um divisor comum. Um numero que divide tanto o 18 quanto o 12.

    A questão que faltaria responder: será que é o maior?
    Mas não vamos tentar argumentar sobre isso hoje.
'''

'''
EXERCICIO

Implemente a funcao recursiva `mdc_subtracao(a, b)`. Voce pode
assumir a, b inteiros > 0.

DICA: caso base — se `a == b`, retorna `a`. Caso recursivo:
    - se a > b, retorna `mdc_subtracao(a - b, b)`
    - se b > a, retorna `mdc_subtracao(a, b - a)`

    >>> mdc_subtracao(6, 6)
    6
    >>> mdc_subtracao(18, 12)
    6
    >>> mdc_subtracao(17, 5)
    1
'''
def mdc_subtracao(a, b):
    pass

# Bloco 1: caso base.
assert mdc_subtracao(7, 7) == 7, 'mdc_subtracao(7, 7) (caso base)'
assert mdc_subtracao(1, 1) == 1, 'mdc_subtracao(1, 1) (caso base)'
assert mdc_subtracao(100, 100) == 100, 'mdc_subtracao(100, 100) (caso base)'
print('Exercicio mdc_subtracao caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert mdc_subtracao(18, 12) == 6
assert mdc_subtracao(12, 18) == 6, 'ordem dos argumentos nao muda o resultado'
assert mdc_subtracao(48, 36) == 12
assert mdc_subtracao(17, 5) == 1, 'coprimos'
assert mdc_subtracao(100, 75) == 25

# Teste de recursividade. mdc_subtracao(100, 1) precisa subtrair 1
# noventa e nove vezes — depth = 99. Estoura recursionlimit(50).
sys.setrecursionlimit(50)
try:
    mdc_subtracao(100, 1)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao mdc_subtracao e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio mdc_subtracao caso recursivo: OK')

'''
OBSERVACAO

`mdc_subtracao` ja eh um avanco — recursivo e elegante. Mas tem um
problema: quando a eh MUITO maior que b, ele faz uma chuva de
subtracoes do mesmo b ate sobrar pouco.

Exemplo: mdc_subtracao(1000, 3). Vai subtrair 3 do 1000 uma, duas,
tres, ... ate sobrar algo menor que 3. Sao MUITAS subtracoes.

Existe um jeito de "pular" todas essas subtracoes de uma vez so —
e eh isso que a parte 3 vai fazer.
'''


# ----- PARTE 3: mdc com `%` (Euclides) -----

'''
EXPLICACAO - revisitando o `%`

Voce ja viu `%` na Fase 3, mas agora vamos olhar com outro angulo:
o operador `%` PULA varias subtracoes de uma vez.

Pense em `a % b` como: "subtraia b de a o maximo de vezes possivel
ate que sobre menos que b. O que sobra eh a % b."

Exemplos:
    14 % 5 = 4
        14 - 5 = 9
        9 - 5 = 4    <- 4 < 5, paro. Resto = 4.
        Foram 2 subtracoes em um unico %.

    100 % 30 = 10
        100 - 30 = 70
        70 - 30 = 40
        40 - 30 = 10  <- 10 < 30, paro. Resto = 10.
        Foram 3 subtracoes em um unico %.

    1000 % 3 = 1
        ... 333 subtracoes ate sobrar 1.
        Mas o `%` calcula direto, em UM passo!
'''

'''
EXERCICIO - aquecimento com `%`

Calcule a mao. Lembre: `a % b` eh o que sobra apos subtrair b o
maximo de vezes possivel.

1) Quanto eh 25 % 7?
   (25 - 7 = 18, 18 - 7 = 11, 11 - 7 = 4. Sao 3 subtracoes.)
'''
resto_de_25_por_7 = 'coloque o valor aqui'

'''
2) Quanto eh 100 % 30?
   (100 - 30 - 30 - 30 = 10)
'''
resto_de_100_por_30 = 'coloque o valor aqui'

assert verifica(resto_de_25_por_7, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'resto_de_25_por_7 incorreta'
assert verifica(resto_de_100_por_30, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'resto_de_100_por_30 incorreta'
print('Exercicio % aquecimento: OK')

'''
EXPLICACAO - mdc com `%`

Reescrevemos a recursao da Parte 2 trocando "subtrair b de a uma
vez" por "subtrair b de a TODAS as vezes possiveis" (= a % b):

    mdc(a, b) = mdc(b, a % b)        quando b != 0
    mdc(a, 0) = a                     (CASO BASE)

Repare: aqui o caso base mudou! Antes era a == b, agora eh b == 0.
Faz sentido — a cada passo, b vira o resto da divisao, que eventualmente
chega a 0 (porque o resto fica menor a cada passo).

EXEMPLO QUE MOSTRA A DIFERENCA — vamos comparar `mdc_subtracao(100, 30)`
com `mdc(100, 30)`:

  Com SUBTRACAO (Parte 2):
    mdc_subtracao(100, 30) -> mdc_subtracao(70, 30)     # 100 - 30
                           -> mdc_subtracao(40, 30)     # 70 - 30
                           -> mdc_subtracao(10, 30)     # 40 - 30
                           -> mdc_subtracao(10, 20)     # 30 - 10
                           -> mdc_subtracao(10, 10) = 10  # caso base
    5 chamadas recursivas.

  Com `%`:
    mdc(100, 30) = mdc(30, 100 % 30) = mdc(30, 10)
    mdc(30, 10)  = mdc(10, 30 % 10)  = mdc(10, 0)
    mdc(10, 0)   = 10                  # CASO BASE
    2 chamadas recursivas.

Cada `%` "pulou" 3 subtracoes em um unico passo. Pra inputs maiores,
a diferenca cresce muito.
'''

a_para_mdc = 100
b_para_mdc = 30

'''
EXERCICIO - variaveis ilustrando o passo recursivo

Considere a = 100, b = 30.

1) Qual o RESTO da divisao de a por b?
   (use uma EXPRESSAO: `a_para_mdc % b_para_mdc`)
'''
resto_da_divisao_mdc = 'coloque o valor aqui'

'''
2) Terceirize: agora o par vira (b, resto) = (30, 10). Quanto vale
   mdc(30, 10)?

   Pode continuar a mao: mdc(30, 10) -> mdc(10, 30 % 10) = mdc(10, 0).
   E mdc(?, 0) cai no CASO BASE: retorna 10.
'''
mdc_de_30_e_10 = 'coloque o valor aqui'

'''
3) Junte: mdc(100, 30) eh o resultado da terceirizacao.
   Use uma EXPRESSAO: `mdc_de_30_e_10`.
'''
mdc_total = 'coloque o valor aqui'

assert verifica(resto_da_divisao_mdc, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'resto_da_divisao_mdc incorreta'
assert verifica(mdc_de_30_e_10, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'mdc_de_30_e_10 incorreta'
assert verifica(mdc_total, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'mdc_total incorreta'
print('Exercicio mdc (com %) terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `mdc(a, b)` — agora a versao rapida,
com `%`. Pode assumir a, b inteiros >= 0 e nao ambos zero.

DICA: caso base — se `b == 0`, retorna `a`. Terceirizacao —
retorna `mdc(b, a % b)`.

    >>> mdc(7, 0)
    7
    >>> mdc(18, 12)
    6
    >>> mdc(17, 5)
    1
'''
def mdc(a, b):
    pass

# Bloco 1: caso base.
assert mdc(7, 0) == 7, 'mdc(7, 0) (caso base)'
assert mdc(1, 0) == 1, 'mdc(1, 0) (caso base)'
assert mdc(100, 0) == 100, 'mdc(100, 0) (caso base)'
print('Exercicio mdc (com %) caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert mdc(12, 18) == 6
assert mdc(18, 12) == 6, 'ordem nao importa pro resultado final'
assert mdc(48, 36) == 12
assert mdc(17, 5) == 1, 'coprimos'
assert mdc(100, 75) == 25
assert mdc(1, 1) == 1
# Conferencia que mdc rapido bate com mdc_subtracao
assert mdc(48, 36) == mdc_subtracao(48, 36)
assert mdc(100, 75) == mdc_subtracao(100, 75)

# Teste de recursividade. Euclides eh logaritmico, mas o pior caso
# sao numeros de Fibonacci consecutivos — ai o numero de passos
# cresce linearmente em n. F_60 e F_61 forcam ~60 passos, o que
# estoura recursionlimit(50).
sys.setrecursionlimit(50)
try:
    mdc(2504730781961, 1548008755920)   # F_61, F_60
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao mdc e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio mdc (com %) caso recursivo: OK')

'''
OBSERVACAO FINAL

Repare o caminho que a gente percorreu:
    1. `mdc_lento` — iterativo, faz sempre ~min(a,b) passos. Sem recursao.
    2. `mdc_subtracao` — recursivo. Bem rapido quando a e b sao parecidos
     em tamanho, mas pode ser MUITO lento quando um eh muito maior que
     o outro. Ex: mdc_subtracao(100, 1) faz 99 chamadas — pior ate que
     mdc_lento(100, 1), que faz 1!
    3. `mdc` — recursivo com `%`. A cada 2 passos o primeiro argumento
     divide por 2 (da pra provar!), entao faz no maximo
     ~2·log2(min(a,b)) passos. SEMPRE rapido — eh o Euclides classico.

    Dessas três complexidades computacionais, esse texto só te explicou a primeira. 
    Só pra você não achar que perdeu alguma coisa

A diferenca entre essas tres versoes nao eh a CORRETUDE — todas dao
o mesmo resultado pros mesmos inputs. Eh a VELOCIDADE. Recursao bem
escolhida pode te dar um salto enorme de desempenho.
'''


print('\n=== PARABENS! Lista 3 completa! ===')
'''
  Se você quiser, uma prova da complexidade o algoritmo recursivo de euclides

  Não precisa nem ler, de jeito nenhum, mas pode se quiser. Se quiser,
  vem falar comigo que a gente faz junto devagar

  Fato: para a > b > 0, vale a % b < a/2.
  - Se b ≤ a/2: então a % b < b ≤ a/2. ✓
  - Se b > a/2: então a < 2b, logo o quociente é 1 e a % b = a - b < a - a/2 = a/2. ✓

  Consequência: em mdc(a, b) → mdc(b, a%b) → mdc(a%b, ...), o primeiro argumento vai a → b → a%b. Pelo
   lema, a%b < a/2 — ou seja, a cada 2 passos o primeiro argumento mais que divide por 2.

  Então depois de 2k passos ele é < max(a,b) / 2^k. Como ele fica ≥ 1 até o fim, 2^k ≤ max(a,b), logo:

  nº de passos ≤ 2·log₂(max(a,b)) = log_√2(max(a,b))

  porque log_√2(x) = log(x)/log(√2) = log(x)/(½·log 2) = 2·log₂(x).

  Usei max na prova, não min, como acima. Depois de entender a prova, tente entender se faz diferença
  do ponto de vista de O grande
'''