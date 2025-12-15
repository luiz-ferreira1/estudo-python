def calcular_imc(individuo):
    """Retorna o IMC de um indivíduo com base na sua altura e peso."""
    peso = individuo['peso']
    altura = individuo['altura']
    return peso / (altura * altura)

def obter_classificacao(imc):
    """Retorna a classificação com base no IMC."""
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Excesso de peso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def situacao_individuo(imc):
    """Retorna a situação ('normal', 'perder peso', 'ganhar peso')."""
    if imc < 18.5:
        return "ganhar peso"
    elif 18.5 <= imc < 25.0:
        return "normal"
    else:
        return "perder peso"

print("--- Calculadora de IMC ---")
peso_input = float(input("Digite seu peso (kg): "))
altura_input = float(input("Digite sua altura (m): "))

pessoa = {
    'peso': peso_input,
    'altura': altura_input
}

valor_imc = calcular_imc(pessoa)
classificacao = obter_classificacao(valor_imc)
situacao = situacao_individuo(valor_imc)

print("\n--- Resultado ---")
print(f"IMC: {valor_imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Situação: Você precisa {situacao}.")