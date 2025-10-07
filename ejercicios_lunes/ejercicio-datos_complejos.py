# Programa de la Mochila Mágica con manejo de excepciones usando try y except

def main():
    # Parte 1: Crear la mochila
    mochila = None
    while True:
        try:
            tamano = input("Ingresa cuántos espacios tendrá la mochila: ")
            tamano = int(tamano)  # Intenta convertir a entero
            if tamano <= 0:
                print("Error: El número de espacios debe ser mayor a cero. Intenta de nuevo.")
                continue
            mochila = [None] * tamano  # Inicializa lista con None para espacios vacíos
            print(f"Mochila creada con {tamano} espacios.")
            break
        except ValueError:
            print("Error: Ingresa un número válido. Intenta de nuevo.")
    
    # Parte 2: Menú principal
    while True:
        print("\n--- Menú de la Mochila ---")
        print("1. Guardar objeto")
        print("2. Ver mochila")
        print("3. Salir")
        # Si se incluye el desafío extra, agregar aquí:
        # print("4. Eliminar objeto")
        
        try:
            opcion = input("Elige una opción: ").strip()
            if not opcion:
                print("Error: Debes elegir una opción válida.")
                continue
            opcion = int(opcion)
            
            if opcion == 1:
                # Guardar objeto
                while True:
                    try:
                        posicion_str = input("Ingresa la posición (0-{}): ".format(len(mochila)-1))
                        if not posicion_str.strip():
                            print("Error: Debes ingresar un número para la posición.")
                            continue
                        posicion = int(posicion_str)  # Try para ValueError
                        
                        # Verificar si la posición existe (IndexError)
                        if 0 <= posicion < len(mochila):
                            nombre = input("Ingresa el objeto mágico: ").strip()
                            if not nombre:
                                print("Error: El nombre del objeto no puede estar vacío.")
                                continue
                            mochila[posicion] = nombre
                            print(f"{nombre} guardado en el espacio {posicion}")
                            break
                        else:
                            raise IndexError("Posición fuera de rango.")
                            
                    except ValueError:
                        print("Error: Ingresa un número válido para la posición.")
                    except IndexError as e:
                        print(f"Error: {e} Intenta con una posición entre 0 y {len(mochila)-1}.")
                
            elif opcion == 2:
                # Ver mochila
                print("\nContenido de la mochila:")
                for i in range(len(mochila)):
                    if mochila[i] is None:
                        print(f"Espacio {i}: --- vacío ---")
                    else:
                        print(f"Espacio {i}: {mochila[i]}")
            
            elif opcion == 3:
                # Salir
                print("¡Gracias por usar la mochila mágica! ¡Hasta luego!")
                break
            
            # Desafío Extra (opcional): Opción 4 - Eliminar objeto
            # Descomenta las siguientes líneas si quieres incluirlo
            # elif opcion == 4:
            #     while True:
            #         try:
            #             posicion_str = input("Ingresa la posición a eliminar (0-{}): ".format(len(mochila)-1))
            #             if not posicion_str.strip():
            #                 print("Error: Debes ingresar un número para la posición.")
            #                 continue
            #             posicion = int(posicion_str)
            #             
            #             if 0 <= posicion < len(mochila):
            #                 if mochila[posicion] is None:
            #                     print(f"El espacio {posicion} ya estaba vacío.")
            #                 else:
            #                     objeto = mochila[posicion]
            #                     mochila[posicion] = None
            #                     print(f"{objeto} eliminado del espacio {posicion}.")
            #                 break
            #             else:
            #                 raise IndexError("Posición fuera de rango.")
            #                 
            #         except ValueError:
            #             print("Error: Ingresa un número válido para la posición.")
            #         except IndexError as e:
            #             print(f"Error: {e} Intenta con una posición entre 0 y {len(mochila)-1}.")
            
            else:
                print("Opción no válida. Elige 1, 2 o 3.")
                
        except ValueError:
            print("Error: Ingresa un número válido para la opción.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()