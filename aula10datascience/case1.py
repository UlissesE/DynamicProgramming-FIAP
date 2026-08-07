import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


framework_A = np.array([
15, 13, 14, 12, 16, 15, 14, 13,
12, 14, 15, 13, 16, 14, 13, 15,
14, 13, 12, 15, 16, 14, 13, 15
])
framework_B = np.array([
10, 9, 11, 10, 9, 10, 11, 9,
10, 9, 10, 11, 9, 10, 9, 11,
10, 9, 10, 11, 9, 10, 9, 10
])

print("Shapiro A - ", stats.shapiro(framework_A))
print("Shapiro B - ", stats.shapiro(framework_B))

print("Levene:", stats.levene(framework_A, framework_B))

mw = stats.mannwhitneyu(framework_A, framework_B, alternative="two-sided")
print("\nMann-Whitney:", mw)

plt.boxplot([framework_A, framework_B], labels=["Framework A", "Framework B"])
plt.title("Tempo de execução dos frameworks")
plt.ylabel("Tempo de execução")
plt.show()