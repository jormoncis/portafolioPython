ENTRADAS_DISPONIBLES = 50
entradas_compradas = 0

while True:
    try:
        print('''
    Menú:
        1. Ver entradas disponibles.
        2. Comprar entradas.
        3. Devolver entradas.
        4. Ver entradas vendidas.
        5. Salir.''')
        opc = int(input('Ingresa una opción(1-5): '))

        if opc == 5:
            break
        elif opc == 1:
            print(f'Entradas disponibles: {ENTRADAS_DISPONIBLES}')
        elif opc == 2:
            com_ent = int(float('¿Cuantas entradas quiere comprar?: '))
            if com_ent > 0 and com_ent < ENTRADAS_DISPONIBLES:
                entradas_compradas += com_ent
                print(f'Se compro un total de {com_ent} entradas.')
            else:
                print('La compra no debe exceder la cantidad disponible y tiene que ser mayor a cero.')
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        else:
            print('Opción no válida.')
    except ValueError:
        print('Solo ingreso númerico.')