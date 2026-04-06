"""
En Python, las variables se suelen escribir en snake_case (minusculas con _)
porque es la convencion recomendada por PEP 8.

Se evita usar mayusculas para variables comunes, ya que las MAYUSCULAS se usan
principalmente para constantes, y el formato TipoClase se reserva para clases.
"""

# Número entero (int): no tiene decimales.
numero_entero = 55

# Número flotante (float): representa decimales.
numero_flotante = 3.14

# Número complejo (complex): tiene parte real e imaginaria.
numero_complejo = 2 + 5j

# Booleano (bool): solo puede ser True o False.
es_python_facil = True

# Cadena de texto (str): secuencia de caracteres.
mensaje = "Hola, Python"

# Bytes (bytes): datos binarios inmutables.
datos_binarios = b"ABC"

# Nulo (NoneType): representa ausencia de valor.
sin_valor = None


def sumar(valor_1, valor_2):
    """Devuelve la suma de dos valores."""
    return valor_1 + valor_2


print(sumar(1,2)) # 3

print("Hola!")