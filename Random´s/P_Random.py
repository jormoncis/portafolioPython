from random import choice
import os

os.system('cls')

opc = ['Piedra', 'Papel', 'Tijera']
cpu = choice(opc)

intentos = 0
intentos_user = 0
intentos_cpu = 0
while True:
    print('''
Opciones: 
1. Piedra
2. Tijeras 
3. Papel''')
    cpu = choice(opc)
    print(cpu)
    usuario = input('Ingrese su opción(Piedra, Papel, Tijera): ').lower()
    usuarios = usuario in('tijera','papel','piedra')
    if not usuarios:
        print('Ingreso incorrecto')
        break
    if usuario == cpu.lower():
        print('Empate!!')
        intentos += 1
    elif (usuario == 'piedra' and cpu == 'Tijera') or (usuario=='tijera' and cpu=='Papel') or (usuario=='papel'and cpu=='Piedra'):
        print('Ganaste!!!')
        intentos += 1
        intentos_user += 1
    elif (cpu=='Tijera' and usuario == 'papel')or (cpu=='Papel' and usuario == 'piedra')or(cpu=='Piedra' and usuario == 'tijera'):
        print('Perdiste, ganó la máquina!!!')
        intentos += 1
        intentos_cpu +=1
    else:
        print('Opción no válida!!!')
        intentos += 1

    if (intentos_user==5)or(intentos_cpu==5):
        if intentos_cpu == 5:
            print(f'Perdiste contra la máquina en {intentos} intentos.')
            
            break
        else:
            print(f'Ganaste en un total de {intentos} intentos.')
            break

print(f'La partida tuvo un total de {intentos} intentos.')
print('Fin del juego')