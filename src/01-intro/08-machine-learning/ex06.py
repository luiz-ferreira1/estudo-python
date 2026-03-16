'''Exercicio 6'''

import pandas as pd
import matplotlib.pyplot as plt

# carregar o dataset
df = pd.read_csv('src/01-intro/08-machine-learning/wine.csv')

# selecionar atributos (exceto Class)
colunas = df.columns.drop('Class')

# percentuais das amostras
tamanhos = [0.10, 0.30, 0.50]

lista_amostras = []

# gerar subconjuntos
for p in tamanhos:
    amostra = df.sample(frac=p, random_state=42)
    lista_amostras.append((f'{int(p*100)}%', amostra))

# adicionar base completa
lista_amostras.append(('100%', df.copy()))

# calcular estatísticas
resultados = {}
for nome, tabela in lista_amostras:
    resultados[nome] = tabela[colunas].describe().loc[['mean', '50%', 'std', 'min', 'max']]

# nomes das métricas
metricas = {
    'mean': 'Média',
    '50%': 'Mediana',
    'std': 'Desvio padrão',
    'min': 'Mínimo',
    'max': 'Máximo'
}

# gerar gráficos
for cod, nome_metrica in metricas.items():

    fig, eixos = plt.subplots(3, 5, figsize=(16, 9))
    eixos = eixos.ravel()

    for i, col in enumerate(colunas):

        valores = [resultados[nome].loc[cod, col] for nome, _ in lista_amostras]
        labels = [nome for nome, _ in lista_amostras]

        eixos[i].bar(labels, valores)
        eixos[i].set_title(col, fontsize=9)
        eixos[i].tick_params(axis='x', rotation=45)

    # esconder gráficos não utilizados
    for eixo in eixos[len(colunas):]:
        eixo.axis('off')

    fig.suptitle(f'Comparação da {nome_metrica} por tamanho de amostra')
    plt.tight_layout()
    plt.show()

# À medida que o tamanho da amostra cresce, os valores estatísticos ficam mais próximos
# daqueles observados na base completa, indicando que amostras maiores representam melhor os dados.