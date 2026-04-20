lista = [2,3,5,6,5,6,7]
for indice, numero in enumerate(lista):
    # Completa la lógica acá.
    pass

frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    pass

autos_coleccion = ["Toyota", "Honda", "Ford"]
for indice, auto in enumerate(autos_coleccion):
    pass # No hace nada

variable = True
if variable:
    pass
elif variable:
    pass
else:
    pass

"""

Sumar cada elemento de la lista, con el valor anterior
si es que hay valor anterior.

"""
lista = [2,3,5,6,5,6,7]
for indice_lista, numero_lista in enumerate(lista):
    if indice_lista == 0:
        continue # Segui de largo
    print(numero_lista + lista[indice_lista-1])

"""
numero_lista = 2
indice_lista = 0

para el primer indice, no tenemos numero atras.

numero_lista = 3
indice_lista = 1

"""
"""
Prueba de escritorio:
5
8
11
11
11
13
"""

0 + 1 = 1
1 + 1 = 2 
1 + 2 = 3
2 + 3 = 5
5 + 3 = 8
8 + 5 = 13

