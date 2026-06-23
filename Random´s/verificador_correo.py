DOMINIO_VALIDO = 'duocuc.cl'
VALIDOS = 'abcdefghijklmnñopqrstuwxyz.@'

nom = ''
dom = ''
acceso = False
validos = False
contar_pun = 0
correo_NV = True
try:
    while True:
        correo = input('Ingrese su correo: ').lower
        for i in correo:
            if i in VALIDOS:
                validos = True
            else:
                print('Correo no válido')
            if i == '@': 
                acceso = True
                continue 

            if not acceso:
                nom += i
            else:
                dom += i

        
        for i in nom:
            if i == '.':
                    contar_pun += 1
            if i in ('1234567890'):
                correo_NV = False 

        if dom != DOMINIO_VALIDO:
            print('Tiene que tener un dominio válido.')

        elif not (10 <= len(nom) <= 11):
            print('El correo debe tener entre 10 y 11 caracteres.')

        elif contar_pun >= 2:
            print('El correo solo puede contener un punto.')

        elif not correo_NV:
            print('El correo no puede contener dígitos.')
        else:
            print('Correo correcto!')
except Exception as e:
    print(e)