print('\n\tCalculadora básica')


numero = ''
resultado = 0
operador = '+'
nnumero = 0

try:
    texto = input('Ingrese la operación: ')

    for caracter in texto + '+':

        if caracter not in '+-*/':

            numero += caracter

        else:

            numero = float(numero)

            if operador == '+':
                resultado += nnumero
                nnumero = numero

            elif operador == '-':
                resultado += nnumero
                nnumero = -numero

            elif operador == '*':
                nnumero *= numero

            elif operador == '/':
                nnumero /= numero

            operador = caracter
            numero = ''

    resultado += nnumero

    print(f'Resultado: {resultado:.02f}')
    
except ZeroDivisionError:
    print('No se puede dividir entre 0.')
        
except ValueError:
    print('Solo se pueden ingresar digitos y operadores en ese orden.')
        