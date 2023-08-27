print("PALINDROMOS")
palabra = input("Ingresa una palabra que se lea igual cuando inviertes su escritura: ")

palabra = palabra.replace("á","a")
palabra = palabra.replace("é","e")
palabra = palabra.replace("í","i")
palabra = palabra.replace("ó","o")
palabra = palabra.replace("ú","u")
palabra = palabra.replace(" ", "")
nueva_palabra = palabra[::-1]

if palabra == nueva_palabra:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")