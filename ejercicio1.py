import numpy as np
import random as rd

#arreglo = np.zeros(10)
#arreglo = np.array(range(10))
#print(arreglo)
arreglo = np.ones(10) #inicializar arreglo
print(arreglo)

for i in range(len(arreglo)):
    arreglo[i] = rd.randint(1,100)

print(arreglo)
arregloDos = arreglo[:].copy()

print("El número mayor del arreglo es: ",arregloDos.max())
print("El número menor del arreglo es: ",arregloDos.min())
print("La suma de los elementos del arreglo es: ",arregloDos.sum())
print("El promedio de los elementos del arreglo es: ",arregloDos.mean())
print(arregloDos)



