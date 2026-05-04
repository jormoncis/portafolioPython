from random import randint

print('Ingrese los límites')
num1 = int(input('Ingresa el rango minimo: '))
num2 = int(input('Ingresa el rango maximo: '))

numero_secreto = randint(num1,num2)

if num1 <= numero_secreto <= num2:
    if not(numero_secreto%2==0):
        numero_secreto -= 1
    else: numero_secreto = numero_secreto

intento = int(input('Ingrese número para hacer un intento(Dentro del RANGO): '))

if numero_secreto == intento:
    print(f'Felicidades has ganado, el número secreto era: {numero_secreto}')
elif numero_secreto != intento:
    if numero_secreto > intento:
        print('')
        print(f'El número a adivinar es más grande que su opción: {intento}')
        print('')
    else:
        print('')
        print(f'El número a adivinar es más pequeño que su opción: {intento}')
        print('')
    print('Segundo intento')
    print('Número diferente al anterior')
    intento2 = int(input('Ingrese número para hacer un intento(Dentro del RANGO): '))
    if numero_secreto == intento2:
        print('')
        print(f'Felicidades has ganado, el número secreto era: {numero_secreto}')
    elif numero_secreto != intento2:
        print('Te daré una pista: ')
        if abs(intento-numero_secreto)<abs(intento2-numero_secreto):
            print('')
            print(f'La opción 1: {intento} se acerca más al número secreto')
            print('')
        else:
            print('')
            print(f'La opción 2: {intento2} se acerca más al número secreto')
            print('')
        print('')
        print('Este es el último intento')
        print('Recuerde usar número dentro del rango')
        intento= int(input('Ingrese número para hacer un intento(Dentro del RANGO): '))
        if intento == numero_secreto:
            print('')
            print(f'Felicidades has ganado, el número secreto era: {numero_secreto}')
        elif intento != numero_secreto:
            print('')
            print(f'Has perdido el número secreto era {numero_secreto}')
print('')
print('Gracias por jugar, hasta luego!!!')
