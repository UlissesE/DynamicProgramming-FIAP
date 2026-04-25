
'''
EXPLICACAO
Uma pilha é uma estrutura de dados que tem um "topo".

Ela guarda quantos elementos quisermos, mas só podemos ver/retirar
o elemento do topo.

Quando adicionamos um elemento, adicionamos no topo.

Em uma pilha a operação "colocar no topo" é chamada de "push",
e a operação "tirar do topo" é chamada de "pop".

Por exemplo:
    [] é uma pilha vazia.
    Se fizermos push(1), teremos a pilha [1] (1 no topo)
    Se fizermos push(2), push(5), teremos [1,2,5] (5 no topo)
    Se fizermos pop(), saiu o topo (5), e sobrou [1,2]
'''

'''
EXERCICIO
Continuando o exemplo, tinhamos [1,2].

Digamos que fazemos push(4), push(8). Como está a pilha? 
Responda na forma de uma lista na variavel pilha1
'''
pilha1=[1,2,4,8]
# preencher essa variavel deve fazer o teste 001 passar

'''
EXERCICIO
Novo exemplo. Temos a pilha vazia []
Fazemos push(9),push(8),pop(),push(7),push(6),pop(). 

Como está a pilha? Responda na variavel pilha2.
'''
pilha2=[9,7]
# preencher essa variavel deve fazer o teste 002 passar

'''
EXERCICIO
Novamente, começamos com uma pilha vazia.
E se fizermos 
push(9),push(8),push(7),push(6),pop(),pop(),pop() ?. 
'''
pilha3=[9]
# preencher essa variavel deve fazer o teste 003 passar

'''
EXPLICACAO
Em python, podemos implementar o conceito de pilha usando uma lista, que têm as funções
append e pop

Por exemplo:

    >pilha = [] #inicializo uma pilha vazia
    >pilha.append(5)
    >pilha.append(8)
    >print(pilha)
    [5,8]
    >pilha.append(4)
    >pilha.append(3)
    >print(pilha)
    [5,8,4,3]
    >topo = pilha.pop()
    >print(topo)
    3
    >print(pilha)
    [5,8,4]

O append insere no final da lista e o pop tira do final da lista
'''

'''
EXERCICIO
Crie uma função poe_pilha, que recebe uma pilha e um número
e coloca o número no topo da pilha
'''
def poe_pilha(pilha,numero):
    pilha.append(numero)

'''
EXERCICIO
Crie uma função tira_pilha, que recebe uma pilha, tira o número que
estava no topo e retorna ele

Exemplo: se a pilha era [1,2,3], a pilha deve ficar sendo [1,2] e a função deve retornar 3
'''
def tira_pilha(pilha):
    return pilha.pop()

'''
EXPLICAÇÃO

Dá pau tentar tirar uma coisa que não está na pilha.

Exemplo:

    > pilha = []
    > pilha.append(3)
    > topo = pilha.pop()
    > print(topo)
    3
    > topo = pilha.pop()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: pop from empty list

Para evitar esse problema, precisamos aprender a verificar se uma pilha está 
vazia.

Basta ver quantos elementos tem na lista. len faz exatamente isso.
    > pilha = []
    > pilha.append(30)
    > pilha.append(40)
    > pilha.append(50)
    > len(pilha)
    3   #pilha tem os 3 elementos: 30,40,50. Posso tirar um
    > topo = pilha.pop()
    > print(topo)
    50
    > len(pilha)
    2   #pilha tem 2 elementos: 30,40. Posso tirar um
    > topo = pilha.pop()
    > print(topo)
    40
    > len(pilha)
    1   #pilha tem 1 elemento: 30. Posso tirar ele
    > topo = pilha.pop()
    > print(topo)
    30
    > len(pilha)
    0   #pilha está vazia. Se eu tentar tirar algum elemento, vai dar pau
'''

'''
EXERCICIO
Faça uma função pilha_vazia que retorna:
     True se a pilha está vazia;
     False se não está
'''
def pilha_vazia(pilha):
    return False if len(pilha) else True


'''
EXERCICIO

Estamos quase prontos para fazer o exercicio principal da aula, a função
'balanceado'.

Primero, vamos fazer uma funcao que verifica se um determinado "abre" 
encaixa com um "fecha".

Por exemplo, "(" encaixa com ")", mas não encaixa com "]", "}", nem "(", nem "["
Por exemplo, "[" encaixa com "]", mas não encaixa com ")", "}", nem "(", nem "["
Na verdade, "(" só encaixa com ")", "[" só encaixa com "]" e "{" só encaixa com "}"

Faça uma função encaixa, que recebe duas strings, um "abre" e um "fecha", e retorna
True se eles encaixam (False se não encaixarem)
'''
def encaixa(abre, fecha):
    fechamento = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    
    if fechamento[abre] == fecha:
        return True
    return False

