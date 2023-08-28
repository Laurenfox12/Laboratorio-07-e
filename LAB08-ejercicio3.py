import random

def password():  
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = minus.upper()
    num = "1234567890"
    simb = "@[]{}+-?¿!¡'()$#%&.,"

    todo = minus + mayus + num + simb

    longitud  = 12

    muestra = random.sample(todo,longitud)
    contraseña = "".join(muestra)
    return contraseña
contraseña_generada = password()
print(contraseña_generada)

