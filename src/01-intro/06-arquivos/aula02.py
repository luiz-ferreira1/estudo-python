"""Manipulando arquivos com python"""

# arq = open('src/01-intro/06-arquivos/arquivo.txt', 'w')

# arq.write('Ola, tudo bem?\n')

# arq.write('Caio\nJoao\nMarcos')

# x = ['Caio', 'Joao', 'Marcos']

# arq.writelines(x)

# for nome in x:
#    arq.write(nome + '\n')

# arq.close()

with open('src/01-intro/06-arquivos/arquivo.txt', 'r') as arq:
    for i in arq:
        print(i)
print('fim')