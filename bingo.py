import random

def generar_carton():
    numeros = random.sample(range(1, 51), 25)
    carton = [numeros[i*5:(i+1)*5] for i in range(5)]
    return carton

def mostrar_carton(carton):
    for fila in carton:
        print(fila)

def marcar_numero(carton, numero):
    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True
    return encontrado

def hay_linea(carton, lineas_marcadas):
    # Revisar filas
    for i in range(5):
        if all(x == 0 for x in carton[i]) and i not in lineas_marcadas:
            lineas_marcadas.add(i)
            print("¡Línea! La fila {} quedó completa en ceros.".format(i+1))
    return lineas_marcadas

def bingo(carton):
    for fila in carton:
        for num in fila:
            if num != 0:
                return False
    return True

def jugar_bingo():
    print("Bienvenido al Bingo")
    carton = generar_carton()
    print("Tu cartón es:")
    mostrar_carton(carton)

    numeros_sorteados = set()
    lineas_marcadas = set()

    while not bingo(carton):
        numero = random.randint(1, 50)
        if numero in numeros_sorteados:
            continue  # No repetir números sorteados
        numeros_sorteados.add(numero)

        print(f"Se sortea el número... {numero}", end=" ")
        if marcar_numero(carton, numero):
            print("-> ¡Lo tenés!")
        else:
            print("-> No está en tu cartón.")

        mostrar_carton(carton)

        # Verificar líneas completas
        lineas_marcadas = hay_linea(carton, lineas_marcadas)

    print("¡Bingo! Tu cartón quedó en:")
    mostrar_carton(carton)

if __name__ == "__main__":
    jugar_bingo()