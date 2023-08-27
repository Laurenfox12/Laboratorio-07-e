string = "Aprendiendo Python con Edem"
palabras = string.split()
conteo = -1
for resultado in palabras:
    resultado = palabras[conteo]
    conteo -= 1
    print(resultado, end= " ")