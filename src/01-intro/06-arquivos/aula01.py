"""Aula 01 - Manipulando arquivos"""

# open ('caminho', 'r')

# Mode
# r - leitura
# a - append / incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

# arquivo = open('src/01-intro/06-arquivos/teste3.txt','x')

# função para saber se um arquivo pode seer lido
# print(arquivo.readable())
# função para ler um arquivo
# print(arquivo.read())

# função para ler linha por linha de um arquivo
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lendo todas as linhas de um arquivo usando uma lista
# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# função para adicionar no final do arquivo caso seja usado 'a'
# limpa o arquivo e começa a escrever tudo de novo, caso seja 'w'
# a função write junto com o 'w' também pode ser utilizada para criar um novo arquivo

# a função write junto com o 'x' cria um arquivo novo da mesma forma que o 'w' 

# arquivo.write("Python\n")
# arquivo.write("C\n")

# arquivo.close()

# biblioteca para remoção de arquivos no python
# arquivo deve estar fechado para poder ser removido

import os

# if os.path.exists('src/01-intro/06-arquivos/teste3.txt'):
#     os.remove('src/01-intro/06-arquivos/teste3.txt')
# else:
#     print('Arquivo não existe')

# usado para remover uma pasta

os.rmdir('src/01-intro/06-arquivos/novapasta')