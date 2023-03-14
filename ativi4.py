import string

nome = 'João Da Silva'
cidade = 'São Paulo'
cpf = '026.649.592-39'

print(nome.upper())
print(cidade.upper())
print(cpf.upper())
print(' ')
print(nome.lower())
print(cidade.lower())
print(cpf.lower())

c = "ã"
print(nome.find(c))
print(cidade.find(c))
print(" ")
print(len(nome))
print(len(cidade))
print(len(cpf))

i = cpf.translate(str.maketrans('', '', string.punctuation))
print(i)





