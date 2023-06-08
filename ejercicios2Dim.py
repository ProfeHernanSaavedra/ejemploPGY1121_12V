import random as rd
import numpy as np

matriz = np.zeros((3,3))

#print(matriz)

for f in range(3):
    for c in range(3):
        matriz[f][c] = rd.randint(0,100)

print(matriz)

print("El promedio de los elementos: ",matriz.mean())
print("La suma de los elementos: ",matriz.sum())
print("El máximo de los elementos: ",matriz.max())
print("El mínimo de los elementos: ",matriz.min())
print("La diagonal de la matriz es : ", matriz.diagonal())

arregloDos = np.diag([1,2,3])
print(arregloDos)

for i in range(3):
    for j in range(3):
        print("matriz[",i,"] [",j,"] = ",matriz[i][j])
        