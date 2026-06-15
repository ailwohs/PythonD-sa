# Media e Mediana - é usado o tempo todo em projetos de análises 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)

grupo_a = np.random.normal(loc=175, scale=5, size=100)
grupo_b = np.random.normal(loc=180, scale=6, size=100)


df_alturas = pd.DataFrame({grupo_a: "Grupo A", grupo_b: "Grupo B"})

def_alturas = pd.DataFrame({
    "Altura": np.concatenate([grupo_a, grupo_b]),
    "Grupo": ["Grupo A"] * len(grupo_a) + ["Grupo B"] * len(grupo_b)
})
plt.figure(figsize=(10, 6))
sns.histplot(data=def_alturas, x="Altura", hue="Grupo", kde=True, bins=20)
plt.title("Distribuição de Alturas dos Grupos A e B")
plt.xlabel("Altura (cm)")
plt.ylabel("Frequência")
plt.show()
media_a = np.mean(grupo_a)
media_b = np.mean(grupo_b)
mediana_a = np.median(grupo_a)
mediana_b = np.median(grupo_b)
print(f"Grupo A - Média: {media_a:.2f}, Mediana: {mediana_a:.2f}")
print(f"Grupo B - Média: {media_b:.2f}, Mediana: {mediana_b:.2f}")
