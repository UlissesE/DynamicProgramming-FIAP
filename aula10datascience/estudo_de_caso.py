import numpy as np
import scipy.stats as stats


algoritmo_A = np.array([12.1, 11.8, 12.5, 11.9, 12.3, 12.0, 11.7, 12.2])
algoritmo_B = np.array([11.2, 11.0, 10.8, 11.3, 11.1, 10.9, 11.4, 11])

print("Média A:", np.mean(algoritmo_A))
print("Média B:", np.mean(algoritmo_B))
print("Shapiro A:", stats.shapiro(algoritmo_A))
print("Shapiro B:", stats.shapiro(algoritmo_B))
print("Levene:", stats.levene(algoritmo_A, algoritmo_B))

ttest = stats.ttest_ind(algoritmo_A, algoritmo_B,
equal_var=True)
print("Teste t:", ttest)
