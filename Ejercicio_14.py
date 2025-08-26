import random


def mostrar_ahorcado(intentos):
    """Muestra el dibujo del ahorcado según el número de intentos fallidos."""
    etapas = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]
    print(etapas[intentos])


def jugar_ahorcado():
    """Función principal del juego del Ahorcado."""
    palabras = ['python', 'programacion', 'computadora', 'desarrollo', 'juego', 'consola']
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = set()
    intentos_fallidos = 0
    intentos_maximos = 6

    print("¡Bienvenido al Ahorcado! Adivina la palabra secreta.")

    while intentos_fallidos < intentos_maximos:
        # 1. Mostrar el estado actual del tablero
        tablero = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                tablero += letra + " "
            else:
                tablero += "_ "

        print("\nPalabra: " + tablero)
        print(f"Letras usadas: {sorted(list(letras_adivinadas))}")
        mostrar_ahorcado(intentos_fallidos)

        # 2. Verificar si el jugador ha ganado
        if "_" not in tablero:
            print(f"\n¡Felicidades, has ganado! La palabra era '{palabra_secreta}'. 🎉")
            break

        # 3. Solicitar y validar la entrada del jugador
        entrada = input("Adivina una letra: ").lower().strip()

        if len(entrada) != 1 or not entrada.isalpha():
            print("¡Oops! Por favor, ingresa solo una letra.")
            continue

        if entrada in letras_adivinadas:
            print("Ya intentaste esa letra. ¡Prueba con otra!")
            continue

        letras_adivinadas.add(entrada)

        # 4. Actualizar el estado del juego
        if entrada in palabra_secreta:
            print("¡Correcto! La letra está en la palabra.")
        else:
            print("Incorrecto. Esa letra no está.")
            intentos_fallidos += 1

    # 5. Lógica del final del juego
    if intentos_fallidos == intentos_maximos:
        print("¡Oh no! Te quedaste sin intentos.")
        mostrar_ahorcado(intentos_fallidos)
        print(f"La palabra secreta era '{palabra_secreta}'. ¡Mejor suerte la próxima vez!")


# Inicia el juego
if __name__ == "__main__":
    jugar_ahorcado()