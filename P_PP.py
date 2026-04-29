membresia = 20000
botella_d = 6000
total = 0
d = ''
de = ''
try:
    dias = int(input('Ingrese la cantidad de días asistidos: '))
    a_mayor = input('Eres adulto mayor(S/N): ').lower()
except ValueError as e:
    print(f'Error: {e}')
else:
    print('')
    print('Descuentos:')
    if dias >= 20 and (a_mayor == 's' or a_mayor== 'si' or a_mayor=='sí'):
        print('Tendrá un "30%" de descuento en membresía.')
        total = (membresia*30) /100
        membresia -= total
        total = 0
        d = '30%'
    elif dias >= 20 and (a_mayor == 'n' or a_mayor== 'no'):
        print('Tendrá un "20%" de descuento en membresía.')
        total = (membresia*20)/100
        membresia -= total
        total = 0
        d = '20%'
    elif (10<= dias < 20) and (a_mayor == 's' or a_mayor== 'si' or a_mayor == 'sí'):
        print('Tendrá un "18%" de descuento en membresía.')
        total = (membresia*18)/100
        membresia -= total
        total = 0
        d = '18%'
    elif (10<= dias < 20) and (a_mayor == 'n' or a_mayor== 'no'):
        print('Tendrá un "10%" de descuento en membresía.')
        total = (membresia*10)/100
        membresia -= total
        total = 0
        d = '10%'
    else:
        print('No tendrá descuentos')
        d = '0%'
    print(f'Tendrá un "{d}" de descuento en membresía.')

    if dias >= 15 and (a_mayor == 's' or a_mayor== 'si' or a_mayor=='sí'):
        print('Tendra un "17%" de descuento en la "Botella Deportiva"')
        total = (botella_d*17)/100
        botella_d -= total
        de = '17%'
    elif (a_mayor == 's' or a_mayor== 'si' or a_mayor=='sí'):
        print('Tendra un "12%" de descuento en "Botella Deportiva"')
        total= (botella_d*12)/100
        botella_d -= total
        de = '12%'
    else:
        print('No tendrás descuentos')
        de='0%'
    
    print('')
    print('Detalles:')
    print(f'Membresía: $20.000 - {d} = {membresia:0.0f}')
    print(f'Botella: $6000 - {de} = {botella_d:0.0f}')
    print(f'Total a pagar: ${membresia+botella_d:0.0f}')