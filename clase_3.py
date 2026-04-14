"""
Tipos de datos

String (cadena de texto) (str)
boolean (verdadero / falso) algebra de bool
integer (entero) (int) int8, int16, int32, int64
float (flotante)
binary (binario) (bytes)
None (Empty)
"""

"""
Operaciones aritmeticas elementales
+ (Suma)
- (Resta)
* (Multiplicacion)
/ (Division)
Hay más
"""

resultado_suma=1+5
resultado_suma = 1 + 6 # Por convención se dejan espacios

resultado_resta = 3 - 2
resultado_multiplicacion = 4 * 2
resultado_division = 10 / 2
# Toda division da un resultado flotante, incluso si el resultado es un número entero

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)

# No se puede dividir por cero
# resultado_division = 10 / 0 # Esto da un error

print("Fallo")

"""
Hay distintos errores en python


errores por sintaxis: errores de tipeo, falta de parentesis, etc

print 10
da un SyntaxError

Error de tipo (TypeError) 10 + "Hola"
print(10 + "Hola")


"""

print(2 * 2)
print('=' * 20)

"""
Operadores lógicos
and / or / not
El operador and verifica si se cumplen ambas condiciones
El operador or verifica si se cumple al menos una de las condiciones
El not invierte el valor de una condición (True a False, y viceversa)

El and es multiplicacion
True and True -> True
True and False -> False
False and True -> False
False and False -> False

1 * 1 = 1
1 * 0 = 0
0 * 1 = 0
0 * 0 = 0


False or False -> False
False or True -> True
True or False -> True
True or True -> True

El or es una suma (binaria) BIT
1 + 1 = 1
1 + 0 = 1
0 + 1 = 1
0 + 0 = 0


      *       +         *
True and True or False and True -> True

1 * 1 + 0 * 1

(True and True) or (False and True) = True and True or False and True


(True or True) and (False or False)

True or True and False or False



Operadores de comparación

Igual, distinto, mayor, menor, mayor o igual, menor o igual
==,     !=,        >,     <,        >=,             <=

== 10 == 5 -> falso
!= 10 != 5 -> verdadero
> 10 > 5 -> verdadero
< 10 < 5 -> falso
>=  10 >= 5 -> verdadero
<= 10 <= 5 -> falso


Condicionales

Si una condición es verdadera, ejecutamos un bloque de código.
si no es verdadera pero evaluamos nuevamente para ejecutar un bloque de código
Si no es verdadero nada de lo anterior, ejecutamos otro bloque de código.

Indentación

if 10 == 10:
    print("Hola")
    print("Sigo dentro del if")

if 10 != 10:
    print("Condicion falsa")
else:
    print("De lo contrario, entra acá.")


if 10 != 10:
    print("Condicion falsa")
elif 10 == 10:
    print("Se ejecuta el elif") # Entra acá
else:
    print("De lo contrario, entra acá.")

if 10 != 10:
    print("Condicion falsa")
elif 10 == 9:
    print("No entra acá")
elif 10 == 10:
    print("Se ejecuta el elif") # Entra acá
else:
    print("De lo contrario, entra acá.")




print("Estoy fuera del if")



"""

variable = True
variable2 = False
print(variable)
print(variable2)
