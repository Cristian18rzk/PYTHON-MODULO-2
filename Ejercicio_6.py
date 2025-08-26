from typing import List
def encontrar_indices(frase: str, letra: str) -> List[int]:
    """
    Encuentra todas las posiciones de una letra en una frase.

    --------------------------------------------------------------------------------------

    Parámetros:
        frase (str): Texto donde se buscará.
        letra (str): Letra a buscar (se considera solo la primera si se pasa más de una).

    --------------------------------------------------------------------------------------

    Retorna:
        List[int]: Lista de índices donde aparece la letra.
    """
    letra = letra[0]
    indices: List[int] = []

    for i, caracter in enumerate(frase):
        if caracter.lower() == letra.lower():
            indices.append(i)

    return indices


if __name__ == "__main__":
    frase_ingresada: str = input("Ingrese una Frase: ")
    letra_ingresada: str = input("Ingrese una letra para Buscar: ")
    print(encontrar_indices(frase_ingresada, letra_ingresada))