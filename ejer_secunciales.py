#Parte 1:Solicitar al usuario el monto total de la cuenta
monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

#Parte 2: Calcular la propina sugerida al 10%
propina_10 = monto_cuenta * 0.10
total_10 = monto_cuenta + propina_10

#Parte 3:Calcular la propina sugerida al 15%
propina_15 = monto_cuenta * 0.15
total_15 = monto_cuenta + propina_15

#Parte 4: Mostrar los resultados en pantalla
print("Propina sugerida (10%):", propina_10)
print("Total a pagar (10%):", total_10)
print("Propina sugerida (15%):", propina_15)
print("Total a pagar (15%):", total_15)