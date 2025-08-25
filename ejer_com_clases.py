def main():
    # Días de la semana y niveles correspondientes
    dias_niveles = {
        "lunes": "inicial",
        "martes": "intermedio",
        "miércoles": "avanzado",
        "jueves": "práctica hablada",
        "viernes": "inglés para viajeros"
    }

    # Solicitar la fecha al usuario
    fecha = input("Ingrese la fecha actual en formato 'día, DD/MM': ")
    
    try:
        dia, fecha_num = fecha.split(", ")
        dia = dia.lower()  # Convertir a minúsculas para comparación
        dia_num, mes_num = map(int, fecha_num.split("/"))
        
        # Validar día de la semana
        if dia not in dias_niveles:
            print("Error: Dia de la semana inexistente.")
            return
        
        # Validar día y mes
        if dia_num < 1 or dia_num > 31 or mes_num < 1 or mes_num > 12:
            print("Error: Fecha invalida.")
            return
        
        # Obtener el nivel correspondiente
        nivel = dias_niveles[dia]
        
        # Procesar según el nivel
        if nivel in ["inicial", "intermedio", "avanzado"]:
            # Preguntar si hubo exámenes
            exámenes = input("¿Se tomaron examenes? (si/no): ").strip().lower()
            if exámenes == "si":
                aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
                no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
                total_alumnos = aprobados + no_aprobados
                if total_alumnos > 0:
                    porcentaje_aprobados = (aprobados / total_alumnos) * 100
                    print("Porcentaje de aprobados: {:.2f}%".format(porcentaje_aprobados))
                else:
                    print("Error: No se ingresaron alumnos.")
        
        elif nivel == "práctica hablada":
            asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
            if asistencia > 50:
                print("Asistió la mayoría.")
            else:
                print("No asistió la mayoría.")
        
        elif nivel == "inglés para viajeros":
            if (dia_num == 1 and mes_num == 1) or (dia_num == 1 and mes_num == 7):
                print("Comienzo de nuevo ciclo.")
                cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
                ingreso_total = cantidad_alumnos * arancel
                print("Ingreso total: ${:.2f}".format(ingreso_total))

    except ValueError:
        print("Error: Formato de fecha incorrecto.")

if __name__ == "__main__":
    main()
