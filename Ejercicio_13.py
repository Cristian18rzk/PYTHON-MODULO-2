def aventura_templo():
    print("El Misterio del Templo Perdido")
    print("Te encuentras en la entrada de un antiguo templo. Debes encontrar la 'Joya del Sol' para escapar.")
    print("Solo tienes 3 movimientos para lograrlo.\n")

    habitacion_actual = "entrada_templo"
    movimientos_restantes = 3
    joya_encontrada = False

    while movimientos_restantes > 0:
        print(f"--- Te quedan {movimientos_restantes} movimiento(s) ---")

        # Lógica para la habitación actual
        if habitacion_actual == "entrada_templo":
            print("\nEstás en la entrada del templo. Hay dos caminos:")
            print("1. 'ir al este' hacia la sala de estatuas")
            print("2. 'ir al norte' hacia el pasillo oscuro")
            accion = input("¿Qué camino eliges? ").lower()

            if accion == "1" or accion == "este":
                habitacion_actual = "sala_estatuas"
            elif accion == "2" or accion == "norte":
                habitacion_actual = "pasillo_oscuro"
            else:
                print(" Acción no válida. Pierdes un movimiento por la indecisión.")

        elif habitacion_actual == "sala_estatuas":
            print("\nHas llegado a la sala de estatuas. Hay una estatua que brilla.")
            print("1. 'examinar' la estatua")
            print("2. 'volver' a la entrada del templo")
            accion = input("¿Qué haces? ").lower()

            if accion == "1" or accion == "examinar":
                print("Revisas la estatua y encuentras la 'Joya del Sol' en su base.")
                joya_encontrada = True
                print("\n🎉 ¡Has encontrado la joya! ¡Ganaste!")
                break  # Sale del bucle para terminar el juego
            elif accion == "2" or accion == "volver":
                habitacion_actual = "entrada_templo"
            else:
                print("Acción no válida. Pierdes un movimiento.")

        elif habitacion_actual == "pasillo_oscuro":
            print("\nEstás en un pasillo oscuro y estrecho. Sientes que algo se mueve...")
            print("1. 'continuar' por el pasillo")
            print("2. 'correr' de regreso a la entrada")
            accion = input("¿Qué haces? ").lower()

            if accion == "1" or accion == "continuar":
                print("\nCaes en una trampa oculta. El suelo se desvanece y caes al vacío.")
                print("\n¡Has perdido! Vuelve a intentarlo.")
                return  # Termina la función y el juego

            elif accion == "2" or accion == "correr":
                habitacion_actual = "entrada_templo"
            else:
                print("Acción no válida. Pierdes un movimiento.")

        # Disminuye los movimientos restantes después de cada acción
        movimientos_restantes -= 1

    # Comprueba el estado final si el bucle termina por los movimientos
    if not joya_encontrada:
        print("\nEl tiempo se ha agotado y no encontraste la joya.")
        print("¡Has perdido! No pudiste escapar del templo.")


# Ejecuta el juego
if __name__ == "__main__":
    aventura_templo()