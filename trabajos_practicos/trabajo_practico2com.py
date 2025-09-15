#Ejercicio 1 Solicitar edad al usuario.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Ejecicio 2 Solicitar nota al usuario.

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3 Progrmama que solo permita ingresar numeros pares.

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4 Ingresar edad e imprimir la categoria.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")    

#Ejercicio 5 permitir contraseña de 8 y 14 caracteres.    

contrasena = input("Ingrese una contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6 funcion que permite una lista de numeros.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")    

#Ejercicio 7 Solicitar al usuario frase o palabra.

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#Ejercicio 8 solicitar al usuario nombre y opciones 1,2 o 3.

nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

#Ejercicio 9 Solicitar al usuario la magnitud de un terreno e imprimir la escala Richter.

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10 Preguntar al usuario en que emisferio se encuntra (n/s) mes,año,día.

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Función para verificar si la fecha está en un rango
def fecha_entre(mes, dia, mes_inicio, dia_inicio, mes_fin, dia_fin):
    if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
        return True
    if mes_inicio < mes < mes_fin:
        return True
    return False

if hemisferio == "N":
    if fecha_entre(mes, dia, 12, 21, 3, 20):
        estacion = "invierno"
    elif fecha_entre(mes, dia, 3, 21, 6, 20):
        estacion = "primavera"
    elif fecha_entre(mes, dia, 6, 21, 9, 20):
        estacion = "verano"
    elif fecha_entre(mes, dia, 9, 21, 12, 20):
        estacion = "otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if fecha_entre(mes, dia, 12, 21, 3, 20):
        estacion = "verano"
    elif fecha_entre(mes, dia, 3, 21, 6, 20):
        estacion = "otoño"
    elif fecha_entre(mes, dia, 6, 21, 9, 20):
        estacion = "invierno"
    elif fecha_entre(mes, dia, 9, 21, 12, 20):
        estacion = "primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no válido"

print(f"Estación: {estacion}") 