import funciones as fn

#nombres = ["Juan","Maria","Jose"]
nombres = []
#for i in range(len(nombres)):
#    print(nombres[i])

for i in range(5):
    print("Nombre", i)
    nom = input("Ingrese el nombre: ")
    nombres.append(nom)
    
for i in nombres:
    print(i)

for i in range(4):
    nom  = input("Ingrese su nombre: ")
    fn.saludo(nom)

print(nom)

añoNac = int(input("Ingrese su año de nacimiento"))
fn.calcularEdad(añoNac)

print("Segundo commit")
print("tercer commit")



