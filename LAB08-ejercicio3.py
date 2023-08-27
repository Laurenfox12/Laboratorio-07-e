import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contraseña) and
            any(c.isupper() for c in contraseña) and
            any(c.isdigit() for c in contraseña) and
            any(c in string.punctuation for c in contraseña)):
            return contraseña

longitud_deseada = int(input("Ingrese la longitud deseada de la contraseña: "))
if longitud_deseada >= 8: 
    contraseña_generada = generar_contraseña(longitud=longitud_deseada)
    print("Contraseña generada:", contraseña_generada)
elif longitud_deseada < 8:
    print("La contraseña debe ser como minimo de 8 caracteres")

