ruts = ['20.056.223-8','8.254.336-k']

def mensaje():
    '''
    Uso solo para mensaje de input'''
    return input('Ingrese su rut(Para salir digite x): ')

def ingreso(rut):
    '''
    Aúnque similar a busca_rut este lo compara con el formato correspondiente si lo encuentra manda el mensaje que se encuentra,
    si no lo agrega.
    '''
    if rut in ruts:
        print('El rut procesado ya existe.')
        busca_rut(mensaje())
    else:
        ruts.append(rut)
        print(ruts)
        print('Rut ingresado correctamente.')

def formateo(rut_limpio, dv):
    '''
    Analiza la parte númerica y la clasifica, La ordena en el formato correcto.
    '''
    numero = rut_limpio
    
    if len(numero) == 8:
        formato_rut = numero[0:2] + '.'+ numero[2:5] +'.'+numero[5:8]+'-'+dv
    
    elif len(numero) == 7:
        formato_rut = numero[0:1] + '.'+ numero[1:4]+'.'+numero[4:7]+'-'+dv

    return ingreso(formato_rut)

def limpieza(rut):
    ''' 
    Recibe un rut formato ejemplo(11111111-1,11.111111-1, 11.111.111-1)
    Lo limpia y separa en números sin punto antes del "-" y el digito verificador.
    SOLO limpieza
    resultado => numero = 11111111    dvv = 1
    '''
    numero = rut[:-2]
    dvv = rut[-1]

    nuevo_elemento = numero.replace('.', '')
    rut_correcto = nuevo_elemento.isdigit()

    if rut_correcto:
        return formateo(nuevo_elemento, dvv)
    else:
        busca_rut(mensaje())

def busca_rut(rut_buscar):
    '''
    Busca si lo digitado esta dentro del registro actual de ruts, si lo encuentra manda el mensaje si no continua
    '''
    if rut_buscar in ruts:
        print('El rut ingresado ya existe.')
        busca_rut(mensaje())
    else:
        limpieza(rut_buscar)



rut_ingreso = mensaje()
if rut_ingreso.lower() in 'x':
    exit()
busca_rut(rut_ingreso)
