"""
Práctico 2: Funciones 
"""

# Actividad 1: Función para imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    """
    Imprime el mensaje "Hola Mundo!" por pantalla.
    
    Esta función no recibe parámetros ni devuelve valores.
    Se utiliza para demostrar una función básica sin retorno.
    """
    print("Hola Mundo!")

# Actividad 2: Función para saludar al usuario
def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y devuelve un saludo personalizado.
    
    Parámetros:
    - nombre (str): El nombre del usuario.
    
    Retorna:
    - str: Un saludo en formato "Hola [nombre]!".
    """
    return f"Hola {nombre}!"

# Actividad 3: Función para imprimir información personal
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe cuatro parámetros y los imprime en un mensaje formateado.
    
    Parámetros:
    - nombre (str): El nombre de la persona.
    - apellido (str): El apellido de la persona.
    - edad (int): La edad en años.
    - residencia (str): El lugar de residencia.
    
    Esta función imprime directamente y no devuelve valores.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Actividad 4: Funciones para calcular área y perímetro de un círculo
import math

def calcular_area_circulo(radio):
    """
    Calcula y devuelve el área de un círculo dado su radio.
    
    Parámetros:
    - radio (float): El radio del círculo en unidades arbitrarias.
    
    Retorna:
    - float: El área del círculo (π * radio²).
    """
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """
    Calcula y devuelve el perímetro de un círculo dado su radio.
    
    Parámetros:
    - radio (float): El radio del círculo en unidades arbitrarias.
    
    Retorna:
    - float: El perímetro del círculo (2 * π * radio).
    """
    return 2 * math.pi * radio

# Actividad 5: Función para convertir segundos a horas
def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.
    
    Parámetros:
    - segundos (float): La cantidad de segundos a convertir.
    
    Retorna:
    - float: La cantidad equivalente en horas (segundos / 3600).
    """
    return segundos / 3600

# Actividad 6: Función para imprimir la tabla de multiplicar
def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número del 1 al 10.
    
    Parámetros:
    - numero (int): El número para el cual se genera la tabla.
    
    Esta función imprime directamente y no devuelve valores.
    """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Actividad 7: Función para operaciones básicas
def operaciones_basicas(a, b):
    """
    Realiza operaciones básicas entre dos números y devuelve una tupla con los resultados.
    
    Parámetros:
    - a (float): El primer número.
    - b (float): El segundo número.
    
    Retorna:
    - tuple: Una tupla con (suma, resta, multiplicación, división).
             Nota: Si b es 0, la división devolverá un error (ZeroDivisionError).
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)

# Actividad 8: Función para calcular el IMC
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso y la altura.
    
    Parámetros:
    - peso (float): El peso en kilogramos.
    - altura (float): La altura en metros.
    
    Retorna:
    - float: El IMC calculado (peso / altura²).
    """
    return peso / (altura ** 2)

# Actividad 9: Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    
    Parámetros:
    - celsius (float): La temperatura en grados Celsius.
    
    Retorna:
    - float: La temperatura equivalente en grados Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

# Actividad 10: Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.
    
    Parámetros:
    - a (float): El primer número.
    - b (float): El segundo número.
    - c (float): El tercer número.
    
    Retorna:
    - float: El promedio de los tres números ((a + b + c) / 3).
    """
    return (a + b + c) / 3

# Programa principal: Llamadas a todas las funciones para probarlas
if __name__ == "__main__":
    # Actividad 1
    imprimir_hola_mundo()
    
    # Actividad 2
    nombre = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre)
    print(saludo)
    
    # Actividad 3
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    # Actividad 4
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    
    # Actividad 5
    segundos = float(input("Ingresa los segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"Horas equivalentes: {horas:.2f}")
    
    # Actividad 6
    numero = int(input("Ingresa un número para la tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    # Actividad 7
    a = float(input("Ingresa el primer número (a): "))
    b = float(input("Ingresa el segundo número (b): "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
    
    # Actividad 8
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    
    # Actividad 9
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}")
    
    # Actividad 10
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio es: {promedio:.2f}")