'''
EXPLICACAO
Uma sequencia de parenteses "(" ")", colchetes "[" "]" e chaves "{" "}" 
é dita balanceada se cada simbolo "aberto" é "fechado" 
em um momento apropriado 

Por exemplo
'([])' é uma sequencia balanceada
'([)]' não é balanceada
'([]' não é balanceada
')' não é balanceada
'' é balanceada

Como já discutimos, esse problema é interessante porque
tem uma correspondencia com o problema de validar um arquivo html,
onde as tags html abrem e fecham, como os parenteses.

De uma olhada no arquivo pilhas_simulacao para relembrar
como o algoritmo proposto deve funcionar.
'''

'''
EXERCICIO RESOLVIDO. 

De uma olhada no arquivo pilhas_simulacao para relembrar
como o algoritmo proposto deve funcionar.

Agora, considere a seguinte string balanceada: '(()[a])'

Como vimos, o algoritmo vai lendo caractere a caractere
e atualizando a pilha. O que está na pilha, quando o 
algoritmo lê a letra "a"? 

Vou deixar esse respondido pra você ver o que é esperado

pilha_respondida=['(','[']

O que aconteceu a história da pilha foi a seguinte:
    []
    ['(']
    ['(','(']
    ['('] (um '(' foi retirado para encaixar com o ')'
    ['(','[']
'''    

'''
EXERCICIO

Agora, considere a seguinte string balanceada: '(([]{a}))'

O que está na pilha, quando o algoritmo lê a letra "a"? 

Responda na variável pilha_balanceada1
'''
pilha_balanceada1=['(', '(', '{']
# fazer corretamente essa função deve  fazer o teste 020 passar -- sim, houve um pulo
'''
EXERCICIO

Agora, considere a seguinte string balanceada: '{}[](a)'

O que está na pilha, quando o algoritmo lê a letra "a"? 

Responda na variável pilha_balanceada2
'''
pilha_balanceada2=['(']
# fazer corretamente essa função deve  fazer o teste 021 passar
'''
EXERCICIO

Agora, considere a seguinte string balanceada: '()(()[]{a})'

O que está na pilha, quando o algoritmo lê a letra "a"? 

Responda na variável pilha_balanceada3
'''
pilha_balanceada3=['(','{']
# fazer corretamente essa função deve  fazer o teste 022 passar

'''
EXERCICIO

Escreva uma funcao "balanceada" que recebe uma string e
retorna "True" se a string representa uma sequencia balanceada, 
"False" caso contrário.

Não deixe de olhar o arquivo pilhas_simulacao para entender/relembrar 
como o algoritmo deve funcionar

Sua função só vai receber parênteses, colchetes e chaves.
Não precisa se preocupar com nenhum outro caractere
'''

#o teste 024 é mais fácil, mas você só terminou de verdade quando passar também o 025
def balanceada(string):
    aberturas = ['(','[','{', '<']
    fechamentos = [')',']','}', '>']

    stack = []
    stackLength = 0
    
    for char in string:

        if char in aberturas:
            stack.append(char)

        elif char in fechamentos:
            if not stack: # Se a stack estiver vazia
                return False 
            
            ultimo = stack.pop()

            if not encaixa(ultimo, char):
                return False
            
        if stackLength < len(stack):
            stackLength+= 1
        
    return not stack # True if len(stack) == 0 else False
            
        

'''
EXERCICIO

Podemos fazer alguns upgrades na funcao balanceada:
    * Além de aceitar (, [ e {, queremos que ela aceite <, que será fechado com >
    * Se vier alguma letra/numero (ou qualquer outra coisa que nao seja (){}[]<> a funcao
    deve ignorar ao invés de dar pau
    * Se a string for balanceada, a funcao deve calcular qual foi o **maximo** 
    tamanho da pilha. Esse valor deve ser "fotografado" uma unica vez, 
    no final da execucao. Sugiro que você vá calculando, sem saber se a string
    é balanceada ou não, mas tire a fotografia uma linha antes do "return true"
'''
# O upgrade do < e > é o teste 026
# O upgrade das letras aletórias é o teste 027

