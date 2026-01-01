"""Aula 07 - Relacionamentos entre classes"""


class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep 
        self.numero = numero
    
    def __str__(self):
        return f'Endereco[cep={self.cep}, numero={self.numero}]'

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'

class Pessoa:
    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = []
    
    def add_endereco(self, endereco):
        self.enderecos.append(endereco)
    
    def print_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}]'
    
telefone = Telefone('11', '1111-1111')
pessoa1 = Pessoa('112332130', 'João da Silva', telefone)
pessoa1.add_endereco(Endereco('02832477', 123))
pessoa2 = Pessoa('216326483', 'Maria', telefone)
pessoa2.add_endereco(Endereco('123734837', 365))

pessoa3 = Pessoa('323232322', 'Pedro da Silva', telefone)

print(pessoa1)
print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

print(pessoa2)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
pessoa3.print_enderecos()