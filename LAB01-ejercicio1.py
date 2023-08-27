print("Identificador de numeros primos")
numero = int(input("Ingrese un número: "))

if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("{} no es un número primo.".format(numero))
            break
    else:
        print("{} es un número primo.".format(numero))
else:
    print("{} no es un número primo.".format(numero))