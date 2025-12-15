"""Aula 06 - Conversão de Tipos"""

# Conversão de tipo implícita e explícita

leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

# conversão explícita (type casting)
soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70

# mensagem = nome + ' tem a altura de ' + str(altura)
mensagem = f' {nome} tem a altura de {altura}'

print(mensagem)
