'''Exercicio 2'''

import pandas as pd
import matplotlib.pyplot as plt

# carregar os dados
df = pd.read_csv('src/01-intro/08-machine-learning/wine.csv')

# selecionar colunas numéricas e remover 'Class'
colunas = df.select_dtypes(include=['number']).drop(columns=['Class']).columns

# criar a figura com subplots
fig, eixos = plt.subplots(nrows=3, ncols=5, figsize=(15, 8))
eixos = eixos.ravel()

# gerar histogramas
for idx, atributo in enumerate(colunas):
    eixo = eixos[idx]
    eixo.hist(df[atributo], bins=10, edgecolor='black')
    eixo.set_title(atributo)
    eixo.set_xlabel('Valores')
    eixo.set_ylabel('Frequência')

# esconder gráficos que não serão usados
for eixo in eixos[len(colunas):]:
    eixo.axis('off')

plt.tight_layout()
plt.show()