'''
EXERCICIO
IMPLEMENTE A PROXIMA FUNCAO USANDO PILHAS


Defina uma função palindromo, 
que recebe uma string e retorna
True se ela é um palindromo, False caso contrario.

Um palindromo é uma string "espelhada"

Por exemplo palindromo('abbabba') retorna True
Por exemplo palindromo('aaa') retorna True
Por exemplo palindromo('aaaa') retorna True
Por exemplo palindromo('aac') retorna False
Por exemplo palindromo('a') retorna True
Por exemplo palindromo('') retorna True

dicas:
    Usando pilhas, podemos "empilhar" até a metade da string,
    depois "desempilhar" e ir verificando se o caracter desempilhado
    corresponde ao proximo caracter da string.

    Por exemplo, ao recebermos 'abbccbba'

    Empilhamos os primeiros 4 (a pilha fica 'abbc')
    damos pop() (o resultado é c) e comparamos com o proximo caractere (c)
    damos pop() (o resultado é b) e comparamos com o proximo caractere (b)
    damos pop() (o resultado é b) e comparamos com o proximo caractere (b)
    damos pop() (o resultado é a) e comparamos com o proximo caractere (a)

    Assim, a string é um palindromo
    
'''

# Se você chegou aqui, estou muito feliz. Continuar é legal, mas não se sinta obrigado/obrigada
# Esse é o teste 030, 031 e 032
def palindromo(string):
    
    result = []
    mid = len(string) // 2
    for i in range(mid):
        result.append(string[i])
    
    if (len(string) % 2 != 0):
        mid += 1

    for i in range(mid, len(string)):
        tmp = result.pop()
        if (tmp != string[i]):
            return False
    return True



    # final = len(string) - 1
    # for i in range(len(string)):
    #     if string[i] != string[final - i]:
    #         return False
    # return True



#Esse exercicio é de classes, mas nós não te ensinamos classe em python. Ele é o ultimo. Só faça se quiser, e me peça ajuda, se for o caso
'''
EXERCICIO

Implemente uma classe pilha que dá suporte a 6 operações:
    *push (coloca um elemento na pilha)
    *pop (retira o elemento do topo e o retorna)
    *tamanho (verifica quantos elementos existem na pilha)
    *vazia (retorna True se a pilha está vazia, False caso contrário)
    *top (retorna o elemento do topo sem alterar a pilha)

    Já vou te fornecer parte do código. Depois do código, tem uma descricao de 
    como testar
'''

class Pilha():

    def __repr__(self):
        return str(self.lista)

    def __init__(self):
        self.lista = []

    def push(self,elemento):
        self.lista.append(elemento)

    def pop(self):
        return self.lista.pop()

    def tamanho(self):
        pass #implemente!

    def top(self):
        pass #implemente!

    def vazia(self):
        pass #implemente!

'''
    Veja abaixo como usar os métodos já fornecidos

    > p = Pilha() #cria uma nova pilha
    > p.push(2) #coloca o 2 na pilha
    > p.push(3) #coloca o 3 na pilha
    > p.pop()
    3
    > p.pop()
    2

    O exercicio consiste em implementar os outros métodos
'''


