alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

mensaje_original = input("Ingrese el mensaje a cifrar: ").upper()
desplazamiento = int(input("Ingrese el desplazamiento: "))
mensaje_cifrado = ""

for letra in mensaje_original:
    if letra in alfabeto:
        indice = alfabeto.find(letra)
        nuevo_indice = (indice + desplazamiento) % 26
        mensaje_cifrado += alfabeto[nuevo_indice]
    else:
        mensaje_cifrado += letra

print("Mensaje cifrado:", mensaje_cifrado.lower())