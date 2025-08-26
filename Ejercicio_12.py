import random
def simular_dados(lanzamientos: int = 10000) -> dict:
    """
    Simula el lanzamiento de dos dados 'lanzamientos' veces y
    cuenta la frecuencia de cada suma posible (2 a 12).

    -----------------------------------------------------------------------------

    Parámetros:
        lanzamientos (int): Número de veces que se lanzan los dados.

    -----------------------------------------------------------------------------

    Retorna:
        dict: Diccionario con las sumas como claves y su frecuencia como valores.
    """
    frecuencias = {}

    for _ in range(lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        print(dado1, dado2)
        # Usamos get para simplificar el conteo
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    return frecuencias


def reporte_frecuencia(frecuencias: dict) -> None:
    """
    Imprime un reporte con las frecuencias de cada suma.
    """
    print("Resultados:")
    for suma in range(2, 13):  # de 2 a 12
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")
if __name__ == "__main__":
    resultados = simular_dados()
    reporte_frecuencia(resultados)
