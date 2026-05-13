DOMINIO_VALIDO = '@duocuc.cl'
nom = ''
dom = ''
acceso = False
try:
    correo = input('Ingrese su correo: ')
    for i in correo:
        if i in '@': acceso = True

        if not acceso:
            nom += i
        else:
            dom += i

    contar_pun = 0
    for i in nom:
        if i == '.':
                contar_pun += 1
        if i in ('1234567890'):
            correo_NV = False 
    
    if not (10 <= len(nom) <= 11 and dom in DOMINIO_VALIDO):
        if not(dom in DOMINIO_VALIDO):
            print('Tiene que tener un dominio válido.')
            exit()
        elif 10 <= len(nom) <= 11:
            print('El correo tiene que tener 10 caracteres.')
    if contar_pun >= 2:
        print('El correo solo puede contener un punto.')
        exit()
    if nom in '1234567890':
        print('El correo no puede contener ningun digito en el.')
        exit()
    else:
        print('Correo correcto!')

except TypeError as e:
    print(f'Error: {e}')