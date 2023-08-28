import random
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
num = "1234567890"
simb = "@[]{}+-?¿!¡'()$#%&.,"

def password(longitud,con_mayus = True, con_minus = True, con_num = True, con_simb = True):

    if longitud <= 0:
        raise ValueError("El valor debe ser un numero positivo. ")
    
    caracteres = ""
    if con_mayus: caracteres += mayus
    if con_minus: caracteres += minus
    if con_num: caracteres += num
    if con_simb : caracteres += simb

    if not caracteres: raise ValueError("La contraseña debe contener al menos un caracater. ")

    generar_caracteres = lambda: random.choice(caracteres)
    contraseña = "".join(generar_caracteres() for _ in range(longitud))
    return contraseña

try: 
    longitud = int(input("¿Cuantos caracteres tiene la contraseña?"))
    contraseña_generada = password(longitud,con_mayus = True, con_minus = True, con_num = True, con_simb = True)
    print(contraseña_generada)
except ValueError:
    print("Valor incorrecto.")
