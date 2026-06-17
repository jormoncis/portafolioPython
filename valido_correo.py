ruts = ['19992116-9','20.056.223-8','8254336-k']

def mensaje():
    return input('Ingrese su rut(Para salir digite x): ')

def ingreso(rut):
    if rut in ruts:
        print('El rut procesado ya existe.')
        busca_rut(mensaje())
    else:
        ruts.append(rut)
        print('Rut ingresado correctamente.')

def formateo(rut_limpio, dv):
    numero = rut_limpio
    
    if len(numero) == 8:
        formato_rut = numero[0:2] + '.'+ numero[2:5] +'.'+numero[5:8]+'-'+dv
    
    elif len(numero) == 7:
        formato_rut = numero[0:1] + '.'+ numero[1:4]+'.'+numero[4:7]+'-'+dv

    elif len(numero) == 10:
        formato_rut = rut_limpio + '-' + dv

    return ingreso(formato_rut)

def limpieza(rut):
    numero = rut[:-2]
    dvv = rut[-1]
    nuevo_elemento = ''
    
    for elemento in numero:
        if elemento != '.':
            nuevo_elemento += elemento

    rut_correcto = nuevo_elemento.isdigit()

    print(nuevo_elemento)
    if rut_correcto:
        return formateo(nuevo_elemento, dvv)
    else:
        busca_rut(mensaje())

def busca_rut(rut_buscar):
    if rut_buscar in 'xX':
        exit()
    if rut_buscar in ruts:
        print('El rut ingresado ya existe.')
        busca_rut(mensaje())
    else:
        limpieza(rut_buscar)

def valido(rut):
    if rut in ruts:
        print('El rut ingresado ya existe.')
        busca_rut(mensaje())
    else:
        banderilla = False

banderilla = True
busca_rut(mensaje())
