entrada = input('Digite as notas separadas por vírgula: ')

notas = []

numeros = entrada.split(',')

for numero in numeros:
    n = float(numero)
    notas.append(n)

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print(media)

if media > 6.0:
    print('Aprovado')
elif 4.0 <= media <= 6.0:
    print('Recuperação')
else:
    print('Reprovado')