import numpy as np
#exeplo01
x = np.ones((2,2))
y = np.eye(2)
print("X", x)
print("Y", y)
print(" ")
print("Soma:\n", x + y)
print("Soma float\n", x + 2.)

#exemplo02

print("Subtração:\n", x - y)
print("Sub broadcasting\n", x -2)
print(" ")

#exemplo03
#print("Divisão:\n", x / y)
print("Broadcasting:\n", x / 2)

#exempço04
print("Combinação: \n", (x+y)/(x-2))

#multiplicao matricial

print("np.dot:\n", np.dot(x,y))
print("@: \n", x @ y)
print(".dot:\n",x.dot(y))
print(" ")
#exemplo:
a = np.array([[1,2], [3,-2]])
c = np.array([[7],[-11]])
print("A\n",a)
print("C\n" , c)
x2 = np.dot(np.linalg.inv(a),c)
print("A,b: ", x2.ravel())