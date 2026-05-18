print('Clasificación de bultos por kg')

total_bultos = 0

try:
    can_bultos = int(input('Ingrese la cantidad de bultos(¿Cuantos son?): '))

    for i in range(can_bultos):
        bultos = float(input('Ingrese la cantidad de kilos por bulto: '))
        if 6 <= bultos <= 10:
            print('Categoría "Normal"')
            total_bultos += 2000
        elif 1 <= bultos <= 5:
            print('Categoría "Liviana"')
            total_bultos += 1000
        else:
            print('No válido, la cantidad debe ser mayor a 0 y menor o igual 10.')
    if total_bultos > 0:
        print(f'El total es: ${total_bultos}')
    else:
        print('No hay datos que calcular')
except ValueError as e:
    print('Se deben ingresar números.')