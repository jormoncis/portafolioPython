'''
VALORES BASE
'''
membresia_mensual = 20000
botella_deportiva = 6000
porcentaje_membresia = 0
porcentaje_botella = 0

print("Bienvenido al Gimnasio Municipal")
dias = int(input("Ingrese el número de días asistidos: "))
print("")
adulto = input("¿Adulto mayor? (s/n): ")

'''Solo evalua si es adulto o no para la botella'''
if(adulto == "s"):
    porcentaje_botella = 12
if(dias >= 15 and adulto == "s"):
    porcentaje_botella += 5

if(dias >= 20):
    if(adulto == "s"):
       porcentaje_membresia = 30
    else:
        porcentaje_membresia = 20
elif (dias >= 10 and dias < 20):
    if(adulto == "s"):
        porcentaje_membresia = 18
    else:
        porcentaje_membresia = 10


print()
print(f'Membresía: {membresia_mensual} - {porcentaje_membresia}% = {membresia_mensual * (1-(porcentaje_membresia/100))}')
print(f'Botella deportiva: {botella_deportiva} - {porcentaje_botella}% =  {botella_deportiva * (1-(porcentaje_botella/100))}')
Total = membresia_mensual * (1-(porcentaje_membresia/100)) + botella_deportiva * (1-(porcentaje_botella/100))
print(f'El total a pagar es: {Total}')