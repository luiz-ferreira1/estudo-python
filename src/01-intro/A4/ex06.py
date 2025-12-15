def calcular_volume(dimensoes):
    """Calcula o volume em litros: (c * a * l) / 1000"""
    c = dimensoes['comprimento']
    a = dimensoes['altura']
    l = dimensoes['largura']
    return (c * a * l) / 1000

def calcular_potencia_termostato(volume, temp_desejada, temp_ambiente):
    """Potência = volume * 0.05 * (temp_desejada - temp_ambiente)"""
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def calcular_filtragem(volume):
    """Retorna uma lista com a filtragem mínima (2x) e máxima (3x)"""
    minima = volume * 2
    maxima = volume * 3

    return (minima, maxima)

print("--- Configuração do Aquário ---")
comp = float(input("Comprimento (cm): "))
alt = float(input("Altura (cm): "))
larg = float(input("Largura (cm): "))
t_amb = float(input("Temperatura ambiente atual (°C): "))
t_des = float(input("Temperatura desejada (°C): "))

aquario_dados = {
    'comprimento': comp,
    'altura': alt,
    'largura': larg
}

vol = calcular_volume(aquario_dados)
potencia = calcular_potencia_termostato(vol, t_des, t_amb)
filt_min, filt_max = calcular_filtragem(vol)

print(f"Volume do aquário: {vol:.2f} Litros")
print(f"Potência indicada do termostato: {potencia:.2f} W")
print(f"Filtragem necessária: Entre {filt_min:.2f} e {filt_max:.2f} Litros/hora")