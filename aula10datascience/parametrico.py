import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
sistema_antigo = np.array([4, 5, 6, 5, 7, 8, 6, 7, 5, 6, 8, 9, 7, 6, 5, 8, 7, 6, 9, 10, 4, 5, 6, 7, 8, 9, 20, 22, 25, 30])
sistema_novo = np.array([3, 4, 4, 5, 5, 6, 7, 8, 5, 6, 4, 5, 6, 5, 4, 6, 5, 4, 5, 6, 4, 5, 6, 5, 4, 5, 6, 5, 4, 5])
print("Média antigo:", np.mean(sistema_antigo))
print("Média novo:", np.mean(sistema_novo))
print("Mediana antigo:", np.median(sistema_antigo))
print("Mediana novo:", np.median(sistema_novo))
print("\nShapiro antigo:", stats.shapiro(sistema_antigo))
print("Shapiro novo:", stats.shapiro(sistema_novo))
mw = stats.mannwhitneyu(sistema_antigo, sistema_novo, alternative="two-sided")
print("\nMann-Whitney:", mw)
plt.boxplot([sistema_antigo, sistema_novo], labels=["Sistema antigo", "Sistema novo"])
plt.title("Tempo de resolução de tickets")
plt.ylabel("Tempo de resolução")
plt.show()