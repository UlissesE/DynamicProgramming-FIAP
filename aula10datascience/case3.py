import scipy.stats as stats

antes = [
15, 18, 17, 16, 19, 20, 14, 18,
16, 17, 18, 15, 19, 16, 17, 18,
14, 15, 16, 17, 18, 19, 20, 16
]
depois = [
18, 20, 19, 21, 22, 24, 17, 21,
19, 20, 21, 18, 22, 19, 20, 21,
17, 18, 19, 20, 21, 22, 23, 19
]

def aplicar_teste_t(grupo1, grupo2):
    print(stats.ttest_rel(grupo1, grupo2))

aplicar_teste_t(antes, depois)