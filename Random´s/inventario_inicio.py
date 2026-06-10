inventario = {
    "R001": ["Cadena", 25, 15.99],
    "R002": ["Freno de disco", 12, 45.50],
    "R003": ["Cámara de aire", 40, 8.75],
    "R004": ["Lubricante", 18, 12.30],
    "R005": ["Casco urbano", 8, 35.00],
    "R006": ["Cadena de aire", 12, 17.99]}


print('''
╔══════════════════════════════════════════╗
║     CICLOREPUESTOS MASTER - INVENTARIO   ║
╠══════════════════════════════════════════╣
║  1. 🆕 Agregar repuesto                  ║
║  2. 🔍 Buscar repuesto                   ║
║  3. 📦 Actualizar stock                  ║
║  4. ❌ Eliminar repuesto                 ║
║  5. 📋 Mostrar todo el inventario        ║
║  6. ⚠️  Repuestos con bajo stock         ║
║  7. 💰 Valor total por categoría         ║
║  8. 🚪 Salir                             ║
╚══════════════════════════════════════════╝''')
#codigo opción uno
try:
    opc = int(input('Ingrese una opción(1-8): '))
except ValueError:
    print('Error: La opción tiene que ser númerica.')
else:
    if opc == 1:
        while True:
            cod = input('Ingrese el código del producto: ')
            if cod in inventario:
                print('Error: el código ya existe.')
            else:
                try:
                    nom = input('Ingrese el nombre del producto: ')
                    can = int(input('Ingrese la cantidad: '))
                    pre = float(input('Ingrese el precio del producto: '))

                except ValueError: print('Error: Cantidad o precio inválido.')

                else:
                    rev = cod[1:].isdigit()
                    if cod == '': print('Error: El codigo no puede estar Vacío')
                    elif not rev or cod[0] != 'R': print('Error: Código ingresado no válido.')
                    elif nom == '': print('Error: El nombre no puede estar vacío.')
                    elif can <= 0 and pre <=0: print('Error: Cantidad y precio deben ser mayyores que cero.')
                    elif can <= 0: print('Error: La cantidad debe ser mayor que cero')
                    elif pre <= 0:print('Error: El precio tiene que ser mayor a cero.')
                    else:
                        inventario[cod] = [nom,can,pre]
                        print(f'El producto "{nom}" ha sido agregado exitosamente.')
                        break
    elif opc == 2:
        try:
            buscar_x = int(input('Buscar por (1-Código / 2-Nombre): '))
        except ValueError:
            print('Error: La opción tiene que ser númerica.')
        else:
            if buscar_x == 1:
                cod_busc = input('Ingrese el código del respuesto: ')
                if cod_busc in inventario:
                    for k, v in inventario.items():
                        if k == cod_busc:
                            cod, nom, can, pre = k,v[0],v[1],v[2]
                    print('-------------------')
                    print(f'Código: {cod} | {nom} | Stock: {can} | Precio: ${pre}')
                else:
                    print(f'El código "{cod_busc}", no ha sido encontrado')
            elif buscar_x == 2:
                nom_busc = input('Ingresa el nombre del producto a buscar: ')
                for k, v in inventario.items():
                    en = False
                    enn = False
                    if nom_busc.lower() in v[0].lower():
                        cod, nom, can, pre = k,v[0],v[1],v[2]
                        en = True
                        enn = True
                    if en:
                        print('-------------------')
                        print(f'Código: {cod} | {nom} | Stock: {can} | Precio: ${pre}')
                        en = False
                if not enn:
                    print(f'El nombre buscado => "{nom_busc}", no ha sido encontrado')
            else:
                print('Error: Opción no válida.')
    elif opc == 3:
        mod_re = input('Ingresa el Código a modificar: ')
        if mod_re in inventario:
            print(f'Stock actual: {inventario[mod_re][1]} => ({inventario[mod_re][0]})')
            opc = int(input('¿Qué desea hacer? (1-Agregar / 2-Quitar / 3-Ajustar manual): '))
            en = False
            if opc == 1:
                try:
                    can = int(input('Cuanto desea agregar: '))
                except ValueError:
                    print('Error: La cantidad tiene que ser númerica.')
                else:
                    if can > 0:
                        inventario[mod_re][1] += can
                        en  = True
                    else:
                        print('Error: Cantidad no válida.')
            elif opc == 2:
                try:
                    eli = int(input('Ingrese la cantidad a quitar: '))
                except ValueError:
                    print('Error: La cantidad tiene que ser númerica.')
                else:
                    if eli <= inventario[mod_re][1]:
                        inventario[mod_re][1] -= eli
                        en = True
                    else:
                        print('Error: Cantidad no válida.')
            elif opc == 3:
                try:
                    aju = int(input('Ingrese la nueva cantidad del producto: '))
                except ValueError:
                    print('Error: La cantidad tiene que ser númerica.')
                else:
                    if aju > 0:
                        inventario[mod_re][1] = aju
                        en = True
                    else:
                        print('Error: Cantidad no válida.')
            else:
                print('Error: Opción no válida.')
            if en:
                print(f'✓ Stock actualizado. Nueva cantidad: {inventario[mod_re][1]} unidades')
    elif opc == 4:
        eli_re = input('Ingresa el código de respuesto a eliminar: ')
        if eli_re in inventario:
            
            preg = input('Esta seguro que quiere eliminarlo?(S/N): ')
            if preg in 'sSiIíÍ':
                if inventario[eli_re][1] > 0:
                    print(f'Todavía hay {inventario[eli_re][1]} unidades en stock.')
                    preg = input('¿Eliminar de todas formas?(S/N): ')
                    if preg in 'sSiIíÍ':
                        inventario.pop(eli_re)
                        print(f'Se elimino el producto con código => {eli_re}')
            else:
                print('No se ha eliminado.')
        else:
            print(f'No se encontro el código ingresado.')
    elif opc == 5:
        acumula = 0
        en = False
        for k, v in inventario.items():
            cod, nom, can, pre = k,v[0],v[1],v[2]
            en = True
            acumula += pre
            if en:
                print(f'Código: {cod} Nombre: {nom} Cantidad: {can} Precio: {pre}')
                en = False
        print(f'Precio final de todo el stock: ${acumula}')