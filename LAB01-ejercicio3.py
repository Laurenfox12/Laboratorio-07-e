print("Factorial de un numero")
numero = int(input("Ingrese un número: "))
resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print("El factorial de {} es {}".format(numero,resultado))