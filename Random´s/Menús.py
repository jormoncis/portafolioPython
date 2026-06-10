CUPOS_DISPONIBLES = 100
t_reserva = 0

while True:
    print('''
Menú:
    1. Ver cupos disponibles.
    2. Reservar cupos.
    3. Cancelar reservación.
    4. Ver reservas totales
    5. Salir.''')
    try:
        opc = int(input('Ingrese su opción(1-5): '))
        if opc == 1:
            print(f'Cupos disponibles => {CUPOS_DISPONIBLES}')
            
        elif opc == 2:
            while True:
                try:
                    reserva = int(input('Cuántos cupos va a reservar: '))

                    if (reserva >= 1) and (reserva <= CUPOS_DISPONIBLES):
                        print(f'Se realizará una reservación, total reservado => {reserva}')
                        CUPOS_DISPONIBLES -= reserva
                        t_reserva += reserva
                        break
                    else:
                        print('La reserva tiene que ser mayor a cero y menor o igual a los cupos disponibles.')

                except ValueError:
                    print('Solo ingreso númerico.')
                    

        elif opc == 3:
            while True:
                try:
                    cancelar_r = int(input('Ingrese la cantidad a devolver: '))

                    if (cancelar_r > 0) and (cancelar_r <= t_reserva) and (CUPOS_DISPONIBLES <= 100):
                        print(f'Se realizará una cancelación de cupos, cantidad cancelada => {cancelar_r}')
                        CUPOS_DISPONIBLES += cancelar_r
                        t_reserva -= cancelar_r
                        break
                    elif (t_reserva == 0) and (CUPOS_DISPONIBLES == 100):
                        print('Aún no se registran reservas.')
                        break
                    else:
                        print('No puede superar a la cantidad de reservas adquiridas.')

                except ValueError:
                    print('La cantidad cancelada tiene que ser un número entero positivo.')
                    

        elif opc == 4:
            print(f'Cupos reservados => {t_reserva}')
        elif opc == 5:
            print('Gracias por utilizar el sistema Splash World."')
            break
        else:
            print('Opción no válida.')
    except ValueError:
        print('Opciones en el menú es solo númerico.')
    