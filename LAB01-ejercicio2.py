print("Encontrar todos los numeros primos menores que n")

n = int(input("Ingrese un número límite: ")) #n es igual al limite 
primos = []

for num in range(2, n):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        primos.append(num)

print("Números primos hasta {}: {}".format(n,primos))

