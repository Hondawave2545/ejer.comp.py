# Práctico 11 - Aplicación de la Recursividad

# 1 Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales():
    limite = int(input("Ingrese un número para calcular factoriales: "))
    for i in range(1, limite + 1):
        print(f"{i}! = {factorial(i)}")

# 2 Serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    posicion = int(input("Ingrese la posición máxima de la serie Fibonacci: "))
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")

# 3 Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def probar_potencia():
    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

# 4 Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario():
    numero = int(input("Ingrese un número decimal: "))
    binario = decimal_a_binario(numero)
    print(f"Binario: {binario if binario else '0'}")

# 5 Verificar palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def probar_palindromo():
    palabra = input("Ingrese una palabra: ").lower()
    print("¿Es palíndromo?", es_palindromo(palabra))

# 6 Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def probar_suma_digitos():
    numero = int(input("Ingrese un número: "))
    print("Suma de dígitos:", suma_digitos(numero))

# 7 Contar bloques en pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def probar_contar_bloques():
    nivel = int(input("Bloques en el nivel más bajo: "))
    print("Total de bloques:", contar_bloques(nivel))

# 8 Contar ocurrencias de un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def probar_contar_digito():
    numero = int(input("Número: "))
    digito = int(input("Dígito a contar (0-9): "))
    print("Cantidad de veces que aparece:", contar_digito(numero, digito))

# Menu interactivo
def menu():
    print("\n--- Práctico 11: Recursividad ---")
    print("1. Factoriales")
    print("2. Serie Fibonacci")
    print("3. Potencia")
    print("4. Decimal a Binario")
    print("5. Palíndromo")
    print("6. Suma de Dígitos")
    print("7. Contar Bloques")
    print("8. Contar Dígito")
    print("9. Salir")

    while True:
        opcion = input("\nElegí una opción (1-9): ")
        if opcion == "1":
            mostrar_factoriales()
        elif opcion == "2":
            mostrar_fibonacci()
        elif opcion == "3":
            probar_potencia()
        elif opcion == "4":
            convertir_a_binario()
        elif opcion == "5":
            probar_palindromo()
        elif opcion == "6":
            probar_suma_digitos()
        elif opcion == "7":
            probar_contar_bloques()
        elif opcion == "8":
            probar_contar_digito()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intentá de nuevo.")

# Ejecutar menu
if __name__ == "__main__":
    menu()