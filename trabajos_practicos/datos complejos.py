# Práctico 6: Estructuras de datos complejas

# Actividad 1: Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Actividad 1 - Precios frutas:", precios_frutas)

# Actividad 2: Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Actividad 2 - Precios actualizados:", precios_frutas)

# Actividad 3: Lista de frutas sin precios
frutas = list(precios_frutas.keys())
print("Actividad 3 - Frutas:", frutas)

# Actividad 4: Programa para contactos telefónicos
def actividad_4():
    contactos = {}
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        numero = input(f"Ingrese el número de {nombre}: ")
        contactos[nombre] = numero
    consulta = input("Ingrese el nombre a consultar: ")
    if consulta in contactos:
        print(f"El número de {consulta} es: {contactos[consulta]}")
    else:
        print("Contacto no encontrado.")

# Actividad 5: Procesar frase
def actividad_5():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    unicas = set(palabras)
    print("Palabras únicas:", list(unicas))
    recuento = {}
    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1
    print("Recuento:", recuento)

# Actividad 6: Promedio de notas
def actividad_6():
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        notas = tuple(int(input(f"Ingrese nota {j+1} para {nombre}: ")) for j in range(3))
        alumnos[nombre] = notas
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {nombre}: {promedio:.2f}")

# Actividad 7: Operaciones con sets
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}
ambos = parcial1 & parcial2
solo_uno = (parcial1 - parcial2) | (parcial2 - parcial1)
total = parcial1 | parcial2
print("Actividad 7 - Ambos:", ambos)
print("Actividad 7 - Solo uno:", solo_uno)
print("Actividad 7 - Total:", total)

# Actividad 8: Gestión de stock
def actividad_8():
    stock = {'Manzana': 10, 'Banana': 5}
    while True:
        accion = input("¿Qué desea hacer? (consultar/agregar/salir): ").lower()
        if accion == 'salir':
            break
        producto = input("Ingrese el producto: ")
        if accion == 'consultar':
            print(f"Stock de {producto}: {stock.get(producto, 0)}")
        elif accion == 'agregar':
            if producto in stock:
                unidades = int(input("Ingrese unidades a agregar: "))
                stock[producto] += unidades
            else:
                unidades = int(input("Ingrese stock inicial: "))
                stock[producto] = unidades
            print(f"Stock actualizado: {stock}")

# Actividad 9: Agenda
def actividad_9():
    agenda = {("lunes", "10:00"): "Reunión", ("martes", "15:00"): "Clase de inglés"}
    dia = input("Ingrese el día: ")
    hora = input("Ingrese la hora: ")
    clave = (dia, hora)
    if clave in agenda:
        print(f"Actividad: {agenda[clave]}")
    else:
        print("No hay actividad programada.")

# Actividad 10: Invertir diccionario
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print("Actividad 10 - Invertido:", invertido)

# Llamadas a funciones interactivas (ejecuta estas líneas al final para probar)
# actividad_4()
# actividad_5()
# actividad_6()
# actividad_8()
# actividad_9()