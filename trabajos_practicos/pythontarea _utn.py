def ejercicio1():
    print("Hola Mundo!")

def ejercicio2():
    nombre = input("Ingrese su nombre:")
    print(f"Hola  {nombre}!" )

def ejercicio3():
    nombre = input("ingrese su nombre:")
    apellido = input("ingrese su apellido:")
    edad = input("ingrese su edad: ")
    residencia = input("ingrese su lugar de residencia:")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def ejercicio4():
    radio = float(input("Ingrese el radio del círculo:"))
    area = 3.1416 * radio * radio
    perimetro = 2 * 3.1416 * radio
    print(f"El area del circulo es:{area:.2f}")
    print(f"El perímetro del circulo es: {perimetro:.2f}")

def ejercicio5():
    segundos = int(input("Ingrese la cantidad de segundos:"))
    horas = segundos / 3600
    print(f"{segundos} segundos equivale a {horas:.2f} horas.")

def ejercicio6():
    numero = int(input("Ingrese un número para ver su tabla de multiplicar:"))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def ejercicio7():
    num1 = int(input("Ingrese el primer número (distinto de 0): "))
    num2 = int(input("Ingrese el segundo número (distinto de 0): "))
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2 
    division = num1 / num2
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación:{multiplicacion}")
    print(f"division:{division}")

def ejercicio8():
    peso_kg = float(input("Ingrese su peso en kg (ej. 70):"))
    altura_m = float(input("Ingrese su altura en metros (ej. 1.75):"))
    imc = peso_kg / (altura_m ** 2)
    print(f"Su indice de masa corporal (IMC) es:{imc:.2f}")

def ejercicio9():
    celsius = float(input("Ingrese la temperatura en grados celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}  °C equivalen a {fahrenheit} °F")

def ejercicio10():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de numero es: {promedio:.2f}")

while True:
    print("\n--- Menú de ejercicios ---")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        ejercicio7()
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()
    elif opcion == "0":
        break
    else:
        print("Opción inválida")