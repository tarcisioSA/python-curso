def quantidade():
    qtd = int(input('Digite a quantidade de TV: '))
    return qtd

lg = quantidade()
samsung = quantidade()

total = lg + samsung

def floorshare(marca):
    floor = (marca * 100) / total
    return floor

print(f'A quantidade de LG é: {floorshare(lg):.2f}%\nA quantidade de samsung é: {floorshare(samsung):.2f}%')

