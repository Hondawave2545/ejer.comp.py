# Programa principal
productos = []

# Paso 4: Cargar productos en lista de diccionarios
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            'nombre': datos[0],
            'precio': float(datos[1]),
            'cantidad': int(datos[2])
        }
        productos.append(producto)

# Paso 2: Mostrar productos
print("Productos actuales:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Paso 3: Agregar producto desde teclado
nombre_nuevo = input("Ingresa el nombre del producto: ")
precio_nuevo = float(input("Ingresa el precio: "))
cantidad_nueva = int(input("Ingresa la cantidad: "))
nuevo_producto = {
    'nombre': nombre_nuevo,
    'precio': precio_nuevo,
    'cantidad': cantidad_nueva
}
productos.append(nuevo_producto)  # Agrega a la lista

# Paso 5: Buscar producto por nombre
nombre_buscar = input("Ingresa el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    if p['nombre'].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")

# Paso 6: Guardar productos actualizados
with open('productos.txt', 'w') as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Cambios guardados en productos.txt")