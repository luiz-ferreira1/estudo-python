def carregar_dados_alunos(nome_arquivo):
    
    projetos = [] 
    
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # remove \n do final
            
            # ignora linhas vazias
            if linha == "":
                continue
            
            # separa manualmente pelos separadores de vírgula
            partes = linha.split(",")
            
            # garante que existem exatamente 3 campos
            if len(partes) != 3:
                continue  # ou poderia lançar erro
            
            codigo = partes[0].strip()
            titulo = partes[1].strip()
            responsavel = partes[2].strip()
            
            projeto = {
                "prontuario": codigo,
                "nome": titulo,
                "email": responsavel
            }
            
            projetos.append(projeto)
    
    return tuple(projetos)

resultado = carregar_dados_alunos('src/01-intro/06-arquivos/projetos.txt')

print(resultado)