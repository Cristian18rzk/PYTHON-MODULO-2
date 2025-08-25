import random
def jugar(jugador: str, computadora: str | None = None) -> tuple[str, str, str]:
    """
    Juegr piedra papel o tijera

    -----------------------------------------------------------------------------------

    Parámetros:
        jugador (str): opción del jugador ("piedra", "papel" o "tijeras").

    -----------------------------------------------------------------------------------

    Retorna:
        tuple[str, str, str]: (jugador, computadora, resultado)
                              resultado puede ser "jugador", "computadora" o "empate".
    """
    opciones = ["piedra", "papel", "tijeras"]

    jugador = jugador.lower()
    if jugador not in opciones:
        raise ValueError("Opcion no valida use piedra papel o tijeras")

    if computadora is None:
        computadora = random.choice(opciones)

    if jugador == computadora:
        return jugador, computadora, "empate"
    if (jugador == "piedra" and computadora == "tijeras") \
       or (jugador == "tijeras" and computadora == "papel") \
       or (jugador == "papel" and computadora == "piedra"):
        return jugador, computadora, "jugador"
    return jugador, computadora, "computadora"


if __name__ == "__main__":
    victorias_jugador = 0
    victorias_computadora = 0
    empates= 0

    while victorias_jugador < 3 and victorias_computadora < 3:
        eleccion = input("Elija piedra, papel o tijeras: ").strip().lower().replace(" ","")
        try:
            jugador, computadora, resultado = jugar(eleccion)
        except ValueError as e:
            print(e)
            continue

        print(f"Tú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")

        if resultado == "jugador":
            victorias_jugador += 1
            print("Ganaste esta ronda!")
        elif resultado == "computadora":
            victorias_computadora += 1
            print("La computadora ganó esta ronda!")
        else:
            empates+=1
            print("Empate!")

        print(f"Marcador: Jugador {victorias_jugador} - Computadora {victorias_computadora} empates {empates}\n")

    if victorias_jugador == 3:
        print("Ganaste")
    else:
        print("La computadora ganó")
