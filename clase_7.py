"""
    Tipo de datos
    variables
    operadores aritmeticos
    operadores logicos

    if /elif /else

    for /while
"""

naranja_aptas: int = 0
naranja_no_apta: int = 0
naranjas: list = ["verde", "verde", "madura", "pasada"]

for naranja in naranjas:
    if naranja == "madura":
        naranja_aptas+=1
    else:
        naranja_no_apta+=1


naranja_aptas: int = 0
naranja_no_apta: int = 0

indice = 0
while indice < len(naranjas):
    # Esta es la manera de obtener a partir del indice el contenido de una lista en su posición
    naranja = naranjas[indice]
    if naranja == "madura":
        naranja_aptas+=1
    else:
        naranja_no_apta+=1
    indice += 1

# Agregar un elemento a una lista con append
naranjas.append("verde")

# Eliminar un elemento de una lista (obteniendo el valor)
naranjas.pop(1) # elimina la posición 1 y te la devuelve
naranja = naranjas.pop(0)
# pop viene de Popping (tomar)
naranjas.copy()
naranjas.count("verde")

"""
["verde", "verde", "madura", "pasada"]
naranjas_outlet = ["verde", "podrida"]
naranjas.extend(naranjas_outlet)
["verde", "verde", "madura", "pasada", "verde", "podrida"]
"""
naranjas_outlet = ["verde", "podrida"]
naranjas.extend(naranjas_outlet)
naranjas.clear()
naranjas2 = naranjas.copy()

aa = [1,2,3, [1,2,3]]
bb = aa.copy()

ff = [[1,2],[1,2]]
zz = ff.copy()

import copy
yy = copy.deepcopy(ff)

lista_compleja = [[[[[[[[],[[[[[[[[[[[]],[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]
lista_compleja2 = [[[[[[[[],[[[[[[[[[[[]],[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]
hh = copy.deepcopy(lista_compleja)

alumnos = [1,2]
alumnos2 = []

#...#...

"""
FIFO
"""
alumnos = []
alumnos.append("pepe")
alumnos.append("jose")
alumnos.pop(0)
alumnos.pop(0)


"""
LIFO
"""
alumnos = []
alumnos.append("pepe")
alumnos.append("jose")
alumnos.pop()
alumnos.pop()


"""
diccionarios
"""
# diccionario
diccionario = {"clave": "valor"}

diccionario2 = {
    "clave": "valor",
    "clave2": "valor2"
}


# Tipo de dato estructurado

docente = {
    "nombre": "Juan",
    "apellido": "Bonini",
    "documento": 675656
}


alumnos = [
    {
        "nombre": "Trinidad",
        "apellido": "Madrid",
        "documento": 123123
    },
    {
        "nombre": "Alan",
        "documento": 12312312,
        "apellido": "Medina"
    },
    { # Esto hay que evitarlo, no se tiene que mezclar claves, hay que mentener estructura.
        "name": "Facundo",
        "last_name": "Badell",
        "id_number": None
    }
]

# for alumno in alumnos:
#     nombre = alumno["nombre"]
#     apellido = alumno["apellido"]
#     documento = alumno["documento"]
#     print(nombre, apellido, documento)

# for alumno in alumnos:
#     # el or acá es muy pythonico
#     nombre = alumno.get("nombre") or alumno.get("name")
#     apellido = alumno.get("apellido") or alumno.get("last_name")
#     documento = alumno.get("documento") or alumno.get("id_number")
#     print(nombre, apellido, documento)


# manejo de errores
for alumno in alumnos:
    try:
        nombre = alumno["nombre"]
        apellido = alumno["apellido"]
        documento = alumno["documento"]
        print(nombre, apellido, documento)
    except ValueError:
        print("Error de valor")
    except KeyError:
        print("Se detectaron claves en ingles")
        nombre = alumno["name"]
        apellido = alumno["last_name"]
        documento = alumno["id_number"]
        print(nombre, apellido, documento)
    except Exception:
        pass


# conjunto
{1,1,1,1}

def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

suma(1, 2)

def division_segura(valor1, valor2):
    resultado = None
    try:
        resultado = valor1 / valor2
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    return resultado

division_segura(10, 2)
division_segura(10, 0)

class Votante:
    TIPO_DOCUMENTO = "DNI"


class Votante:
    TIPO_DOCUMENTO = "DNI" # Variable de clase
    def __init__(self, documento): # Metodo
        self.documento = documento # Variable de instancia
        # Al crear la instancia
        print("Se instancia el objeto Votante")

votante = Votante() # Instanciar una clase y obtenemos un objeto