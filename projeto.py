# Media e Mediana - é usado o tempo todo em projetos de análises 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)

grupo_a = np.random.normal(loc=175, scale=5, size=100)
grupo_b = np.random.normal(loc=180, scale=6, size=100)


df_alturas = pd.DataFrame({grupo_a: "Grupo A", grupo_b: "Grupo B"})

