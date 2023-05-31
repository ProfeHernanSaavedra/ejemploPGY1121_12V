import numpy as np

arreglo = np.array([1,3,5,7,9])

print(arreglo)
print("Dimension del arreglo: ",arreglo.ndim)
print("largo del arreglo: ", len(arreglo))

print(arreglo.shape)
print(arreglo[0:3])
print(arreglo[1:4:2])
print(arreglo[::2])
print(arreglo[2::1])
print(arreglo[-2])

#recorrer arreglo
for i in range(len(arreglo)):
    print("posicion [",i,"]:",arreglo[i])

suma = arreglo[1] + arreglo[3]
print(suma)
print("otro arreglo")
#otro arreglo
arreglo1 = np.array([1,2,3])
arreglo2 = arreglo1[:]

print(arreglo2)
arreglo2[0] = 100
print(arreglo2)
print(arreglo1)

print("\nCopia de arreglos")
#copia de arreglos
arreglo3 = np.array([1,2,3])
arreglo4 = arreglo3[:].copy()
print(arreglo4)
arreglo4[0] = 100
print(arreglo4)
print(arreglo3)





