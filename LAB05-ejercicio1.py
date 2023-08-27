edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Problema a
edades.sort()
max = edades[-1]
min = edades[0]
print("La lista ordenada es: {} \nValor maximo : {}\nValor minimo : {}".format(edades,max,min))
#Problema b
edades.append(max)
edades.append(min)
print("La lista actual es: {}".format(edades))
#Problema c
n = len(edades)
if n % 2 == 1:
    edad_mediana = edades[n // 2]
else:
    mediana_izquierda = edades[n // 2 - 1]
    mediana_derecha = edades[n // 2]
    edad_mediana = (mediana_izquierda + mediana_derecha) / 2
    print("Edad mediana:", edad_mediana)
#Problema d
conteo = 0
for i in edades:
    conteo += i 
promedio = conteo/n
print(promedio)

#Problema e
rango_edades = max - min
print("El rango  de las edades es {}".format(rango_edades))

#Problema f
dif_min = abs(min - promedio)
dif_max = abs(max - promedio)
print("Diferencia mínima entre mínimo y promedio:", dif_min)
print("Diferencia máxima entre máximo y promedio:", dif_max)

