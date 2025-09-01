# Alfabeto español con ñ
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Pedimos el corrimiento
corrimiento = int(input("Ingrese el corrimiento para la cifra de César: "))

# Pedimos los 5 mensajes
mensajes = []
for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i+1}: ")
    mensajes.append(mensaje)

def encriptar(mensaje, corrimiento):
    resultado = ""
    for letra in mensaje:
        letra_minuscula = letra.lower()
        if letra_minuscula in alfabeto:
            indice = alfabeto.index(letra_minuscula)
            nuevo_indice = (indice + corrimiento) % 27
            letra_encriptada = alfabeto[nuevo_indice]
            # Mantener mayúscula si la letra original era mayúscula
            if letra.isupper():
                letra_encriptada = letra_encriptada.upper()
            resultado += letra_encriptada
        else:
            # Si no es letra del alfabeto, se deja igual
            resultado += letra
    return resultado

print("\nMensajes encriptados:")
for mensaje in mensajes:
    print(encriptar(mensaje, corrimiento))    





#Ejercicio 2: Piedra, Papel,o Tijera
import random

opciones = ["piedra", "papel", "tijera"]

# Marcadores
puntos_jugador = 0
puntos_computadora = 0

while True:
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    eleccion = input("Ingrese el número de su elección: ")

    if eleccion == "4":
        print("\nJuego terminado.")
        print(f"Puntos jugador: {puntos_jugador}")
        print(f"Puntos computadora: {puntos_computadora}")
        break

    if eleccion not in ["1", "2", "3"]:
        print("Opción inválida, intente de nuevo.")
        continue

    eleccion_jugador = opciones[int(eleccion) - 1]
    eleccion_computadora = random.choice(opciones)

    print(f"Jugador eligió: {eleccion_jugador}")
    print(f"Computadora eligió: {eleccion_computadora}")

    # Determinar ganador
    if eleccion_jugador == eleccion_computadora:
        print("Empate.")
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_jugador == "tijera" and eleccion_computadora == "papel") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra"):
        print("¡Ganaste!")
        puntos_jugador += 1
    else:
        print("Gana la computadora.")
        puntos_computadora += 1          