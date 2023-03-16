import numpy as np

x = np.linspace(start=10, stop=100, num=10)
print("X", x)
print("shape", x.shape)

print("Primeiro elemento", x[0])
print("Segundo elemento", x[1])
print('Ultimo elemento', x[9])
print('Ultimo elemento', x[-1])

print(" ")
#Segundo exemplo:

print("x", x)
print('Dois primeiros elementos', x[0:2]) #o elemento dois não aparece aqui
print("Dois primeiros elementos", x[:2])
print("dois ultimos elementos ", x[-2:])

#Terceiro exemplo

x = x.reshape(2, 5)
print("x\n", x)
print("primeiro linha, segunda coluna", x[0,1])
print("Segunda linha, penultima coluna", x[1, -2])
print("ultima linha, ultima coluna", x[1, 4])
print('ultima linha, ultima coluna' ,x[-1, -1])
print(" ")
#Quarto exemplo
print('x\n', x)
print("primeira linha inteira: ", x[0, :])
print("Primeira lina, segunda a quarta coluna: ", x[0, 1:4])
print("Ultima coluna inteira: \n", x[:,[4]])
print(" ")
#Quinto exemplo
x2 = np.array([1,2,3])
print("X2 antes", x2)
y = x2[:2]
y[0] = -100
print("X2 depois",x2)
print(" ")
#Sexto exemplo
x3 = np.array([1,2,3])
print("X3 antes", x3)
y2 = x3[:2].copy()
y2[0] = -100
print("X3 depois", x3)
print(y2)