lista_uno  = [1,2,3,4,5,6,7,8,9,10]
lista_dos  = [5,6,7,8,9,10,11,12,13,14,15]
lista_tres = [10,11,12,13,14,15,16,17,18,19,20]

#Problema a
a = set(lista_uno)
b = set(lista_dos)
c = set(lista_tres)

# Problema b: Encontrar el conjunto de números presentes en las tres listas
numeros_en_tres_listas = a.intersection(b.intersection(c))

# Problema c: Encontrar el conjunto de números presentes en al menos una lista
numeros_en_al_menos_una_lista = a.union(b.union(c))
# d. Encontrar el conjunto de números en la primera lista pero no en la última
numeros_en_primera_no_en_ultima = a.difference(c)

print("Numeros que se encuentran en las tres listas: ",numeros_en_tres_listas)
print("Numeros que se encuentran en almenos una lista: ",numeros_en_al_menos_una_lista)
print("Numeros que se encuentran en la primera lista, pero no en la ultima: ",numeros_en_primera_no_en_ultima)

tuplas = (tuple(a),tuple(b),tuple(c))
sumar_first_ulti = [tupla[0] + tupla[-1] for tupla in tuplas]
print("Suma del primer y último elemento de cada tupla:",sumar_first_ulti)