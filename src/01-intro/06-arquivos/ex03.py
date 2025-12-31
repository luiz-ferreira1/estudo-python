def linha_para_dict(linha, chaves):

    # Remove espaços e quebras de linha do começo/fim
    linha = linha.strip()

    # Separa os valores manualmente pelas vírgulas
    valores = linha.split(",")

    resultado = {}

    for i in range(len(chaves)):
        # caso haja menos valores que chaves
        if i < len(valores):
            resultado[chaves[i]] = valores[i].strip()
        else:
            resultado[chaves[i]] = ""

    return resultado


arq = open('src/01-intro/06-arquivos/dados.txt', 'r')
linha = arq.readline()

chaves = ['prontuario', 'nome', 'email']

resultado = linha_para_dict(linha, chaves)

print(resultado)
