# ex04.py

identificador = input("Digite o identificador para validação detalhada: ")

erros = []

if len(identificador) != 7:
    erros.append("O identificador deve conter exatamente 7 caracteres.")

if not identificador.startswith("BR"):
    erros.append("O identificador não inicia com a sequência BR.")

parte_numerica = ""
if len(identificador) >= 6:
    parte_numerica = identificador[2:6]
    
    if not parte_numerica.isdigit():
        erros.append("A parte central do identificador deve conter apenas números.")
    else:
        numero = int(parte_numerica)
        if not (1 <= numero <= 9999):
             erros.append("O número deve ser um inteiro entre 0001 e 9999.")

if not identificador.endswith("X"):
    erros.append("O identificador não finaliza com o caractere X.")

if not erros:
    print("Identificador Válido.")
else:
    print("Erros encontrados:")
    for erro in erros:
        print(f"- {erro}")