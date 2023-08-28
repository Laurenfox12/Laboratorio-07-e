print("Calculadora simple")
print("Opciones:\n1)SUMA\n2)RESTA\n3)MULTIPLICACION\n4)DIVISON")
try:
    opcion = int(input("Seleccione una opcion: "))
    if opcion >= 1 and opcion  <= 4:
        if opcion == 1:
            print("Elegiste la suma: ")
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            resultado = a + b
            print("El resultado de la suma de {} + {} = {}".format(a,b,resultado))
        elif opcion == 2:
            print("Elegiste la resta: ")
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            resultado = a - b
            print("El resultado de la resta de {} - {} = {}".format(a,b,resultado))
        elif opcion == 3 :
            print("Elegiste la multiplicacion: ")
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            resultado = a * b
            print("El resultado de la multiplicacion de {} + {} = {}".format(a,b,resultado))
        else:
            try:
                print("Elegiste la division: ")
                a = int(input("Ingrese el primer numero: "))
                b = int(input("Ingrese el segundo numero: "))
                resultado = a / b
                print("El resultado de la division de {} / {} = {:.2f}".format(a,b,resultado))
            except ZeroDivisionError:
                print("Ocurrio un error por division por cero")
    else:
        print("Fuera de rango de opciones")
except ValueError:
    print("Opcion no valida")
    
