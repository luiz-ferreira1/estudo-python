def soma_args(*args):
    return sum(args)

# Teste (podemos passar quantos números quisermos)
print(f"Soma flexível: {soma_args(10, 20, 30, 40, 50)}")