# Media e Mediana - é usado o tempo todo em projetos de análises 


# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Definindo a semente para reprodutibilidade
np.random.seed(42)

# Gerando dados de alturas para dois grupos (A e B)

grupo_a = np.random.normal(loc=175, scale=5, size=100)
grupo_b = np.random.normal(loc=180, scale=6, size=100)

# Criando um DataFrame para as alturas dos grupos A e B
df_alturas = pd.DataFrame({grupo_a: "Grupo A", grupo_b: "Grupo B"})

def_alturas = pd.DataFrame({
    "Altura": np.concatenate([grupo_a, grupo_b]),
    "Grupo": ["Grupo A"] * len(grupo_a) + ["Grupo B"] * len(grupo_b)
})
# Visualizando as distribuições de alturas dos grupos A e B

plt.figure(figsize=(10, 6))
sns.histplot(data=def_alturas, x="Altura", hue="Grupo", kde=True, bins=20)
plt.title("Distribuição de Alturas dos Grupos A e B")
plt.xlabel("Altura (cm)")
plt.ylabel("Frequência")
plt.show()
# Calculando a média e a mediana dos grupos A e B
media_a = np.mean(grupo_a)
media_b = np.mean(grupo_b)
mediana_a = np.median(grupo_a)
mediana_b = np.median(grupo_b)
print(f"Grupo A - Média: {media_a:.2f}, Mediana: {mediana_a:.2f}")
print(f"Grupo B - Média: {media_b:.2f}, Mediana: {mediana_b:.2f}")

# Comparando as listas A e B
lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4, 100]
media_a = np.mean(lista_a)
media_b = np.mean(lista_b)
mediana_a = np.median(lista_a)
mediana_b = np.median(lista_b)
print(f"Lista A - Média: {media_a:.2f}, Mediana: {mediana_a:.2f}")
print(f"Lista B - Média: {media_b:.2f}, Mediana: {mediana_b:.2f}")

# Visualizando as distribuições das listas A e B
figura, eixos = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(lista_a, bins=5, ax=eixos[0], kde=True)
eixos[0].set_title("Lista A")
sns.histplot(lista_b, bins=5, ax=eixos[1], kde=True)
eixos[1].set_title("Lista B")
plt.tight_layout()
plt.show()


