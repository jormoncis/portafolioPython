for i in range(5):
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        print("Número incorrecto.")
        i = i - 1
    