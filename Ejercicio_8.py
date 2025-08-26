from typing import List
def procesar_list(numeros: List[int]) -> tuple[List[int], List[int], List[str]]:
    """
    Procesa una lista de números para generar:
    1. Una lista con solo los números positivos.
    2. Una lista con los cuadrados de todos los números.
    3. Una lista de strings "positivo" o "negativo" para cada número.

    ---------------------------------------------------------------------

    Parámetros:
        numeros (List[int]): Lista de números enteros.

    ---------------------------------------------------------------------

    Retorna:
        tuple[List[int], List[int], List[str]]:
            - Lista de positivos.
            - Lista de cuadrados.
            - Lista de etiquetas "positivo"/"negativo".
    """
    positivos = [n for n in numeros if n > 0]
    negativos = [n for n in numeros if n < 0]
    cuadrados = [n**2 for n in numeros]
    etiquetas = ["positivo" if n > 0 else "negativo" for n in numeros]

    return positivos,negativos, cuadrados, etiquetas


if __name__ == "__main__":
    lista_inicial: List[int] = [-5, 10, -15, 20, -25, 30]
    positivos,negativos, cuadrados, etiquetas = procesar_list(lista_inicial)

    print("Números positivos:", positivos)
    print("Números negativos:", negativos)
    print("Cuadrados:", cuadrados)
    print("Etiquetas:", etiquetas)