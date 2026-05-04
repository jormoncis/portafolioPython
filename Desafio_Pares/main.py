from random import randint

print("Dafio de Pares")
print()

nIni= int(input("Ingrese un numero Inicial: "))
nFin= int(input("Ingrese un numero Final: "))

def calculoCercano(random, opc):
    calculado = random - opc
    if calculado < 0:
        calculado = calculado * -1
    return calculado
    

if(nIni > nFin):
    print("El numero inicial no puede ser mayor al numero final")
    exit()

nRandom = randint(nIni, nFin)
ajustado = (nRandom // 2) * 2
if ajustado < nIni:
    ajustado = nIni

print("Solo cuentas con 3 intentos para adivinar el numero")
opc1 = int(input("Intento 1: "))
if opc1 == ajustado:
    print("¡Felicitaciones, pudiste adivinar.")
else: 
    if(ajustado < opc1):
        print("El numero es mayor al numero aleatorio generado!")
    else:        
        print("El numero es menor al numero aleatorio generado!")
    print("¡Intenta de nuevo!")
    opc2 = int(input("Intento 2: "))
    if opc2 == ajustado:
        print("Felicitaciones, pudiste adivinar.")
    else:
        opc1 = calculoCercano(ajustado, opc1)
        opc2 = calculoCercano(ajustado, opc2)
        if( opc1 < opc2):
            print("¡El numero es mas cercano es al primer intento!")     
        else:
            print("¡El numero es mas cercano es al segundo intento!")
        opc3 = int(input("Intento 3: "))
        if opc3 == ajustado:
            print("¡Felicitaciones, pudiste adivinar.")
        else:
            print(f"Perdiste, el numero aleatorio generado era: {ajustado}")


