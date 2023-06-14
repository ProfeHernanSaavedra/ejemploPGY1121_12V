def saludo(nombre):
    print("hola",nombre)
    print("Bienvenido a este mágico lenguaje de programación")

def calcularEdad(añoNac):
    añoActual = 2023
    edad = añoActual - añoNac
    print("Ud tiene ",edad, " años app")


def sumar(num1,num2):
    suma = num1 + num2
    return suma

def calculoIVA(precio):
    iva = precio * 0.19
    return iva

def descuento(precio,descuento):
    total = precio - (precio * descuento/100)
    return total

def calculoIMC(peso,estatura):
    imc = peso /estatura**2

    if imc < 18.5:
        print("Bajo peso")
    else:
        if imc >= 18.5 and imc <= 24.9:
            print("Adecuado")
        else:
            if imc >=25 and imc <= 29.9:
                print("Sobrepeso")
            else:
                if imc >=30 and imc <= 34.9:
                    print("Obesidad Grado 1")
                else:
                    if imc >= 35 and imc <= 39.9:
                        print("Obesidad Grado 2")
                    else:
                        if imc > 40 :
                            print("Obesidad Grado 3") 
