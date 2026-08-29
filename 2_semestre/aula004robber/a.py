
def rouba(rua, casa, memo):
    print(casa)

    if casa in memo.keys() : return memo[casa]
    
    if casa >= len(rua): return 0

    usei = rua[casa] + rouba(rua, casa+2, memo)

    n_usei = rouba(rua, casa+1, memo)

    memo[casa] = max(usei, n_usei)
    return memo[casa]

rouba([2, 7, 9, 3, 1, 20, 23, 11, 9, 23]*100, 0, {})