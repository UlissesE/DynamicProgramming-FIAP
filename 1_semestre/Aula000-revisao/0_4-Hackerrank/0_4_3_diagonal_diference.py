def sumDiagonal(matriz):
    sum = 0
    for i in range(len(matriz)):
        sum += matriz[i][i]
    return sum

def sumInverseDiagonal(matriz):
    sum = 0
    for i in range(len(matriz)):
        sum += matriz[i][len(matriz)-1-i]
    return sum

def diagonalDifference(mat):
    somaDiagonal = sumDiagonal(mat)
    somaDiagonalInversa = sumInverseDiagonal(mat)
    
    diferencaDiagonais = somaDiagonal - somaDiagonalInversa
    
    if diferencaDiagonais < 0:
        return diferencaDiagonais*(-1)
    return diferencaDiagonais
    
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

matriz_2x2 = [
    [1, 2],
    [3, 4]
]

assert diagonalDifference(matriz_2x2) == 0
assert diagonalDifference(matriz_3x3) == 2