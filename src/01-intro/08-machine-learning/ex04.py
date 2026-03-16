'''Exercicio 4'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# carregar o dataset
df = pd.read_csv('src/01-intro/08-machine-learning/wine.csv')

# criar cópia com valores faltantes
df_faltantes = df.copy()

rng = np.random.default_rng(42)
taxa = 0.10

# selecionar colunas numéricas exceto 'Class'
colunas = df_faltantes.columns.drop('Class')

# inserir valores nulos aleatórios
for c in colunas:
    quantidade = int(len(df_faltantes) * taxa)
    posicoes = rng.choice(df_faltantes.index, size=quantidade, replace=False)
    df_faltantes.loc[posicoes, c] = np.nan

# criar bases preenchidas
df_media = df_faltantes.copy()
df_mediana = df_faltantes.copy()
df_moda = df_faltantes.copy()

for c in colunas:
    df_media[c].fillna(df[c].mean(), inplace=True)
    df_mediana[c].fillna(df[c].median(), inplace=True)
    df_moda[c].fillna(df[c].mode()[0], inplace=True)

# função para gerar histogramas
def plotar_histogramas(dados, titulo):
    fig, eixos = plt.subplots(3, 5, figsize=(15, 8))
    eixos = eixos.ravel()

    for i, col in enumerate(colunas):
        eixo = eixos[i]
        eixo.hist(dados[col], bins=10, edgecolor='black')
        eixo.set_title(col)

    # esconder gráficos extras
    for eixo in eixos[len(colunas):]:
        eixo.axis('off')

    fig.suptitle(titulo)
    plt.tight_layout()
    plt.show()

# mostrar histogramas
plotar_histogramas(df_media, 'Histogramas após imputação pela média')
plotar_histogramas(df_mediana, 'Histogramas após imputação pela mediana')
plotar_histogramas(df_moda, 'Histogramas após imputação pela moda')