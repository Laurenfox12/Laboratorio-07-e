"Serie de fibonacchi hasta n-termino"
termino_n = int(input("Ingrese el n-ésimo término: "))
fibonacci = [0, 1]

while len(fibonacci) < termino_n:
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)

print("Serie de Fibonacci hasta el {} ésimo término: {}".format(termino_n,fibonacci))
