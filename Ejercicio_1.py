def entradas(edad: int, es_estudiante: str) -> int:
    """
    Calcula el precio de una entrada de cine según la edad y si es estudiante.

    -------------------------------------------------------------------------------

    tarifas:
    - Niños (<12): $10,000
    - Jóvenes (12-17): $15,000
    - Adultos (>=18): $20,000
    - Si es estudiante, aplica 10% de descuento sobre el precio.

    -------------------------------------------------------------------------------

    Parámetros:
        edad (int): Edad del cliente (debe ser >= 0).
        es_estudiante (str): 'si' o 'no', indicando si es estudiante.

    -------------------------------------------------------------------------------

    Retorna:
        int: Precio final de la entrada.
    """
    if edad <= 0:
        raise ValueError("La edad no puede ser negativa o igual a 0.")
    if edad < 12:
        precio = 10000
    elif edad <= 17:  # como tal no hace falta 12 <= edad <= 17
        precio = 15000
    else:
        precio = 20000

    return int(precio * 0.9) if es_estudiante == "si" else precio


if __name__ == "__main__":
    try:
        edad_usuario = int(input("Ingresa Tu edad: "))
        estudiante_usuario = input("¿Eres estudiante? (si/no): ").strip().lower().replace(" ", "")
        precio_final = entradas(edad_usuario, estudiante_usuario)
        print(f"El Valor de la entrada es: ${precio_final}")
    except ValueError as e:
        print(f"Error: {e}")
