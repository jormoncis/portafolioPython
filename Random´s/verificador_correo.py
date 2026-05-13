DOMINIO_VALIDO = '@duocuc.cl'
nom = ''
dom = ''
acceso = False

correo = input('Ingrese su correo: ')
for i in correo:
    if i == '@': acceso = True

    if not acceso:
        nom += i
    else:
        dom += i

contar_pun = 0
correo_NV = True
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
