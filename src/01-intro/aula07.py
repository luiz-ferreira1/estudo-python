""" I/O Input and Outpu """

#saída padrão - sys stdout
print('hello world' , 'Maria', 1 , True, sep = ' @', end = '!!!!\n')
#print('hello world' , 'Maria', 1 , True, sep = ' @', end = '')

arquivo = open('nome.txt', 'w', encoding = 'uft-8')
print('joao@email.com',
      'maria@email.com', 
      'pedro@email.com',
      file = arquivo,
      sep = ';')

#Entrada
#input
nome = input('Dif=gite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print(f'{nome}, você é maior de idade')
else:
    print(f'{nome}, você é menor de idade')

#file
arquivo_notas = open('notas.txt','r', encoding = 'utf-8')
conteudo = arquivo_notas.read()
print(type,conteudo)
notas = conteudo.slip(sep = ';')
print(notas)
notas = [float(nota) for nota in notas]
print(notas)
media = (notas[0] + notas[1] + notas[2]) / len(notas)
print(media)