import requests
import xml.etree.ElementTree as ET

def menu_principal():
    print('''
========== MENÚ PRINCIPAL ==========
1. Agregar estudiante
2. Buscar estudiante
3. Eliminar estudiante
4. Actualizar estados
5. Mostrar estudiantes
6. Salir
=====================================
''')
    
def opcion_tcl():
    while True:
        try:
            opc = int(input('Ingrese su opción: '))

            if opc >= 1 and opc <=6:
                return opc
            else:
                print('\nOpción no válida, tiene que ser entre 1-6.')
        except ValueError:
            print('\nLa opción elegida debe ser númerica.')

def validar_nombre(nombre):
    return nombre.strip() != ''
def validar_edad(edad):
    return edad >= 0
def validar_nota(nota):
    return nota >= 1 and nota <= 7

def agregar_estudiante(estudiantes):
    nombre = input('Ingrese el nombre del estudiante: ')
    if not validar_nombre(nombre):
        print('El nombre no puede estar vacio, ni ser solo un espacio.')
        return -1

    try:
        edad = int(input('Ingrese la edad del estudiante: '))
    except ValueError:
        print('La edad solo permite números.')
        return -1
    else:
        if not validar_edad(edad):
            print('La edad tiene que ser mayor o igual a cero.')
            return -1
    try: 
        nota = float(input('Ingrese la nota del estudiante: '))
    except ValueError:
        print('La nota tiene que estar entre 1 y 7.')
        return -1
    else:
        if not validar_nota(nota):
            print('La nota debe ser entre "1.0" y "7.0"')
            return -1
    return nombre, edad, nota

def buscar_estudiante(estudiantes,alumno_buscar):
        for i in range(len(estudiantes)):
            if estudiantes[i]['Nombre'].lower() == alumno_buscar:
                return i
        return -1

def actualizar_estado(estudiantes):
    for i in range(len(estudiantes)):
        if estudiantes[i]['Nota'] >= 4:
            estudiantes[i]['Estado'] = True

def recorrido_lista(estudiantes):
    print('\n=== LISTA DE ESTUDIANTES ===')
    for i in range(len(estudiantes)):
        print(f"Nombre: {estudiantes[i]['Nombre']}")
        print(f"Edad: {estudiantes[i]['Edad']}")
        print(f"Nota: {estudiantes[i]['Nota']}")

        if estudiantes[i]['Estado']:
            print('Estado: APROBADO')
        else:
            print('Estado: REPROBADO')
        print('********************************************')


def web_service(estudiantes, alumno_buscar):
    print(alumno_buscar)
    url = "http://testbigauto.dyndns.org:7171/BWSPruebasJAMC"
    # 1. Definimos las cabeceras (normalmente se usa para tokens de API, formato, etc.)
    mis_cabeceras = {
        "user": "BWS",
        "pass": "12345"
    }

    posicion = buscar_estudiante(estudiantes, alumno_buscar)
    if posicion == -1:
        print('Alumno no encontrado.')
        return None

    estatus = 1 if estudiantes[posicion]['Estado'] else 0

    mis_parametros = {
        "nombre": estudiantes[posicion]['Nombre'],
        "edad": estudiantes[posicion]['Edad'],
        "nota": estudiantes[posicion]['Nota'],
        "estado": estatus
    }

    try:
        # 3. Enviamos ambos diccionarios en la petición GET
        respuesta = requests.get(url, headers=mis_cabeceras, params=mis_parametros)

        # Verificar si hubo errores de tipo 4xx o 5xx
        respuesta.raise_for_status()

        # Procesar la respuesta
        datos_json = respuesta.json()
        info_usuario = datos_json["Response"][0]
        # 3. Ahora ya puedes extraer cada dato usando sus claves
        nombre = info_usuario["usuario"]
        mensaje = info_usuario["message"]
        edad = info_usuario["edad"]
        posicion = info_usuario["posicion"]
        
        # 4. Lo imprimes (usando comillas dobles afuera y simples adentro para evitar el SyntaxError)
        print("\n=== RESPUESTA DEL SERVIDOR ===")
        print(f"Estado de la API: {mensaje}")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad} años")
        print(f"Posición en la lista: {posicion}")

    except requests.exceptions.HTTPError as err:
        print(f"Error en la petición (HTTP): {err}")
        # Puedes imprimir la respuesta del servidor para ver el mensaje de error exacto
        print(respuesta.text)
    except Exception as err:
        print(f"Ocurrió otro error: {err}")


def programa_principal():
    estudiantes = []
    while True:
        menu_principal()
        opc = opcion_tcl()
        if opc == 6:
            print('\nGracias por usar el sistema. Vuelva Pronto.')
            break
        elif opc == 1:
            datos = agregar_estudiante(estudiantes)
            if datos != -1:
                nuevo_ingreso = {'Nombre':datos[0],'Edad':datos[1],'Nota':datos[2],'Estado':False}
                estudiantes.append(nuevo_ingreso)
                print(estudiantes)
                web_service(estudiantes, datos[0])
            else:
                print('\nAlumno no registrado')

        elif opc == 2:
            alumno_buscar = input('Ingrese el nombre del alumno a buscar: ').lower()
            posicion = buscar_estudiante(estudiantes, alumno_buscar)
            if posicion != -1:
                print(f"\nPosición: {posicion}")
                print(f"Nombre: {estudiantes[posicion]['Nombre']}")
                print(f"Edad: {estudiantes[posicion]['Edad']}")
                print(f"Nota: {estudiantes[posicion]['Nota']}")
                print(f"Estado: {estudiantes[posicion]['Estado']}")
            else:
                print('Alumno no encontrado.')

        elif opc == 3:
            alumno_eliminar = input('Ingrese el nombre del alumno a eliminar: ')
            posicion = buscar_estudiante(estudiantes, alumno_eliminar)
            if posicion != -1:
                del estudiantes[posicion]
                print('Alumno eliminado con éxito.')
            else:
                print(f'El estudiante {alumno_eliminar} no se encuentra registrado.')

        elif opc == 4:
            if estudiantes != []: actualizar_estado(estudiantes)
            else: print('\nAún no existen registros.')

        elif opc == 5:
            if estudiantes != []:
                actualizar_estado(estudiantes)
                recorrido_lista(estudiantes)
            else: print('\nAún no existen registros.')

programa_principal()