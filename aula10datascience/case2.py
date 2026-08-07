import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

api_1 = np.array([
120, 130, 125, 140, 128, 127, 135, 132, 129, 131,
134, 136, 133, 137, 138, 126, 124, 123, 139, 141,
150, 160, 170, 200, 300, 450, 500
])
api_2 = np.array([
118, 122, 121, 124, 119, 123, 120, 122, 121, 119,
120, 121, 122, 123, 119, 118, 120, 121, 122, 120,
121, 122, 119, 120, 121, 122, 120
])

print("Média API_1:", np.mean(api_1))
print("Média API_2:", np.mean(api_2))
print("Mediana API_1:", np.median(api_1))
print("Mediana API_2:", np.median(api_2))

print()
print("Shapiro 1:", stats.shapiro(api_1))
print("Shapiro 2:", stats.shapiro(api_2))
print("Levene:", stats.levene(api_1, api_2))

mw = stats.mannwhitneyu(api_1, api_2, alternative="two-sided")
print("\nMann-Whitney:", mw)

plt.boxplot([api_1, api_2], labels=["API 1", "API 2"])
plt.title("Tempo de resposta das APIs")
plt.ylabel("Tempo de resposta")
plt.show()