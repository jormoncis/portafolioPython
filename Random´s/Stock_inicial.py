def menu_principal():
    print('''
========== MENÚ PRINCIPAL ========== 
1. Agregar videojuego 
2. Buscar videojuego 
3. Eliminar videojuego 
4. Actualizar disponibilidad 
5. Mostrar videojuegos 
6. Salir 
==================================== ''')
    
def opcion_selec():
    while True:
        try:
            opc = int(input('Ingrese su opción: '))
            if opc >= 1 and opc <= 6:
                return opc
            else:
                print('Opción tiene que estar entre 1 y 6.')
        except ValueError:
            print('Ingreso de opciónes por el indice númerico.')

def validar_titulo(titulo):
    return titulo.strip() != ''
def validar_precio(precio):
    return precio >= 0

def validar_stock(stock):
        if stock >= 0:
            return True

def agregar_juego(video_juegos):
    titulo = input('Ingrese el nombre del videojuego: ')

    if not validar_titulo(titulo):
        print('El titulo no puede contener espacios, ni estar vacio. ')
        return None
    
    try:
        precio = float(input('Ingrese el precio: '))
    except ValueError:
        print('Error: El precio tiene que ser mayor a 0.')
        return None
    else:
        if not validar_precio(precio):
            print('Error: El precio tiene que ser un número mayor a cero')
            return None
    
    try:
        stock = float(input('Ingrese la cantidad en stock: '))
    except ValueError:
        print('Error: El stock tiene que ser mayor o igual 0.')
        return 
    else:
        if not validar_stock(stock):
            print('Error: La cantidad de stock ingresada debe ser válido.')
            return 
    
    return titulo,precio,stock

def recorrido_disponibilidad(video_juegos):
    for i in range(len(video_juegos)):
        if video_juegos[i]['stock']!= 0:
            video_juegos[i]['disponible'] = True
    
    
def buscar_videojuego(video_juegos,titulo_videojuego):
    for i in range(len(video_juegos)):
        if video_juegos[i]['titulo'] == titulo_videojuego:
            return i
    return -1

def mostrar_catalogo(video_juegos):
    for i in range(len(video_juegos)):
        print(f'Nombre: {video_juegos[i]['titulo']}')
        print(f'Precio: ${video_juegos[i]['precio']}')
        print(f'Cantidad en stock: {video_juegos[i]['stock']}')
        print('********************************************')

def programa_principal():
    video_juegos = []
    while True:
        menu_principal()
        opc = opcion_selec()
        if opc == 1:
            datos = agregar_juego(video_juegos)
            if datos != None:
                ingresos = {'titulo':datos[0] ,'precio': datos[1],'stock':datos[2],'disponible': False}
                video_juegos.append(ingresos)

        elif opc == 2:
            titulo = input('Ingrese el titulo del videojuego: ')
            posicion = buscar_videojuego(video_juegos, titulo)
            if posicion != -1:
                print('====================================')
                print(f'Posición: {posicion+1}') #pide posición no indice de ubicación
                print(f'Nombre: {video_juegos[posicion]['titulo']}')
                print(f'Stock: {video_juegos[posicion]['stock']}')
                print(f'Precio: {video_juegos[posicion]['precio']}')

                if video_juegos[posicion]['disponible']: print('Estado: Disponible.')

                else: print('Estado: No disponible.')
            else:
                print('Titulo no encontrado.')

        elif opc == 3:
            titulo = input('Ingrese el titulo a buscar: ')
            posicion = buscar_videojuego(video_juegos,titulo)
            if posicion != -1:
                video_juegos.pop(posicion)
                print(f'El videojuego "{titulo}" ha sido eliminado.')
            else: print('No se ha encontrado el elemento.')

        elif opc == 4:
            recorrido_disponibilidad(video_juegos)
            print('Disponibilidad actualizada.')
        elif opc == 5:
            print('\n=== LISTA DE VideoJuegos ===')
            mostrar_catalogo(video_juegos)
        elif opc == 6:
            print('Gracias por usar el sistema. Vuelva Pronto')
            break

programa_principal()