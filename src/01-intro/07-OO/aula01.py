"""Aula 01 - Introdução a Orientação a objetos"""

# paradigma de programação

# calcular a área e o perímetro de um retangulo
# area = base * altura
# perímetro e 2 * (base + altura)
# estrutura para armazenar os valores necessários para os calulos

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}

# Realizar os cálculos


def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']


def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])


print(calcular_area(retangulo1))
print(calcular_perimetro(retangulo1))
print(calcular_area(retangulo2))
print(calcular_perimetro(retangulo2))
