# ex02.py

meses = (
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
)

numero = int(input("Digite o número do mês (1 a 12): "))

if 1 <= numero <= 12:
    print(f"O mês é: {meses[numero - 1]}")
else:
    print("Número inválido! Digite entre 1 e 12.")