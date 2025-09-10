import random


def aventura_templo(acciones):
    """
    Simula la aventura del templo con una lista de acciones predefinidas.
    Devuelve un string con el resultado del juego.
    """
    movimientos_restantes = 3
    joya_encontrada = False
    habitacion_actual = "entrada_templo"

    # Crea un iterador para consumir las acciones una por una
    acciones_iter = iter(acciones)

    while movimientos_restantes > 0:
        try:
            accion = next(acciones_iter).lower()
        except StopIteration:
            # Si se acaban las acciones, el jugador se queda sin movimientos
            break

        if habitacion_actual == "entrada_templo":
            if accion in ["1", "este"]:
                habitacion_actual = "sala_estatuas"
            elif accion in ["2", "norte"]:
                habitacion_actual = "pasillo_oscuro"
            else:
                movimientos_restantes -= 1
                continue  # No cambia de habitación

        elif habitacion_actual == "sala_estatuas":
            if accion in ["1", "examinar"]:
                joya_encontrada = True
                return "victoria"
            elif accion in ["2", "volver"]:
                habitacion_actual = "entrada_templo"
            else:
                movimientos_restantes -= 1
                continue

        elif habitacion_actual == "pasillo_oscuro":
            if accion in ["1", "continuar"]:
                return "derrota_trampa"
            elif accion in ["2", "correr"]:
                habitacion_actual = "entrada_templo"
            else:
                movimientos_restantes -= 1
                continue

        movimientos_restantes -= 1

    if not joya_encontrada:
        return "derrota_tiempo"


# Esta es la función que ejecutarías para jugar en la consola
def jugar_aventura_consola():
    print("El Misterio del Templo Perdido")
    print("...")

    # Aquí es donde leemos la entrada del usuario
    acciones_usuario = []
    while True:
        accion = input("¿Qué camino eliges? ")
        acciones_usuario.append(accion)

        # Llama a la lógica principal con las acciones del usuario
        resultado = aventura_templo(acciones_usuario)

        # Muestra el resultado final al usuario
        if resultado:
            if resultado == "victoria":
                print("\n¡Has encontrado la joya! ¡Ganaste!")
            elif resultado == "derrota_trampa":
                print("\nCaes en una trampa oculta. ¡Has perdido!")
            elif resultado == "derrota_tiempo":
                print("\nEl tiempo se ha agotado. ¡Has perdido!")
            break


if __name__ == "__main__":
    jugar_aventura_consola()