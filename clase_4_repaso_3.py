"""Repaso

    Tipos de datos

    String (cadena de texto) (str)
    boolean (verdadero / falso) algebra de bool
    integer (entero) (int) int8, int16, int32, int64
    float (flotante)
    binary (binario) (bytes)
    None (Empty)

    Operaciones aritmeticas elementales
    + (Suma)
    - (Resta)
    * (Multiplicacion)
    / (Division)
    Hay más
"""

"Cadenas de texto"
True
False
20
2.0
b'bin'
None # Ausencia de valor

CONSTANTE = 15


"""
Type hints (escriba sugerencia)
"""

resultado: None | int = None

valor = False
if valor:
    resultado = 2 - 2

print(resultado)

resultado_suma = 20 + 10
resultado_resta = 20 - 10
resultado_multiplicacion = 20 * 10
resultado_division = 20 / 10

"""
Operadores lógicos
and or not
"""

and_falso = True and False
and_verdadero = True and True

or_falso = False or False
or_verdadero = True or False

"""
Operadores de comparación
"""

mayor = 10 > 5 # True
menor = 10 < 5 # False
mayor_igual = 10 >= 5
menor_igual = 10 <= 5

uno = 1
cuatro = 4
variable_nombre_hermoso = 10

print(uno > cuatro) # Esto no pasa por memoria

if mayor or menor:
    print(True)

es_igual = 10 == 10 # True
es_distinto = 10 != 11 # True


if es_igual:
    print("Es igual") # El bloque esta indentado con 4 espacios.

if not es_distinto:
    print("Es distinto")

if not es_igual:
    print("No entra acá")
elif not es_distinto:
    print("No entra acá")
else:
    print("Entra acá")

if es_distinto:
    print("Es distinto")
else:
    print("No entra acá")

if not es_distinto:
    print("Es distinto")
elif es_igual:
    print("Es igual")


if not es_distinto:
    print("Es distinto")
elif es_igual:
    print("Es igual")
elif es_igual:
    print("Es igual")
elif es_igual:
    print("Es igual")
elif es_igual:
    print("Es igual")
elif es_igual:
    print("Es igual")
