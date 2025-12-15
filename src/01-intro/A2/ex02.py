# ex02.py

entrada = input("Digite as notas separadas por vírgula: ")

notas = [float(n) for n in entrada.split(',')]

media = sum(notas) / len(notas)

print(f"Média calculada: {media:.2f}")

if media > 6.0:
    print("Situação: Aprovado")
elif 4.0 <= media <= 6.0:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")