medicamento_mes = 60,000
despacho_domicilio = 8,000

porc_desc_medicamento = 0
porc_desc_despacho = 0
print('''
Ejercicio 2: Costo de medicamento por comuna.
      ''')

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo de salud (A, B, C, D): ")

'''Calculo de porcentaje de Despacho a domicilio'''
if (tramo == "A" or tramo == "B"):
    porc_desc_despacho = 10
    if (edad >= 55):
        porc_desc_despacho += 5

print(porc_desc_despacho)