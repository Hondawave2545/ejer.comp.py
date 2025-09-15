
# Ejercicio 1 Imprime números del 0 al 100, uno por línea
for numero in range(101):  # range(101) genera números de 0 a 100
    print(numero)


# Ejercicio 2 Solicita un número entero y calcula la cantidad de dígitos
numero = input("Ingrese un número entero: ")

# Validar que sea un número entero (puede ser negativo)
while not (numero.lstrip('-').isdigit()):
    numero = input("Entrada inválida. Ingrese un número entero: ")

# Contar dígitos sin considerar el signo negativo
cantidad_digitos = len(numero.lstrip('-'))

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")


#Ejericio 3 Solicitar dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Asegurar que num1 sea menor que num2 para facilitar el rango
if num1 > num2:
    num1, num2 = num2, num1

# Sumar números entre num1 y num2, excluyendo los extremos
suma = 0
for n in range(num1 + 1, num2):
    suma += n

print(f"La suma de los números entre {num1} y {num2} (excluyendo extremos) es: {suma}")



# Ejercicio 4 Sumar números ingresados por el usuario hasta que ingrese 0
total = 0

while True:
    entrada = input("Ingrese un número entero (0 para terminar): ")
    # Validar entrada
    if not entrada.lstrip('-').isdigit():
        print("Entrada inválida, intente de nuevo.")
        continue

    numero = int(entrada)
    if numero == 0:
        break
    total += numero

print(f"La suma total acumulada es: {total}")


#Ejeercicio 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0

print("Adivina el número entre 0 y 9.")

while True:
    intento = input("Ingrese su intento: ")
    if not intento.isdigit():
        print("Por favor, ingrese un número válido.")
        continue

    intento = int(intento)
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Número incorrecto, intenta de nuevo.")


# Ejercicio 6 Imprimir números pares de 100 a 0 en orden decreciente
for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)     



# Ejercicio 7 Solicitar número entero positivo
while True:
    entrada = input("Ingrese un número entero positivo: ")
    if entrada.isdigit() and int(entrada) >= 0:
        limite = int(entrada)
        break
    else:
        print("Entrada inválida. Intente de nuevo.")

# Calcular suma desde 0 hasta limite (inclusive)
suma = sum(range(limite + 1))

print(f"La suma de los números desde 0 hasta {limite} es: {suma}")


# Ejercicio 8
def contar_numeros(cantidad=100):
    pares = impares = negativos = positivos = 0
    for _ in range(cantidad):
        num = int(input("Ingresa un número entero: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num < 0:
            negativos += 1
        elif num > 0:
            positivos += 1
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números negativos: {negativos}")
    print(f"Números positivos: {positivos}")

# Para probar con menos números, cambia el parámetro, por ejemplo contar_numeros(5)
contar_numeros()

# Ejercicio 9
def calcular_media(cantidad=100):
    suma = 0
    for _ in range(cantidad):
        num = int(input("Ingresa un número entero: "))
        suma += num
    media = suma / cantidad
    print(f"La media de los {cantidad} números es: {media}")

# Para probar con menos números, cambia el parámetro, por ejemplo calcular_media(5)
calcular_media()


# Ejercicio 10
def invertir_digitos():
    num = input("Ingresa un número entero: ")
    # Si el número es negativo, separamos el signo
    signo = ''
    if num.startswith('-'):
        signo = '-'
        num = num[1:]
    # Invertimos los dígitos
    num_invertido = num[::-1]
    print(f"Número invertido: {signo}{num_invertido}")

invertir_digitos()