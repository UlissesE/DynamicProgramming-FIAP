import numpy as np
import scipy.stats as stats

modelo_A = np.array([0.82, 0.84, 0.83, 0.85, 0.81, 0.84])
modelo_B = np.array([0.78, 0.79, 0.80, 0.77, 0.79, 0.78])
modelo_C = np.array([0.86, 0.87, 0.88, 0.85, 0.87, 0.86])

print("Média modelo A:", np.mean(modelo_A))
print("Média modelo B:", np.mean(modelo_B))
print("Média modelo C:", np.mean(modelo_C))
print("Desvio padrão modelo A:", np.std(modelo_A, ddof=1))
print("Desvio padrão modelo B:", np.std(modelo_B, ddof=1))
print("Desvio padrão modelo C:", np.std(modelo_C, ddof=1))


resultado_anova = stats.f_oneway(modelo_A, modelo_B, modelo_C)

print("Resultado da ANOVA:", resultado_anova)
print("Estatística F:", resultado_anova.statistic)
print("p-valor:", resultado_anova.pvalue)

print("-" * 30)

todos = np.concatenate([modelo_A, modelo_B, modelo_C])
media_geral = np.mean(todos)
ss_total = np.sum((todos - media_geral) ** 2)
ss_entre = (
len(modelo_A) * (np.mean(modelo_A) - media_geral) ** 2 +
len(modelo_B) * (np.mean(modelo_B) - media_geral) ** 2 +
len(modelo_C) * (np.mean(modelo_C) - media_geral) ** 2
)
eta_squared = ss_entre / ss_total
print("Eta squared:", eta_squared)