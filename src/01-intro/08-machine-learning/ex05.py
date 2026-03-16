'''Exercicio 5'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv('src/01-intro/08-machine-learning/wine.csv')

# criar cópia com valores ausentes
df_nulos = df.copy()

rng = np.random.default_rng(42)
taxa_nulos = 0.10

# selecionar colunas numéricas exceto 'Class'
colunas = df_nulos.columns.drop('Class')

# gerar valores nulos aleatórios
for c in colunas:
    quantidade = int(len(df_nulos) * taxa_nulos)
    indices = rng.choice(df_nulos.index, size=quantidade, replace=False)
    df_nulos.loc[indices, c] = np.nan

# criar bases para imputação
df_media = df_nulos.copy()
df_mediana = df_nulos.copy()
df_moda = df_nulos.copy()

for c in colunas:
    df_media[c].fillna(df[c].mean(), inplace=True)
    df_mediana[c].fillna(df[c].median(), inplace=True)
    df_moda[c].fillna(df[c].mode()[0], inplace=True)

# criar gráficos
fig, eixos = plt.subplots(3, 5, figsize=(16, 9))
eixos = eixos.ravel()

for i, col in enumerate(colunas):
    dados_boxplot = [
        df[col].dropna(),
        df_media[col].dropna(),
        df_mediana[col].dropna(),
        df_moda[col].dropna()
    ]

    eixos[i].boxplot(dados_boxplot, labels=['Orig', 'Média', 'Mediana', 'Moda'])
    eixos[i].set_title(col)

# ocultar eixos não utilizados
for eixo in eixos[len(colunas):]:
    eixo.axis('off')

plt.tight_layout()
plt.show()

# O boxplot permite visualizar e comparar como a distribuição dos dados muda
# após preencher os valores ausentes usando média, mediana ou moda.
# Alguns atributos podem mostrar assimetria ou presença de outliers.