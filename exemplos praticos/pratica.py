def entrada_dados():
    quntidade = int(input('Digite a quantidade de TV: '))
    return quntidade

lg = entrada_dados()
samsung = entrada_dados()

total = (lg + samsung)

floorshareLg = (lg * 100) / total
floorshareSamsung = (samsung *100) / total

print('O floorshare de lg é: {:.2f}%'.format(floorshareLg))
print('O floorshare de samsung é: {:.2f}%'.format(floorshareSamsung))
