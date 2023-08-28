print("Conevertir temperatura: ")
print("1: Farenheit --> Celsius\n2: Celsius --> Farenheit")
opcion = int(input("Seleccione una opcion( 1 0 2 ):"))

temperatura = int(input("Ingrese la temperatura a convertir: "))
if opcion == 1:
    Celsius =   (temperatura-32) / 1.8
    Celsius = float(Celsius)
    print("Los grados {}° Farenheit a ° Celsius son {:.2f}°".format(temperatura,Celsius))
elif opcion == 2:
    Farenheit =   (temperatura* 1.8 ) +32
    Farenheit = float(Farenheit)
    print("Los grados {}° Celsius a ° Farenheit son {:.2f}°".format(temperatura,Farenheit)) 