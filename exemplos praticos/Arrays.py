import numpy as np
# Expemplo 1
lista1 = [1, 2, 3]
x1 = np.array(lista1)
print("x1", x1)
print("shape", x1.shape)
print(" ")

# Exemplo 2
lista2 = [[1,2],[3,4]]
x2 = np.array(lista2)
print("x2\n", x2)
print("shape", x2.shape)
print(" ")

#exemplo 3
dim = (5,5)
x3 = np.zeros(dim)
print("x3\n", x3)
print("shape", x3.shape)
print(" ")

#exemplo 4
size = (2,2)
x4 = np.ones(size)
print("x4\n", x4)
print("shape", x4.shape)
print(" ")

#exemplo 5
x_min, x_max = 5,15
x5 = np.linspace(start=x_min, stop=x_max, num=6)
print("x5", x5)
print("shape", x5.shape)
print(" ")

#exemplo 6
n = 10
x6 = np.eye(n)
print("x6:\n", x6)
print("shape", x6.shape)

#exemplo 7
x7 = np.random.random(size=(2, 3))
print("x7:\n", x7)
print("shape: ", x7.shape)


