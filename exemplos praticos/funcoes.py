l1 = [1, 2, 3, 4, 5, 6]
l2 = [36, 20, 5, 0, 11]
l3 = [25, 20, 14, 33, 12]

def soma(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

soma_l1 = soma(l1)
soma_l2 = soma(l2)
soma_l3 = soma(l3)

print(soma_l1)
print(soma_l2)
print(soma_l3)

def multiplica(lista):
    resultado = 1
    for item in lista:
        resultado = resultado * item
    return resultado

multi_l1 = multiplica(l1)
multi_l2 = multiplica(l2)
multi_l3 = multiplica(l3)

print(f'Resultado: l1: {multi_l1}, l2: {multi_l2}, l3: {multi_l3}')