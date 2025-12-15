# ex03.py

identificador = input("Digite o identificador: ")

valido = True

if len(identificador) != 7:
    valido = False

if not identificador.startswith("BR"):
    valido = False

if not identificador.endswith("X"):
    valido = False

numero_str = identificador[2:6]

if not numero_str.isdigit():
    valido = False
else:
    numero = int(numero_str)
    if numero < 1 or numero > 9999:
        valido = False

if valido:
    print("Identificador Válido")
else:
    print("Identificador Inválido")