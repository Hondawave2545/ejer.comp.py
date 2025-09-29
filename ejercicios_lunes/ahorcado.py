import random

def elegir_palabra():
    """
    Selecciona una palabra al azar de la lista de palabras.
    """
    palabras = [
        "python", "programacion", "tecnologia", "computadora",
        "algoritmo", "variable", "funcion", "desarrollador",
        "software", "hardware"
    ]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    """
    Muestra el estado actual de la palabra con guiones bajos para letras no adivinadas.
    """
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    print("\nPalabra: " + estado.strip())

def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"Tienes {intentos_restantes} intentos para adivinar la palabra.\n")

    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Ingresa una letra: ").lower()

        # Validar entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.\n")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.\n")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_secreta:
            print("¡Adivinaste una letra correctamente!\n")
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta, te quedan {intentos_restantes} intentos.\n")

        # Verificar si el jugador ha adivinado todas las letras
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break
    else:
        print(f"¡Has perdido! La palabra correcta era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()