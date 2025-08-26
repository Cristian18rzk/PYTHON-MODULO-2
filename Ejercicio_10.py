from typing import List
def transponer_matriz_de_for(matriz: List[List[int]]) -> List[List[int]]:

    """
    Transpone una matriz usando bucles for anidados.
    Convierte filas en columnas.
    """

    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []

    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)

    return transpuesta


def transponer_matriz_de_comprehension(matriz: List[List[int]]) -> List[List[int]]:
    """
    Transpone una matriz usando list comprehensions anidadas.
    """
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]


if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6]]

    print("Matriz original:", matriz)
    print("Transpuesta en for:", transponer_matriz_de_for(matriz))
    print("Transpuesta con comprehension:", transponer_matriz_de_comprehension(matriz))