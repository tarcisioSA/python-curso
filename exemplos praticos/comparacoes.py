import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([1.5, 3.5])
print("x", x)
print("y", y)
print(' ')
#comparações

print('Comparação de um array com um escalar (>): \n', x > 2)
print('Comparação de um array com escalar (>=): \n', x >= 2)
print('Comparação de um array com escalar (<): \n', x < 2)
print('Comparação de um array com escalar (<=): \n', x <= 2)
print('Comparação entre arrays (==): \n', x == x)
print('Comparação entre arrays (>): \n', x > x)
print('Comparação entre arrays (>): \n', x > y)
print(" ")
#indexação booleana
a = np.array([[1,3,7], [4,11,21], [42,8,9]])
print('a:\n', a)
print(' ')
b = 11
cond = a > b
print('condição:\n', cond)
print('elementos maiores que {}'.format(b), a[cond])
print('numero de elementos maiores que {}'.format(b), len(a[cond]))

print('Transformação de em um vetor coluna:\n ', a.reshape(1,9))
print('a transposição: \n',a.T)
print(' ')
print("A: \n", a)
print('Soma de todos os elementos de a:', np.sum(a))
print("A soma de a ao longo das linhas: \n", np.sum(a, axis=0))
print("A soma de a ao longo das colunas: ", np.sum(a, axis=1))
print(" ")
print(a)
print("média de todos os elementos: \n", np.mean(a))
print("média de A ao longo das linhas: ", np.mean(a, axis=0))
print("Média de A ao longo de colunas: ", np.mean(a, axis=1))
print(" ")
cond = a % 2 == 0
print('Condição: \n', cond)
i, j = np.where(cond)
print('i', i)
print("j", j)
print(" ")
print(a)
condicao = a % 2 == 0
print(condicao)
i_row = np.where(np.sum(condicao, axis=1))[0]
print(i_row)
print(a[i_row, :])