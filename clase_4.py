"""
Bucles
"""

# Lista (list)
lista = [3,4,2,3,4,5,6,7,5,4,4,5,6,7] # las listas son mutables
lista2 = lista
lista3 = lista

# for 

# for cada elemento en la lista

# numeros = [1,2,3,4,5]
# print(numeros)
# for numero in numeros:
#     resultado = numero * 2
#     print(f"El resultado es: {resultado}")



numeros = [1,2,3,4,5]
nueva_lista = []
for numero in numeros:
    resultado = numero * 2 # Si no entra en el for, el resultado queda sin declarar.
    nueva_lista.append(resultado)
# No podría usar resultado fuera del for


print(f"El resultado es: {nueva_lista}")
print(f"Lo números originales son: {numeros}")


"""
Definimos una lista de 1 a 5
definimos una lista vacia

por cada numero en la lista de numeros
multiplicamos por dos el numero
lo guardamos en la nueva lista
e imprimimos el resultado
"""

"""
Desde la variable numeros esta asignada la lista
desde la variable nueva lista esta en blanco
por numeros en numeros
se le va a asignar el resultado numeros por dos
y en la nueva lista va a ser el restulado
"""

personas = ["Pedro", "Miguel", "Ana", "Pablo", "Maria", "Ana"]

for persona in personas:
    if persona == "Ana":
        print("Hola Ana!")
        break
