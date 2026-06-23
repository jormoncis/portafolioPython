print('Ayuda a la venta de pasajes')

total_pasaje = 0
conteo_pasaje = 0

try:
    pasajes = int(input('Ingresa la cantidad de pasajes a vender: '))
    while True:
        valor_pasaje = int(input('Ingrese el valor del pasaje: '))
        if valor_pasaje > 0:
            total_pasaje += valor_pasaje
            conteo_pasaje += 1
        else:
            print('Debe ser entero y mayor a cero.')
        if pasajes == conteo_pasaje:
            print(f'Total a pagar: ${total_pasaje}')
            break
        
except ValueError:
    print('El ingreso por teclado tiene que ser númerico.')