import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

    def test_001_var_pilha1(self):
        self.verifica_pilha(pilha1,'30683e81e541f4f031f50134b6c4df4fb2325fb6222265fffa004832')
    def test_002_var_pilha2(self):
        self.verifica_pilha(pilha2,'12f16a9f7220b8fbba114ca53fa589d2137060e48ef51f87ede96a7d')
    def test_003_var_pilha3(self):
        self.verifica_pilha(pilha3,'fc53f829aced039d8170455b2e1b24e1fa08bebfd5457257832257a4')

    def test_010_poe_pilha(self):
        pilha_teste1 = [2,3]
        poe_pilha(pilha_teste1,4)
        self.assertEqual(pilha_teste1,[2,3,4])
        poe_pilha(pilha_teste1,5)
        self.assertEqual(pilha_teste1,[2,3,4,5])
        pilha_teste2 =[]
        poe_pilha(pilha_teste2,5)
        self.assertEqual(pilha_teste2,[5])
    
    def test_011_tira_pilha(self):
        pilha_teste3 = [1,2,3,4,5,6,7]
        topo = tira_pilha(pilha_teste3)
        self.assertEqual(topo,7)
        self.assertEqual(pilha_teste3,[1,2,3,4,5,6])
        topo = tira_pilha(pilha_teste3)
        self.assertEqual(topo,6)
        self.assertEqual(pilha_teste3,[1,2,3,4,5])
        topo = tira_pilha(pilha_teste3)
        self.assertEqual(topo,5)
        self.assertEqual(pilha_teste3,[1,2,3,4])

    def test_012_pilha_vazia(self):
        pilha_teste4 = [1,2,3]
        vazia =[]
        self.assertTrue(pilha_vazia(vazia))
        self.assertFalse(pilha_vazia(pilha_teste4))


   
    def test_018_encaixa(self):
        self.assertTrue(encaixa('(',')'))
        self.assertTrue(encaixa('[',']'))
        self.assertTrue(encaixa('{','}'))
        self.assertFalse(encaixa('{',')'))
        self.assertFalse(encaixa('{',']'))
        self.assertFalse(encaixa('{','{'))
        self.assertFalse(encaixa('(',']'))
        self.assertFalse(encaixa('(','}'))
        self.assertFalse(encaixa('(','('))
        self.assertFalse(encaixa('[','}'))

    def test_020_pilha_balanceada1(self):
        self.verifica_pilha(pilha_balanceada1,'d05014e01b5592cef47539758e813503f58c743512164f6021ee62ac')
    
    def test_021_pilha_balanceada2(self):
        self.verifica_pilha(pilha_balanceada2,'53edf5c1b62d1568ba48e5f9ae4c65790a60a7084c91e6afbf600471')
    
    def test_022_pilha_balanceada3(self):
        self.verifica_pilha(pilha_balanceada3,'45ec24251c4b6f1be75226ba5bc896de21a0d4100de755ea870268e6')

    def test_024_primeiros_exemplos_balanceado(self):
        self.assertEqual(balanceada('([])'),True)
        self.assertEqual(balanceada('([]{})'),True)
        self.assertEqual(balanceada('([][])'),True)
        self.assertEqual(balanceada('([}[])'),False)
        self.assertEqual(balanceada('([}{])'),False)
        self.assertEqual(balanceada('([}{])'),False)
        self.assertEqual(balanceada('(])'),False)
    
    def test_025_balanceado_mais_complexo(self):
        self.assertEqual(balanceada('([]'),False)
        self.assertEqual(balanceada('('),False)
        self.assertEqual(balanceada('((('),False)
        self.assertEqual(balanceada('((()'),False)
        self.assertEqual(balanceada(')'),False)
        self.assertEqual(balanceada('()))'),False)
        self.assertEqual(balanceada(''),True)

    def test_026_balanceado_upgrade_parenteses_angulares(self):
        self.assertEqual(balanceada('([]<>)'),True)
        self.assertEqual(balanceada('(<>{})'),True)
        self.assertEqual(balanceada('<[][]>'),True)
        self.assertEqual(balanceada('([}<>)'),False)
        self.assertEqual(balanceada('([><])'),False)
        self.assertEqual(balanceada('(<}{>)'),False)
        self.assertEqual(balanceada('<[]'),False)
        self.assertEqual(balanceada('<'),False)
        self.assertEqual(balanceada('>'),False)
    
    def test_027_balanceado_upgrade_letras_aleatorias(self):
        self.assertEqual(balanceada('([a]a<>i)'),True)
        self.assertEqual(balanceada('(<>g{g}j)'),True)
        self.assertEqual(balanceada('<[][]>'),True)
        self.assertEqual(balanceada('g(g[g}<>)'),False)




    
    def test_030_palindromo_comprimentos_pares(self):
        self.assertEqual(palindromo('aaaa') , True)
        self.assertEqual(palindromo('ac') , False)
        self.assertEqual(palindromo('abcddcba') , True)
        self.assertEqual(palindromo('abcdecba') , False)


    def test_031_palindromo_comprimentos_impares(self):    
        self.assertEqual(palindromo('abbabba'), True)
        self.assertEqual(palindromo('aaa') , True)
        self.assertEqual(palindromo('aac') , False)
        self.assertEqual(palindromo('abcdedcba') , True)

    def test_032_palindromo_peq(self):    
        self.assertEqual(palindromo('a') , True)
        self.assertEqual(palindromo('') , True)
    
    def test_040_classe_pilha_tamanho(self):
        p = Pilha()
        self.assertEqual(p.tamanho(),0)
        p.push(10)
        self.assertEqual(p.tamanho(),1)
        p.push(29)
        self.assertEqual(p.tamanho(),2)
        topo = p.pop()
        self.assertEqual(p.tamanho(),1)
    
    def test_041_classe_pilha_topo(self):
        p = Pilha()
        p.push(10)
        self.assertEqual(p.top(),10)
        p.push(29)
        self.assertEqual(p.top(),29)
        topo_antigo = p.pop()
        self.assertEqual(p.top(),10)
    
    def test_042_classe_pilha_vazia(self):
        p = Pilha()
        self.assertTrue(p.vazia())
        p.push(10)
        self.assertFalse(p.vazia())
        p.push(29)
        self.assertFalse(p.vazia())
        topo_antigo = p.pop()
        self.assertFalse(p.vazia())
        topo_antigo = p.pop()
        self.assertTrue(p.vazia())

    def verifica_pilha(self,pilha,codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(pilha).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno,codigo_correto)
    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)



try: 
    from pilhas_gabarito import *
except:
    pass

runTests()
