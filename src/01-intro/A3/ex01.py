# ex01.py

numeros = []

print("Digite 3 números:")

for i in range(3):
    valor = float(input(f"Número {i+1}: "))
    numeros.append(valor)

print(f"Lista armazenada: {numeros}")

print(f"O menor elemento é: {min(numeros)}")
print(f"O maior elemento é: {max(numeros)}")