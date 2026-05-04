
VALOR_MEDICAMENTO_MENSUAL = 60000
VALOR_DESPACHO = 8000

edad = int(input('Ingrese su edad: '))
tramo = input('Ingrese su tramo(A,B,C o D): ').lower()

descuento_medicamento = 0
descuento_despacho = 0

if edad <= 0:
    print('Ingresa una edad válida, diferente y mayor a 0.')
    exit()

if edad <= 30:
    if tramo == 'a' or tramo == 'b':
        descuento_medicamento = 0.18
    else:
        descuento_medicamento = 0.12
elif 31 <= edad <= 60:
    if tramo == 'a' or tramo == 'b':
        descuento_medicamento = 0.12
    else:
        descuento_medicamento = 0.08



if edad > 60:
    descuento_despacho = 0
elif (tramo =='a'or tramo =='b') and edad >= 55:
    descuento_despacho = 0.15
else:
    descuento_despacho = 0.10


valor_medicamento = VALOR_MEDICAMENTO_MENSUAL-(VALOR_MEDICAMENTO_MENSUAL*descuento_medicamento)
valor_despacho = VALOR_DESPACHO-(VALOR_DESPACHO*descuento_despacho)

print('')
print(f'El valor del medicamento es: ${valor_medicamento:.0f}')
print(f'El valor del despacho es: ${valor_despacho:.0f}')