import random

def crear_tablero(tamano):
    """Crea un tablero de juego lleno de 'O' para el agua."""
    tablero = []
    for _ in range(tamano):
        tablero.append(["O"] * tamano)
    return tablero


def colocar_barco(tablero):
    """Coloca un barco de 3 casillas aleatoriamente en el tablero."""
    tamano = len(tablero)
    orientacion = random.choice(['horizontal', 'vertical'])

    if orientacion == 'horizontal':
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 3)
        for i in range(3):
            tablero[fila][columna + i] = "B"
    else:  # vertical
        fila = random.randint(0, tamano - 3)
        columna = random.randint(0, tamano - 1)
        for i in range(3):
            tablero[fila + i][columna] = "B"
    return tablero


def mostrar_tablero(tablero, oculto=True):
    """Imprime el tablero en la consola."""
    print("  " + " ".join([chr(65 + i) for i in range(len(tablero))]))
    for i, fila in enumerate(tablero):
        fila_str = ""
        for casilla in fila:
            if oculto and casilla == "B":
                fila_str += "O "
            else:
                fila_str += casilla + " "
        print(f"{i + 1} {fila_str}")


def jugar_batalla_naval():
    """Lógica principal del juego."""
    tamano_tablero = 5
    intentos_maximos = 10
    intentos_restantes = intentos_maximos
    casillas_tocadas = 0

    tablero_secreto = crear_tablero(tamano_tablero)
    tablero_visible = crear_tablero(tamano_tablero)
    tablero_secreto = colocar_barco(tablero_secreto)

    print("¡Bienvenido a Batalla Naval!")
    print(f"Tienes {intentos_maximos} turnos para hundir el barco de 3 casillas.")
    print("Ingresa coordenadas en formato 'A1', 'C5', etc.\n")

    while intentos_restantes > 0 and casillas_tocadas < 3:
        print(f"--- Te quedan {intentos_restantes} disparo(s) ---")
        mostrar_tablero(tablero_visible)

        try:
            disparo = input("Ingresa tu coordenada: ").upper().strip()

            if len(disparo) < 2:
                print("Coordenada no válida. Por favor, usa el formato letra-número (ej. B3).\n")
                continue

            columna_letra = disparo[0]
            fila_str = disparo[1:]

            columna = ord(columna_letra) - ord('A')
            fila = int(fila_str) - 1

            if not (0 <= fila < tamano_tablero and 0 <= columna < tamano_tablero):
                print("Coordenada fuera del tablero o con formato incorrecto. Intenta de nuevo.\n")
                continue

            if tablero_visible[fila][columna] != "O":
                print("Ya disparaste en esta coordenada. ¡Elige otra!\n")
                continue

            if tablero_secreto[fila][columna] == "B":
                print("¡Tocado! Has golpeado una parte del barco.")
                tablero_visible[fila][columna] = "X"
                casillas_tocadas += 1
            else:
                print("¡Agua! El disparo cayó al mar.")
                tablero_visible[fila][columna] = "-"

            intentos_restantes -= 1
            print("-" * 25)

        except (ValueError, IndexError):
            print("Formato de entrada incorrecto. Usa 'A1', 'C5', etc.\n")

    print("\n¡Juego terminado!")
    if casillas_tocadas == 3:
        print("¡Felicidades! ¡Has hundido el barco y ganado el juego!")
    else:
        print("Se te acabaron los intentos. El barco no fue hundido.")

    print("La ubicación del barco era:")
    mostrar_tablero(tablero_secreto, oculto=False)


if __name__ == "__main__":
    jugar_batalla_naval()