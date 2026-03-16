'''S7-A2 Exercicio 1'''

import pandas as pd

# leitura do arquivo
df = pd.read_csv('src/01-intro/08-machine-learning/wine.csv')

# seleciona apenas colunas numéricas
numericas = df.select_dtypes(include=['number'])

# remove a coluna Class
numericas = numericas.drop(columns=['Class'])

# calcula estatísticas
estatisticas = numericas.describe().T
estatisticas['variancia'] = numericas.var()

# imprime os resultados
for atributo, linha in estatisticas.iterrows():
    print(f"\nAtributo: {atributo}")
    print(f"Média: {linha['mean']:.2f}")
    print(f"Mediana: {numericas[atributo].median():.2f}")
    print(f"Desvio padrão: {linha['std']:.2f}")
    print(f"Variância: {linha['variancia']:.2f}")
    print(f"Mínimo: {linha['min']:.2f}")
    print(f"Máximo: {linha['max']:.2f}")