"""
Ejercicio 1: Total de puntos obtenidos
Crear una lista con los puntos obtenidos por una persona en distintas rondas de un juego.

Recorrer la lista con for y calcular el puntaje total acumulado.

Al finalizar, mostrar cuántos puntos se obtuvieron en total.
"""
# Suponemos que el puntaje es de 0 a 10.
puntajes_maria = [8,7,5,8,4,6]
puntaje_total = 0 # Acumulador
for puntaje_maria in puntajes_maria:
    puntaje_total = puntaje_total + puntaje_maria

print(puntaje_total)

# Usando +=
puntajes_maria = [8,7,5,8,4,6]
puntaje_total = 0 # Acumulador
for puntaje_maria in puntajes_maria:
    puntaje_total += puntaje_maria


print(puntaje_total)

"""
Ejercicio 2: Notas aprobadas
Crear una lista con las notas de varios estudiantes.

Recorrer la lista con for y contar cuántas notas están aprobadas. Se considera aprobada toda nota mayor o igual a 6.

Al finalizar, mostrar la cantidad de estudiantes aprobados y la cantidad de estudiantes desaprobados.
"""
# Suponemos que hay una nota por estudiante
nota_estudiantes = [8,7,5,8,4,6]
aprobados = 0
NOTA_PARA_APROBAR = 6

for nota_estudiante in nota_estudiantes:
    if nota_estudiante >= NOTA_PARA_APROBAR:
        aprobados += 1

no_aprobados = len(nota_estudiantes) - aprobados
print(f"Alumnos aprobados {aprobados}")
print(f"Alumnos no aprobados {no_aprobados}")


# otra alternativa
nota_estudientes = [8,7,5,8,4,6]
aprobados = 0
no_aprobados = 0
NOTA_PARA_APROBAR = 6

for nota_estudiante in nota_estudientes:
    if nota_estudiante >= NOTA_PARA_APROBAR:
        aprobados += 1
    else:
        no_aprobados +=1


print(f"Alumnos aprobados {aprobados}")
print(f"Alumnos no aprobados {no_aprobados}")


"""
Ejercicio 10: Primer valor que supera un límite
Crear una lista de números y definir un valor límite.

Recorrer la lista usando for con enumerate y detectar cuál es el primer número que supera ese límite.

Al finalizar, mostrar si existe algún número que supere el límite,
cuál fue ese número y en qué posición apareció por primera vez dentro de la lista.
"""

LIMITE = 15
valores = [5,4,3,6,7,10,12,14,13,4,5,16,5,6,3,1,18,20]

for posicion, valor in enumerate(valores):
    if valor > LIMITE:
        print(f"El valor: {valor} se encuentra en a posición: {posicion} supera al limite: {LIMITE}")
        break


"""
Ejercicio 11: Gastos diarios ingresados por teclado
Solicitar al usuario que ingrese los gastos realizados durante varios días.

Recorrer la lista de gastos con for, calcular el gasto total y contar cuántos días tuvieron un gasto mayor a 5000.

Al finalizar, mostrar el total gastado, la cantidad de días cargados y la cantidad de días en los que el gasto fue alto.

Dejar indicado qué sucede si el usuario ingresa un valor que no puede utilizarse como número.
"""

# gastos = []
# while True:
#     fecha = input("Ingresar fecha: ")

#     if fecha == 'salir':
#         break
#     gasto = input("Ingresar gasto: ")
#     gastos.append((fecha, gasto))



# Esta logica se encarga de la recolección de gastos.
gastos = []
GASTO_ALTO = 5000
while True:
    # Si ingresan algo que no es un valor numerico, me da un error
    gasto = input("Ingresar gasto: ")
    if gasto == 'salir':
        break
    gastos.append(int(gasto))

# Esta lógica se encarga de chequear si superaste o no el presupuesto
# Si suponemos que se ingresa 1 gasto por día
gastos_totales = 0
dias_gasto_mayor = 0
for dia, resultado in enumerate(gastos, 1):
    gastos_totales += resultado
    if resultado > 5000:
        dias_gasto_mayor += 1

if gastos_totales > GASTO_ALTO:
    print(f"Los gastos superaron los {GASTO_ALTO}")
else:
    print(f"Los gastos no superaron los {GASTO_ALTO}")

if dias_gasto_mayor:
    print(f"Los días con mayores gastos fueron: {dias_gasto_mayor}")


"""
Solicitar al usuario que ingrese las temperaturas registradas durante varios días.

Recorrer la lista de temperaturas con for,
calcular el promedio y contar cuántos días tuvieron una temperatura mayor o igual a 30 grados.

Al finalizar, mostrar la cantidad de temperaturas cargadas,
el promedio y la cantidad de días calurosos.

Dejar indicado qué sucede si el usuario ingresa un valor que no puede utilizarse como número.
"""

# Dias caluroso mayor a 30
temperaturas = []
dias_temperatura_mayor_30 = 0
suma_temperaturas = 0
while True:
    temperatura = input("Ingresar temperatura: ")
    if temperatura == 'salir':
        break
    temperaturas.append(temperatura)

    suma_temperaturas += temperatura

    if temperatura > 30:
        dias_temperatura_mayor_30 +=1

promedio_temperatura = suma_temperaturas / len(temperaturas)
print(f"Temperaturas cargadas: {temperaturas}")
print(f"El promedio de temperaturas es: {promedio_temperatura}")
print(f"La cantidad de días calurosos fue de: {dias_temperatura_mayor_30}")
