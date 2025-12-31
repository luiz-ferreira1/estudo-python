def carregar_dados_alunos(nome_arquivo):
    
    alunos = [] 
    
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
            
            prontuario = partes[0].strip()
            nome = partes[1].strip()
            email = partes[2].strip()
            
            aluno = {
                "prontuario": prontuario,
                "nome": nome,
                "email": email
            }
            
            alunos.append(aluno)
    
    return tuple(alunos)

resultado = carregar_dados_alunos('src/01-intro/06-arquivos/dados.txt')

print(resultado)

