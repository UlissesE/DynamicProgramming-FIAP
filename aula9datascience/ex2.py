import numpy as np
import pandas as pd
import scipy.stats as stats

tabela = pd.DataFrame({
"Cancelou": [30, 20, 10],
"Não cancelou": [70, 80, 90]
}, index=["Básico", "Intermediário", "Premium"])

qui2, p, graus_liberdade, esperados = stats.chi2_contingency(tabela)
print("Qui-quadrado:", qui2)
print("p-valor:", p)
print("Graus de liberdade:", graus_liberdade)
print("Valores esperados:")
print(esperados)