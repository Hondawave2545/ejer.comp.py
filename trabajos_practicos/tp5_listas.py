# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
multiplos_de_4 = list(range(4, 101, 4))
print("1)", multiplos_de_4)

# 2) Crear una lista con cinco elementos y mostrar el penúltimo.
mis_elementos = ["manzana", "perro", "python", "cielo", "música"]
print("2) Penúltimo elemento:", mis_elementos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir.
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("3)", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales”.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"   # segundo elemento (índice 1)
animales[-1] = "oso"   # último elemento (índice -1)
print("4)", animales)

# 5) Explicación del programa:
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)
# Explicación: El programa crea una lista de números, luego elimina el valor máximo de la lista (en este caso 22) usando remove(max(numeros)) y finalmente imprime la lista sin ese valor máximo.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print("5)", numeros)

# 6) Crear una lista con números del 10 al 30 (incluido), saltando de 5 en 5, y mostrar los dos primeros.
lista_10_30 = list(range(10, 31, 5))
print("6) Dos primeros:", lista_10_30[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista "autos".
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupé"]
print("7)", autos)

# 8) Crear lista vacía "dobles" y agregar el doble de 5, 10 y 15 usando append.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8)", dobles)

# 9) Modificar la lista "compras" según las indicaciones.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"
# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")
print("9)", compras)

# 10) Crear lista anidada "lista_anidada" con los elementos indicados.
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10)", lista_anidada)
