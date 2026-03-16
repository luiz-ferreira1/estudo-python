'''exercicio 3'''

import pandas as pd
import numpy as np

# carregar dados
df = pd.read_csv('src/01-intro/08-machine-learning/wine.csv')

# criar cópia com falhas
df_nulos = df.copy()

rng = np.random.default_rng(42)
taxa_nulos = 0.10

# selecionar colunas numéricas (exceto Class)
colunas = df_nulos.columns.drop('Class')

# inserir valores nulos aleatórios
for col in colunas:
    qtd = int(len(df_nulos) * taxa_nulos)
    indices = rng.choice(df_nulos.index, size=qtd, replace=False)
    df_nulos.loc[indices, col] = np.nan

# criar cópias para cada tipo de preenchimento
df_media = df_nulos.copy()
df_mediana = df_nulos.copy()
df_moda = df_nulos.copy()

# preencher valores faltantes
for col in colunas:
    df_media[col].fillna(df[col].mean(), inplace=True)
    df_mediana[col].fillna(df[col].median(), inplace=True)
    df_moda[col].fillna(df[col].mode()[0], inplace=True)

# mostrar quantidade de valores nulos
print("Valores ausentes antes do preenchimento:")
print(df_nulos.isnull().sum())

print("\nValores ausentes após preenchimento pela média:")
print(df_media.isnull().sum())

print("\nValores ausentes após preenchimento pela mediana:")
print(df_mediana.isnull().sum())

print("\nValores ausentes após preenchimento pela moda:")
print(df_moda.isnull().sum())