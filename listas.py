nombres = []

nombres = ["Juan","maria","jose",22]

print(nombres[2])
print(nombres[0])
print(nombres[3])
print()
print(nombres[-2])
print(nombres[-1])
nombres.append("pedro")
print(nombres)
dato = input("Ingresa nombre: ")
nombres.append(dato)
print(nombres)
nombres2 = ["Francisca","Paola"]
nombres.extend(nombres2)
print(nombres)
print(nombres[6])
nombres.insert(2,"Josefa")
print(nombres)
nombres.remove("jose")
print(nombres)
nombres.pop()
print(nombres)
nombres.pop(1)
print(nombres)