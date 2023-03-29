idades = [27, 49, 12, 84, 15, 20, 2, 7, 9]

maior_idade = idades[0]

for idade in idades:
    if idade > maior_idade:
        maior_idade = idade


print(idades.index(maior_idade))