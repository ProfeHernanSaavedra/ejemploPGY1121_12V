import funciones as fn

op = 3
while op != 4:
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op = int(input("Ingrese su opcion: "))

    if op == 1:
        precio = int(input("Ingrese precio del producto: "))
        #iva = fn.calculoIVA(precio)
        print("IVA: ",fn.calculoIVA(precio))
    else:
        if op == 2:
            precio = int(input("Ingrese precio del producto: "))
            descuento = float(input("Ingrese tasas de descuento: "))
            precioFinal = fn.descuento(precio,descuento)
            print("El precio final es: ",precioFinal)
        else:
            if op == 3:
                peso = int(input("Ingrese su peso: "))
                estatura = float(input("Ingrese su estatura: "))
                fn.calculoIMC(peso,estatura)
                


