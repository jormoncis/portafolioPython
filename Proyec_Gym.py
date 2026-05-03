VALOR_MEMBRESIA = 20000
VALOR_BOTELLA = 6000

try:
    # Entradas pedidas al usuario
    dias = int(input('Ingrese la cantidad de días asistidos: '))
    a_mayor = input('Eres adulto mayor(S/N): ').lower()
    # Validación datos válidos
    if dias <= 0:
        print('El número tiene que ser mayor a 0.')
        exit()
    if a_mayor not in ('s','si','sí','n','no'):
        print('Ingrese una "S" o "N"')
        exit()

except ValueError:
    print('Digite cantidad de dás asistidos válidos.')
    exit()

else:
    es_mayor = a_mayor in ('s','si','sí')

    #descuentos membresía dias >= 20 y es mayor 30, si no 20, 10<=dias < 20  si es mayor 18, si no 10, si ninguna 0
    if dias >= 20:
        descuento = 0.3 if es_mayor else 0.2
    elif 10 <= dias < 20:
        descuento = 0.18 if es_mayor else 0.1
    else:
        descuento = 0

    #descuento botella si dias >= 15 si es mayor 17, si no 0(USO DE TERCIARIOS)
    if es_mayor:
        descuento_botella = 0.17 if dias >= 15 else 0.12
    else:
        descuento_botella = 0

    descuento_membresiafin = VALOR_MEMBRESIA-(VALOR_MEMBRESIA*descuento)
    descuento_botellafinal = VALOR_BOTELLA-(VALOR_BOTELLA*descuento_botella)
    total = descuento_botellafinal+descuento_membresiafin
    
    print('')
    print('Detalles:')
    print(f'Membresía: ${VALOR_MEMBRESIA} - {descuento*100} = {descuento_membresiafin:.0f}')
    print(f'Botella: ${VALOR_BOTELLA} - {descuento_botella*100} = {descuento_botellafinal:.0f}')
    print(f'Total a pagar: ${total:.0f}')